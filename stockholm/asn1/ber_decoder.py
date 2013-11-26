# -*- coding: utf-8 -*-
import logging
import struct

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def get_binary(data):  # TODO Ver de borrar si no se usa
    return bin(struct.unpack('@B', data)[0])[2:].zfill(8)


def lvq_decode(byte_string):
    """
    Return the value of the byte string in base 128, and the number of octets.
    :param byte_string: string of bytes
    :return: (int, int)
    """
    values = []
    result = 0
    size = 0
    while True:
        b = ord(byte_string[size:size+1])  # get decimal value
        size += 1
        values.append((b & 0x7f))  # add to list the value with out the 8th bit
        if b & 0x80 == 0:  # it has 0 in the 8th bit exit the loop
            break
    shift = 7 * (len(values) - 1)  # how many shifts I must do
    for i in values:
        i << shift
        result |= i
        shift - 7
    return result, size


def get_bit(number, index):
    """
    Return the bit at index position (starts from 0) from the number in base 2.
    :param number: int
    :param index: int
    :return: int
    """
    return int((number & (1 << index)) != 0)


class Tag(object):
    """
    Representation of an asn1 tag.
    :param byte_string: string of bytes
    """
    _type_name = ('primitive', 'constructed')
    indefinite_tag_headers = ('\xa1', '\x00')  # TODO Borrar

    def __init__(self, byte_string=None, must_load_content=True):
        self.number = None
        self.type = None
        self.content = None
        self.nested_tags = ()
        # Header
        self.header_octets = 0
        self.identifier_octets = 0
        self.length_octets = 0
        # Counters
        self.data_length = 0
        self.total_octets = 0
        self.extra_data_length = 0
        # Setup
        self.must_load_content = must_load_content
        if byte_string:
            self.decode(byte_string)

    def __repr__(self):
        if self.type == 0:
            return "[{0.number:<3}] - {0.content}".format(self)
        elif self.type == 1:
            if self.nested_tags:
                return "[{0:<3}]\n\t{1}".format(self.number, "\n\t".join((str(x) for x in self.nested_tags)))
            else:
                return "Tag(number={0.number})(type={0.get_type})(header length={0.header_octets}" \
                       "[identifier={0.identifier_octets}, length={0.length_octets}])" \
                       "(data length={0.data_length})(extra data={0.extra_data_length})".format(self)

    def decode(self, byte_string):
        """
        Decode the Tag type, number and number of the Tag identifiers octets.
        :param byte_string: string of bytes
        """
        self.type = Tag.decode_tag_type(byte_string)  # 0 - primitive, 1 - constructed
        self.number, self.identifier_octets = Tag.decode_tag_identifier(byte_string)
        self.decode_length(byte_string)
        if self.must_load_content:
            self.load_content(byte_string)

    @staticmethod
    def decode_tag_identifier(byte_string):
        """
        Return the tag number and the number of identifier octets.
        :param byte_string: string of bytes
        :return: (int, int)
        """
        identifier_octets = 0
        first_octet = ord(byte_string[0])
        if first_octet & 31 == 31:  # long format Tag (first 5 bits are 1)
            number, identifier_octets = lvq_decode(byte_string[1:])
        else:  # short format Tag
            number = first_octet - (first_octet & 224)
        identifier_octets += 1
        return number, identifier_octets

    @staticmethod
    def decode_tag_type(byte_string):
        """
        Decode tge tag type from the 6th bit of the first octet.
        Return 0 if it's Primitive or 1 if it's Constructed.
        :param byte_string: string of bytes
        :return: int
        """
        first_octet = ord(byte_string[0])
        return int(first_octet & 32 == 32)

    @property
    def get_type(self):
        """
        Return the name of the Tag type.

        :return: str
        """
        type_name = Tag._type_name[self.type]
        if self.data_length == 0:
            type_name = "{}-Indefinite".format(type_name)
        return type_name

    def decode_length(self, byte_string):
        first_octet = ord(byte_string[self.identifier_octets])
        if first_octet == 128:  # Indefinite size
            self.length_octets = 1
            self.header_octets = self.identifier_octets + self.length_octets
            self.extra_data_length = len(byte_string) - self.header_octets
        else:  # definite size
            if get_bit(first_octet, 7):  # long format
                number_of_extra_length_octets = first_octet - (first_octet & 128)
                self.length_octets = 1 + number_of_extra_length_octets
                self.header_octets = self.identifier_octets + self.length_octets  # The offset of octets to read the content
                index = self.identifier_octets + 1
                if number_of_extra_length_octets > 1:
                    bin_value = ''
                    for i in range(number_of_extra_length_octets):
                        bin_value = "{}{}".format(bin_value, bin(ord(byte_string[index]))[2:].zfill(8))
                        index += 1
                    self.data_length = int(bin_value, 2)
                else:
                    self.data_length = ord(byte_string[index])
                self.extra_data_length = 0
            else:  # short format
                self.length_octets = 1
                self.header_octets = self.identifier_octets + self.length_octets
                self.data_length = first_octet
                self.extra_data_length = len(byte_string) - self.header_octets - self.data_length
        self.total_octets = self.header_octets + self.data_length

    def load_content(self, byte_string):
        if self.type == 0:
            self.content = byte_string[self.header_octets:self.total_octets].encode('hex')
        elif self.type == 1:
            self.content = byte_string[self.header_octets:self.total_octets]

    def add_nested_tag(self, tag):
        item = (tag,)
        if self.type == 1:
            self.nested_tags += (tag,)