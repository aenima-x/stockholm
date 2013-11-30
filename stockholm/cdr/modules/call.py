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
    _data_tag_types = {0: (ct.TAC,),
                       1: (ct.CallIDNumber,),
                       2: (ct.RecordSequenceNumber,),
                       3: (ct.TypeOfCallingSubscriber,),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.AddressString, "calledPartyNumber"),
                       6: (ct.IMSI, "calledSubscriberIMSI"),
                       7: (ct.DisconnectingParty,),
                       8: (ct.Date, "dateForStartOfCharge"),
                       9: (ct.Time, "timeForStartOfCharge"),
                       10: (ct.Time, "timeForStopOfCharge"),
                       11: (ct.Time, "chargeableDuration"),
                       12: (ct.Time, "interruptionTime"),
                       13: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       14: (ct.ChargedParty,),
                       15: (ct.ChargingOrigin,),
                       16: (ct.TariffClass,),
                       17: (ct.TariffSwitchInd,),
                       18: (ct.NumberOfMeterPulses,),
                       19: (ct.ExchangeIdentity,),
                       20: (ct.AddressString, "mSCIdentification"),
                       21: (ct.Route, "outgoingRoute"),
                       22: (ct.Route, "incomingRoute"),
                       23: (ct.MiscellaneousInformation,),
                       25: (ct.INMarkingOfMS,),
                       26: (ct.CallPosition,),
                       27: (ct.EosInfo,),
                       28: (ct.InternalCauseAndLoc,),
                       29: (ct.AddressString, "originalCalledNumber"),
                       30: (ct.AddressString, "redirectingNumber"),
                       31: (ct.RedirectionCounter,),
                       32: (ct.AddressString, "redirectingDropBackNumber"),
                       33: (ct.Tag, "redirectingDropBack"),
                       34: (ct.Tag, "restartDuringCall"),
                       35: (ct.Tag, "restartDuringOutputIndicator"),
                       36: (ct.Tag, "iCIOrdered"),
                       37: (ct.OutputForSubscriber,),
                       38: (ct.Tag, "lastPartialOutput"),
                       39: (ct.PartialOutputRecNum,),
                       40: (ct.CallIDNumber, "relatedCallNumber"),
                       41: (ct.FaultCode,),
                       42: (ct.SubscriptionType,),
                       43: (ct.Tag, "incompleteCallDataIndicator"),
                       44: (ct.Tag, "incompleteCompositeCDRIndicator"),
                       45: (ct.SwitchIdentity,),
                       46: (ct.NetworkCallReference,),
                       47: (ct.Tag, "disconnectionDueToSystemRecovery"),
                       48: (ct.Tag, "forloppDuringOutputIndicator"),
                       49: (ct.Tag, "forloppReleaseDuringCall"),
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
                       61: (ct.GSMCallReferenceNumber,),
                       62: (ct.C7ChargingMessage,),
                       63: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       64: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       65: (ct.ChargingIndicator, "aCMChargingIndicator"),
                       66: (ct.ChargingIndicator, "aNMChargingIndicator"),
                       67: (ct.AddressString, "mSCAddress"),
                       68: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       69: (ct.TransitCarrierInfo, "carrierInformationForward"),
                       70: (ct.ChargeInformation,),
                       71: (ct.Date, "disconnectionDate"),
                       72: (ct.Time, "disconnectionTime"),
                       73: (ct.ChargeAreaCode, "entryPOICA"),
                       74: (ct.ChargeAreaCode, "exitPOICA"),
                       75: (ct.Tag, "internationalCallIndicator"),
                       76: (ct.MobileUserClass1, "mobileUserClass1"),
                       77: (ct.MobileUserClass2, "mobileUserClass2"),
                       78: (ct.Tag, "originatingAccessISDN"),
                       79: (ct.CarrierInfo, "originatingCarrier"),
                       80: (ct.ChargeAreaCode, "originatingChargeArea"),
                       81: (ct.Counter, "tDSCounter"),
                       82: (ct.Tag, "terminatingAccessISDN"),
                       83: (ct.CarrierInfo, "terminatingCarrier"),
                       84: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       85: (ct.MobileUserClass1, "terminatingMobileUserClass1"),
                       86: (ct.MobileUserClass2, "terminatingMobileUserClass2"),
                       87: (ct.AddressString, "contractorNumber"),
                       88: (ct.UserClass, "terminatingUserClass"),
                       89: (ct.UserClass,),
                       90: (ct.AddressString, "calledPartyMNPInfo"),
                       91: (ct.AddressString, "chargeNumber"),
                       92: (ct.OriginatingLineInformation,),
                       93: (ct.MultimediaInformation,),
                       94: (ct.GlobalCallReference,),
                       95: (ct.Tag, "rTCIndicator"),
                       96: (ct.RTCSessionID,),
                       97: (ct.RTCDefaultServiceHandling,),
                       98: (ct.RTCFailureIndicator,),
                       99: (ct.RTCNotInvokedReason,),
                       100: (ct.AddressString, "calledDirectoryNumber"),
                       101: (ct.PChargingVector, "incomingPChargingVector"),
                       102: (ct.OutputType,),
                       103: (ct.PChargingVector, "outgoingPChargingVector"),
                       24: (ct.OriginatedCode,),
                       121: (ct.Tag, "reroutingIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(Transit, self).__init__(tag, byte_string)


class MSOriginating(CallModule):
    _data_tag_types = {0: (ct.TAC,),
                       1: (ct.CallIDNumber,),
                       2: (ct.RecordSequenceNumber,),
                       3: (ct.TypeOfCallingSubscriber,),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.IMSI, "callingSubscriberIMSI"),
                       6: (ct.IMEI, "callingSubscriberIMEI"),
                       7: (ct.AddressString, "calledPartyNumber"),
                       8: (ct.DisconnectingParty, "disconnectingParty"),
                       9: (ct.Date, "dateForStartOfCharge"),
                       10: (ct.Time, "timeForStartOfCharge"),
                       11: (ct.Time, "timeForStopOfCharge"),
                       12: (ct.Time, "chargeableDuration"),
                       13: (ct.Time, "interruptionTime"),
                       14: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       15: (ct.ChargedParty,),
                       16: (ct.ChargingOrigin,),
                       17: (ct.ChargingCase,),
                       18: (ct.TariffClass,),
                       19: (ct.TariffSwitchInd,),
                       20: (ct.ExchangeIdentity,),
                       21: (ct.AddressString, "mSCIdentification"),
                       22: (ct.Route, "outgoingRoute"),
                       23: (ct.Route, "incomingRoute"),
                       24: (ct.MiscellaneousInformation,),
                       25: (ct.AddressString, "originatingLocationNumber"),
                       26: (ct.Time, "timeForTCSeizureCalling"),
                       27: (ct.LocationInformation, "firstCallingLocationInformation"),
                       28: (ct.LocationInformation, "lastCallingLocationInformation"),
                       29: (ct.TeleServiceCode,),
                       30: (ct.BearerServiceCode,),
                       31: (ct.TransparencyIndicator,),
                       32: (ct.FirstRadioChannelUsed,),
                       33: (ct.CallPosition,),
                       34: (ct.EosInfo,),
                       35: (ct.InternalCauseAndLoc,),
                       36: (ct.Tag, "restartDuringCall"),
                       37: (ct.Tag, "restartDuringOutputIndicator"),
                       38: (ct.NumberOfMeterPulses,),
                       39: (ct.C7ChargingMessage,),
                       40: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       41: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       42: (ct.AddressString, "calledPartyMNPInfo"),
                       43: (ct.CarrierIdentificationCode,),
                       44: (ct.Tag, "dTMFUsed"),
                       45: (ct.Tag, "iCIOrdered"),
                       46: (ct.OutputForSubscriber,),
                       47: (ct.INMarkingOfMS,),
                       48: (ct.Tag, "lastPartialOutput"),
                       49: (ct.PartialOutputRecNum,),
                       50: (ct.CUGInterlockCode,),
                       51: (ct.CUGIndex,),
                       52: (ct.Tag, "cUGOutgoingAccessUsed"),
                       53: (ct.Tag, "cUGOutgoingAccessIndicator"),
                       54: (ct.RegionalServiceUsed,),
                       55: (ct.ChargingOrigin, "regionDependentChargingOrigin"),
                       56: (ct.SSCode,),
                       57: (ct.ChannelAllocationPriorityLevel,),
                       58: (ct.RadioChannelProperty,),
                       59: (ct.FaultCode,),
                       60: (ct.IntermediateRate,),
                       61: (ct.SpeechCoderVersion, "firstAssignedSpeechCoderVersion"),
                       62: (ct.SpeechCoderPreferenceList, "speechCoderPreferenceList"),
                       63: (ct.SubscriptionType,),
                       64: (ct.Tag, "incompleteCallDataIndicator"),
                       65: (ct.Tag, "incompleteCompositeCDRIndicator"),
                       67: (ct.SwitchIdentity,),
                       68: (ct.NetworkCallReference,),
                       69: (ct.FrequencyBandSupported,),
                       70: (ct.Tag, "disconnectionDueToSystemRecovery"),
                       71: (ct.Tag, "forloppDuringOutputIndicator"),
                       72: (ct.Tag, "forloppReleaseDuringCall"),
                       73: (ct.AccountCode,),
                       74: (ct.AddressString, "translatedNumber"),
                       75: (ct.CAMELTDPData, "bCSMTDPData1"),
                       76: (ct.CAMELTDPData, "bCSMTDPData2"),
                       77: (ct.CAMELTDPData, "bCSMTDPData3"),
                       78: (ct.CAMELTDPData, "bCSMTDPData4"),
                       79: (ct.CAMELTDPData, "bCSMTDPData5"),
                       80: (ct.CAMELTDPData, "bCSMTDPData6"),
                       81: (ct.CAMELTDPData, "bCSMTDPData7"),
                       82: (ct.CAMELTDPData, "bCSMTDPData8"),
                       83: (ct.CAMELTDPData, "bCSMTDPData9"),
                       84: (ct.CAMELTDPData, "bCSMTDPData10"),
                       85: (ct.GSMCallReferenceNumber,),
                       86: (ct.AddressString, "mSCAddress"),
                       87: (ct.EMLPPPriorityLevel,),
                       88: (ct.PositionAccuracy,),
                       89: (ct.UserTerminalPosition,),
                       90: (ct.ChannelCodings, "acceptableChannelCodings"),
                       91: (ct.Route, "incomingAssignedRoute"),
                       92: (ct.ChannelCodings, "channelCodingUsed"),
                       93: (ct.RANAPCauseCode,),
                       94: (ct.AddressString, "gsmSCFAddress"),
                       95: (ct.FixedNetworkUserRate, "fNURRequested"),
                       96: (ct.AirInterfaceUserRate, "aIURRequested"),
                       97: (ct.NumberOfChannels, "numberOfChannelsRequested"),
                       98: (ct.BSSMAPCauseCode,),
                       99: (ct.Tag, "multimediaCall"),
                       100: (ct.BitRate, "guaranteedBitRate"),
                       101: (ct.TariffClass,),
                       102: (ct.OutputType,),
                       103: (ct.TargetRNCid, "rNCidOfFirstRNC"),
                       104: (ct.BitRate, "maxBitRateDownlink"),
                       105: (ct.BitRate, "maxBitRateUplink"),
                       106: (ct.TransferDelay,),
                       107: (ct.DeliveryOfErroneousSDU, "deliveryOfErroneousSDU1"),
                       108: (ct.DeliveryOfErroneousSDU, "deliveryOfErroneousSDU2"),
                       109: (ct.DeliveryOfErroneousSDU, "deliveryOfErroneousSDU3"),
                       110: (ct.ErrorRatio, "residualBitErrorRatio1"),
                       111: (ct.ErrorRatio, "residualBitErrorRatio2"),
                       112: (ct.ErrorRatio, "residualBitErrorRatio3"),
                       113: (ct.ErrorRatio, "sDUErrorRatio1"),
                       114: (ct.ErrorRatio, "sDUErrorRatio2"),
                       115: (ct.ErrorRatio, "sDUErrorRatio3"),
                       116: (ct.ChargingIndicator, "aCMChargingIndicator"),
                       117: (ct.ChargingIndicator, "aNMChargingIndicator"),
                       118: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       119: (ct.ChargeInformation,),
                       120: (ct.Date, "disconnectionDate"),
                       124: (ct.Time, "disconnectionTime"),
                       125: (ct.CarrierInfo, "originatingCarrier"),
                       126: (ct.ChargeAreaCode, "originatingChargeArea"),
                       127: (ct.Counter, "tDSCounter"),
                       128: (ct.Tag, "terminatingAccessISDN"),
                       129: (ct.CarrierInfo, "terminatingCarrier"),
                       130: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       131: (ct.MobileUserClass1, "terminatingMobileUserClass1"),
                       132: (ct.MobileUserClass2, "terminatingMobileUserClass2"),
                       133: (ct.UserClass, "terminatingUserClass"),
                       134: (ct.AddressString, "contractorNumber"),
                       135: (ct.CarrierInformation,),
                       136: (ct.CarrierSelectionSubstitutionInformation,),
                       137: (ct.AddressString, "chargeNumber"),
                       138: (ct.Tag, "interExchangeCarrierIndicator"),
                       139: (ct.OriginatingLineInformation,),
                       140: (ct.SelectedCodec,),
                       141: (ct.Tag, "wPSCallIndicator"),
                       142: (ct.UserToUserService1Information,),
                       143: (ct.IMEISV, "callingSubscriberIMEISV"),
                       144: (ct.GlobalCallReference,),
                       145: (ct.RoamingPriorityLevel,),
                       146: (ct.Tag, "rTCIndicator"),
                       147: (ct.RTCSessionID,),
                       148: (ct.RTCDefaultServiceHandling,),
                       149: (ct.RTCFailureIndicator,),
                       150: (ct.RTCNotInvokedReason,),
                       151: (ct.AddressString,"calledDirectoryNumber"),
                       152: (ct.PChargingVector, "outgoingPChargingVector"),
                       153: (ct.IuCodec,),
                       66: (ct.OriginatedCode,),
                       121: (ct.Tag, "reroutingIndicator"),
                       122: (ct.Tag, "invocationOfCallHold"),
                       123: (ct.Tag, "retrievalOfHeldCall")
  }

    def __init__(self, tag=None, byte_string=None):
        super(MSOriginating, self).__init__(tag, byte_string)


