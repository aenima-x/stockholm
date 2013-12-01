================================================
Stockholm: Decoder of Ericsson Call Data Records
================================================

Stockholm is a python module to decode the CDR from Ericsson

Example:
========
The two main methods are get_cdrs_from_file() and get_cdrs_from_data() from CallDataRecordFactory.

These two static methods return a Generator to obtain all the CDRs from a file or raw data of bytes.

```python
from stockholm.factory import CallDataRecordFactory

cdr_file = "SOME_FILE"
for cdr in CallDataRecordFactory.get_cdrs_from_file(cdr_file):
    cdr.pretty_print()
```

This is an output example:
```
CallDataRecord
Call Module - MSTerminatingSMSinMSC (7)
[dateForStartOfCharge (6)] - 130507
[exchangeIdentity (10)] - MSRSR1
[recordSequenceNumber (2)] - 7149508
[timeForStartOfCharge (7)] - 150708
[outputType (102)] - 4
[callIdentificationNumber (1)] - 1758587
[chargedParty (9)] - 0
[outgoingRoute (12)] - BURS1GO
[calledSubscriberIMEI (5)] - 012791001771710
[calledSubscriberIMEISV (43)] - 0127910017717101
[calledSubscriberIMSI (4)] - 722077140145585
[firstCalledLocationInformation (13)] - 27f27009610dee
[numberOfShortMessages (28)] - 1
[calledPartyNumber (3)] - 11543413836335
[frequencyBandSupported (26)] - 0
[teleServiceCode (14)] - 21
[mSCIdentification (11)] - 1154079007103
[lastCalledLocationInformation (29)] - 27f27009610dee
[serviceCentreAddress (15)] - 1154079000801
[tAC (0)] - 0e020b
[originForCharging (8)] - 4
[messageTypeIndicator (34)] - 00
[originatingAddress (33)] - 413014621269f3
```

I don't have examples of all the values so some of the encodings could be wrong.

TODO:
======
Add more documentation.

Fix nested data tags from Call Modules.

Do the decoding of the data tags of the Event Modules.