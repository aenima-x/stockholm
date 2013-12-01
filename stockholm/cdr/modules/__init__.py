# -*- coding: utf-8 -*-
import logging
from stockholm.asn1 import ber_decoder
from .custom_tags import *

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Module(object):
    _data_tag_types = {}  # In every sub class I must put here the custom data tags

    def __init__(self, tag=None, byte_string=None):
        self.tag = tag
        if not self.tag:
            if byte_string:
                self.tag = ber_decoder.Tag()
                self.tag.decode(byte_string)
        self.data_tags = ()  # This must be a tuple of the data tags for this Module

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.tag.header.number)

    def add_data_tag(self, tag):
        self.data_tags += (tag, )

    def get_data_tag(self, header):
        a = self.__class__._data_tag_types.get(header.number, (ber_decoder.Tag, None))
        tag_class, tag_name = self.__class__._data_tag_types.get(header.number, (ber_decoder.Tag, None))
        tag = tag_class(header=header, name=tag_name)
        return tag

    def decode(self):
        if self.tag:
            if self.tag.header.type == 1 and self.tag.header.data_length > 0:
                index_from = 0
                data_tags_octets_counter = self.tag.header.data_length  # number of header_octets for data tags
                cdr_last_octet = index_from + self.tag.header.data_length  # pointer to the end of the CDR
                while data_tags_octets_counter > 0:  # as long I have bytes to read
                    tag_content = self.tag.value[index_from:cdr_last_octet]
                    header = ber_decoder.Header(tag_content)
                    data_tag = self.get_data_tag(header)
                    data_tag.decode(tag_content)
                    self.add_data_tag(data_tag)
                    if data_tag.header.type == 1 and data_tag.header.data_length > 0:
                        # Here I load any nested Tag in this Constructed Tag
                        nested_index = 0
                        while nested_index < data_tag.header.data_length:
                            nested_tag = ber_decoder.Tag()
                            nested_tag.decode(data_tag.value[nested_index:])
                            nested_index += nested_tag.header.total_octets
                            data_tag.add_nested_tag(nested_tag)
                    index_from += data_tag.header.total_octets
                    data_tags_octets_counter -= data_tag.header.total_octets
        else:
            raise ValueError("Can't decode without Tag")