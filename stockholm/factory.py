# -*- coding: utf-8 -*-
import logging
import os

from asn1 import ber_decoder
from cdr import call_data_record
from cdr.modules.call import *
from cdr.modules.event import *

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CallDataRecordFactory(object):
    call_modules_dict = {0: Transit, 1: MSOriginating, 2: RoamingCallForwarding, 3: CallForwarding,
                         4: MSTerminating, 5: MSOriginatingSMSinMSC, 6: MSOriginatingSMSinSMS_IWMSC,
                         7: MSTerminatingSMSinMSC, 8: MSTerminatingSMSinSMS_GMSC, 9: SSProcedure,
                         13: TransitINOutgoingCall, 14: INIncomingCall, 15: INOutgoingCall, 17: ISDNOriginating,
                         18: ISDNCallForwarding, 19: ISDNSSProcedure, 21: SCFChargingOutput, 24: LocationServices}
    event_modules_dict = {10: AoCEventModule, 11: SSIEventModule, 16: INServiceDataEventModule,
                          20: ChargeRateChangeEventModule, 23: ISDNSSInvocationEventModule, 25: HandOverEventModule}

    @staticmethod
    def get_cdrs_from_data(byte_string):
        cdrs = []
        if len(byte_string) >= 100:
            ARBITRARY_CDR_TAG_LENGTH = 100
        else:
            ARBITRARY_CDR_TAG_LENGTH = len(byte_string)
        index_from = 0
        while index_from != len(byte_string):
            cdr_tag = ber_decoder.Tag(byte_string[index_from:index_from + ARBITRARY_CDR_TAG_LENGTH], False)
            if cdr_tag.type == 1:  # constructed
                index_from += cdr_tag.header_octets
                if cdr_tag.data_length > 0:  # Definite length
                    call_module_tag = ber_decoder.Tag(byte_string[index_from:index_from + cdr_tag.data_length])
                    #print("New CallDataRecord - {}".format(cdr_tag))
                    if call_module_tag.number in CallDataRecordFactory.call_modules_dict:
                        cdr = call_data_record.CallDataRecord()
                        cdr.tag = cdr_tag
                        cdr.call_module = CallDataRecordFactory.call_modules_dict.get(call_module_tag.number)(call_module_tag)
                        #print("Found Call Module -> {}".format(cdr.call_module))
                        index_from += call_module_tag.total_octets
                        cdr.call_module.decode()
                        if cdr_tag.data_length > call_module_tag.total_octets: #  This CDR has event Modules
                            ## Bypass the sequence and decode the event modules
                            sequence_length = cdr_tag.data_length - call_module_tag.total_octets
                            end_of_sequence_octet = index_from + sequence_length
                            event_module_sequence_tag = ber_decoder.Tag(byte_string[index_from:end_of_sequence_octet], False)
                            optional_event_modules_length = sequence_length - event_module_sequence_tag.header_octets
                            index_from += event_module_sequence_tag.header_octets
                            ##
                            while optional_event_modules_length > 0:
                                event_module_tag = ber_decoder.Tag(byte_string[index_from:index_from + event_module_sequence_tag.extra_data_length])
                                if event_module_tag.number in CallDataRecordFactory.event_modules_dict:
                                    event_module = CallDataRecordFactory.event_modules_dict.get(event_module_tag.number)(event_module_tag)
                                    event_module.decode()
                                    cdr.add_event_module(event_module)
                                    optional_event_modules_length -= (event_module_tag.data_length + event_module_tag.header_octets)
                                    index_from += (event_module_tag.data_length + event_module_tag.header_octets)
                                else:
                                    raise ValueError("Invalid Event Module Number {} {}".format(event_module_tag.number, index_from))
                                while index_from < len(byte_string):
                                    if ord(byte_string[index_from]) == 0:  # Bypass Fillers
                                        index_from += 1
                                        optional_event_modules_length -= 1
                                    else:
                                        break
                        yield cdr
                    else:
                        raise ValueError("Invalid Call Module Number {}".format(call_module_tag.number))
                else:
                    pass
                    #print("Skip Indefinite Tag")
            else:  # Primitive
                raise ValueError("A primitive Tag can't be a CallDataRecord Tag {}".format(index_from))
            while index_from < len(byte_string):
                if ord(byte_string[index_from]) == 0:  # Bypass Fillers
                    index_from += 1
                else:
                    break


    @staticmethod
    def get_cdrs_from_file(path_to_file):
        logger.info("Processing file %s", path_to_file)
        file_name = os.path.basename(path_to_file)
        file_object = open(path_to_file, "rb")
        byte_string = file_object.read()
        file_object.close()
        try:
            return CallDataRecordFactory.get_cdrs_from_data(byte_string)
        except Exception as e:
            logger.exception("%s on %s", e, file_name)
            raise e
