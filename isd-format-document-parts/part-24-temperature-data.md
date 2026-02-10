## Part 24 - Temperature Data

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

Pressure Data
FLD LEN: 3
         ATMOSPHERIC-PRESSURE-OBSERVATION identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               MA1 An indicator of the occurrence of the following items:
                     ATMOSPHERIC-PRESSURE-OBSERVATION altimeter setting rate
                     ATMOSPHERIC-PRESSURE-OBSERVATION altimeter quality code
                     ATMOSPHERIC-PRESSURE-OBSERVATION station pressure rate
                     ATMOSPHERIC-PRESSURE-OBSERVATION station pressure quality code

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION altimeter setting rate
         The pressure value to which an aircraft altimeter is set so that it will indicate the altitude relative to mean sea level of an
         aircraft on the ground at the location for which the value was determined.
         MIN: 08635        MAX: 10904       UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
                Missing = 99999




                                                                   88


---

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION altimeter quality code
         The code that denotes a quality status of an altimeter setting rate.
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

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION station pressure rate
         The atmospheric pressure at the observation point.
         MIN: 04500     MAX: 10900 UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION station pressure quality code
         The code that denotes a quality status of the station pressure of an ATMOSPHERIC-PRESSURE-OBSERVATION.
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
         ATMOSPHERIC-PRESSURE-CHANGE identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-CHANGE data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               Domain Value ID: Domain Value Definition Text
               MD1 An indicator of the occurrence of the following items:
                     ATMOSPHERIC-PRESSURE-CHANGE tendency code
                     ATMOSPHERIC-PRESSURE-CHANGE quality tendency code
                     ATMOSPHERIC-PRESSURE-CHANGE three hour quantity
                     ATMOSPHERIC-PRESSURE-CHANGE quality three hour code
                     ATMOSPHERIC-PRESSURE-CHANGE twenty four hour quantity
                     ATMOSPHERIC-PRESSURE-CHANGE quality twenty four hour code

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-CHANGE tendency code
         The code that denotes the characteristics of an ATMOSPHERIC-PRESSURE-CHANGE that occurs over a period of
         three hours.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               Domain Value ID: Domain Value Definition Text
               0 = Increasing, then decreasing; atmospheric pressure the same or higher than 3 hours ago
               1 = Increasing then steady; or increasing, then increasing more slowly; atmospheric pressure now higher than 3
                 hours ago
               2 = Increasing (steadily or unsteadily); atmospheric pressure now higher than 3 hours ago
               3 = Decreasing or steady, then increasing; or increasing, then increasing more rapidly; atmospheric pressure now
                   higher than 3 hours ago
               4 = Steady; atmospheric pressure the same as 3 hours ago
               5 = Decreasing, then increasing; atmospheric pressure the same or lower than 3 hours ago
               6 = Decreasing, then steady; or decreasing, then decreasing more slowly; atmospheric pressure now lower than 3
                   hours ago
               7 = Decreasing (steadily or unsteadily); atmospheric pressure now lower than 3 hours ago




                                                              89


---

                 8 = Steady or increasing, then decreasing; or decreasing, then decreasing more rapidly; atmospheric pressure
                     now lower than 3 hours ago
                 9 = Missing
FLD LEN: 1
         ATMOSPHERIC-PRESSURE-CHANGE quality tendency code
         The code that denotes a quality status of the tendency of an ATMOSPHERIC-PRESSURE-CHANGE.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect
               3 = Erroneous
               9 = Passed gross limits check if element is present


FLD LEN: 3
       ATMOSPHERIC-PRESSURE-CHANGE three hour quantity
       The absolute value of the quantity of change in atmospheric pressure measured at the
       beginning and end of a three hour period.
       MIN: 000      MAX: 500       UNITS: Hectopascals
       SCALING FACTOR: 10
       DOM: A general domain comprised of the numeric characters (0-9).
             Missing = 999

FLD LEN: 1
       ATMOSPHERIC-PRESSURE-CHANGE quality three hour code
       The code that denotes the quality status of the three hour quantity for an ATMOPSHERIC-
       PRESSURE-CHANGE.
       DOM: A specific domain comprised of the characters in the ASCII character set.
             0 = Passed gross limits check
             1 = Passed all quality control checks
             2 = Suspect
             3 = Erroneous
             9 = Passed gross limits check if element is present

FLD LEN: 4
        ATMOSPHERIC-PRESSURE-CHANGE twenty four hour quantity
       The quantity of change in atmospheric pressure measured at the beginning and end of a twenty four
       hour period.
       MIN: -800        MAX: +800    UNITS: Hectopascals
       SCALING FACTOR: 10
       DOM: A general domain comprised of the numeric characters(0-9), a plus sign (+), and a minus
              sign (-).
             +999 = Missing

