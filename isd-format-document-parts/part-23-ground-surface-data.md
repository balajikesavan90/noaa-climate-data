## Part 23 - Ground Surface Data

Ground Surface Data

FLD LEN: 3
    GROUND-SURFACE-OBSERVATION identifier
    The identifier that denotes the availability of a GROUND-SURFACE-OBSERVATION.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    IA1: An indicator of the occurrence of the following data item:
    GROUND-SURFACE-OBSERVATION code
    GROUND-SURFACE-OBSERVATION quality code

    FLD LEN: 2
    GROUND-SURFACE-OBSERVATION code
    The code that denotes the physical condition of the ground's surface.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    NOTE: Code values 10-19 indicate the state of the ground without snow or measurable ice cover.
    00 = Surface of ground dry (no appreciable amount of dust or loose sand)
    01 = Surface of ground dry (without cracks and no appreciable amount of dust or loose sand
    and without snow or measurable ice cover)
    02 = Extremely dry with cracks (without snow or measurable ice cover)
    03 = Loose dry dust or sand not covering ground completely (without snow or measurable ice cover)
    04 = Loose dry dust or sand covering more than one-half of ground (but not completely)
    05 = Loose dry dust or sand covering ground completely
    06 = Thin cover of loose dry dust or sand covering ground completely (without snow or measurable ice cover)
    07 = Moderate or thick cover of loose dry dust or sand covering ground completely (without snow or measurable
    ice cover)
    08 = Surface of ground moist
    09 = Surface of ground moist (without snow or measurable ice cover)
    10 = Surface of ground wet (standing water in small or large pools on surface)
    11 = Surface of ground wet (standing water in small or large pools on surface without snow or
    measurable ice cover)
    12 = Flooded (without snow or measurable ice cover)
    13 = Surface of ground frozen
    14 = Surface of ground frozen (without snow or measurable ice cover)
    15 = Glaze or ice on ground, but no snow or melting snow
    16 = Glaze on ground (without snow or measurable ice cover)
    17 = Ground predominantly covered by ice
    18 = Snow or melting snow (with or without ice) covering less than one-half of the ground
    19 = Snow or melting snow (with or without ice) covering more than one-half of the ground but ground not
    completely covered
    20 = Snow or melting snow (with or without ice) covering ground completely
    21 = Loose dry snow covering less than one-half of the ground
    22 = Loose dry snow covering at least one half of the ground (but not completely)
    23 = Even layer of loose dry snow covering ground completely
    24 = Uneven layer of loose dry snow covering ground completely
    25 = Compact or wet snow (with or without ice) covering less than one-half of the ground
    26 = Compact or wet snow (with or without ice) covering at least one-half of the ground but ground not completely
    covered
    27 = Even layer of compact or wet snow covering ground completely
    28 = Uneven layer of compact or wet snow covering ground completely
    29 = Snow covering ground completely; deep drifts
    30 = Lose dry dust or sand covering one-half of the ground (but not completely)
    31 = Loose dry snow, dust or sand covering ground completely
    99 = Missing




    76


---

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION code quality code
    The code that denotes a quality status of the reported GROUND-SURFACE-OBSERVATION code.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    GROUND-SURFACE-OBSERVATION minimum-temperature identifier
    The identifier that denotes the availability of GROUND-SURFACE-OBSERVATION minimum temperature data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    IA2: An indicator of the occurrence of the following data item:
    GROUND-SURFACE-OBSERVATION minimum-temperature period quantity
    GROUND-SURFACE-OBSERVATION minimum temperature
    GROUND-SURFACE-OBSERVATION minimum temperature quality code

FLD LEN: 3
    GROUND-SURFACE-OBSERVATION minimum-temperature period quantity
    The quantity of time over which the ground temperature was sampled to determine the minimum temperature.
    MIN: 001           MAX: 480           UNITS: hours
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing

