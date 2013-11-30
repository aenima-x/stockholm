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


def get_ascii(byte_string):
    return byte_string.encode('ascii')

## Custom Tags

class AccountCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(AccountCode, self).__init__(header, load_value)
        self.name = "accountCode"

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class AddressString(Tag):
    def __init__(self, header=None, load_value=True):
        super(AddressString, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AddressStringExtended(Tag):
    def __init__(self, header=None, load_value=True):
        super(AddressStringExtended, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AgeOfLocationEstimate(Tag):
    def __init__(self, header=None, load_value=True):
        super(AgeOfLocationEstimate, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AirInterfaceUserRate(Tag):
    def __init__(self, header=None, load_value=True):
        super(AirInterfaceUserRate, self).__init__(header, load_value)


class AoCCurrencyAmountSent(Tag):
    def __init__(self, header=None, load_value=True):
        super(AoCCurrencyAmountSent, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ApplicationIdentifier(Tag):
    def __init__(self, header=None, load_value=True):
        super(ApplicationIdentifier, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AsyncSyncIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(AsyncSyncIndicator, self).__init__(header, load_value)


class BearerServiceCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(BearerServiceCode, self).__init__(header, load_value)
        self.name = "bearerServiceCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string,)


class BitRate(Tag):
    def __init__(self, header=None, load_value=True):
        super(BitRate, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class BSSMAPCauseCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(BSSMAPCauseCode, self).__init__(header, load_value)
        self.name = "bSSMAPCauseCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CallAttemptState(Tag):
    def __init__(self, header=None, load_value=True):
        super(CallAttemptState, self).__init__(header, load_value)


class CallIDNumber(Tag):
    def __init__(self, header=None, load_value=True):
        super(CallIDNumber, self).__init__(header, load_value)
        self.name = "callIdentificationNumber"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CAMELTDPData(Tag):  # TODO ojo es una secuencia
    def __init__(self, header=None, load_value=True):
        super(CAMELTDPData, self).__init__(header, load_value)


class CarrierIdentificationCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(CarrierIdentificationCode, self).__init__(header, load_value)
        self.name = "carrierIdentificationCode"

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CarrierInfo(Tag):
    def __init__(self, header=None, load_value=True):
        super(CarrierInfo, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CarrierInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(CarrierInformation, self).__init__(header, load_value)
        self.name = "carrierInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CarrierSelectionSubstitutionInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(CarrierSelectionSubstitutionInformation, self).__init__(header, load_value)
        self.name = "carrierSelectionSubstitutionInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CauseCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(CauseCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChangeInitiatingParty(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChangeInitiatingParty, self).__init__(header, load_value)


class CallPosition(Tag):
    def __init__(self, header=None, load_value=True):
        super(CallPosition, self).__init__(header, load_value)
        self.name = "callPosition"


class ChannelAllocationPriorityLevel(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChannelAllocationPriorityLevel, self).__init__(header, load_value)
        self.name = "channelAllocationPriorityLevel"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChannelCodings(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChannelCodings, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargeAreaCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargeAreaCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargedParty(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargedParty, self).__init__(header, load_value)
        self.name = "chargedParty"


class ChargeInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargeInformation, self).__init__(header, load_value)
        self.name = "chargeInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingCase(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargingCase, self).__init__(header, load_value)
        self.name = "chargingCase"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargingIndicator, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingOrigin(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargingOrigin, self).__init__(header, load_value)
        self.name = "originForCharging"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingUnitsAddition(Tag):
    def __init__(self, header=None, load_value=True):
        super(ChargingUnitsAddition, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Counter(Tag):
    def __init__(self, header=None, load_value=True):
        super(Counter, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CRIIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(CRIIndicator, self).__init__(header, load_value)


class CRIToMS(Tag):
    def __init__(self, header=None, load_value=True):
        super(CRIToMS, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CUGIndex(Tag):
    def __init__(self, header=None, load_value=True):
        super(CUGIndex, self).__init__(header, load_value)
        self.name = "cUGIndex"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CUGInterlockCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(CUGInterlockCode, self).__init__(header, load_value)
        self.name = "cUGInterlockCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class C7CHTMessage(Tag):
    def __init__(self, header=None, load_value=True):
        super(C7CHTMessage, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class C7ChargingMessage(Tag):
    def __init__(self, header=None, load_value=True):
        super(C7ChargingMessage, self).__init__(header, load_value)
        self.name = "c7ChargingMessage"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Date(Tag):
    def __init__(self, header=None, load_value=True):
        super(Date, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string, 2)


class DecipheringKeys(Tag):
    def __init__(self, header=None, load_value=True):
        super(DecipheringKeys, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class DefaultCallHandling(Tag):
     def __init__(self, header=None, load_value=True):
        super(DefaultCallHandling, self).__init__(header, load_value)


class DefaultSMS_Handling(Tag):
    def __init__(self, header=None, load_value=True):
        super(DefaultSMS_Handling, self).__init__(header, load_value)


class DeliveryOfErroneousSDU(Tag):
    def __init__(self, header=None, load_value=True):
        super(DeliveryOfErroneousSDU, self).__init__(header, load_value)


class DisconnectingParty(Tag):
    def __init__(self, header=None, load_value=True):
        super(DisconnectingParty, self).__init__(header, load_value)
        self.name = "disconnectingParty"


class Distributed(Tag):
    def __init__(self, header=None, load_value=True):
        super(Distributed, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EMLPPPriorityLevel(Tag):
    def __init__(self, header=None, load_value=True):
        super(EMLPPPriorityLevel, self).__init__(header, load_value)
        self.name = "eMLPPPriorityLevel"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EndToEndAccessDataMap(Tag):
    def __init__(self, header=None, load_value=True):
        super(EndToEndAccessDataMap, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EosInfo(Tag):
    def __init__(self, header=None, load_value=True):
        super(EosInfo, self).__init__(header, load_value)
        self.name = "eosInfo"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ErrorRatio(Tag):
    def __init__(self, header=None, load_value=True):
        super(ErrorRatio, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EventCRIToMS(Tag):
    def __init__(self, header=None, load_value=True):
        super(EventCRIToMS, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ExchangeIdentity(Tag):
    def __init__(self, header=None, load_value=True):
        super(ExchangeIdentity, self).__init__(header, load_value)
        self.name = "exchangeIdentity"

    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class FaultCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(FaultCode, self).__init__(header, load_value)
        self.name = "faultCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class FirstRadioChannelUsed(Tag):
    def __init__(self, header=None, load_value=True):
        super(FirstRadioChannelUsed, self).__init__(header, load_value)
        self.name = "firstRadioChannelUsed"


class FixedNetworkUserRate(Tag):
    def __init__(self, header=None, load_value=True):
        super(FixedNetworkUserRate, self).__init__(header, load_value)


class FreeFormatData(Tag):
    def __init__(self, header=None, load_value=True):
        super(FreeFormatData, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class FrequencyBandSupported(Tag):
    def __init__(self, header=None, load_value=True):
        super(FrequencyBandSupported, self).__init__(header, load_value)
        self.name = "frequencyBandSupported"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GenericDigitsSet(Tag):  # TODO Ojo ver
    def __init__(self, header=None, load_value=True):
        super(GenericDigitsSet, self).__init__(header, load_value)


class GenericNumbersSet(Tag):  # TODO Ojo ver
    def __init__(self, header=None, load_value=True):
        super(GenericNumbersSet, self).__init__(header, load_value)


class GlobalCallReference(Tag):
    def __init__(self, header=None, load_value=True):
        super(GlobalCallReference, self).__init__(header, load_value)
        self.name = "globalCallReference"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GlobalTitle(Tag):
    def __init__(self, header=None, load_value=True):
        super(GlobalTitle, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GlobalTitleAndSubSystemNumber(Tag):
    def __init__(self, header=None, load_value=True):
        super(GlobalTitleAndSubSystemNumber, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GSMCallReferenceNumber(Tag):
    def __init__(self, header=None, load_value=True):
        super(GSMCallReferenceNumber, self).__init__(header, load_value)
        self.name = "gSMCallReferenceNumber"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class IMEI(Tag):
    def __init__(self, header=None, load_value=True):
        super(IMEI, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMEISV(Tag):
    def __init__(self, header=None, load_value=True):
        super(IMEISV, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMSI(Tag):
    def __init__(self, header=None, load_value=True):
        super(IMSI, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class INMarkingOfMS(Tag):
    def __init__(self, header=None, load_value=True):
        super(INMarkingOfMS, self).__init__(header, load_value)
        self.name = "iNMarkingOfMS"


class INServiceTrigger(Tag):
    def __init__(self, header=None, load_value=True):
        super(INServiceTrigger, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class IntermediateRate(Tag):
    def __init__(self, header=None, load_value=True):
        super(IntermediateRate, self).__init__(header, load_value)
        self.name = "intermediateRate"


class InternalCauseAndLoc(Tag):
    def __init__(self, header=None, load_value=True):
        super(InternalCauseAndLoc, self).__init__(header, load_value)
        self.name = "internalCauseAndLoc"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class IuCodec(Tag):
    def __init__(self, header=None, load_value=True):
        super(IuCodec, self).__init__(header, load_value)
        self.name = "iuCodec"


class LCSAccuracy(Tag):
    def __init__(self, header=None, load_value=True):
        super(LCSAccuracy, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LCSClientType(Tag):
    def __init__(self, header=None, load_value=True):
        super(LCSClientType, self).__init__(header, load_value)


class LCSDeferredEventType(Tag):
    def __init__(self, header=None, load_value=True):
        super(LCSDeferredEventType, self).__init__(header, load_value)


class LegID(Tag):
    def __init__(self, header=None, load_value=True):
        super(LegID, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LevelOfCAMELService(Tag):
    def __init__(self, header=None, load_value=True):
        super(LevelOfCAMELService, self).__init__(header, load_value)


class LocationCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(LocationCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LocationEstimate(Tag):
    def __init__(self, header=None, load_value=True):
        super(LocationEstimate, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LocationInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(LocationInformation, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MessageReference(Tag):
    def __init__(self, header=None, load_value=True):
        super(MessageReference, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MessageTypeIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(MessageTypeIndicator, self).__init__(header, load_value)


class MiscellaneousInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(MiscellaneousInformation, self).__init__(header, load_value)
        self.name = "miscellaneousInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MobileUserClass1(Tag):
    def __init__(self, header=None, load_value=True):
        super(MobileUserClass1, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MobileUserClass2(Tag):
    def __init__(self, header=None, load_value=True):
        super(MobileUserClass2, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MultimediaInformation(Tag):  # TODO ojo verificar
    def __init__(self, header=None, load_value=True):
        super(MultimediaInformation, self).__init__(header, load_value)
        self.name = "multimediaInformation"


class NetworkCallReference(Tag):
    def __init__(self, header=None, load_value=True):
        super(NetworkCallReference, self).__init__(header, load_value)
        self.name = "networkCallReference"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class NumberOfChannels(Tag):
    def __init__(self, header=None, load_value=True):
        super(NumberOfChannels, self).__init__(header, load_value)


class NumberOfMeterPulses(Tag):
    def __init__(self, header=None, load_value=True):
        super(NumberOfMeterPulses, self).__init__(header, load_value)
        self.name = "numberOfMeterPulses"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class NumberOfOperations(Tag):
    def __init__(self, header=None, load_value=True):
        super(NumberOfOperations, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class NumberOfShortMessage(Tag):
    def __init__(self, header=None, load_value=True):
        super(NumberOfShortMessage, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class OperationIdentifier(Tag):
    def __init__(self, header=None, load_value=True):
        super(OperationIdentifier, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class OptimalRoutingType(Tag):
    def __init__(self, header=None, load_value=True):
        super(OptimalRoutingType, self).__init__(header, load_value)
        self.name = "optimalRoutingType"


class OriginatedCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(OriginatedCode, self).__init__(header, load_value)
        self.name = "originatedCode"


class OriginatingLineInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(OriginatingLineInformation, self).__init__(header, load_value)
        self.name = "originatingLineInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class OutputForSubscriber(Tag):
    def __init__(self, header=None, load_value=True):
        super(OutputForSubscriber, self).__init__(header, load_value)
        self.name = "outputForSubscriber"


class OutputType(Tag):
    def __init__(self, header=None, load_value=True):
        super(OutputType, self).__init__(header, load_value)
        self.name = "outputType"


class PartialOutputRecNum(Tag):
    def __init__(self, header=None, load_value=True):
        super(PartialOutputRecNum, self).__init__(header, load_value)
        self.name = "partialOutputRecNum"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PChargingVector(Tag):
    def __init__(self, header=None, load_value=True):
        super(PChargingVector, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PositioningDelivery(Tag):
    def __init__(self, header=None, load_value=True):
        super(PositioningDelivery, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PointCodeAndSubSystemNumber(Tag):
    def __init__(self, header=None, load_value=True):
        super(PointCodeAndSubSystemNumber, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PositionAccuracy(Tag):
    def __init__(self, header=None, load_value=True):
        super(PositionAccuracy, self).__init__(header, load_value)
        self.name = "positionAccuracy"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PresentationAndScreeningIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(PresentationAndScreeningIndicator, self).__init__(header, load_value)
        self.name = "presentationAndScreeningIndicator"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ProcedureCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(ProcedureCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class RadioChannelProperty(Tag):
    def __init__(self, header=None, load_value=True):
        super(RadioChannelProperty, self).__init__(header, load_value)
        self.name = "radioChannelProperty"


class RANAPCauseCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(RANAPCauseCode, self).__init__(header, load_value)
        self.name = "rANAPCauseCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RecordSequenceNumber(Tag):
    def __init__(self, header=None, load_value=True):
        super(RecordSequenceNumber, self).__init__(header, load_value)
        self.name = "recordSequenceNumber"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RedirectionCounter(Tag):
    def __init__(self, header=None, load_value=True):
        super(RedirectionCounter, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RegionalServiceUsed(Tag):
    def __init__(self, header=None, load_value=True):
        super(RegionalServiceUsed, self).__init__(header, load_value)
        self.name = "regionalServiceUsed"


class ResponseTimeCategory(Tag):
    def __init__(self, header=None, load_value=True):
        super(ResponseTimeCategory, self).__init__(header, load_value)


class RoamingPriorityLevel(Tag):
    def __init__(self, header=None, load_value=True):
        super(RoamingPriorityLevel, self).__init__(header, load_value)
        self.name = "roamingPriorityLevel"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Route(Tag):
    def __init__(self, header=None, load_value=True):
        super(Route, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class RTCDefaultServiceHandling(Tag):
    def __init__(self, header=None, load_value=True):
        super(RTCDefaultServiceHandling, self).__init__(header, load_value)
        self.name = "rTCDefaultServiceHandling"


class RTCFailureIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(RTCFailureIndicator, self).__init__(header, load_value)
        self.name = "rTCFailureIndicator"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RTCNotInvokedReason(Tag):
    def __init__(self, header=None, load_value=True):
        super(RTCNotInvokedReason, self).__init__(header, load_value)
        self.name = "rTCNotInvokedReason"


class RTCSessionID(Tag):
    def __init__(self, header=None, load_value=True):
        super(RTCSessionID, self).__init__(header, load_value)
        self.name = "rTCSessionID"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SelectedCodec(Tag):
    def __init__(self, header=None, load_value=True):
        super(SelectedCodec, self).__init__(header, load_value)
        self.name = "selectedCodec"


class ServiceCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(ServiceCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ServiceFeatureCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(ServiceFeatureCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ServiceKey(Tag):
    def __init__(self, header=None, load_value=True):
        super(ServiceKey, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ServiceSwitchingType(Tag):
    def __init__(self, header=None, load_value=True):
        super(ServiceSwitchingType, self).__init__(header, load_value)


class Single(Tag):
    def __init__(self, header=None, load_value=True):
        super(Single, self).__init__(header, load_value)


class SMSResult(Tag):
    def __init__(self, header=None, load_value=True):
        super(SMSResult, self).__init__(header, load_value)


class SpeechCoderPreferenceList(Tag):
    def __init__(self, header=None, load_value=True):
        super(SpeechCoderPreferenceList, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SpeechCoderVersion(Tag):
    def __init__(self, header=None, load_value=True):
        super(SpeechCoderVersion, self).__init__(header, load_value)


class SSCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(SSCode, self).__init__(header, load_value)
        self.name = "sSCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SSFChargingCase(Tag):
    def __init__(self, header=None, load_value=True):
        super(SSFChargingCase, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SSRequest(Tag):
    def __init__(self, header=None, load_value=True):
        super(SSRequest, self).__init__(header, load_value)


class SubscriberState(Tag):
    def __init__(self, header=None, load_value=True):
        super(SubscriberState, self).__init__(header, load_value)


class SubscriptionType(Tag):
    def __init__(self, header=None, load_value=True):
        super(SubscriptionType, self).__init__(header, load_value)
        self.name = "subscriptionType"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SwitchIdentity(Tag):
    def __init__(self, header=None, load_value=True):
        super(SwitchIdentity, self).__init__(header, load_value)
        self.name = "switchIdentity"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TAC(Tag):
    def __init__(self, header=None, load_value=True):
        super(TAC, self).__init__(header, load_value)
        self.name = "TAC"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TargetRNCid(Tag):
    def __init__(self, header=None, load_value=True):
        super(TargetRNCid, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TariffClass(Tag):
    def __init__(self, header=None, load_value=True):
        super(TariffClass, self).__init__(header, load_value)
        self.name = "tariffClass"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TariffSwitchInd(Tag):
    def __init__(self, header=None, load_value=True):
        super(TariffSwitchInd, self).__init__(header, load_value)
        self.name = "tariffSwitchInd"


class TeleServiceCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(TeleServiceCode, self).__init__(header, load_value)
        self.name = "teleServiceCode"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Time(Tag):
    def __init__(self, header=None, load_value=True):
        super(Time, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string, 2)


class TrafficActivityCode(Tag):
    def __init__(self, header=None, load_value=True):
        super(TrafficActivityCode, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)



class TransferDelay(Tag):
    def __init__(self, header=None, load_value=True):
        super(TransferDelay, self).__init__(header, load_value)
        self.name = "transferDelay"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TransitCarrierInfo(Tag):
    def __init__(self, header=None, load_value=True):
        super(TransitCarrierInfo, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TransparencyIndicator(Tag):
    def __init__(self, header=None, load_value=True):
        super(TransparencyIndicator, self).__init__(header, load_value)
        self.name = "transparencyIndicator"


class TriggerData(Tag):
    def __init__(self, header=None, load_value=True):
        super(TriggerData, self).__init__(header, load_value)


class TriggerDetectionPoint(Tag):
    def __init__(self, header=None, load_value=True):
        super(TriggerDetectionPoint, self).__init__(header, load_value)


class TypeOfCalledSubscriber(Tag):
    def __init__(self, header=None, load_value=True):
        super(TypeOfCalledSubscriber, self).__init__(header, load_value)


class TypeOfCallingSubscriber(Tag):
    def __init__(self, header=None, load_value=True):
        super(TypeOfCallingSubscriber, self).__init__(header, load_value)
        self.name = "typeOfCallingSubscriber"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TypeOfLocationRequest(Tag):
    def __init__(self, header=None, load_value=True):
        super(TypeOfLocationRequest, self).__init__(header, load_value)


class TypeOfSignalling(Tag):
    def __init__(self, header=None, load_value=True):
        super(TypeOfSignalling, self).__init__(header, load_value)


class UILayer1Protocol(Tag):
    def __init__(self, header=None, load_value=True):
        super(UILayer1Protocol, self).__init__(header, load_value)


class UnsuccessfulPositioningDataReason(Tag):
    def __init__(self, header=None, load_value=True):
        super(UnsuccessfulPositioningDataReason, self).__init__(header, load_value)


class UserClass(Tag):
    def __init__(self, header=None, load_value=True):
        super(UserClass, self).__init__(header, load_value)
        self.name = "userClass"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserRate(Tag):
    def __init__(self, header=None, load_value=True):
        super(UserRate, self).__init__(header, load_value)


class UserTerminalPosition(Tag):
    def __init__(self, header=None, load_value=True):
        super(UserTerminalPosition, self).__init__(header, load_value)
        self.name = "userTerminalPosition"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserToUserInformation(Tag):
    def __init__(self, header=None, load_value=True):
        super(UserToUserInformation, self).__init__(header, load_value)
        self.name = "userToUserInformation"

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserToUserService1Information(Tag):
    def __init__(self, header=None, load_value=True):
        super(UserToUserService1Information, self).__init__(header, load_value)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)
######