FLD LEN: 1
       ATMOSPHERIC-PRESSURE-CHANGE quality twenty four hour code
       The code that denotes a quality status of a reported twenty four hour ATMOSPHERIC-PRESSURE-
       CHANGE.
       DOM: A specific domain comprised of the characters in the ASCII character set.
             0 = Passed gross limits check
             1 = Passed all quality control checks
             2 = Suspect
             3 = Erroneous
             9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
       GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL identifier
       The identifier that denotes the availability of GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL data.
       DOM: A specific domain comprised of the characters in the ASCII character set.
             ME1: An indicator of the occurrence of the following data items:
                     GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL code
                     GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL height dimension
                     GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL height dimension quality code




                                                              90


---

FLD LEN: 1
         GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL code
         The code that denotes the isobaric surface used to represent geopotential height.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               Domain Value ID: Domain Value Definition Text
                                 1 = 1000 hectopascals
                                 2 = 925 hectopascals
                                 3 = 850 hectopascals
                                 4 = 700 hectopascals
                                 5 = 500 hectopascals
                                 9 = Missing

FLD LEN: 4
         GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL height dimension
         The height of a GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL
         MIN: 0000       MAX: 9998    UNITS: Geopotential Meters
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing

FLD LEN: 1
         GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL height dimension quality code
         The code that denotes a quality status of the reported GEOPOTENTIAL-HEIGHT-ISOBARIC-LEVEL height dimension.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect
               3 = Erroneous
               9 = Passed gross limits check if element is present


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) occurrence identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               MF1 An indicator of the following items:
                     ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average station pressure for the day (derived)
                     ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average station pressure quality code
                     ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average sea level pressure for the day (derived)
                     ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average sea level pressure quality code



FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average station pressure for the day
         The average pressure at the observed point for the day derived computationally from other QC’ed elements
         MIN: 04500       MAX: 10900        UNITS: hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) quality code
         The code that denotes a quality status of an average station pressure
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




                                                              91


---

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) average sea level pressure for the day
         The average sea level pressure at the observed point for the day derived computationally from other QC’ed elements
         MIN: 08600        MAX: 10900         UNITS: hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION (STP/SLP) quality code
         The code that denotes a quality status of an average station pressure
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect
               3 = Erroneous
               4 = Passed gross limits check, data originate from an NCEI data source
               5 = Passed all quality control checks, data originate from an NCEI data source
               6 = Suspect, data originate from an NCEI data source
               7 = Erroneous, from NCEI ASOS/AWOS
               9 = Missing


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         ATMOSPHERIC-PRESSURE-OBSERVATION identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               MG1 An indicator of the occurrence of the following items:
                     ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure for the day
                     ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure quality code
                     ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure for the day
                     ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure quality code

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure for the day
         The average pressure at the observation point for the day.
         MIN: 04500     MAX: 10900      UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure quality code
         The code that denotes the quality status of an average station pressure.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               4 = Passed gross limits check, data originate from an NCEI data source
               5 = Passed all quality control checks, data originate from an NCEI data source
              6 = Suspect, data originate from an NCEI data source
              7 = Erroneous, data originate from an NCEI data source
              M = Manual change made to value based on information provided by NWS or FAA
              9 = Passed gross limits check if element is present

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure for the day
         The minimum sea level pressure for the day at the observation point.
         MIN: 08600     MAX: 10900 UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure for the day quality code
         The code that denotes the quality status of the minimum sea level pressure for the day.
         DOM: A specific domain comprised of the characters in the ASCII character set.
              4 = Passed gross limits check, data originate from an NCEI data source
              5 = Passed all quality control checks, data originate from an NCEI data source
              6 = Suspect, data originate from an NCEI data source



                                                              92


---

               7 = Erroneous, data originate from an NCEI data source
               M = Manual change made to value based on information provided by NWS or FAA
               9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               MH1 An indicator of the occurrence of the following items:
                     ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure for the month
                     ATMOSPHERIC-PRESSURE-OBSERVATION average station pressure quality code
                     ATMOSPHERIC-PRESSURE-OBSERVATION average sea level pressure for the month
                     ATMOSPHERIC-PRESSURE-OBSERVATION average sea level pressure quality code

FLD LEN: 5
       ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH average station pressure for the month
       The average pressure at the observation point for the month.
       MIN: 04500     MAX: 10900      UNITS: Hectopascals
       SCALING FACTOR: 10
       DOM: A general domain comprised of the numeric characters (0-9).
              99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH average station pressure quality code
         The code that denotes the quality status of an average station pressure.
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

FLD LEN: 5
        ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH average sea level pressure for the month
        The average sea level pressure for the month at the observation point.
        MIN: 08600     MAX: 10900 UNITS: Hectopascals
        SCALING FACTOR: 10
        DOM: A general domain comprised of the numeric characters (0-9).
              99999 = Missing.

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH average sea level pressure for the month quality
         code
         The code that denotes the quality status of the average sea level pressure for the month.
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




                                                         93


---