FLD LEN: 5
    GROUND-SURFACE-OBSERVATION minimum temperature
    The minimum temperature of the ground's surface recorded during the observation period.
    MIN: -1100    MAX: +1500      UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign(-).
    +9999 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION minimum temperature quality code
    The code that denotes a quality status of the reported GROUND-SURFACE-OBSERVATION minimum temperature.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Surface Temperature Section identifier
    The identifier that indicates an hourly observation of surface temperature as measured by a radiation sensor for the
    ground surface. This section appears in the last ISD record of the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    IB1 An indicator of the following items:
    SURFTEMP hourly average surface temperature
    SURFTEMP_QC quality code
    SURFTEMP_FLAG quality code
    SURFTEMP_MIN minimum surface temperature
    SURFTEMP_MIN_QC quality code
    SURFTEMP_MIN_FLAG quality code
    SURFTEMP_MAX maximum surface temperature
    SURFTEMP_MAX_QC quality code
    SURFTEMP_MAX_FLAG quality code
    SURFTEMP_STD surface temperature standard deviation for the hour
    SURFTEMP_STD_QC quality code
    SURFTEMP_STD_FLAG quality code




    77


---

FLD LEN: 5
    SURFTEMP hourly average surface temperature
    The hourly average surface temperature.
    MIN: -9999     MAX: +9998        UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9) a plus sign (+), and a minus sign (-).
    +9999 = Missing.

FLD LEN: 1
    SURFTEMP_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly average surface temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SURFTEMP_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly average surface temperature.
    Most users will find the preceding quality code SURFTEMP_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 5
    SURFTEMP_MIN hourly minimum surface temperature
    The minimum 10 second surface temperature for the hour.
    MIN: -9999     MAX: +9998 UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9) a plus sign (+), and a minus sign (-)
    +9999 = Missing.

FLD LEN: 1
    SURFTEMP_MIN_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly minimum surface temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SURFTEMP_MIN_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly minimum surface temperature.
    Most users will find the preceding quality code SURFTEMP_MIN_QC to be the simplest and most useful quality
    indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 5
    SURFTEMP_MAX hourly maximum surface temperature
    The maximum 10 second surface temperature for the hour.
    MIN: -9999     MAX: +9998      UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-)
    +9999 = Missing.

FLD LEN: 1
    SURFTEMP_MAX_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly maximum surface temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing




    78


---

FLD LEN: 1
    SURFTEMP_MAX_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly maximum surface
    temperature. Most users will find the preceding quality code SURFTEMP_MAX_QC to be the simplest and most
    useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 4
    SURFTEMP_STD hourly surface temperature standard deviation
    The hourly surface temperature standard deviation.
    MIN: 0000      MAX: 9998
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    SURFTEMP_STD_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly surface temperature standard deviation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SURFTEMP_STD_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of hourly surface temperature standard
    deviation. Most users will find the preceding quality code SURFTEMP_STD_QC to be the simplest and most
    useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Surface Temperature Sensor Section identifier
    The identifier that indicates an hourly observation of the equipment temperature for the sensor used to measure ground
    surface temperature. This section appears in the last ISD record of the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    IB2 An indicator of the following items:
    SURFTEMP_SB equipment temperature
    SURFTEMP_SB_QC quality code
    SURFTEMP_SB_FLAG quality code
    SURFTEMP_SB_STD equipment temperature standard deviation for the hour
    SURFTEMP_SB_STD _QC quality code
    SURFTEMP_SB_STD _FLAG quality code

FLD LEN: 5
    SURFTEMP_SB equipment temperature
    The average temperature of the surface temperature sensor housing (sensor body) for the hour.
    MIN: -9999     MAX: +9998        UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-)
    +9999 = Missing.

FLD LEN: 1
    SURFTEMP_SB_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the surface temperature sensor housing temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing




    79


---

