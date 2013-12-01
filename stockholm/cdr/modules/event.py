# -*- coding: utf-8 -*-
import logging

from . import Module
from . import custom_tags as ct

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


class AoCEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TAC, None),
        1: (ct.CRIToMS, None),
        2: (ct.CRIIndicator, None),
        3: (ct.SSCode, None),
        4: (ct.Time, "timeForEvent"),
        5: (ct.Tag, "incompleteCallDataIndicator"),
        6: (ct.Tag, "gsmSCFControlOfAoC")
    }

    def __init__(self, tag=None, byte_string=None):
        super(AoCEventModule, self).__init__(tag, byte_string)


class SSIEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TAC, None),
        1: (ct.SSCode, None),
        2: (ct.SSRequest, None),
        3: (ct.Time, "timeForEvent"),
        4: (ct.LocationInformation, "firstCallingLocationInformation"),
        5: (ct.CRIIndicator, None),
        6: (ct.EventCRIToMS, None),
        7: (ct.Tag, "incompleteCallDataIndicator"),
        9: (ct.NetworkCallReference, None),
        10: (ct.Tag, "sSInvocationNotification"),
        11: (ct.GlobalCallReference, None)
    }

    def __init__(self, tag=None, byte_string=None):
        super(SSIEventModule, self).__init__(tag, byte_string)


class ServiceSwitchEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TAC, None),
        1: (ct.Time, "timeForEvent"),
        2: (ct.ServiceSwitchingType, None),
        3: (ct.Tag, "incompleteCallDataIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(ServiceSwitchEventModule, self).__init__(tag, byte_string)


class INServiceDataEventModule(EventModule):
    _data_tag_types = {
        0: (ct.Distributed, "chargePartyDistributed"),
        1: (ct.Single, "chargePartySingle"),
        2: (ct.ChargingUnitsAddition, None),
        3: (ct.GenericDigitsSet, "genericChargingDigits"),
        4: (ct.GenericNumbersSet, "genericChargingNumbers"),
        5: (ct.ServiceFeatureCode, None),
        6: (ct.Time, "timeForEvent"),
        7: (ct.Tag, "incompleteCallDataIndicator"),
        8: (ct.FreeFormatData, None),
        9: (ct.LegID, "sSFLegID"),
        10: (ct.FreeFormatData, "freeFormatData2"),
        11: (ct.Tag, "freeFormatDataAppendIndicator"),
        12: (ct.Tag, "freeFormatDataAppendIndicator2")
    }

    def __init__(self, tag=None, byte_string=None):
        super(INServiceDataEventModule, self).__init__(tag, byte_string)


class ChargeRateChangeEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TAC, None),
        1: (ct.Time, "timeForEvent"),
        2: (ct.RadioChannelProperty, None),
        3: (ct.ChangeInitiatingParty, None),
        4: (ct.TariffClass, None),
        7: (ct.AirInterfaceUserRate, "aIURRequested"),
        8: (ct.NumberOfChannels, "numberOfChannelsRequested"),
        9: (ct.ChannelCodings, "channelCodingUsed")
    }

    def __init__(self, tag=None, byte_string=None):
        super(ChargeRateChangeEventModule, self).__init__(tag, byte_string)


class ISDNSSInvocationEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TrafficActivityCode, None),
        1: (ct.Tag, "incompleteCallDataIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(ISDNSSInvocationEventModule, self).__init__(tag, byte_string)


class HandOverEventModule(EventModule):
    _data_tag_types = {
        0: (ct.TAC, None),
        1: (ct.Time, "timeForEvent"),
        2: (ct.TargetRNCid, "rNCidOfTargetRNC"),
        3: (ct.Tag, "incompleteCallDataIndicator"),
        4: (ct.LocationInformation, "targetLocationInformation"),
        5: (ct.RadioChannelProperty, None),
        6: (ct.ChannelCodings, "channelCodingUsed"),
        7: (ct.BSSMAPCauseCode, None),
        8: (ct.RANAPCauseCode, None),
        9: (ct.Tag, "interRegionHandoverIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(HandOverEventModule, self).__init__(tag, byte_string)