FLD LEN: 3
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH identifier
         The identifier that denotes the start of an ATMOSPHERIC-PRESSURE-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               MK1 An indicator of the occurrence of the following items:
                     ATMOSPHERIC-PRESSURE-OBSERVATION maximum sea level pressure for the month
                     ATMOSPHERIC-PRESSURE-OBSERVATION maximum sea level pressure date-time
                     ATMOSPHERIC-PRESSURE-OBSERVATION maximum sea level pressure quality code
                     ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure for the month
                     ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure date-time
                     ATMOSPHERIC-PRESSURE-OBSERVATION minimum sea level pressure quality code

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH maximum sea level pressure for the month
         The maximum sea level pressure at the observation point for the month.
         MIN: 08600     MAX: 10900     UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing

FLD LEN: 6
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH maximum sea level pressure, date-time
         The date-time of occurrence of the pressure value, given as the date-time; e.g., 051500 indicates day 05, time 1500.
         MIN: 010000       MAX: 312359
         DOM: A general domain comprised of the numeric characters (0-9).
               999999 = Missing

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH maximum sea level pressure quality code
         The code that denotes the quality status of a maximum sea level pressure.
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

FLD LEN: 5
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH minimum sea level pressure for the month
         The minimum sea level pressure at the observation point for the month.
         MIN: 08600     MAX: 10900     UNITS: Hectopascals
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing

FLD LEN: 6
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH minimum sea level pressure, date-time
         The date-time of occurrence of the pressure value, given as the date-time; e.g., 051500 indicates day 05, time 1500.
         MIN: 010000       MAX: 312359
         DOM: A general domain comprised of the numeric characters (0-9).
               999999 = Missing

FLD LEN: 1
         ATMOSPHERIC-PRESSURE-OBSERVATION FOR THE MONTH minimum sea level pressure quality code
         The code that denotes the quality status of a minimum sea level pressure.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect
               3 = Erroneous
               4 = Passed gross limits check, data originate from an NCEI data source
               5 = Passed all quality control checks, data originate from an NCEI data source
               6 = Suspect, data originate from an NCEI data source
               7 = Erroneous, data originate from an NCEI data source



                                                               94


---

                 M = Manual change made to value based on information provided by NWS or FAA
                 9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Weather Occurrence Data

FLD LEN: 3
         PRESENT-WEATHER-IN-VICINITY-OBSERVATION occurrence identifier
         The identifier that signifies the reporting of present weather.
         DOM: A specific domain comprised of the ASCII characters.
               MV1 = first weather reported
               MV2 = second weather reported
               MV3 = third weather reported
               MV4 = fourth weather reported
               MV5 = fifth weather reported
               MV6 = sixth weather reported
               MV7 = seventh weather reported
               An indicator of up to 7 repeating fields of the following items:
               PRESENT-WEATHER-OBSERVATION atmospheric condition code.
               PRESENT-WEATHER-OBSERVATION quality manual atmospheric condition code

FLD LEN: 2
         PRESENT-WEATHER-IN-VICINITY-OBSERVATION atmospheric condition code
         The code that denotes a specific type of weather observed between 5 and 10 statute miles of the station at the time of
         Observation. Observed at selected statons from July 1, 1996 to present.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               00 = No observation
               01 = Thunderstorm in vicinity
               02 = Showers in vicinity
               03 = Sandstorm in vicinity
               04 = Sand / dust whirls in vicinity
               05 = Duststorm in vicinity
               06 = Blowing snow in vicinity
               07 = Blowing sand in vicinity
               08 = Blowing dust in vicinity
               09 = Fog in vicinity
               99 = Missing

FLD LEN: 1
         PRESENT-WEATHER-IN-VICINITY-OBSERVATION quality atmospheric condition code
         The code that denotes a quality status of a reported present weather in vicinity observation from a station.
         DOM: A specific domain comprised of the characters in the ASCII character set.
              4 = Passed gross limits check, data originate from an NCEI data source
              5 = Passed all quality control checks, data originate from an NCEI data source
              6 = Suspect, data originate from an NCEI data source
              7 = Erroneous, data originate from an NCEI data source
              9 = Passed gross limits check if element is present

  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         PRESENT-WEATHER-OBSERVATION manual occurrence identifier
         The identifier that signifies the reporting of present weather.
         DOM: A specific domain comprised of the ASCII characters.
               MW1 = first weather reported
               MW2 = second weather reported
               MW3 = third weather reported
               MW4 = fourth weather reported
               MW5 = fifth weather reported
               MW6 = sixth weather reported
               MW7 = seventh weather reported
               An indicator of up to 7 repeating fields of the following items:
               PRESENT-WEATHER-OBSERVATION manual atmospheric condition code.
               PRESENT-WEATHER-OBSERVATION quality manual atmospheric condition code




                                                                95


---

