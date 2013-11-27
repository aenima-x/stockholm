# -*- coding: utf-8 -*-
import logging

from . import Module
from . import custom_tags as ct

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class CallModule(Module):
    """
    Data related to a call.
    Types of Call Modules:
    0 - Transit
    1 - MSOriginating
    2 - RoamingCallForwarding
    3 - CallForwarding
    4 - MSTerminating
    5 - MSOriginatingSMSinMSC
    6 - MSOriginatingSMSinSMS-IWMSC
    7 - MSTerminatingSMSinMSC
    8 - MSTerminatingSMSinSMS-GMSC
    9 - SSProcedure
    13 - TransitINOutgoingCall
    14 - INIncomingCall
    15 - INOutgoingCall
    17 - ISDNOriginating
    18 - ISDNCallForwarding
    19 - ISDNSSProcedure
    21 - SCFChargingOutput
    24 - LocationServices
    """

    def __init__(self, tag=None, byte_string=None):
        super(CallModule, self).__init__(tag, byte_string)

    def __repr__(self):
        return "Call Module - {} ({})".format(self.__class__.__name__, self.tag.header.number)


class Transit(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(Transit, self).__init__(tag, byte_string)


class MSOriginating(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(MSOriginating, self).__init__(tag, byte_string)


class RoamingCallForwarding(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(RoamingCallForwarding, self).__init__(tag, byte_string)


class CallForwarding(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(CallForwarding, self).__init__(tag, byte_string)


class MSTerminating(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(MSTerminating, self).__init__(tag, byte_string)


class MSOriginatingSMSinMSC(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(MSOriginatingSMSinMSC, self).__init__(tag, byte_string)


class MSOriginatingSMSinSMS_IWMSC(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(MSOriginatingSMSinSMS_IWMSC, self).__init__(tag, byte_string)


class MSTerminatingSMSinMSC(CallModule):
    data_tags = {
        6: ct.Date
    }
    def __init__(self, tag=None, byte_string=None):
        super(MSTerminatingSMSinMSC, self).__init__(tag, byte_string)


class MSTerminatingSMSinSMS_GMSC(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(MSTerminatingSMSinSMS_GMSC, self).__init__(tag, byte_string)


class SSProcedure(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(SSProcedure, self).__init__(tag, byte_string)


class TransitINOutgoingCall(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(TransitINOutgoingCall, self).__init__(tag, byte_string)


class INIncomingCall(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(INIncomingCall, self).__init__(tag, byte_string)


class INOutgoingCall(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(INOutgoingCall, self).__init__(tag, byte_string)


class ISDNOriginating(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(ISDNOriginating, self).__init__(tag, byte_string)


class ISDNCallForwarding(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(ISDNCallForwarding, self).__init__(tag, byte_string)


class ISDNSSProcedure(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(ISDNSSProcedure, self).__init__(tag, byte_string)


class SCFChargingOutput(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(SCFChargingOutput, self).__init__(tag, byte_string)


class LocationServices(CallModule):
    def __init__(self, tag=None, byte_string=None):
        super(LocationServices, self).__init__(tag, byte_string)
