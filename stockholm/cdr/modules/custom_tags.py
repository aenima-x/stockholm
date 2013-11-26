# -*- coding: utf-8 -*-

from stockholm.asn1.ber_decoder import Tag


def get_octet_string(byte_string):
    return "".join(map(lambda x: str(ord(x)), byte_string))


def get_int_octet_string(byte_string):
    return int(byte_string.encode('hex'), 16)


def get_filled_octet_string(byte_string, fill_positions):
    return "".join(map(lambda x: str(ord(x)).zfill(fill_positions), byte_string))


def get_ascii(byte_string):
    return byte_string.encode('ascii')


class Date(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string, 2)


class Time(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string, 2)


class ExchangeIdentity(Tag):
    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class RecordSequenceNumber(Tag):
    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Time(Tag):
    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CallIDNumber(Tag):
    def decode_value(self, byte_string):
        return get_int_octet_string(byte_string)

class Route(Tag):
    def decode_value(self, byte_string):
        return get_ascii(byte_string)