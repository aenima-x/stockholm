#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from stockholm.factory import CallDataRecordFactory


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt="%D %T",
                    filename="/tmp/stockholm.log",
                    filemode='w')

logger = logging.getLogger(__name__)


def main():
    cdr_file = "TTGSM-6237.20121130065710"
    f = open(cdr_file)
    data = f.read()
    f.close()
    count = 0
    for cdr in CallDataRecordFactory.get_cdrs_from_data(data):
        count += 1
        print("CDR: {}".format(count))
        cdr.pretty_print()
        print("\n")
    print(count)
if __name__ == "__main__":
    main()