FLD LEN: 1
    SURFTEMP_SB_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the surface temperature sensor housing
    temperature. Most users will find the preceding quality code SURFTEMP_SB_QC to be the simplest and most
    useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 4
    SURFTEMP_SB_STD hourly sensor housing temperature standard deviation for the hour
    The hourly 10 second hourly surface temperature standard deviation.
    MIN: 0000      MAX: 9998
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    SURFTEMP_SB_STD_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly sensor housing temperature standard
    deviation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SURFTEMP_SB_STD_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of sensor housing temperature standard
    deviation.. Most users will find the preceding quality code SURFTEMP_SB_STD_QC to be the simplest and most useful
    quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    1 – 9 = Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    GROUND-SURFACE-OBSERVATION pan evaporation data identifier
    The identifier that denotes the availability of GROUND-SURFACE-OBSERVATION evaporation data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    IC1: An indicator of the occurrence of the following data item:
    GROUND-SURFACE-OBSERVATION time period in hours
    GROUND-SURFACE-OBSERVATION wind movement
    GROUND-SURFACE-OBSERVATION wind movement condition code
    GROUND-SURFACE-OBSERVATION wind movement quality code
    GROUND-SURFACE-OBSERVATION evaporation data
    GROUND-SURFACE-OBSERVATION evaporation condition code
    GROUND-SURFACE-OBSERVATION evaporation quality code
    GROUND-SURFACE-OBSERVATION maximum pan water temperature
    GROUND-SURFACE-OBSERVATION maximum water temperature condition code
    GROUND-SURFACE-OBSERVATION maximum water temperature quality code
    GROUND-SURFACE-OBSERVATION minimum pan water temperature
    GROUND-SURFACE-OBSERVATION minimum water temperature condition code
    GROUND-SURFACE-OBSERVATION minimum water temperature quality code

FLD LEN: 2
    GROUND-SURFACE-OBSERVATION time period in hours
    The quantity of time over which the evaporation and related data were sampled.
    MIN: 01           MAX: 98         UNITS: hours
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing

FLD LEN: 4
    GROUND-SURFACE-OBSERVATION wind movement
    The wind movement over the evaporation pan during the time period of the observation.
    MIN: 0000    MAX: 9998      UNITS: Statute Miles
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing



    80


---

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION wind movement condition code
    The code that denotes certain conditions or flags which describe the data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = No special conditions
    2 = Data will be included in subsequent observation
    3 = Data are accumulated from previous observation(s), so cover a longer than typical time period
    9 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION wind movement quality code
    The code that denotes a quality status of the reported wind movement data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    4 = Passed gross limits check, from NCEI Data source
    5 = Passed all quality control checks, from NCEI Data source
    6 = Suspect, from NCEI Data source
    7 = Erroneous, from NCEI Data source
    9 = Passed gross limits check if element is present

FLD LEN: 3
    GROUND-SURFACE-OBSERVATION evaporation data
    The total evaporation which was measured during the time period of the observation.
    MIN: 000     MAX: 998      UNITS: Inches
    SCALING FACTOR: 100
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION evaporation condition code
    The code that denotes certain conditions or flags which describe the data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = No special conditions
    2 = Data will be included in subsequent observation
    3 = Data are accumulated from previous observation(s), so cover a longer than typical time period
    9 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION evaporation quality code
    The code that denotes a quality status of the reported evaporation data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    4 = Passed gross limits check, from NCEI Data source
    5 = Passed all quality control checks, from NCEI Data source
    6 = Suspect, from NCEI Data source
    7 = Erroneous, from NCEI Data source
    9 = Passed gross limits check if element is present

FLD LEN: 4
    GROUND-SURFACE-OBSERVATION maximum pan water temperature
    The maximum temperature in the evaporation pan during the time period of the observation.
    MIN: -100    MAX: +500   UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), as a signed field.
    +999 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION maximum pan water temperature condition code
    The code that denotes certain conditions or flags which describe the data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = No special conditions
    2 = Data will be included in subsequent observation
    3 = Data are accumulated from previous observation(s), so cover a longer than typical time period
    9 = Missing




    81


---

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION maximum pan water temperature quality code
    The code that denotes a quality status of the reported maximum water temperature data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    4 = Passed gross limits check, from NCEI Data source
    5 = Passed all quality control checks, from NCEI Data source
    6 = Suspect, from NCEI Data source
    7 = Erroneous, from NCEI Data source
    9 = Passed gross limits check if element is present

