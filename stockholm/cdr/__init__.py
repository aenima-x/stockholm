# -*- coding: utf-8 -*-

def get_cdrs_from_data(byte_string):
    """
    extract cdrs from hex data.
    @param byte_string: hex data
    """
    index_from = 0
    index_to = 0
    tag_start = '\xa0' # Indica donde empieza un call record, pasar a class atribute
    while index_from != len(byte_string):
        tag_header = byte_string[index_from]
        if tag_header in CallDataRecord.indefinite_tag_headers:
            index_from += 2
        else:
            if tag_header == tag_start:
                container_tag = berDecoder.Tag(byte_string[index_from:])
                index_to = index_from + container_tag.end_of_content_octet
                index_from += container_tag.number_of_header_octets
                tag_number, i = berDecoder.Tag.decode_tag_identifier(byte_string[index_from:index_to])
                if tag_number in CallDataRecord.include_tags:
                    cdr = CallDataRecord(byte_string[index_from:index_to])
                    yield cdr
                else:
                    if tag_number not in CallDataRecord.exclude_tags:
                        logger.warning("Not Allowed Tag(%s)!!",  tag_number)
                index_from = index_to
            else:
                logger.warning("ERROR Unknown header tag: %s at index: %s byte_string left:", tag_header.encode('hex'), index_from, len(byte_string[index_from:]))
                break