class RoamingCallForwarding(CallModule):
    _data_tag_types = {0: (ct.TAC,),
                       1: (ct.CallIDNumber,),
                       2: (ct.RecordSequenceNumber,),
                       3: (ct.TypeOfCallingSubscriber,),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.AddressString, "calledPartyNumber"),
                       6: (ct.IMSI, "calledSubscriberIMSI"),
                       7: (ct.AddressString, "mobileStationRoamingNumber"),
                       8: (ct.DisconnectingParty,),
                       9: (ct.Date, "dateForStartOfCharge"),
                       10: (ct.Time, "timeForStartOfCharge"),
                       11: (ct.Time, "timeForStopOfCharge"),
                       12: (ct.Time, "chargeableDuration"),
                       13: (ct.Time, "interruptionTime"),
                       14: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       15: (ct.ChargedParty,),
                       16: (ct.ChargingOrigin,),
                       17: (ct.TariffClass,),
                       18: (ct.TariffSwitchInd,),
                       19: (ct.ExchangeIdentity,),
                       20: (ct.AddressString, "mSCIdentification"),
                       21: (ct.Route, "outgoingRoute"),
                       22: (ct.Route, "incomingRoute"),
                       23: (ct.MiscellaneousInformation,),
                       24: (ct.SubscriptionType,),
                       25: (ct.CallPosition,),
                       26: (ct.EosInfo,),
                       27: (ct.InternalCauseAndLoc,),
                       28: (ct.AddressString, "originalCalledNumber"),
                       29: (ct.AddressString, "redirectingNumber"),
                       30: (ct.RedirectionCounter,),
                       31: (ct.Tag, "restartDuringCall"),
                       32: (ct.Tag, "restartDuringOutputIndicator"),
                       33: (ct.NumberOfMeterPulses,),
                       34: (ct.C7ChargingMessage,),
                       35: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       36: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       37: (ct.Tag, "iCIOrdered"),
                       38: (ct.OutputForSubscriber,),
                       39: (ct.Tag, "lastPartialOutput"),
                       40: (ct.PartialOutputRecNum,),
                       41: (ct.CallIDNumber, "relatedCallNumber"),
                       42: (ct.CUGInterlockCode,),
                       43: (ct.Tag, "cUGOutgoingAccessIndicator"),
                       44: (ct.PresentationAndScreeningIndicator,),
                       45: (ct.FaultCode,),
                       46: (ct.Tag, "incompleteCallDataIndicator"),
                       47: (ct.MultimediaInformation,),
                       48: (ct.SwitchIdentity,),
                       49: (ct.NetworkCallReference,),
                       50: (ct.Tag, "disconnectionDueToSystemRecovery"),
                       51: (ct.Tag, "forloppDuringOutputIndicator"),
                       52: (ct.Tag, "forloppReleaseDuringCall"),
                       53: (ct.GSMCallReferenceNumber,),
                       54: (ct.AddressString, "mSCAddress"),
                       55: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       56: (ct.Tag, "originatingAccessISDN"),
                       57: (ct.CarrierInfo, "originatingCarrier"),
                       58: (ct.ChargeAreaCode, "originatingChargeArea"),
                       59: (ct.Tag, "terminatingAccessISDN"),
                       60: (ct.CarrierInfo, "terminatingCarrier"),
                       61: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       62: (ct.AddressString, "contractorNumber"),
                       63: (ct.CarrierIdentificationCode,),
                       64: (ct.CarrierInformation,),
                       65: (ct.CarrierSelectionSubstitutionInformation,),
                       66: (ct.AddressString, "chargeNumber"),
                       67: (ct.Tag, "interExchangeCarrierIndicator"),
                       68: (ct.OriginatingLineInformation,),
                       69: (ct.UserToUserInformation,),
                       70: (ct.GlobalCallReference,),
                       71: (ct.Tag, "rTCIndicator"),
                       72: (ct.RTCSessionID,),
                       73: (ct.RTCDefaultServiceHandling,),
                       74: (ct.RTCFailureIndicator,),
                       75: (ct.RTCNotInvokedReason,),
                       76: (ct.AddressString, "mobileSubscriberNumberForHLRInterrogation"),
                       77: (ct.PChargingVector, "outgoingPChargingVector"),
                       102: (ct.OutputType,),
                       121: (ct.Tag, "reroutingIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(RoamingCallForwarding, self).__init__(tag, byte_string)


class CallForwarding(CallModule):
    _data_tag_types = {0: (ct.TAC,),
                       1: (ct.CallIDNumber,),
                       2: (ct.RecordSequenceNumber,),
                       3: (ct.TypeOfCallingSubscriber,),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.AddressString, "calledPartyNumber"),
                       6: (ct.AddressString, "originalCalledNumber"),
                       7: (ct.AddressString, "redirectingNumber"),
                       8: (ct.RedirectionCounter,),
                       9: (ct.AddressString, "redirectingSPN"),
                       10: (ct.IMSI, "redirectingIMSI"),
                       11: (ct.AddressString, "mobileStationRoamingNumber"),
                       12: (ct.DisconnectingParty,),
                       13: (ct.Date, "dateForStartOfCharge"),
                       14: (ct.Time, "timeForStartOfCharge"),
                       15: (ct.Time, "timeForStopOfCharge"),
                       16: (ct.Time, "chargeableDuration"),
                       17: (ct.Time, "interruptionTime"),
                       18: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       19: (ct.ChargedParty,),
                       20: (ct.ChargingOrigin,),
                       21: (ct.TariffClass,),
                       22: (ct.TariffSwitchInd,),
                       23: (ct.ExchangeIdentity,),
                       24: (ct.AddressString, "mSCIdentification"),
                       25: (ct.Route, "outgoingRoute"),
                       26: (ct.Route, "incomingRoute"),
                       27: (ct.MiscellaneousInformation,),
                       28: (ct.AddressString, "originatingLocationNumber"),
                       29: (ct.CallPosition,),
                       30: (ct.EosInfo,),
                       31: (ct.InternalCauseAndLoc,),
                       32: (ct.Tag, "restartDuringCall"),
                       33: (ct.Tag, "restartDuringOutputIndicator"),
                       34: (ct.NumberOfMeterPulses,),
                       35: (ct.C7ChargingMessage,),
                       36: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       37: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       38: (ct.Tag, "iCIOrdered"),
                       39: (ct.OutputForSubscriber,),
                       40: (ct.INMarkingOfMS,),
                       41: (ct.Tag, "lastPartialOutput"),
                       42: (ct.PartialOutputRecNum,),
                       43: (ct.CallIDNumber, "relatedCallNumber"),
                       44: (ct.CUGInterlockCode,),
                       45: (ct.CUGIndex,),
                       46: (ct.Tag, "cUGOutgoingAccessUsed"),
                       47: (ct.Tag, "cUGOutgoingAccessIndicator"),
                       48: (ct.RegionalServiceUsed,),
                       49: (ct.ChargingOrigin,),
                       50: (ct.PresentationAndScreeningIndicator,),
                       51: (ct.FaultCode,),
                       52: (ct.SubscriptionType,),
                       53: (ct.Tag, "incompleteCallDataIndicator"),
                       54: (ct.Tag, "incompleteCompositeCDRIndicator"),
                       56: (ct.SwitchIdentity,),
                       57: (ct.NetworkCallReference,),
                       58: (ct.Tag, "disconnectionDueToSystemRecovery"),
                       59: (ct.Tag, "forloppDuringOutputIndicator"),
                       60: (ct.Tag, "forloppReleaseDuringCall"),
                       61: (ct.AddressString, "translatedNumber"),
                       62: (ct.Tag, "cAMELInitiatedCallForwarding"),
                       63: (ct.CAMELTDPData, "bCSMTDPData1"),
                       64: (ct.CAMELTDPData, "bCSMTDPData2"),
                       65: (ct.CAMELTDPData, "bCSMTDPData3"),
                       66: (ct.CAMELTDPData, "bCSMTDPData4"),
                       67: (ct.CAMELTDPData, "bCSMTDPData5"),
                       68: (ct.CAMELTDPData, "bCSMTDPData6"),
                       69: (ct.CAMELTDPData, "bCSMTDPData7"),
                       70: (ct.CAMELTDPData, "bCSMTDPData8"),
                       71: (ct.CAMELTDPData, "bCSMTDPData9"),
                       72: (ct.CAMELTDPData, "bCSMTDPData10"),
                       73: (ct.GSMCallReferenceNumber,),
                       74: (ct.AddressString, "mSCAddress"),
                       75: (ct.ChargingIndicator, "aCMChargingIndicator"),
                       76: (ct.ChargingIndicator, "aNMChargingIndicator"),
                       77: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       78: (ct.ChargeInformation,),
                       79: (ct.Date, "disconnectionDate"),
                       80: (ct.Time, "disconnectionTime"),
                       81: (ct.ChargeAreaCode, "exitPOICA"),
                       82: (ct.CarrierInfo, "originatingCarrier"),
                       83: (ct.ChargeAreaCode, "originatingChargeArea"),
                       84: (ct.Tag, "terminatingAccessISDN"),
                       85: (ct.CarrierInfo, "terminatingCarrier"),
                       86: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       87: (ct.MobileUserClass1, "terminatingMobileUserClass1"),
                       88: (ct.MobileUserClass2, "terminatingMobileUserClass2"),
                       89: (ct.UserClass, "terminatingUserClass"),
                       90: (ct.Tag, "originatingAccessISDN"),
                       91: (ct.AddressString, "contractorNumber"),
                       92: (ct.AddressString, "calledPartyMNPInfo"),
                       93: (ct.CarrierIdentificationCode,),
                       94: (ct.CarrierInformation,),
                       95: (ct.CarrierSelectionSubstitutionInformation,),
                       96: (ct.AddressString, "chargeNumber"),
                       97: (ct.Tag, "interExchangeCarrierIndicator"),
                       98: (ct.OriginatingLineInformation,),
                       99: (ct.OptimalRoutingType,),
                       100: (ct.Tag, "optimalRoutingInvocationFailed"),
                       101: (ct.UserToUserInformation,),
                       102: (ct.OutputType,),
                       103: (ct.MultimediaInformation,),
                       104: (ct.GlobalCallReference,),
                       105: (ct.Tag, "rTCIndicator"),
                       106: (ct.RTCSessionID,),
                       107: (ct.RTCDefaultServiceHandling,),
                       108: (ct.RTCFailureIndicator,),
                       109: (ct.RTCNotInvokedReason,),
                       110: (ct.AddressString, "calledDirectoryNumber"),
                       111: (ct.PChargingVector, "outgoingPChargingVector"),
                       55: (ct.OriginatedCode,),
                       121: (ct.Tag, "reroutingIndicator")
    }

    def __init__(self, tag=None, byte_string=None):
        super(CallForwarding, self).__init__(tag, byte_string)