FLD LEN: 4
    GROUND-SURFACE-OBSERVATION minimum pan water temperature
    The maximum temperature in the evaporation pan during the time period of the observation.
    MIN: -100    MAX: +500   UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), as a signed field.
    +999 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION minimum pan water temperature condition code
    The code that denotes certain conditions or flags which describe the data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = No special conditions
    2 = Data will be included in subsequent observation
    3 = Data are accumulated from previous observation(s), so cover a longer than typical time period
    9 = Missing

FLD LEN: 1
    GROUND-SURFACE-OBSERVATION minimum pan water temperature quality code
    The code that denotes a quality status of the reported minimum water temperature data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    4 = Passed gross limits check, from NCEI Data source
    5 = Passed all quality control checks, from NCEI Data source
    6 = Suspect, from NCEI Data source
    7 = Erroneous, from NCEI Data source
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


Temperature Data

FLD LEN: 3
    EXTREME-AIR-TEMPERATURE identifier
    The identifier that denotes the start of an EXTREME-AIR-TEMPERATURE data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KA1-KA4 An indicator of up to 4 repeating fields of the following items:
    EXTREME-AIR-TEMPERATURE period quantity
    EXTREME-AIR-TEMPERATURE code
    EXTREME-AIR-TEMPERATURE air temperature
    EXTREME-AIR-TEMPERATURE temperature quality code

FLD LEN: 3
    EXTREME-AIR-TEMPERATURE period quantity
    The quantity of time over which temperatures were sampled to determine the
    EXTREME-AIR-TEMPERATURE.
    MIN: 001     MAX: 480      UNITS: Hours
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9)
    999 = Missing

FLD LEN: 1
    EXTREME-AIR-TEMPERATURE code
    The code that denotes an EXTREME-AIR-TEMPERATURE as a maximum or a minimum.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    N = Minimum temperature
    M = Maximum temperature
    O = Estimated minimum temperature
    P = Estimated maximum temperature
    9 = Missing



    82


---

FLD LEN: 5
    EXTREME-AIR-TEMPERATURE temperature
    The temperature of the high or low air temperature for a given period.
    MIN: -0932      MAX: +0618       UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus
    sign (-).
    +9999 = Missing

FLD LEN: 1
    EXTREME-AIR-TEMPERATURE temperature quality code
    The code that denotes a quality status of the reported EXTREME-AIR-TEMPERATURE temperature.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    M = Manual change made to value based on information provided by NWS or FAA
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    AVERAGE-AIR-TEMPERATURE identifier
    The identifier that denotes the start of an AVERAGE-AIR-TEMPERATURE data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KB1-KB3 An indicator of up to 3 repeating fields for the following items:
    AVERAGE-AIR-TEMPERATURE period quantity
    AVERAGE-AIR-TEMPERATURE type code
    AVERAGE-AIR-TEMPERATURE air temperature
    AVERAGE-AIR-TEMPERATURE temperature quality code

FLD LEN: 3
    AVERAGE-AIR-TEMPERATURE period quantity
    The quantity of time over which temperatures were sampled to determine the
    AVERAGE-AIR-TEMPERATURE.
    MIN: 001     MAX: 744      UNITS: Hours
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9)
    999 = Missing

FLD LEN: 1
    AVERAGE-AIR-TEMPERATURE code
    The code that denotes an AVERAGE-AIR-TEMPERATURE as a mean, an average maximum, or an average minimum.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    N = Minimum temperature average
    M = Maximum temperature average
    A = Mean temperature
    9 = Missing

FLD LEN: 5
    AVERAGE-AIR-TEMPERATURE temperature
    The mean air temperature for a given period, typically for the day or month, as reported by the station (ie, not derived
    from other data fields).
    MIN: -9900     MAX: +6300       UNITS: Degrees Celsius
    SCALING FACTOR: 100
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing




    83


---

FLD LEN: 1
    AVERAGE-AIR-TEMPERATURE temperature quality code
    The code that denotes a quality status of the reported AVERAGE-AIR-TEMPERATURE temperature.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    EXTREME AIR-TEMPERATURE FOR THE MONTH identifier
    The identifier that denotes the start of an EXTREME AIR-TEMPERATURE data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KC1-KC2 An indicator of up to 2 repeating fields for the following items:
    EXTREME AIR-TEMPERATURE code
    EXTREME AIR-TEMPERATURE condition code
    EXTREME AIR-TEMPERATURE temperature
    EXTREME AIR-TEMPERATURE date of occurrence
    EXTREME AIR-TEMPERATURE temperature quality code