FLD LEN: 2
          PRESENT-WEATHER-OBSERVATION manual atmospheric condition code
          The code that denotes a specific type of weather observed manually.
          DOM: A specific domain comprised of the characters in the ASCII character set.
          Note: Lack of an MW1 report normally indicates that the station did not report any present weather data.
          ------------------------------------------------------------------------
          No precipitation, fog, ice fog (except for 11 and 12), duststorm, sandstorm, drifting or blowing snow at the
                 station at the time of observation or, except for 09 and 17, during the preceding hour.
          ------------------------------------------------------------------------
                  00 = Cloud development not observed or not observable
                  01 = Clouds generally dissolving or becoming less developed
                  02 = State of sky on the whole unchanged
                  03 = Clouds generally forming or developing
                  04 = Visibility reduced by smoke, e.g. veldt or forest fires, industrial smoke or volcanic ashes
                  05 = Haze
                  06 = Widespread dust in suspension in the air, not raised by wind at or near the station at the time of observation
                  07 = Dust or sand raised by wind at or near the station at the time of observation, but no well-developed dust
                         whirl(s) sand whirl(s), and no duststorm or sandstorm seen or, in the case of ships, blowing spray at the
                         station
                  08 = Well developed dust whirl(s) or sand whirl(s) seen at or near the station during the preceding hour or at the
                         time of observation, but no duststorm or sandstorm
                  09 = Duststorm or sandstorm within sight at the time of observation, or at the station during the preceding hour
                  10 = Mist
                  11 = Patches of shallow fog or ice fog at the station, whether on land or sea, not deeper than about 2 meters on
                         land or 10 meters at sea
                  12 = More or less continuous shallow fog or ice fog at the station, whether on land or sea, not deeper than about 2
                         meters on land or 10 meters at sea
                  13 = Lightning visible, no thunder heard
                  14 = Precipitation within sight, not reaching the ground or the surface of the sea
                  15 = Precipitation within sight, reaching the ground or the surface of the sea, but distant, i.e., estimated to be more
                         than 5 km from the station
                  16 = Precipitation within sight, reaching the ground or the surface of the sea, near to, but not at the station
                  17 = Thunderstorm, but no precipitation at the time of observation
                  18 = Squalls at or within sight of the station during the preceding hour or at the time of observation
                  19 = Funnel cloud(s) (Tornado cloud or waterspout) at or within sight of the station during the preceding hour or at
                         the time of observation
          -----------------------------------------------------------------------
          Precipitation, fog, ice fog or thunderstorm at the station during the preceding hour, but not at the time
                 Observation
          ----------------------------------------------------------------------
                 20 = Drizzle (not freezing) or snow grains not falling as shower(s)
                 21 = Rain (not freezing) not falling as shower(s)
                 22 = Snow not falling as shower(s)
                 23 = Rain and snow or ice pellets not falling as shower(s)
                 24 = Freezing drizzle or freezing rain not falling as shower(s)
                 25 = Shower(s) of rain
                 26 = Shower(s) of snow or of rain and snow
                 27 = Shower(s) of hail (Hail, small hail, snow pellets), or rain and hail
                 28 = Fog or ice fog
                 29 = Thunderstorm (with or without precipitation)
        -----------------------------------------------------------------------
        Dust, sand, or blowing snow in the air, but no precipitation at the time of observation.
        -----------------------------------------------------------------------
                 30 = Slight or moderate duststorm or sandstorm has decreased during the preceding hour
                 31 = Slight or moderate duststorm or sandstorm no appreciable change during the preceding hour
                 32 = Slight or moderate duststorm or sandstorm has begun or has increased during the preceding hour
                 33 = Severe duststorm or sandstorm has decreased during the preceding hour
                 34 = Severe duststorm or sandstorm no appreciable change during the preceding hour
                 35 = Severe duststorm or sandstorm has begun or has increased during the preceding hour
                 36 = Slight or moderate drifting snow generally low (below eye level)
                 37 = Heavy drifting snow generally low (below eye level)
                 38 = Slight or moderate blowing snow generally high (above eye level)
                 39 = Heavy blowing snow generally high (above eye level)
        -----------------------------------------------------------------------
        Fog or ice fog at the time of observation
        -----------------------------------------------------------------------
                 40 = Fog or ice fog at a distance at the time of observation, but not at the station during the preceding
                        hour, the fog or ice fog extending to a level above that of the observer
                 41 = Fog or ice fog in patches



                                                                  96


---

        42 = Fog or ice fog, sky visible, has become thinner during the preceding hour
        43 = Fog or ice fog, sky invisible, has become thinner during the preceding hour
        44 = Fog or ice fog, sky visible, no appreciable change during the preceding hour
        45 = Fog or ice fog, sky invisible, no appreciable change during the preceding hour
        46 = Fog or ice fog, sky visible, has begun or has become thicker during the preceding hour
        47 = Fog or ice fog, sky invisible, has begun or has become thicker during the preceding hour
         48 = Fog, depositing rime, sky visible
         49 = Fog, depositing rime, sky invisible
