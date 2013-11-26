# -*- coding: utf-8 -*-
import logging
from ..asn1 import ber_decoder

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CallDataRecord(object):
    def __init__(self, byte_string=None):
        super(CallDataRecord, self).__init__()
        self.tag = None
        self.call_module = None
        self.event_modules = ()

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