FLD LEN: 1
    EXTREME AIR-TEMPERATURE FOR THE MONTH code
    The code that denotes an EXTREME AIR-TEMPERATURE FOR THE MONTH as a maximum or a minimum.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    N = Minimum temperature
    M = Maximum temperature
    9 = Missing

FLD LEN: 1
    EXTREME AIR-TEMPERATURE FOR THE MONTH condition code
    The code for EXTREME AIR-TEMPERATURE FOR THE MONTH
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = The value occurred on other dates in addition to those listed
    9 = Missing or not applicable

FLD LEN: 5
    EXTREME AIR-TEMPERATURE FOR THE MONTH temperature
    The extremes air temperature for the month, as reported by the station (ie, not derived from other data fields).
    MIN: -1100    MAX: +0630        UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing

FLD LEN: 6
    EXTREME AIR-TEMPERATURE FOR THE MONTH dates of occurrence
    The dates of occurrence of EXTREME AIR-TEMPERATURE, given as the date for each occurrence, for up to 3
    occurrences; e.g., 041016 indicates days 04, 10, and 16.
    MIN: 01      MAX: 31
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = missing for each of the 3 sub-fields.

FLD LEN: 1
    EXTREME AIR-TEMPERATURE FOR THE MONTH temperature quality code
    The code that denotes a quality status of the reported EXTREME AIR-TEMPERATURE FOR THE MONTH.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source



    84


---

    7 = Erroneous, data originate from an NCEI data source
    M = Manual change made to value based on information provided by NWS or FAA
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    HEATING-COOLING-DEGREE-DAYS identifier
    The identifier that denotes the start of an HEATING-COOLING-DEGREE-DAYS data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KD1-KD2 An indicator of up to 2 repeating fields of the following items:
    HEATING-COOLING-DEGREE-DAYS period quantity
    HEATING-COOLING-DEGREE-DAYS code
    HEATING-COOLING-DEGREE-DAYS value
    HEATING-COOLING-DEGREE-DAYS quality code

FLD LEN: 3
    HEATING-COOLING-DEGREE-DAYS period quantity
    The quantity of time over which temperatures were sampled to determine the HEATING-COOLING-DEGREE-DAYS.
    MIN: 001     MAX: 744      UNITS: Hours
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing

FLD LEN: 1
    HEATING-COOLING-DEGREE-DAYS code
    The code that denotes the value as being heating degree days or cooling degree days.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    H = Heating Degree Days
    C = Cooling Degree Days

FLD LEN: 4
    HEATING-COOLING-DEGREE-DAYS value
    The total heating or cooling degree days for a given period, typically for the day or month, as reported by the station (ie,
    not derived from other data fields). These data use the 65-degree Fahrenheit base as raditionally used for degree days.
    MIN: 0000      MAX: 5000        UNITS: Heating or Cooling Degree Days
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing

FLD LEN: 1
    HEATING-COOLING-DEGREE-DAYS quality code
    The code that denotes a quality status of the reported HEATING-COOLING-DEGREE-DAYS data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH identifier
    The identifier that represents NUMBER OF DAYS EXCEEDING CRITERIA data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KE1 An indicator of the following items:
    EXTREME TEMPERATURE, NUMBER OF DAYS with maximum temperature 32 F or lower
    EXTREME TEMPERATURE, NUMBER OF DAYS quality code
    EXTREME TEMPERATURE, NUMBER OF DAYS with maximum temperature 90 F or higher
    EXTREME TEMPERATURE, NUMBER OF DAYS quality code
    EXTREME TEMPERATURE, NUMBER OF DAYS with minimum temperature 32 F or lower
    EXTREME TEMPERATURE, NUMBER OF DAYS quality code
    EXTREME TEMPERATURE, NUMBER OF DAYS with minimum temperature 0 F or lower
    EXTREME TEMPERATURE, NUMBER OF DAYS quality code



    85