-----------------------------------------------------------------------
Precipitation at the station at the time of observation – including Drizzle, Rain, Solid Precipitation, and
         Precipitation with current or recent Thunder
-----------------------------------------------------------------------
         50 = Drizzle, not freezing, intermittent, slight at time of observation
         51 = Drizzle, not freezing, continuous, slight at time of observation
         52 = Drizzle, not freezing, intermittent, moderate at time of observation
         53 = Drizzle, not freezing, continuous, moderate at time of observation
         54 = Drizzle, not freezing, intermittent, heavy (dense) at time of observation
         55 = Drizzle, not freezing, continuous, heavy (dense) at time of observation
         56 = Drizzle, freezing, slight
         57 = Drizzle, freezing, moderate or heavy (dense)
         58 = Drizzle and rain, slight
         59 = Drizzle and rain, moderate or heavy
         60 = Rain, not freezing, intermittent, slight at time of observation
         61 = Rain, not freezing, continuous, slight at time of observation
         62 = Rain, not freezing, intermittent, moderate at time of observation
         63 = Rain, not freezing, continuous, moderate at time of observation
         64 = Rain, not freezing, intermittent, heavy at time of observation
         65 = Rain, not freezing, continuous, heavy at time of observation
         66 = Rain, freezing, slight
         67 = Rain, freezing, moderate or heavy
         68 = Rain or drizzle and snow, slight
         69 = Rain or drizzle and snow, moderate or heavy
         70 = Intermittent fall of snowflakes, slight at time of observation
         71 = Continuous fall of snowflakes, slight at time of observation
         72 = Intermittent fall of snowflakes, moderate at time of observation
         73 = Continuous fall of snowflakes, moderate at time of observation
         74 = Intermittent fall of snowflakes, heavy at time of observation
         75 = Continuous fall of snowflakes, heavy at time of observation
         76 = Diamond dust (with or without fog)
         77 = Snow grains (with or without fog)
         78 = Isolated star-like snow crystals (with or without fog)
        79 = Ice pellets
        80 = Rain shower(s), slight
        81 = Rain shower(s), moderate or heavy
        82 = Rain shower(s), violent
        83 = Shower(s) of rain and snow mixed, slight
        84 = Shower(s) of rain and snow mixed, moderate or heavy
        85 = Show shower(s), slight
        86 = Snow shower(s), moderate or heavy
        87 = Shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed, slight
        88 = Shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed, moderate or heavy
         89 = Shower(s) of hail (hail, small hail, snow pellets), with or without rain or rain and snow mixed, not associated
               with thunder, slight
         90 = Shower(s) of hail (hail, small hail, snow pellets), with or without rain or rain and snow mixed, not associated
               with thunder, moderate or heavy
         91 = Slight rain at time of observation, thunderstorm during the preceding hour but not at time of observation
         92 = Moderate or heavy rain at time of observation, thunderstorm during the preceding hour but not at time of
               observation
         93 = Slight snow, or rain and snow mixed or hail (Hail, small hail, snow pellets), at time of observation,
               thunderstorm during the preceding hour but not at time of observation
         94 = Moderate or heavy snow, or rain and snow mixed or hail(Hail, small hail, snow pellets) at time of observation,
               thunderstorm during the preceding hour but not at time of observation
        95 = Thunderstorm, slight or moderate, without hail (Hail, small hail, snow pellets), but with rain and/or snow at time
               of observation, thunderstorm at time of observation
        96 = Thunderstorm, slight or moderate, with hail (hail, small hail, snow pellets) at time of observation, thunderstorm
               at time of observation
         97 = Thunderstorm, heavy, without hail (Hail, small hail, snow pellets), but with rain and/or snow at time of
               observation, thunderstorm at time of observation




                                                        97


---

                98 = Thunderstorm combined with duststorm or sandstorm at time of observation, thunderstorm at time of
                     observation
                99 = Thunderstorm, heavy, with hail (Hail, small hail, snow pellets) at time of observation, thunderstorm at time of
                     observation

FLD LEN: 1
         PRESENT-WEATHER-OBSERVATION quality manual atmospheric condition code
         The code that denotes a quality status of a reported present weather observation from a manual station.
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

Wind Data

FLD LEN: 3
         SUPPLEMENTARY-WIND-OBSERVATION identifier
         The identifier that denotes the start of a SUPPLEMENTARY-WIND-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               OA1 - OA3: An indicator of up to 3 occurrences of the following item:
                              SUPPLEMENTARY-WIND-OBSERVATION type code
                              SUPPLEMENTARY-WIND-OBSERVATION period quantity
                              SUPPLEMENTARY-WIND-OBSERVATION speed rate
                              SUPPLEMENTARY-WIND-OBSERVATION speed rate quality code

