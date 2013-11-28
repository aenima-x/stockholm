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


def get_filled_octet_string(byte_string, fill_positions=0):  # TODO Borrar esta reimplementada arriba
    raise Exception("No Usar")
    return "".join(map(lambda x: str(ord(x)).zfill(fill_positions), byte_string))


def get_ascii(byte_string):
    return byte_string.encode('ascii')


class AddressString(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class AddressStringExtended(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class AgeOfLocationEstimate(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class AirInterfaceUserRate(Tag):
    pass


class AoCCurrencyAmountSent(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ApplicationIdentifier(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class AsyncSyncIndicator(Tag):
    pass


class BearerServiceCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string,)


class BitRate(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class BSSMAPCauseCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CallAttemptState(Tag):
    pass


class CallIDNumber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CAMELTDPData(Tag):  # TODO ojo es una secuencia
    pass


class CarrierIdentificationCode(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CarrierInfo(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CarrierInformation(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CarrierSelectionSubstitutionInformation(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CauseCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChangeInitiatingParty(Tag):
    pass

class CallPosition(Tag):
    pass


class ChannelAllocationPriorityLevel(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChannelCodings(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargeAreaCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargedParty(Tag):
    pass


class ChargeInformation(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargingCase(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargingIndicator(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargingOrigin(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ChargingUnitsAddition(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class Counter(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CRIIndicator(Tag):
    pass


class CRIToMS(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class CUGIndex(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class CUGInterlockCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class C7CHTMessage(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class C7ChargingMessage(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class Date(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string, 2)


class DecipheringKeys(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class DefaultCallHandling(Tag):
    pass


class DefaultSMS_Handling(Tag):
    pass


class DeliveryOfErroneousSDU(Tag):
    pass


class DisconnectingParty(Tag):
    pass


class Distributed(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class EMLPPPriorityLevel(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class EndToEndAccessDataMap(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class EosInfo(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ErrorRatio(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class EventCRIToMS(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ExchangeIdentity(Tag):
    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class FaultCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class FirstRadioChannelUsed(Tag):
    pass


class FixedNetworkUserRate(Tag):
    pass


class FreeFormatData(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class FrequencyBandSupported(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class GenericDigitsSet(Tag):  # TODO Ojo ver
    pass


class GenericNumbersSet(Tag):  # TODO Ojo ver
    pass


class GlobalCallReference(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class GlobalTitle(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class GlobalTitleAndSubSystemNumber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class GSMCallReferenceNumber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class IMEI(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMEISV(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class IMSI(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class INMarkingOfMS(Tag):
    pass


class INServiceTrigger(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class IntermediateRate(Tag):
    pass


class InternalCauseAndLoc(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class IuCodec(Tag):
    pass


class LCSAccuracy(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class LCSClientType(Tag):
    pass


class LCSDeferredEventType(Tag):
    pass


class LegID(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class LevelOfCAMELService(Tag):
    pass


class LocationCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class LocationEstimate(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class MessageReference(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class MessageTypeIndicator(Tag):
    pass


class MiscellaneousInformation(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class MobileUserClass1(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class MobileUserClass2(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class MultimediaInformation(Tag):  # TODO ojo verificar
    pass


class NetworkCallReference(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class NumberOfChannels(Tag):
    pass


class NumberOfMeterPulses(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class NumberOfOperations(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class NumberOfShortMessage(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class OperationIdentifier(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)



class OptimalRoutingType(Tag):
    pass


class OptimalRoutingType(Tag):
    pass


class OriginatedCode(Tag):
    pass


class OriginatingLineInformation(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class OutputForSubscriber(Tag):
    pass


class OutputType(Tag):
    pass


class PartialOutputRecNum(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class PChargingVector(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class PositioningDelivery(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class PointCodeAndSubSystemNumber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class PositionAccuracy(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class PresentationAndScreeningIndicator(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ProcedureCode(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class RadioChannelProperty(Tag):
    pass


class RANAPCauseCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class RecordSequenceNumber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class RedirectionCounter(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class RegionalServiceUsed(Tag):
    pass


class ResponseTimeCategory(Tag):
    pass


class RoamingPriorityLevel(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class Route(Tag):
    def decode_value(self, byte_string):
        return get_ascii(byte_string)


class RTCDefaultServiceHandling(Tag):
    pass


class RTCFailureIndicator(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class RTCNotInvokedReason(Tag):
    pass


class RTCSessionID(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class SelectedCodec(Tag):
    pass


class ServiceCode(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)


class ServiceFeatureCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ServiceKey(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class ServiceSwitchingType(Tag):
    pass


class Single(Tag):
    pass


class SMSResult(Tag):
    pass


class SpeechCoderPreferenceList(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class SpeechCoderVersion(Tag):
    pass


class SSCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class SSFChargingCase(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class SSRequest(Tag):
    pass


class SubscriberState(Tag):
    pass


class SubscriptionType(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class SwitchIdentity(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TAC(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TargetRNCid(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TariffClass(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TariffSwitchInd(Tag):
    pass


class TeleServiceCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class Time(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string, 2)


class TrafficActivityCode(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TrafficClass(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TransferDelay(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TransitCarrierInfo(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TransparencyIndicator(Tag):
    pass


class TriggerData(Tag):
    pass


class TriggerDetectionPoint(Tag):
    pass


class TypeOfCalledSubscriber(Tag):
    pass


class TypeOfCallingSubscriber(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class TypeOfLocationRequest(Tag):
    pass


class TypeOfSignalling(Tag):
    pass


class UILayer1Protocol(Tag):
    pass


class UnsuccessfulPositioningDataReason(Tag):
    pass


class UserClass(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)


class UserRate(Tag):
    pass


class UserTerminalPosition(Tag):
    def decode_value(self, byte_string):
        return get_filled_octet_string(byte_string)
######






class RecordSequenceNumber(Tag):
    def decode_value(self, byte_string):
        return get_octet_string(byte_string)




class CallIDNumber(Tag):
    def decode_value(self, byte_string):
        return get_int_octet_string(byte_string)



class TBCDString(Tag):
    def decode_value(self, byte_string):
        return get_tbcd_string(byte_string)