# -*- coding: utf-8 -*-
import logging
from ..asn1 import ber_decoder
from ..cdr.modules.call import *
from ..cdr.modules.event import *

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CallDataRecord(object):
    call_modules_dict = {0: Transit, 1: MSOriginating, 2: RoamingCallForwarding, 3: CallForwarding,
                         4: MSTerminating, 5: MSOriginatingSMSinMSC, 6: MSOriginatingSMSinSMS_IWMSC,
                         7: MSTerminatingSMSinMSC, 8: MSTerminatingSMSinSMS_GMSC, 9: SSProcedure,
                         13: TransitINOutgoingCall, 14: INIncomingCall, 15: INOutgoingCall, 17: ISDNOriginating,
                         18: ISDNCallForwarding, 19: ISDNSSProcedure, 21: SCFChargingOutput, 24: LocationServices}

    event_modules_dict = {10: AoCEventModule, 11: SSIEventModule, 16: INServiceDataEventModule,
                          20: ChargeRateChangeEventModule, 23: ISDNSSInvocationEventModule, 25: HandOverEventModule}

    def __init__(self, tag=None, byte_string=None):
        super(CallDataRecord, self).__init__()
        self.tag = tag
        self.call_module = None
        self.event_modules = ()
        if byte_string:
            self.decode(byte_string)

    def decode(self, byte_string):
        if not self.tag:
            self.tag = ber_decoder.Tag(byte_string)
        self.set_call_module(byte_string)
        if self.have_event_modules():
            pass
            #self.find_event_modules(byte_string)

    def have_event_modules(self):
        if self.tag.header.data_length > self.call_module.tag.header.total_octets:
            return True
        else:
            return False

    def find_event_modules(self, byte_string):
        #  This CDR has event Modules

        index_from = self.call_module.tag.header.total_octets  # start of the sequence
        ## Bypass the sequence and decode the event modules
        sequence_length = self.tag.header.data_length - self.call_module.tag.header.total_octets

        end_of_sequence_octet = index_from + sequence_length
        event_module_sequence_tag = ber_decoder.Tag(load_value=False)
        event_module_sequence_tag.decode(byte_string[index_from:end_of_sequence_octet])
        optional_event_modules_length = sequence_length - event_module_sequence_tag.header.octets
        index_from += event_module_sequence_tag.header.octets
        ##
        while optional_event_modules_length > 0:
            self.set_event_module(byte_string[index_from:index_from + event_module_sequence_tag.header.extra_data_length])
            new_event_module = self.event_modules[-1]
            optional_event_modules_length -= new_event_module.tag.header.total_octets
            index_from += new_event_module.tag.header.total_octets
            while index_from < len(byte_string):
                if ord(byte_string[index_from]) == 0:  # Bypass Fillers
                    index_from += 1
                    optional_event_modules_length -= 1
                else:
                    break

    def set_call_module(self, byte_string):
        new_tag = ber_decoder.Tag()
        new_tag.decode(byte_string)
        if new_tag.header.number not in self.__class__.call_modules_dict:
            raise ValueError("Invalid CallModule Tag {}".format(new_tag))
        self.call_module = self.__class__.call_modules_dict.get(new_tag.header.number)(new_tag)
        self.call_module.decode()

    def set_event_module(self, byte_string):
        new_tag = ber_decoder.Tag()
        new_tag.decode(byte_string)
        if new_tag.header.number not in self.__class__.event_modules_dict:
            raise ValueError("Invalid EventModule Tag {}".format(new_tag))
        event_module = self.__class__.event_modules_dict.get(new_tag.header.number)(new_tag)
        self.add_event_module(event_module)

    def add_event_module(self, event_module):
        """
        Add EventModule.
        :param event_module: EventModule
        """
        self.event_modules += (event_module, )

    def __repr__(self):
        return "{}".format(self.__class__.__name__)

    def pretty_print(self):
        """
        Prints a full representation of a CallDataRecord object.
        """
        print(self)
        if self.call_module:
            print(self.call_module)
            if self.call_module.data_tags:
                for data_tag in self.call_module.data_tags:
                    print(data_tag)
        if self.event_modules:
            for event_module in self.event_modules:
                print(event_module)
                if event_module.data_tags:
                    for data_tag in event_module.data_tags:
                        print(data_tag)
