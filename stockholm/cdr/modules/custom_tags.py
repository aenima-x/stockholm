# -*- coding: utf-8 -*-

from stockholm.asn1.ber_decoder import Tag


def get_tbcd_string(byte_string):
    result = []
    for dec in [ord(x) for x in byte_string]:
        result.append(str(dec & 0xf))
        second_digit = (dec & 0xf0) >> 4
        if second_digit ^ 0xf:
            result.append(str(second_digit))
    return "".join(result)


def get_octet_string(byte_string, fill_zeros=0):
    return "".join(map(lambda x: str(ord(x)).zfill(fill_zeros), byte_string))


def get_int_octet_string(byte_string):
    return int(byte_string.encode('hex'), 16)


def get_filled_octet_string(byte_string, fill_positions):  # TODO Borrar esta reimplementada arriba
    raise Exception("No Usar")
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


class TBCDString(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)