FEDERAL CLIMATE COMPLEX
    DATA DOCUMENTATION
    FOR
   INTEGRATED SURFACE DATA
    (ISD)

    January 12, 2018

NOAA - National Centers for Environmental Information
    US Air Force - 14th Weather Squadron
    151 Patton Avenue
    Asheville, NC 28801-5001 USA


## Table of Contents
- [Part 1 - Preface and Dataset Overview](#part-1---preface-and-dataset-overview)
- [Part 2 - Control Data Section](#part-2---control-data-section)
- [Part 3 - Mandatory Data Section](#part-3---mandatory-data-section)
- [Part 4 - Additional Data Section](#part-4---additional-data-section)
- [Precipitation Data](#precipitation-data)
- [Part 5 - Weather Occurrence Data](#part-5---weather-occurrence-data)
- [Part 6 - Climate Reference Network Unique Data](#part-6---climate-reference-network-unique-data)
- [Part 7 - Network Metadata](#part-7---network-metadata)
- [Part 8 - CRN Control Section](#part-8---crn-control-section)
- [Part 9 - Subhourly Temperature Section](#part-9---subhourly-temperature-section)
- [Part 10 - Hourly Temperature Section](#part-10---hourly-temperature-section)
- [Part 11 - Hourly Temperature Extreme Section](#part-11---hourly-temperature-extreme-section)
- [Part 12 - Subhourly Wetness Section](#part-12---subhourly-wetness-section)
- [Part 13 - Hourly Geonor Vibrating Wire Summary Section](#part-13---hourly-geonor-vibrating-wire-summary-section)
- [Part 14 - Runway Visual Range Data](#part-14---runway-visual-range-data)
- [Part 15 - Cloud and Solar Data](#part-15---cloud-and-solar-data)
- [Part 16 - Sunshine Observation Data](#part-16---sunshine-observation-data)
- [Part 17 - Solar Irradiance Section](#part-17---solar-irradiance-section)
- [Part 18 - Net Solar Radiation Section](#part-18---net-solar-radiation-section)
- [Part 19 - Modeled Solar Irradiance Section](#part-19---modeled-solar-irradiance-section)
- [Part 20 - Hourly Solar Angle Section](#part-20---hourly-solar-angle-section)
- [Part 21 - Hourly Extraterrestrial Radiation Section](#part-21---hourly-extraterrestrial-radiation-section)
- [Part 22 - Hail Data](#part-22---hail-data)
- [Part 23 - Ground Surface Data](#part-23---ground-surface-data)
- [Part 24 - Temperature Data](#part-24---temperature-data)
- [Part 25 - Sea Surface Temperature Data](#part-25---sea-surface-temperature-data)
- [Part 26 - Soil Temperature Data](#part-26---soil-temperature-data)
- [Part 27 - Pressure Data](#part-27---pressure-data)
- [Part 28 - Weather Occurrence Data (Extended)](#part-28---weather-occurrence-data-extended)
- [Part 29 - Wind Data](#part-29---wind-data)
- [Part 30 - Marine Data](#part-30---marine-data)

## Part 1 - Preface and Dataset Overview

---

Important notice: In order to accommodate a growing number of stations in the
Integrated Surface Data (ISD), a new methodology for the assignment of
station identifiers is being implemented by approximately January 2013.
Station identifiers which currently appear as an 11-digit numerical field in
positions 5 – 15 of each ISD record in the archive format described in this
document will soon include stations that contain an alphabetic character (A–
Z)for the leading digit (position 5). These assignments will not affect
existing stations unless it becomes necessary to reassign new identifiers to
them. This is occasionally necessary due to station moves or various other
reasons. It will affect most new stations coming into existence after this
implementation occurs. At some point in the future, NCEI will be moving
toward a longer station identifier for ISD. This will extend the current
record layout of the data files and influence all existing station
identifiers which will be reassigned. NCEI will provide further information
on these pending changes as the details are established. You may also keep
abreast of these or other changes by referring to the most recent edition of
the ISD documentation.




1.    Data Set ID:

    DS3505

2.    Data Set Name:

    INTEGRATED SURFACE DATA (ISD)

3.    Data Set Aliases:

    N/A

4.    Access Method and Sort for Archived Data:

The data files are derived from surface observational data, and are stored in
ASCII character format. Data field definitions for elements transmitted are
provided after this preface, providing definition of data fields, position
number for mandatory data fields, field lengths for variable data fields,
minimum/maximum values of transmitted data, and values for missing data
fields. Data are accessible via NCEI’s Climate Data Online system
(cdo.NCEI.noaa.gov), FTP (ftp://ftp.NCEI.noaa.gov/pub/data/noaa/), GIS
services (gis.NCEI.noaa.gov), and by calling NCEI for off-line servicing (see
section 12 below).

Data Sequence - Data will be sequenced using the following data item order:

 1. FIXED-WEATHER-STATION identifier
 2. GEOPHYSICAL-POINT-OBSERVATION date
 3. GEOPHYSICAL-POINT-OBSERVATION time
 4. GEOPHYSICAL-POINT-OBSERVATION latitude coordinates
 5. GEOPHYSICAL-POINT-OBSERVATION longitude coordinates
 6. GEOPHYSICAL-POINT-OBSERVATION type surface report code


    2