FLD LEN: 1
          SUPPLEMENTARY-WIND-OBSERVATION type code
          The code that denotes a type of SUPPLEMENTARY-WIND-OBSERVATION.
          DOM: A specific domain comprised of the ASCII characters.
                1 = Average speed of prevailing wind
                2 = Mean wind speed
                3 = Maximum instantaneous wind speed
                4 = Maximum gust speed
                5 = Maximum mean wind speed
                6 = Maximum 1-minute mean wind speed
                9 = Missing

FLD LEN: 2
          SUPPLEMENTARY-WIND-OBSERVATION period quantity
          The quantity of time over which a SUPPLEMENTARY-WIND-OBSERVATION occurred.
          MIN: 01          MAX: 48          UNITS: Hours
          DOM: A general domain comprised of the numeric characters (0-9).
                99 = Missing

FLD LEN: 4
         SUPPLEMENTARY-WIND-OBSERVATION speed rate
         The rate of horizontal speed of air reported in the SUPPLEMENTARY-WIND-OBSERVATION.
         MIN: 0000       MAX: 2000       UNITS: Meters per Second
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing

FLD LEN: 1
         SUPPLEMENTARY-WIND-OBSERVATION speed rate quality code
         The code that denotes a quality status of the reported SUPPLEMENTARY-WIND-OBSERVATION speed rate.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect


                                                                 98


---

                  3 = Erroneous
                  9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         Hourly/Sub-Hourly Wind Section identifier
         The identifier that indicates an observation of wind speed at a height of 1.5 meters from the ground, typically
         used by Climate Reference Network stations. This section appears one or more time per hour. The wind average value
         in this section is a duplicate of the wind average value in the mandatory data section. It is included in this section so that
         all wind values are conveniently available in a single section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
                 OB1, OB2: An indicator of the following items:
                             WIND_AVG time period
                             WIND_MAX maximum gust
                             WIND_MAX_QC quality code
                             WIND_MAX_FLAG quality code
                             WIND_MAX direction of the maximum gust
                             WIND_MAX_QC direction quality code
                             WIND_MAX_FLAG direction quality code
                             WIND_STD wind speed standard deviation
                             WIND_STD_QC quality code
                             WIND_STD_FLAG quality code
                             WIND_DIR_STD wind direction standard deviation
                             WIND_DIR_STD_QC quality code
                             WIND_DIR_STD_FLAG quality code

FLD LEN: 3
         WIND_AVG Time period in minutes, for which the data in this section (OB1) pertains—eg, 060 = 60 minutes (1
hour).
         MIN: 001       MAX: 998      UNITS: Minutes
         DOM: A general domain comprised of the numeric characters (0-9).
              999 = Missing.

FLD LEN: 4
         WIND_MAX maximum gust
         The maximum 10 second wind speed.
         MIN: 0000       MAX: 9998      UNITS: meters per second
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing.

FLD LEN: 1
         WIND_MAX_QC quality code
         The code that indicates ISD’s evaluation of the quality status of the maximum gust.
         DOM: A specific domain comprised of the numeric characters (0-9).
               1 = Passed all quality control checks
               3 = Failed all quality control checks
               9 = Missing

FLD LEN: 1
         WIND_MAX_FLAG quality code
         A flag that indicates the network’s internal evaluation of the quality status of the maximum gust. Most users will find the
         preceding quality code WIND_MAX_QC to be the simplest and most useful quality indicator.
         DOM: A specific domain comprised of the numeric characters (0-9)
                0 = Passed all quality control checks
                1 – 8 = Did not pass all quality checks
                9 = Missing

FLD LEN: 3
         WIND_MAX direction of the maximum gust
         The direction measured in clockwise angular degrees from which the maximum 10 second wind speed occurred.
         MIN: 001        MAX: 360       UNITS: Angular degrees
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9).
               999 = Missing.




                                                                  99


---

FLD LEN: 1
         WIND_MAX_QC direction quality code
         The code that indicates ISD’s evaluation of the quality status of the maximum gust direction.
         DOM: A specific domain comprised of the numeric characters (0-9).
               1 = Passed all quality control checks
               3 = Failed all quality control checks
               9 = Missing

FLD LEN: 1
         WIND_MAX_FLAG direction quality code
          A flag that indicates the network’s internal evaluation of the quality status of the maximum gust direction. Most users will
         find the preceding quality code WIND_MAX_QC to be the simplest and most useful quality indicator.
         DOM: A specific domain comprised of the numeric characters (0-9)
                0 = Passed all quality control checks
                1 – 8 = Did not pass all quality checks
                9 = Missing

FLD LEN: 5
         WIND_STD wind speed standard deviation
         The wind speed standard deviation.
         MIN: 00000        MAX: 99998
         SCALING FACTOR: 100
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         WIND_STD_QC quality code
         The code that indicates ISD’s evaluation of the quality status of the wind speed standard deviation.
         DOM: A specific domain comprised of the numeric characters (0-9).
               1 = Passed all quality control checks
               3 = Failed all quality control checks
               9 = Missing

