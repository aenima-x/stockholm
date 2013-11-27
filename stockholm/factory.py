# -*- coding: utf-8 -*-
import logging
import os

from .asn1 import ber_decoder
from .cdr import call_data_record

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CallDataRecordFactory(object):

    @staticmethod
    def get_cdrs_from_data(byte_string):
        if len(byte_string) >= 100:
            ARBITRARY_CDR_TAG_LENGTH = 100
        else:
            ARBITRARY_CDR_TAG_LENGTH = len(byte_string)
        index_from = 0
        while index_from != len(byte_string):
            cdr_tag = ber_decoder.Tag(load_value=False)
            cdr_tag.decode(byte_string[index_from:index_from + ARBITRARY_CDR_TAG_LENGTH])
            if cdr_tag.header.type == 1:  # constructed
                index_from += cdr_tag.header.octets
                if cdr_tag.header.data_length > 0:  # Definite length
                    cdr = call_data_record.CallDataRecord()
                    cdr.tag = cdr_tag
                    cdr.set_call_module(byte_string[index_from:index_from + cdr_tag.header.data_length])
                    index_from += cdr.call_module.tag.header.total_octets
                    if cdr_tag.header.data_length > cdr.call_module.tag.header.total_octets:
                        #  This CDR has event Modules
                        ## Bypass the sequence and decode the event modules
                        sequence_length = cdr_tag.header.data_length - cdr.call_module.tag.header.total_octets
                        end_of_sequence_octet = index_from + sequence_length
                        event_module_sequence_tag = ber_decoder.Tag(load_value=False)
                        event_module_sequence_tag.decode(byte_string[index_from:end_of_sequence_octet])
                        optional_event_modules_length = sequence_length - event_module_sequence_tag.header.octets
                        index_from += event_module_sequence_tag.header.octets
                        ##
                        while optional_event_modules_length > 0:
                            cdr.set_event_module(byte_string[index_from:index_from + event_module_sequence_tag.header.extra_data_length])
                            new_event_module = cdr.event_modules[-1]
                            optional_event_modules_length -= new_event_module.tag.header.total_octets
                            index_from += new_event_module.tag.header.total_octets
                            while index_from < len(byte_string):
                                if ord(byte_string[index_from]) == 0:  # Bypass Fillers
                                    index_from += 1
                                    optional_event_modules_length -= 1
                                else:
                                    break
                    yield cdr
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
