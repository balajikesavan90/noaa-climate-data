## Part 20 - Hourly Solar Angle Section


FLD LEN: 3
    Hourly Solar Angle Section identifier
    The identifier that denotes the start of the Hourly Solar angle data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GQ1 An indicator of the occurrence of the following items:
    Hourly solar angle time period
    Hourly mean zenith angle
    Hourly mean zenith angle quality code
    Hourly mean azimuth angle
    Hourly mean azimuth angle quality code




    73


---

FLD LEN: 4
    Time period in minutes, for which the data in this section pertains—eg, 0060 = 60 minutes (1 hour).
    MIN: 0001         MAX: 9998        UNITS: Minutes
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing data

FLD LEN: 4
    Hourly mean zenith angle (for sunup periods)
    The angle between sun and the zenith as the mean of all 1-minute sunup zenith angle values.
    MIN: 0000      MAX: 3600       UNITS: Angular Degrees
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing data

FLD LEN: 1
    Hourly mean zenith angle quality code
    The code that denotes a quality status of the hourly mean zenith angle.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Hourly mean azimuth angle (for sunup periods)
    The angle between sun and north as the mean of all 1-minute sunup azimuth angle values.
    MIN: 0000      MAX: 3600      UNITS: Angular Degrees
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing data

FLD LEN: 1
    Hourly mean azimuth angle quality code
    The code that denotes a quality status of the hourly mean azimuth angle.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Extraterrestrial Radiation Section identifier
    The identifier that denotes the start of the Hourly Extraterrestrial radiation data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GR1 An indicator of the occurrence of the following items:
    Hourly extraterrestrial radiation time period
    Hourly extraterrestrial radiation on a horizontal surface
    Hourly extraterrestrial radiation on a horizontal surface quality code
    Hourly extraterrestrial radiation normal to the sun
    Hourly extraterrestrial radiation normal to the sun quality code

FLD LEN: 4
    Time period in minutes, for which the data in this section pertains—eg, 0060 = 60 minutes (1 hour).
    MIN: 0001         MAX: 9998        UNITS: Minutes
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing data

FLD LEN: 4
    Hourly extraterrestrial radiation on a horizontal surface
    The amount of solar radiation received (modeled) on a horizontal surface at the top of the atmosphere. Unit is watts per
    square meter (W/m2) in whole values.
    MIN: 0000     MAX: 9998         UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
9999 = Missing data

FLD LEN: 1


    74


---

    Hourly extraterrestrial radiation on a horizontal surface quality code
    The code that denotes a quality status of the hourly extraterrestrial radiation on a horizontal surface value .
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Hourly extraterrestrial radiation normal to the sun
    The amount of solar radiation received (modeled) on a surface normal to the sun at the top of the atmosphere. Unit is
    watts per square meter (W/m2) in whole values.
    MIN: 0000      MAX: 9998        UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing data

FLD LEN: 1
    Hourly extraterrestrial radiation normal to the sun quality code
    The code that denotes a quality status of the hourly extraterrestrial radiation normal to the sun value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


Hail Data

FLD LEN: 3
    HAIL identifier
    The identifier that denotes the start of a HAIL data section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    An indicator of the occurrence of the following item:
    Hail size
    Hail size quality code

FLD LEN: 3
    HAIL size
    The diameter of the largest hailstone observed.
    MIN: 000      MAX: 200         UNITS: Centimeters
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9)
    999 = missing

FLD LEN: 1
    HAIL size quality code
    The code that denotes a quality status of the reported HAIL size.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀




    75


---
