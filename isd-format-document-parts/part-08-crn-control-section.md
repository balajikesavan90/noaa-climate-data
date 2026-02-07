## Part 8 - CRN Control Section


---

POS: 93-93
    AIR-TEMPERATURE-OBSERVATION air temperature quality code
    The code that denotes a quality status of an AIR-TEMPERATURE-OBSERVATION.
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
    A = Data value flagged as suspect, but accepted as a good value
    C = Temperature and dew point received from Automated Weather Observing System (AWOS) are reported in
    whole degrees Celsius. Automated QC flags these values, but they are accepted as valid.
    I = Data value not originally in data, but inserted by validator
    M = Manual changes made to value based on information provided by NWS or FAA
    P = Data value not originally flagged as suspect, but replaced by validator
    R = Data value replaced with value computed by NCEI software
    U = Data value replaced with edited value

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

POS: 94-98
    AIR-TEMPERATURE-OBSERVATION dew point temperature
    The temperature to which a given parcel of air must be cooled at constant pressure and water vapor
    content in order for saturation to occur.
    MIN: -0982      MAX: +0368         UNITS: Degrees Celsius
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +9999 = Missing.


POS: 99-99
    AIR-TEMPERATURE-OBSERVATION dew point quality code
    The code that denotes a quality status of the reported dew point temperature.
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
    A = Data value flagged as suspect, but accepted as a good value
    C = Temperature and dew point received from Automated Weather Observing System (AWOS) are reported in
    whole degrees Celsius. Automated QC flags these values, but they are accepted as valid.
    I = Data value not originally in data, but inserted by validator
    M = Manual changes made to value based on information provided by NWS or FAA
    P = Data value not originally flagged as suspect, but replaced by validator
    R = Data value replaced with value computed by NCEI software
    U = Data value replaced with edited value


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀




    11


---

POS: 100-104
    ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure
    The air pressure relative to Mean Sea Level (MSL).
    MIN: 08600      MAX: 10900      UNITS: Hectopascals
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

POS: 105-105
    ATMOSPHERIC-PRESSURE-OBSERVATION sea level pressure quality code
    The code that denotes a quality status of the sea level pressure of an
    ATMOSPHERIC-PRESSURE-OBSERVATION.
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




    12


---