class MSTerminating(CallModule):  # ACA!!!
    _data_tag_types = {0: (ct.TAC,),
                       1: (ct.CallIDNumber,),
                       2: (ct.RecordSequenceNumber,),
                       3: (ct.TypeOfCallingSubscriber,),
                       4: (ct.AddressString, "callingPartyNumber"),
                       5: (ct.AddressString, "calledPartyNumber"),
                       6: (ct.AddressString, "originalCalledNumber"),
                       7: (ct.AddressString, "redirectingNumber"),
                       8: (ct.RedirectionCounter,),
                       9: (ct.AddressString, "redirectingSPN"),
                       10: (ct.IMSI, "redirectingIMSI"),
                       11: (ct.AddressString, "mobileStationRoamingNumber"),
                       12: (ct.DisconnectingParty,),
                       13: (ct.Date, "dateForStartOfCharge"),
                       14: (ct.Time, "timeForStartOfCharge"),
                       15: (ct.Time, "timeForStopOfCharge"),
                       16: (ct.Time, "chargeableDuration"),
                       17: (ct.Time, "interruptionTime"),
                       18: (ct.Time, "timeFromRegisterSeizureToStartOfCharging"),
                       19: (ct.ChargedParty,),
                       20: (ct.ChargingOrigin,),
                       21: (ct.TariffClass,),
                       22: (ct.TariffSwitchInd,),
                       23: (ct.ExchangeIdentity,),
                       24: (ct.AddressString, "mSCIdentification"),
                       25: (ct.Route, "outgoingRoute"),
                       26: (ct.Route, "incomingRoute"),
                       27: (ct.MiscellaneousInformation,),
                       28: (ct.AddressString, "originatingLocationNumber"),
                       29: (ct.CallPosition,),
                       30: (ct.EosInfo,),
                       31: (ct.InternalCauseAndLoc,),
                       32: (ct.Tag, "restartDuringCall"),
                       33: (ct.Tag, "restartDuringOutputIndicator"),
                       34: (ct.NumberOfMeterPulses,),
                       35: (ct.C7ChargingMessage,),
                       36: (ct.C7CHTMessage, "c7FirstCHTMessage"),
                       37: (ct.C7CHTMessage, "c7SecondCHTMessage"),
                       38: (ct.Tag, "iCIOrdered"),
                       39: (ct.OutputForSubscriber,),
                       40: (ct.INMarkingOfMS,),
                       41: (ct.Tag, "lastPartialOutput"),
                       42: (ct.PartialOutputRecNum,),
                       43: (ct.CallIDNumber, "relatedCallNumber"),
                       44: (ct.CUGInterlockCode,),
                       45: (ct.CUGIndex,),
                       46: (ct.Tag, "cUGOutgoingAccessUsed"),
                       47: (ct.Tag, "cUGOutgoingAccessIndicator"),
                       48: (ct.RegionalServiceUsed,),
                       49: (ct.ChargingOrigin,),
                       50: (ct.PresentationAndScreeningIndicator,),
                       51: (ct.FaultCode,),
                       52: (ct.SubscriptionType,),
                       53: (ct.Tag, "incompleteCallDataIndicator"),
                       54: (ct.Tag, "incompleteCompositeCDRIndicator"),
                       56: (ct.SwitchIdentity,),
                       57: (ct.NetworkCallReference,),
                       58: (ct.Tag, "disconnectionDueToSystemRecovery"),
                       59: (ct.Tag, "forloppDuringOutputIndicator"),
                       60: (ct.Tag, "forloppReleaseDuringCall"),
                       61: (ct.AddressString, "translatedNumber"),
                       62: (ct.Tag, "cAMELInitiatedCallForwarding"),
                       63: (ct.CAMELTDPData, "bCSMTDPData1"),
                       64: (ct.CAMELTDPData, "bCSMTDPData2"),
                       65: (ct.CAMELTDPData, "bCSMTDPData3"),
                       66: (ct.CAMELTDPData, "bCSMTDPData4"),
                       67: (ct.CAMELTDPData, "bCSMTDPData5"),
                       68: (ct.CAMELTDPData, "bCSMTDPData6"),
                       69: (ct.CAMELTDPData, "bCSMTDPData7"),
                       70: (ct.CAMELTDPData, "bCSMTDPData8"),
                       71: (ct.CAMELTDPData, "bCSMTDPData9"),
                       72: (ct.CAMELTDPData, "bCSMTDPData10"),
                       73: (ct.GSMCallReferenceNumber,),
                       74: (ct.AddressString, "mSCAddress"),
                       75: (ct.ChargingIndicator, "aCMChargingIndicator"),
                       76: (ct.ChargingIndicator, "aNMChargingIndicator"),
                       77: (ct.TransitCarrierInfo, "carrierInformationBackward"),
                       78: (ct.ChargeInformation,),
                       79: (ct.Date, "disconnectionDate"),
                       80: (ct.Time, "disconnectionTime"),
                       81: (ct.ChargeAreaCode, "exitPOICA"),
                       82: (ct.CarrierInfo, "originatingCarrier"),
                       83: (ct.ChargeAreaCode, "originatingChargeArea"),
                       84: (ct.Tag, "terminatingAccessISDN"),
                       85: (ct.CarrierInfo, "terminatingCarrier"),
                       86: (ct.ChargeAreaCode, "terminatingChargeArea"),
                       87: (ct.MobileUserClass1, "terminatingMobileUserClass1"),
                       88: (ct.MobileUserClass2, "terminatingMobileUserClass2"),
                       89: (ct.UserClass, "terminatingUserClass"),
                       90: (ct.Tag, "originatingAccessISDN"),
                       91: (ct.AddressString, "contractorNumber"),
                       92: (ct.AddressString, "calledPartyMNPInfo"),
                       93: (ct.CarrierIdentificationCode,),
                       94: (ct.CarrierInformation,),
                       95: (ct.CarrierSelectionSubstitutionInformation,),
                       96: (ct.AddressString, "chargeNumber"),
                       97: (ct.Tag, "interExchangeCarrierIndicator"),
                       98: (ct.OriginatingLineInformation,),
                       99: (ct.OptimalRoutingType,),
                       100: (ct.Tag, "optimalRoutingInvocationFailed"),
                       101: (ct.UserToUserInformation,),
                       102: (ct.OutputType,),
                       103: (ct.MultimediaInformation,),
                       104: (ct.GlobalCallReference,),
                       105: (ct.Tag, "rTCIndicator"),
                       106: (ct.RTCSessionID,),
                       107: (ct.RTCDefaultServiceHandling,),
                       108: (ct.RTCFailureIndicator,),
                       109: (ct.RTCNotInvokedReason,),
                       110: (ct.AddressString, "calledDirectoryNumber"),
                       111: (ct.PChargingVector, "outgoingPChargingVector"),
                       55: (ct.OriginatedCode,),
                       121: (ct.Tag, "reroutingIndicator")
    }

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
