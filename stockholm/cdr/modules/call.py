# -*- coding: utf-8 -*-
import logging

from stockholm.asn1 import ber_decoder
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
    _data_tag_types = {0: (ct.TAC, "tAC"),
                       1: (ct.CallIDNumber, "callIdentificationNumber"),
                       2: (ct.RecordSequenceNumber, "recordSequenceNumber"),
                       3: (ct.TypeOfCallingSubscriber, "typeOfCallingSubscriber"),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.AddressString, "calledPartyNumber"),
                       6: (ct.IMSI, "calledSubscriberIMSI"),
                       7: (ct.DisconnectingParty, "disconnectingParty"),
                       8: (ct.Date, "dateForStartOfCharge"),
                       9: (ct.Time, "timeForStartOfCharge"),
                       10: (ct.Time, "timeForStopOfCharge"),
                       11: (ct.Time, "chargeableDuration"),
                       12: (ct.Time, "interruptionTime"),
                       13: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       14: (ct.ChargedParty, "chargedParty"),
                       15: (ct.ChargingOrigin, "originForCharging"),
                       16: (ct.TariffClass, "tariffClass"),
                       17: (ct.TariffSwitchInd, "tariffSwitchInd"),
                       18: (ct.NumberOfMeterPulses, "numberOfMeterPulses"),
                       19: (ct.ExchangeIdentity, "exchangeIdentity"),
                       20: (ct.AddressString, "mSCIdentification"),
                       21: (ct.Route, "outgoingRoute"),
                       22: (ct.Route, "incomingRoute"),
                       23: (ct.MiscellaneousInformation, "miscellaneousInformation"),
                       25: (ct.INMarkingOfMS, "iNMarkingOfMS"),
                       26: (ct.CallPosition, "callPosition"),
                       27: (ct.EosInfo, "eosInfo"),
                       28: (ct.InternalCauseAndLoc, "internalCauseAndLoc"),
                       29: (ct.AddressString, "originalCalledNumber"),
                       30: (ct.AddressString, "redirectingNumber"),
                       31: (ct.RedirectionCounter, "redirectionCounter"),
                       32: (ct.AddressString, "redirectingDropBackNumber"),
                       33: (ber_decoder.Tag, "redirectingDropBack"),
                       34: (ber_decoder.Tag, "restartDuringCall"),
                       35: (ber_decoder.Tag, "restartDuringOutputIndicator"),
                       36: (ber_decoder.Tag, "iCIOrdered"),
                       37: (ct.OutputForSubscriber, "outputForSubscriber"),
                       38: (ber_decoder.Tag, "lastPartialOutput"),
                       39: (ct.PartialOutputRecNum, "partialOutputRecNum"),
                       40: (ct.CallIDNumber, "relatedCallNumber"),
                       41: (ct.FaultCode, "faultCode"),
                       42: (ct.SubscriptionType, "subscriptionType"),
                       43: (ber_decoder.Tag, "incompleteCallDataIndicator"),
                       44: (ber_decoder.Tag, "incompleteCompositeCDRIndicator"),
                       45: (ct.SwitchIdentity, "switchIdentity"),
                       46: (ct.NetworkCallReference, "networkCallReference"),
                       47: (ber_decoder.Tag, "disconnectionDueToSystemRecovery"),
                       48: (ber_decoder.Tag, "forloppDuringOutputIndicator"),
                       49: (ber_decoder.Tag, "forloppReleaseDuringCall"),
                       50: (ct.AddressString, "translatedNumber"),
                       51: (ct.CAMELTDPData, "bCSMTDPData1"),
                       52: (ct.CAMELTDPData, "bCSMTDPData2"),
                       53: (ct.CAMELTDPData, "bCSMTDPData3"),
                       54: (ct.CAMELTDPData, "bCSMTDPData4"),
                       55: (ct.CAMELTDPData, "bCSMTDPData5"),
                       56: (ct.CAMELTDPData, "bCSMTDPData6"),
                       57: (ct.CAMELTDPData, "bCSMTDPData7"),
                       58: (ct.CAMELTDPData, "bCSMTDPData8"),
                       59: (ct.CAMELTDPData, "bCSMTDPData9"),
                       60: (ct.CAMELTDPData, "bCSMTDPData10"),
                       61: (ct.GSMCallReferenceNumber, "gSMCallReferenceNumber"),
                       62: (ct.C7ChargingMessage, "c7ChargingMessage"),
                       63: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       64: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       65: (ct.ChargingIndicator, "aCMChargingIndicator"),
                       66: (ct.ChargingIndicator, "aNMChargingIndicator"),
                       67: (ct.AddressString, "mSCAddress"),
                       68: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       69: (ct.TransitCarrierInfo, "carrierInformationForward"),
                       70: (ct.ChargeInformation, "chargeInformation"),
                       71: (ct.Date, "disconnectionDate"),
                       72: (ct.Time, "disconnectionTime"),
                       73: (ct.ChargeAreaCode, "entryPOICA"),
                       74: (ct.ChargeAreaCode, "exitPOICA"),
                       75: (ber_decoder.Tag, "internationalCallIndicator"),
                       76: (ct.MobileUserClass1, "mobileUserClass1"),
                       77: (ct.MobileUserClass2, "mobileUserClass2"),
                       78: (ber_decoder.Tag, "originatingAccessISDN"),
                       79: (ct.CarrierInfo, "originatingCarrier"),
                       80: (ct.ChargeAreaCode, "originatingChargeArea"),
                       81: (ct.Counter, "tDSCounter"),
                       82: (ber_decoder.Tag, "terminatingAccessISDN"),
                       83: (ct.CarrierInfo, "terminatingCarrier"),
                       84: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       85: (ct.MobileUserClass1, "terminatingMobileUserClass1"),
                       86: (ct.MobileUserClass2, "terminatingMobileUserClass2"),
                       87: (ct.AddressString, "contractorNumber"),
                       88: (ct.UserClass, "terminatingUserClass"),
                       89: (ct.UserClass, "userClass"),
                       90: (ct.AddressString, "calledPartyMNPInfo"),
                       91: (ct.AddressString, "chargeNumber"),
                       92: (ct.OriginatingLineInformation, "originatingLineInformation"),
                       93: (ct.MultimediaInformation, "multimediaInformation"),
                       94: (ct.GlobalCallReference, "globalCallReference"),
                       95: (ber_decoder.Tag, "rTCIndicator"),
                       96: (ct.RTCSessionID, "rTCSessionID"),
                       97: (ct.RTCDefaultServiceHandling, "rTCDefaultServiceHandling"),
                       98: (ct.RTCFailureIndicator, "rTCFailureIndicator"),
                       99: (ct.RTCNotInvokedReason, "rTCNotInvokedReason"),
                       100: (ct.AddressString, "calledDirectoryNumber"),
                       101: (ct.PChargingVector, "incomingPChargingVector"),
                       102: (ct.OutputType, "outputType"),
                       103: (ct.PChargingVector, "outgoingPChargingVector"),
                       24: (ct.OriginatedCode, "originatedCode"),
                       121: (ber_decoder.Tag, "reroutingIndicator")
    }

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
