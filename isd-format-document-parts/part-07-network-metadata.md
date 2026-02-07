## Part 7 - Network Metadata

Network Metadata

FLD LEN: 3
    US-NETWORK-METADATA identifier
    The identifier that indicates the occurrence of US Network metadata, used in NCEI data processing.
    DOM: A specific domain comprised of the ASCII characters.
    CO1 An indicator of the following item:
    NETWORK-METADATA climate division number
    NETWORK-METADATA UTC-LST time conversion

FLD LEN: 2
    NETWORK-METADATA climate division number
    The climate division number, for this station, within the US state that it resides.
    MIN: 00          MAX: 09              UNITS: N/A
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing

FLD LEN: 3
    NETWORK-METADATA UTC-LST time conversion
    The UTC to LST time conversion for this station.
    MIN: -12        MAX: +12            UNITS: hours
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-)
    +99 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀




    45


---

FLD LEN: 3
    US-COOPERATIVE-NETWORK-ELEMENT-TIME-OFFSET identifier
    The identifier that indicates a specified element's observation time differs from the time listed in "Control Section".
    DOM: A specific domain comprised of the ASCII characters.
    CO2 - CO9 An indicator of up to 8 repeating fields of the following item:
    COOPERATIVE-NETWORK-ELEMENT-ID
    COOPERATIVE-NETWORK-TIME-OFFSET

FLD LEN: 3
    COOPERATIVE-NETWORK-ELEMENT-ID
    The element identifier to be offset, based on the identifier as shown in this document.
    DOM: A general domain comprised of the characters in the ASCII character set.
    999 = Missing

FLD LEN: 5
    COOPERATIVE-NETWORK-TIME-OFFSET
    The offset in hours. To obtain the actual observation time of the element/parameter indicated, add the value in this field
    to the date-time value in the “Control Section.”
    MIN: -9999        MAX: +9998            UNITS: Hours
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing




▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    CRN Control Section identifier
    The identifier that indicates an occurrence of datalogger program information.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CR1 An indicator of the following items:
    DL_VN identifier
    DL_VN _QC quality code
    DL_VN_FLAG quality code
FLD LEN: 5
    DL_VN identifier
    The version number which uniquely identifies the datalogger program that produced the CRN observation for
    this hour. This section appears once in every ISD record.
    MIN: 00000                    MAX: 99998
    SCALING FACTOR: 1000
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = missing

FLD LEN: 1
    DL_VN_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the reported datalogger program version number.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    DL_VN_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status of the reported datalogger program version
    number. Most users will find the preceding quality code DL_VN_QC to be the simplest and most useful
    quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Subhourly Temperature Section identifier
    The identifier that indicates one of three concurrent air temperature observations made by co-located sensors.
    Three instances of this section (corresponding to the three temperature sensors) appear in each of the twelve



    46


---

    5-minute data stream records. In the 15-minute data stream, the three instances of this section appear in the
    last record of the hour, and contain the average temperature for the last 5 minutes of the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CT1, CT2, CT3 Three indicators preceding three copies of the following items:
    AVG_TEMP air temperature
    AVG_TEMP_QC quality code
    AVG_TEMP_FLAG quality code

FLD LEN: 5
    AVG_TEMP air temperature
    The average air temperature for a 5-minute period.
    MIN: -9999       MAX: +9998       UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus
    sign (-).
    +9999 = Missing.

FLD LEN: 1
    AVG_TEMP_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the 5-minute air temperature average.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    AVG_TEMP_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status of the 5-minute air temperature average.
    Most users will find the preceding quality code AVG_TEMP_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Temperature Section identifier
    The identifier that indicates one of three concurrent air temperature observations made by co-located sensors.
    Three instances of this section (corresponding to the three temperature sensors) appear in the last ISD record
    of the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CU1, CU2, CU3 Three indicators preceding three copies of the following items:
    TEMP_AVG air temperature
    TEMP_AVG_QC quality code
    TEMP_AVG_FLAG quality code
    TEMP_STD air temperature standard deviation
    TEMP_STD_QC quality code
    TEMP_STD_FLAG quality code

FLD LEN: 5
    TEMP_AVG air temperature
    The average air temperature for an hour.
    MIN: -9999        MAX: +9998        UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing.

FLD LEN: 1
    TEMP_AVG_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly temperature average.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    TEMP_AVG_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status the hourly temperature average. Most users
    will find the preceding quality code TEMP_AVG_QC to be the simplest and most useful quality indicator.



    47


---

    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    TEMP_STD air temperature standard deviation
    The temperature standard deviation.
    MIN: 0000        MAX: 9998
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    TEMP_STD_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly temperature standard deviation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    TEMP_STD_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status the hourly temperature standard deviation.
    Most users will find the preceding quality code TEMP_STD_QC to be the simplest and most useful quality
    indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Temperature Extreme Section identifier
    The identifier that indicates one of three concurrent air temperature observations made by co-located sensors.
    Three instances of this section (corresponding to the three temperature sensors) appear in the last ISD record
    of the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CV1, CV2, CV3 Three indicators preceding three copies of the following items:
    TEMP_MIN minimum air temperature
    TEMP_MIN_QC quality code
    TEMP_MIN_FLAG quality code
    TEMP_MIN_TIME time of minimum air temperature
    TEMP_MIN_TIME_QC quality code
    TEMP_MIN_TIME_FLAG quality code
    TEMP_MAX maximum air temperature
    TEMP_MAX_QC quality code
    TEMP_MAX_FLAG quality code
    TEMP_MAX_TIME time of maximum air temperature
    TEMP_MAX_TIME_QC quality code
    TEMP_MAX_TIME_FLAG quality code