---

FLD LEN: 2
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH
    The number of days with maximum temperature 32 F (0.0 C) or lower.
    MIN: 00     MAX: 31
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing.

FLD LEN: 1
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH quality code
    The code that denotes a quality status of the reported days with max temperature 32 F (0.0 C) or lower.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

FLD LEN: 2
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH
    The number of days with maximum temperature 90 F (32.2 C) or higher, except for Alaska—70 F (21.1 C) or higher.
    MIN: 00     MAX: 31
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing.

FLD LEN: 1
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH quality code
    The code that denotes a quality status of the reported days with max temperature 90 F (32.2 C) or higher (70 F for
    Alaska).
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

FLD LEN: 2
    TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH
    The number of days with minimum temperature 32 F (0.0 C) or lower.
    MIN: 00     MAX: 31
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing.

FLD LEN: 1
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH quality code
    The code that denotes a quality status of the reported days with min temperature 32 F (0.0 C) or lower.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

FLD LEN: 2
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH
    The number of days with minimum temperature 0 F (-17.8 C) or lower.
    MIN: 00     MAX: 31
    DOM: A general domain comprised of the numeric characters (0-9).
    99 = Missing.



    86


---

FLD LEN: 1
    EXTREME TEMPERATURES, NUMBER OF DAYS EXCEEDING CRITERIA, FOR THE MONTH quality code
    The code that denotes a quality status of the reported days with min temperature 0 F (-17.8 C) or lower.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Calculated Temperature Section identifier
    The identifier that indicates a calculated hourly average air temperature derived by an algorithm whose inputs
    are hourly temperature averages from each of the 3 co-located temperature sensors. This section appears in the
    last ISD record of the hour for the 15-minute data stream only. Unlike the temperature value found in the
    mandatory data section which is produced using 5-minute values, this value is calculated using an hourly average.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KF1 An indicator of the following items:
    TEMP derived air temperature
    TEMP_QC quality code

FLD LEN: 5
    TEMP derived air temperature
    The calculated hourly average air temperature.
    MIN: -9999        MAX: +9998        UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing.

FLD LEN: 1
    TEMP_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the calculated hourly average air temperature.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    AVERAGE DEW POINT AND WET BULB TEMPERATURE occurrence identifier
    The identifier that denotes the start of an AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    KG1-KG2 An indicator of up to two repeating fields of the following items:
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE period quantity
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE code
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE temperature
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE derived code
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE quality code


FLD LEN: 3
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE period quantity
    The quantity of time over which temperature were averaged to determine the AVERAGE-DEW-POINT-AND-WET-BULB-
    TEMPERATURE
    MIN: 001         MAX: 744       UNITS: hours
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing.




    87


---

FLD LEN: 1
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE code
    The code that denotes an AVERAGE-DEW-POINT-AND-AVERAGE-WET-BULB-TEMPERATURE as an average
    DOM: A specific domain comprised of the characters in the ASCII character set.
    D = Average dew point temperature
    W = Average wet bulb temperature
    9 = missing

FLD LEN: 5
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE temperature
    The average dew point or average wet bulb temperature for a given period, typically for the day or month, derived from
    other data fields
    MIN: -9900        MAX: +6300      UNITS: degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign ( - ).
    +9999 = missing

FLD LEN: 1
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE derived code
    The code that denotes a quality status of the reported AVERAGE-DEW-POINT-AND-AVERAGE-WET-BULB-
    TEMPERATURE
    DOM: A specific domain comprised of the characters in the ASCII character set.
    D = Derived from hourly values
    9 = missing


FLD LEN: 1
    AVERAGE-DEW-POINT-AND-WET-BULB-TEMPERATURE quality code
    The code that denotes a quality status of the reported AVERAGE-DEW-POINT-AND-AVERAGE-WET-BULB-
    TEMPERATURE
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, from NCEI ASOS/AWOS
    5 = Passed all quality control checks, from NCEI ASOS/AWOS
    6 = Suspect, from NCEI ASOS/AWOS
    7 = Erroneous, from NCEI ASOS/AWOS
    9 = Missing


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
