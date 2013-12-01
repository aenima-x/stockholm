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


def get_hex_string(byte_string):
    return "".join(map(lambda x: x.encode('hex'), byte_string))


def get_ascii(byte_string):
    return byte_string.encode('ascii')


def get_int(byte_string):
    return int(byte_string.encode('hex'), 16)

## Custom Tags

class AccountCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "accountCode"
        super(AccountCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class AddressString(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(AddressString, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class AddressStringExtended(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(AddressStringExtended, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_hex_string(byte_string)


class AgeOfLocationEstimate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "ageOfLocationEstimate"
        super(AgeOfLocationEstimate, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AirInterfaceUserRate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(AirInterfaceUserRate, self).__init__(header, byte_string, load_value, name)


class AoCCurrencyAmountSent(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "aoCCurrencyAmountSentToUser"
        super(AoCCurrencyAmountSent, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ApplicationIdentifier(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ApplicationIdentifier, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class AsyncSyncIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(AsyncSyncIndicator, self).__init__(header, byte_string, load_value, name)


class BearerServiceCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "bearerServiceCode"
        super(BearerServiceCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string,)


class BitRate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(BitRate, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class BSSMAPCauseCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "bSSMAPCauseCode"
        super(BSSMAPCauseCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CallAttemptState(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "callAttemptState"
        super(CallAttemptState, self).__init__(header, byte_string, load_value, name)


class CallIDNumber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "callIdentificationNumber"
        super(CallIDNumber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class CAMELTDPData(Tag):  # TODO ojo es una secuencia
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(CAMELTDPData, self).__init__(header, byte_string, load_value, name)


class CarrierIdentificationCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "carrierIdentificationCode"
        super(CarrierIdentificationCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CarrierInfo(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(CarrierInfo, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CarrierInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "carrierInformation"
        super(CarrierInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CarrierSelectionSubstitutionInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "carrierSelectionSubstitutionInformation"
        super(CarrierSelectionSubstitutionInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CauseCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "causeCode"
        super(CauseCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChangeInitiatingParty(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "changeInitiatingParty"
        super(ChangeInitiatingParty, self).__init__(header, byte_string, load_value, name)


class CallPosition(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "callPosition"
        super(CallPosition, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)

class ChannelAllocationPriorityLevel(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "channelAllocationPriorityLevel"
        super(ChannelAllocationPriorityLevel, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChannelCodings(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ChannelCodings, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargeAreaCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ChargeAreaCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargedParty(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "chargedParty"
        super(ChargedParty, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)



class ChargeInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "chargeInformation"
        super(ChargeInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingCase(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "chargingCase"
        super(ChargingCase, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ChargingIndicator, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingOrigin(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "originForCharging"
        super(ChargingOrigin, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ChargingUnitsAddition(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "chargingUnitsAddition"
        super(ChargingUnitsAddition, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Counter(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Counter, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CRIIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "cRIIndicator"
        super(CRIIndicator, self).__init__(header, byte_string, load_value, name)


class CRIToMS(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "cRIToMS"
        super(CRIToMS, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CUGIndex(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "cUGIndex"
        super(CUGIndex, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class CUGInterlockCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "cUGInterlockCode"
        super(CUGInterlockCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class C7CHTMessage(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(C7CHTMessage, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class C7ChargingMessage(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "c7ChargingMessage"
        super(C7ChargingMessage, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Date(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Date, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string, 2)


class DecipheringKeys(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "decipheringKeys"
        super(DecipheringKeys, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class DefaultCallHandling(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "defaultCallHandling"
        super(DefaultCallHandling, self).__init__(header, byte_string, load_value, name)


class DefaultSMS_Handling(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "defaultSMSHandling"
        super(DefaultSMS_Handling, self).__init__(header, byte_string, load_value, name)


class DeliveryOfErroneousSDU(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(DeliveryOfErroneousSDU, self).__init__(header, byte_string, load_value, name)


class DisconnectingParty(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "disconnectingParty"
        super(DisconnectingParty, self).__init__(header, byte_string, load_value, name)


class Distributed(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Distributed, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EMLPPPriorityLevel(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "eMLPPPriorityLevel"
        super(EMLPPPriorityLevel, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EndToEndAccessDataMap(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "endToEndAccessDataMap"
        super(EndToEndAccessDataMap, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EosInfo(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "eosInfo"
        super(EosInfo, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ErrorRatio(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ErrorRatio, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class EventCRIToMS(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "eventCRIToMS"
        super(EventCRIToMS, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ExchangeIdentity(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "exchangeIdentity"
        super(ExchangeIdentity, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class FaultCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "faultCode"
        super(FaultCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class FirstRadioChannelUsed(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "firstRadioChannelUsed"
        super(FirstRadioChannelUsed, self).__init__(header, byte_string, load_value, name)


class FixedNetworkUserRate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(FixedNetworkUserRate, self).__init__(header, byte_string, load_value, name)


class FreeFormatData(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "freeFormatData"
        super(FreeFormatData, self).__init__(header, byte_string, load_value, name)


class FrequencyBandSupported(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "frequencyBandSupported"
        super(FrequencyBandSupported, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GenericDigitsSet(Tag):  # TODO Ojo ver
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(GenericDigitsSet, self).__init__(header, byte_string, load_value, name)


class GenericNumbersSet(Tag):  # TODO Ojo ver
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(GenericNumbersSet, self).__init__(header, byte_string, load_value, name)


class GlobalCallReference(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "globalCallReference"
        super(GlobalCallReference, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GlobalTitle(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(GlobalTitle, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GlobalTitleAndSubSystemNumber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(GlobalTitleAndSubSystemNumber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class GSMCallReferenceNumber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "gSMCallReferenceNumber"
        super(GSMCallReferenceNumber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_hex_string(byte_string)


class IMEI(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(IMEI, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMEISV(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(IMEISV, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMSI(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(IMSI, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class INMarkingOfMS(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "iNMarkingOfMS"
        super(INMarkingOfMS, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class INServiceTrigger(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "iNServiceTrigger"
        super(INServiceTrigger, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class IntermediateRate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "intermediateRate"
        super(IntermediateRate, self).__init__(header, byte_string, load_value, name)


class InternalCauseAndLoc(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "internalCauseAndLoc"
        super(InternalCauseAndLoc, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class IuCodec(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "iuCodec"
        super(IuCodec, self).__init__(header, byte_string, load_value, name)


class LCSAccuracy(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(LCSAccuracy, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LCSClientType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "lCSClientType"
        super(LCSClientType, self).__init__(header, byte_string, load_value, name)


class LCSDeferredEventType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "lCSDeferredEventType"
        super(LCSDeferredEventType, self).__init__(header, byte_string, load_value, name)


class LegID(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(LegID, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LevelOfCAMELService(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "levelOfCAMELService"
        super(LevelOfCAMELService, self).__init__(header, byte_string, load_value, name)


class LocationCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "locationCode"
        super(LocationCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LocationEstimate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "locationEstimate"
        super(LocationEstimate, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class LocationInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(LocationInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_hex_string(byte_string)


class MessageReference(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "messageReference"
        super(MessageReference, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MessageTypeIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "messageTypeIndicator"
        super(MessageTypeIndicator, self).__init__(header, byte_string, load_value, name)


class MiscellaneousInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "miscellaneousInformation"
        super(MiscellaneousInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MobileUserClass1(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "mobileUserClass1"
        super(MobileUserClass1, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MobileUserClass2(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "mobileUserClass2"
        super(MobileUserClass2, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class MultimediaInformation(Tag):  # TODO ojo verificar
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "multimediaInformation"
        super(MultimediaInformation, self).__init__(header, byte_string, load_value, name)


class NetworkCallReference(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "networkCallReference"
        super(NetworkCallReference, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_hex_string(byte_string)


class NumberOfChannels(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(NumberOfChannels, self).__init__(header, byte_string, load_value, name)


class NumberOfMeterPulses(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "numberOfMeterPulses"
        super(NumberOfMeterPulses, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class NumberOfOperations(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "numberOfOperations"
        super(NumberOfOperations, self).__init__(header, byte_string, load_value, name)


    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class NumberOfShortMessage(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "numberOfShortMessages"
        super(NumberOfShortMessage, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class OperationIdentifier(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(OperationIdentifier, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class OptimalRoutingType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "optimalRoutingType"
        super(OptimalRoutingType, self).__init__(header, byte_string, load_value, name)


class OriginatedCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "originatedCode"
        super(OriginatedCode, self).__init__(header, byte_string, load_value, name)


class OriginatingLineInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "originatingLineInformation"
        super(OriginatingLineInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class OutputForSubscriber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "outputForSubscriber"
        super(OutputForSubscriber, self).__init__(header, byte_string, load_value, name)


class OutputType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "outputType"
        super(OutputType, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)

class PartialOutputRecNum(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "partialOutputRecNum"
        super(PartialOutputRecNum, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PChargingVector(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(PChargingVector, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PositioningDelivery(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "positioningDelivery"
        super(PositioningDelivery, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PointCodeAndSubSystemNumber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(PointCodeAndSubSystemNumber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PositionAccuracy(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "positionAccuracy"
        super(PositionAccuracy, self).__init__(header, byte_string, load_value, name)
    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class PresentationAndScreeningIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "presentationAndScreeningIndicator"
        super(PresentationAndScreeningIndicator, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ProcedureCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ProcedureCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class RadioChannelProperty(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "radioChannelProperty"
        super(RadioChannelProperty, self).__init__(header, byte_string, load_value, name)


class RANAPCauseCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "rANAPCauseCode"
        super(RANAPCauseCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RecordSequenceNumber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "recordSequenceNumber"
        super(RecordSequenceNumber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class RedirectionCounter(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "redirectionCounter"
        super(RedirectionCounter, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RegionalServiceUsed(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "regionalServiceUsed"
        super(RegionalServiceUsed, self).__init__(header, byte_string, load_value, name)


class ResponseTimeCategory(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "responseTimeCategory"
        super(ResponseTimeCategory, self).__init__(header, byte_string, load_value, name)


class RoamingPriorityLevel(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "roamingPriorityLevel"
        super(RoamingPriorityLevel, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class Route(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Route, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class RTCDefaultServiceHandling(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "rTCDefaultServiceHandling"
        super(RTCDefaultServiceHandling, self).__init__(header, byte_string, load_value, name)


class RTCFailureIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "rTCFailureIndicator"
        super(RTCFailureIndicator, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class RTCNotInvokedReason(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "rTCNotInvokedReason"
        super(RTCNotInvokedReason, self).__init__(header, byte_string, load_value, name)

class RTCSessionID(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "rTCSessionID"
        super(RTCSessionID, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SelectedCodec(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "selectedCodec"
        super(SelectedCodec, self).__init__(header, byte_string, load_value, name)


class ServiceCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ServiceCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ServiceFeatureCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "serviceFeatureCode"
        super(ServiceFeatureCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ServiceKey(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(ServiceKey, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class ServiceSwitchingType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "serviceSwitchingType"
        super(ServiceSwitchingType, self).__init__(header, byte_string, load_value, name)


class Single(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Single, self).__init__(header, byte_string, load_value, name)


class SMSResult(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "sMSResult"
        super(SMSResult, self).__init__(header, byte_string, load_value, name)


class SpeechCoderPreferenceList(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(SpeechCoderPreferenceList, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SpeechCoderVersion(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(SpeechCoderVersion, self).__init__(header, byte_string, load_value, name)


class SSCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "sSCode"
        super(SSCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SSFChargingCase(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "sSFChargingCase"
        super(SSFChargingCase, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class SSRequest(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "sSRequest"
        super(SSRequest, self).__init__(header, byte_string, load_value, name)


class SubscriberState(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "subscriberState"
        super(SubscriberState, self).__init__(header, byte_string, load_value, name)


class SubscriptionType(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "subscriptionType"
        super(SubscriptionType, self).__init__(header, byte_string, load_value, name)


class SwitchIdentity(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "switchIdentity"
        super(SwitchIdentity, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class TAC(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "tAC"
        super(TAC, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_hex_string(byte_string)


class TargetRNCid(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(TargetRNCid, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TariffClass(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "tariffClass"
        super(TariffClass, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)


class TariffSwitchInd(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "tariffSwitchInd"
        super(TariffSwitchInd, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_int(byte_string)

class TeleServiceCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "teleServiceCode"
        super(TeleServiceCode, self).__init__(header, byte_string, load_value, name)


class Time(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(Time, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string, 2)


class TrafficActivityCode(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "trafficActivityCode"
        super(TrafficActivityCode, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)



class TransferDelay(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "transferDelay"
        super(TransferDelay, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TransitCarrierInfo(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(TransitCarrierInfo, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TransparencyIndicator(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "transparencyIndicator"
        super(TransparencyIndicator, self).__init__(header, byte_string, load_value, name)


class TriggerData(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(TriggerData, self).__init__(header, byte_string, load_value, name)


class TriggerDetectionPoint(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(TriggerDetectionPoint, self).__init__(header, byte_string, load_value, name)


class TypeOfCalledSubscriber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "typeOfCalledSubscriber"
        super(TypeOfCalledSubscriber, self).__init__(header, byte_string, load_value, name)


class TypeOfCallingSubscriber(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "typeOfCallingSubscriber"
        super(TypeOfCallingSubscriber, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class TypeOfLocationRequest(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "typeOfLocationRequest"
        super(TypeOfLocationRequest, self).__init__(header, byte_string, load_value, name)


class TypeOfSignalling(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "typeOfSignalling"
        super(TypeOfSignalling, self).__init__(header, byte_string, load_value, name)


class UILayer1Protocol(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(UILayer1Protocol, self).__init__(header, byte_string, load_value, name)


class UnsuccessfulPositioningDataReason(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "unsuccessfulPositioningDataReason"
        super(UnsuccessfulPositioningDataReason, self).__init__(header, byte_string, load_value, name)


class UserClass(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "userClass"
        super(UserClass, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserRate(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(UserRate, self).__init__(header, byte_string, load_value, name)


class UserTerminalPosition(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "userTerminalPosition"
        super(UserTerminalPosition, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserToUserInformation(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        if not name:
            name = "userToUserInformation"
        super(UserToUserInformation, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)


class UserToUserService1Information(Tag):
    def __init__(self, header=None, byte_string=None, load_value=True, name=None):
        super(UserToUserService1Information, self).__init__(header, byte_string, load_value, name)

    def decode_value(self, byte_string):
        return get_octet_string(byte_string)
######
