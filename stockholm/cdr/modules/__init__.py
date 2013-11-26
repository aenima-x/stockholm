# -*- coding: utf-8 -*-
import logging
from stockholm.asn1 import ber_decoder

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class Module(object):
    def __init__(self, tag=None, byte_string=None):
        self.tag = tag
        if not self.tag:
            if byte_string:
                self.tag = ber_decoder.Tag(byte_string)
        self.data_tags = None  # This must be a tuple of the data tags for this Module

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.tag.number)

    def add_data_tag(self, tag):
        item = (tag, )
        if not self.data_tags:
            self.data_tags = item
        else:
            self.data_tags += item

    def decode(self):
        if self.tag:
            if self.tag.type == 1 and self.tag.data_length > 0:
                index_from = 0
                data_tags_octets_counter = self.tag.data_length  # number of octets for data tags
                cdr_last_octet = index_from + self.tag.data_length  # pointer to the end of the CDR
                while data_tags_octets_counter > 0:  # as long I have bytes to read
                    data_tag = ber_decoder.Tag(self.tag.content[index_from:cdr_last_octet])
                    self.add_data_tag(data_tag)
                    if data_tag.type == 1 and data_tag.data_length > 0:
                        # Here I load any nested Tag in this Constructed Tag
                        nested_index = 0
                        while nested_index < data_tag.data_length:
                            nested_tag = ber_decoder.Tag(data_tag.content[nested_index:])
                            nested_index += nested_tag.total_octets
                            data_tag.add_nested_tag(nested_tag)
                    index_from += data_tag.total_octets
                    data_tags_octets_counter -= data_tag.total_octets
        else:
            raise ValueError("Can't decode without Tag")