FLD LEN: 1
         WIND_STD_FLAG quality code
         A flag that indicates the network’s internal evaluation of the quality status of the wind speed standard deviation. Most
         users will find the preceding quality code WIND_STD_QC to be the simplest and most useful quality indicator.
         DOM: A specific domain comprised of the numeric characters (0-9)
               0 = Passed all quality control checks
               1 – 8 = Did not pass all quality checks
               9 = Missing

FLD LEN: 5
         WIND_DIR_STD wind direction standard deviation
         The wind direction standard deviation.
         MIN: 00000         MAX: 99998
         SCALING FACTOR: 100
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing.

FLD LEN: 1
         WIND_DIR_STD_QC quality code
         The code that indicates ISD’s evaluation of the quality status of the wind direction standard deviation.
         DOM: A specific domain comprised of the numeric characters (0-9).
               1 = Passed all quality control checks
               3 = Failed all quality control checks
               9 = Missing

FLD LEN: 1
         WIND_DIR_STD_FLAG quality code
         A flag that indicates the network’s internal evaluation of the quality status of the wind direction standard deviation. Most
         users will find the preceding quality code WIND_STD_QC to be the simplest and most useful quality indicator.
         DOM: A specific domain comprised of the numeric characters (0-9)
               0 = Passed all quality control checks
               1 – 8 = Did not pass all quality checks
               9 = Missing


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀



                                                                100


---

FLD LEN: 3
         WIND-GUST-OBSERVATION identifier
         The identifier that denotes the start of a WIND-GUST-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               OC1: An indicator of the occurrence of the following item:
                      WIND-GUST-OBSERVATION speed rate
                      WIND-GUST-OBSERVATION quality code

FLD LEN: 4
         WIND-GUST-OBSERVATION speed rate
         The rate of speed of a wind gust.
         MIN: 0050      MAX: 1100      UNITS: Meters per second
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing

FLD LEN: 1
         WIND-GUST-OBSERVATION quality code
         The code that denotes a quality status of a reported WIND-GUST-OBSERVATION speed rate.
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
         SUPPLEMENTARY-WIND-OBSERVATION identifier
         The identifier that denotes the start of a SUPPLEMENTARY-WIND-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               OD1 - OD3: An indicator of up to 3 occurrences of the following item:
                              SUPPLEMENTARY-WIND-OBSERVATION type code
                              SUPPLEMENTARY-WIND-OBSERVATION period quantity
                              SUPPLEMENTARY-WIND-OBSERVATION direction quantity
                              SUPPLEMENTARY-WIND-OBSERVATION speed rate
                              SUPPLEMENTARY-WIND-OBSERVATION speed rate quality code

FLD LEN: 1
          SUPPLEMENTARY-WIND-OBSERVATION type code
          The code that denotes a type of SUPPLEMENTARY-WIND-OBSERVATION.
          DOM: A specific domain comprised of the ASCII characters.
                1 = Average speed of prevailing wind
                2 = Mean wind speed
                3 = Maximum instantaneous wind speed
                4 = Maximum gust speed
                5 = Maximum mean wind speed
                6 = Maximum 1-minute mean wind speed
                9 = Missing
FLD LEN: 2
          SUPPLEMENTARY-WIND-OBSERVATION period quantity
          The quantity of time over which a SUPPLEMENTARY-WIND-OBSERVATION occurred.
          MIN: 01          MAX: 48          UNITS: Hours
          DOM: A general domain comprised of the numeric characters (0-9).
                99 = Missing




                                                          101


---

FLD LEN: 4
         SUPPLEMENTARY-WIND-OBSERVATION speed rate
         The rate of horizontal speed of air reported in the SUPPLEMENTARY-WIND-OBSERVATION.
         MIN: 0000       MAX: 2000       UNITS: Meters per Second
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing

FLD LEN: 1
         SUPPLEMENTARY-WIND-OBSERVATION speed rate quality code
         The code that denotes a quality status of the reported SUPPLEMENTARY-WIND-OBSERVATION speed rate.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               0 = Passed gross limits check
               1 = Passed all quality control checks
               2 = Suspect
               3 = Erroneous
               9 = missing
 FLD LEN: 3
         SUPPLEMENTARY-WIND-OBSERVATION direction quantity
         The angle, measured in a clockwise direction, between true north and the direction from which the wind is blowing.
         MIN: 001      MAX: 360       UNITS: Angular Degrees
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9).
               999 = Missing
               Note: A direction of 999 with a speed of 0000 indicates calm conditions (0 wind speed).




FLD LEN: 3
         SUMMARY-OF-DAY-WIND-OBSERVATION identifier
         The identifier that denotes the start of a SUMMARY-OF-DAY-WIND-OBSERVATION data section.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               OE1 - OE3: An indicator of up to 3 occurrences of the following item:
                             SUMMARY-OF-DAY-WIND-OBSERVATION type code
                             SUMMARY-OF-DAY-WIND-OBSERVATION period quantity
                             SUMMARY-OF-DAY-WIND-OBSERVATION speed rate
                             SUMMARY-OF-DAY-WIND-OBSERVATION direction
                             SUMMARY-OF-DAY-WIND-OBSERVATION time of occurrence
                             SUMMARY-OF-DAY-WIND-OBSERVATION quality code

