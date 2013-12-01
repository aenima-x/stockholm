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
            cdr_tag_data = byte_string[index_from:index_from + ARBITRARY_CDR_TAG_LENGTH]
            cdr_tag.decode(cdr_tag_data)
            if cdr_tag.type == 1:  # constructed
                if cdr_tag.header.data_length > 0:  # Definite length
                    cdr = call_data_record.CallDataRecord(tag=cdr_tag)
                    cdr_data = byte_string[index_from:index_from + cdr_tag.total_octets]
                    cdr.decode(cdr_data)
                    index_from += cdr.tag.total_octets
                    yield cdr
                else:
                    index_from += cdr_tag.octets
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