FLD LEN: 5
    TEMP_MIN minimum air temperature
    The minimum air temperature for the hour.
    MIN: -9999        MAX: +9998        UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing.

FLD LEN: 1
    TEMP_MIN_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the minimum hourly temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing




    48


---

FLD LEN: 1
    TEMP_MIN_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status the minimum hourly. Most users will find the
    preceding quality code TEMP_MIN_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    TEMP_MIN_TIME time of minimum air temperature
    The time at which the minimum temperature occurred, in z-time HHMM format
    MIN: 0000        MAX: 2359
    DOM: A specific domain comprised of the numeric characters (0-9)
    9999 = Missing.

FLD LEN: 1
    TEMP_MIN_TIME_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the time of minimum hourly temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    TEMP_MIN_TIME_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status of the time of minimum hourly temperature.
    Most users will find the preceding quality code TEMP_MIN_TIME_QC to be the simplest and most useful quality
    indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 5
    TEMP_MAX maximum air temperature
    The maximum air temperature for an hour.
    MIN: -9999       MAX: +9999       UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing.

FLD LEN: 1
    TEMP_MAX_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the maximum hourly.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    TEMP_MAX_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status the maximum hourly. Most users will find the
    preceding quality code TEMP_MAX_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    TEMP_MAX_TIME time of maximum air temperature
    The time at which the maximum temperature occurred, in z-time HHMM format
    MIN: 0000        MAX: 2359
    DOM: A specific domain comprised of the numeric characters (0-9)
    9999 = Missing.

FLD LEN: 1
    TEMP_MAX_TIME_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the time of maximum hourly temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks



    49


---

    9 = Missing

FLD LEN: 1
    TEMP_MAX_TIME_FLAG quality code
    A flag that indicates the network’s internal evaluation of the quality status of the time of maximum hourly temperature.
    Most users will find the preceding quality code TEMP_MAX_TIME_QC to be the simplest and most useful quality
    indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Subhourly Wetness Section identifier
    The identifier that indicates a subhourly wetness sensor observation.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CW1 An indicator of the following items:
    WET1 wetness indicator
    WET1_QC quality code
    WET1_FLAG quality code
    WET2 wetness indicator
    WET2_QC quality code
    WET2_FLAG quality code

FLD LEN: 5
    WET1 wetness indicator
    Wetness sensor channel 1 value indicating the existence or non-existence of moisture on the sensor.
    MIN: 00000     MAX: 99999
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    WET1_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the wetness sensor channel 1 value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    WET1_FLAG quality code
    The code that indicates ISD’s evaluation of the quality status of the wetness sensor channel 1 value.
    Most users will find the preceding quality code WET1_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks
FLD LEN: 5
    WET2 wetness indicator
    Wetness sensor channel 2 value indicating the existence or non-existence of moisture on the sensor.
    MIN: 00000        MAX: 99999
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    WET2_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the wetness sensor channel 2 value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing




    50


---

FLD LEN: 1
    WET2_FLAG quality code
    The code that indicates ISD’s evaluation of the quality status of the wetness sensor channel 2 value.
    Most users will find the preceding quality code WET2_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9)
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Geonor Vibrating Wire Summary Section identifier
    The identifier that indicates the presence of summary data for three concurrent precipitation observations made
    by co-located sensors. It appears in the last ISD record of the hour for the 15-minute data stream only. This
    section is not present for the 5-minute data stream.
    Note: This section contains the frequencies which are the fundamental output from a vibrating wire transducer. They
    were transmitted as part of datastream versions which held 15 minute precipitation values. When the 5 minute
    datastream was defined, the decision was made to transmit engineering units such as millimeters which could be
    reversed to the fundamental output values using the formulas and coefficients found in the metadata.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    CX1, CX2, CX3 An indicator of the following items:
    PRECIPITATION total hourly precipitation
    PRECIP_QC quality code
    PRECIP_FLAG quality code
    FREQ_AVG hourly average frequency
    FREQ_AVG_QC quality code
    FREQ_AVG_FLAG
    FREQ_MIN hourly minimum frequency
    FREQ_MIN_QC quality code
    FREQ_MIN_FLAG quality code
    FREQ_MAX hourly maximum frequency
    FREQ_MAX_QC quality code
    FREQ_MAX_FLAG quality code

FLD LEN: 6
    PRECIPITATION total hourly precipitation
    The total hourly precipitation amount for the sensor.
    MIN: -99999       MAX: +99999          UNITS: millimeters
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-)
    +99999 = Missing.

FLD LEN: 1
    PRECIP_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly precipitation amount.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing
FLD LEN: 1
    PRECIP_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly precipitation amount. Most
    users will find the preceding quality code PRECIP_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    FREQ_AVG hourly average frequency
    The hourly average frequency for the sensor.
    MIN: 0000      MAX: 9999       UNITS: Hertz
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.




    51


---

FLD LEN: 1
    FREQ_AVG_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly average frequency.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    FREQ_AVG_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly average frequency. Most
    users will find the preceding quality code FREQ_AVG_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    FREQ_MIN hourly minimum frequency
    The minimum frequency during the hour for the sensor.
    MIN: 0000     MAX: 9998        UNITS: Hertz
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    FREQ_MIN_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly minimum frequency.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    FREQ_MIN_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly minimum frequency. Most
    users will find the preceding quality code FREQ_MIN_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

FLD LEN: 4
    FREQ_MAX hourly maximum frequency
    The minimum frequency during the hour for the sensor.
    MIN: 0000     MAX: 9998       UNITS: Hertz
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    FREQ_MAX_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly maximum frequency.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    FREQ_MAX_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly maximum frequency. Most
    users will find the preceding quality code FREQ_MAX_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀




    52


---