FLD LEN: 1
          SUMMARY-OF-DAY-WIND-OBSERVATION type code
          The code that denotes a type of SUMMARY-OF-DAY-WIND-OBSERVATION.
          DOM: A specific domain comprised of the ASCII characters.
                1 = Peak wind speed for the day
                2 = Fastest 2-minute wind speed for the day
                3 = Average wind speed for the day
                4 = Fastest 5-minute wind speed for the day
                5 = Fastest mile wind speed for the day

FLD LEN: 2
          SUMMARY-OF-DAY-WIND-OBSERVATION period quantity
          The quantity of time over which a SUMMARY-OF-DAY-WIND-OBSERVATION occurred.
          MIN: 24          MAX: 24          UNITS: Hours
          DOM: A general domain comprised of the ASCII characters.
                99 = Missing

FLD LEN: 5
         SUMMARY-OF-DAY-WIND-OBSERVATION speed
         The rate of horizontal wind speed of air reported in the SUMMARY-OF-DAY-WIND-OBSERVATION.
         MIN: 00000       MAX: 20000      UNITS: Meters per Second
         SCALING FACTOR: 100
         DOM: A general domain comprised of the numeric characters (0-9).
               99999 = Missing




                                                              102


---

FLD LEN: 3
         SUMMARY-OF-DAY-WIND-OBSERVATION direction of wind
         The angle, measured in a clockwise direction, between true north and the direction from which the wind is blowing, for
         the summary of day wind report.
         MIN: 001      MAX: 360       UNITS: Angular Degrees
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9).
               999 = Missing
               Note: A direction of 999 with a speed of 00000 indicates calm conditions (0 wind speed).

FLD LEN: 4
         SUMMARY-OF-DAY-WIND-OBSERVATION time of occurrence in Z-time (UTC)
         The time of occurrence of the wind reported in the SUMMARY-OF-DAY-WIND-OBSERVATION.
         MIN: 0000      MAX: 2359       UNITS: hours-minutes
         SCALING FACTOR: 10
         DOM: A general domain comprised of the numeric characters (0-9).
               9999 = Missing

FLD LEN: 1
         SUMMARY-OF-DAY-WIND-OBSERVATION quality code
         The code that denotes a quality status of the reported SUMMARY-OF-DAY-WIND-OBSERVATION.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               4 = Passed gross limits check, data originate from an NCEI data source
               5 = Passed all quality control checks, data originate from an NCEI data source
               6 = Suspect, data originate from an NCEI data source
               7 = Erroneous, data originate from an NCEI data source
               M = Manual change made to value based on information provided by NWS or FAA
               9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
         RELATIVE HUMIDITY occurrence identifier
         The identifier that denotes the start of a RELATIVE-HUMIDITY data section
         DOM: A specific domain comprised of the characters in the ASCII character set
               RH1 – RH3: An indicator of up to 3 occurrences of the following items
                              RELATIVE HUMIDITY period quantity
                              RELATIVE HUMIDITY code
                              RELATIVE HUMIDITY percentage
                              RELATIVE HUMIDITY derived code
                              RELATIVE HUMIDITY quality code

FLD LEN: 3
         RELATIVE HUMIDITY period quantity
         The quantity of time over which relative humidity percentages were averaged to determine the RELATIVE HUMIDITY
         MIN: 001 MAX: 744 UNITS: Hours
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9)
               999 = missing

FLD LEN: 1
         RELATIVE HUMIDITY code
         The code that denotes the RELATIVE HUMIDITY as an average, maximum or minimum
         DOM: A specific domain comprised of the characters in the ASCII character set
               M = Mean relative humidity
               N = Minimum relative humidity
               X = Maximum relative humidity
               9 = missing

FLD LEN: 3
         RELATIVE HUMIDITY percentage
          The average maximum or minimum relative humidity for a given period, typically for the day or month, derived from
         other data fields. Note: Values only take into account hourly observations (not specials or other unscheduled
         observations).
         MIN: 000          MAX: 100       UNITS: percent
         SCALING FACTOR: 1
         DOM: A general domain comprised of the numeric characters (0-9).
               999 = missing




                                                              103


---

FLD LEN: 1
         RELATIVE HUMIDITY derived code
         The code that denotes a derived code of the reported RELATIVE HUMIDITY percentage.
         DOM: A specific domain comprised of the characters in the ASCII character set.
               D = Derived from hourly values
               9 = missing


FLD LEN: 1
         RELATIVE HUMIDITY quality code
         The code that denotes a quality status of the reported RELATIVE HUMIDITY percentage
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
