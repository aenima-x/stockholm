# -*- coding: utf-8 -*-
import logging
from . import Module

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class EventModule(Module):
    """
    Data Events to a call.
    Types of Event Modules:
    10 - AoCEventModule
    11 - SSIEventModule
    12 - ServiceSwitchEventModule
    16 - INServiceDataEventModule
    20 - ChargeRateChangeEventModule
    23 - ISDNSSInvocationEventModule
    25 - HandOverEventModule
    """

    def __init__(self, tag=None, byte_string=None):
        super(EventModule, self).__init__(tag, byte_string)

    def __repr__(self):
        return "Event Module - {} ({})".format(self.__class__.__name__, self.tag.number)


class AoCEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(AoCEventModule, self).__init__(tag, byte_string)


class SSIEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(SSIEventModule, self).__init__(tag, byte_string)


class ServiceSwitchEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(ServiceSwitchEventModule, self).__init__(tag, byte_string)


class INServiceDataEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(INServiceDataEventModule, self).__init__(tag, byte_string)


class ChargeRateChangeEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(ChargeRateChangeEventModule, self).__init__(tag, byte_string)


class ISDNSSInvocationEventModule(Module):
        def __init__(self, tag=None, byte_string=None):
            super(ISDNSSInvocationEventModule, self).__init__(tag, byte_string)


class HandOverEventModule(Module):
    def __init__(self, tag=None, byte_string=None):
        super(HandOverEventModule, self).__init__(tag, byte_string)