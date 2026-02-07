## Part 9 - Subhourly Temperature Section


---

  7. GEOPHYSICAL-REPORT-TYPE code

Record Structure - Each record is of variable length and is comprised of a
control and mandatory data section and may also contain additional, remarks,
and element quality data sections.

Maximum record size: 2,844 characters

Maximum block length: 8,192 characters for data provided on tape

Control Data Section - The beginning of each record provides information
about the report including date, time, and station location information. Data
fields will be in positions identified in the applicable data definition.
control data section is fixed length and is 60 characters long.

Mandatory Data Section - The mandatory data section contains meteorological
information on the basic elements such as winds, visibility, and temperature.
These are the most commonly reported parameters and are available most of the
time. The mandatory data section is fixed length and is 45 characters long.

Additional Data Section - Variable length data are provided after the
mandatory data. These additional data contain information of significance
and/or which are received with varying degrees of frequency. Identifiers are
used to note when data are present in the record. If all data fields in a
group are missing, the entire group is usually not reported. If no groups are
reported the section will be omitted. The additional data section is variable
in length with a minimum of 0 characters and a maximum of 637 (634 characters
plus a 3 character section identifier) characters.

Note: Specific information (where applicable) pertaining to each variable
group of data elements is provided in the data item definition.

Remarks Data - The numeric and character (plain language) remarks are
provided if they exist. The data will vary in length and are identified in
the applicable data definition. The remarks section has a maximum length of
515 (512 characters plus a 3 character section identifier) characters.

Element Quality Data Section - The element quality data section contains
information on data that have been determined erroneous or suspect during
quality control procedures. Also, some of the original data source codes and
flags are stored here. This section is variable in length and contains 16
characters for each erroneous or suspect parameter. The section has a minimum
length of 0 characters and a maximum length of 1587 (1584 plus a 3 character
section identifier) characters.

Missing Values - Missing values for any non-signed item are filled (i.e.,
999). Missing values for any signed item are positive filled (i.e., +99999).

Longitude and Latitude Coordinates - Longitudes will be reported with
negative values representing longitudes west of 0 degrees, and latiudes will
be negative south of the equator. Although the data field allows for values
to a thousandth of a degree, the values are often only computed to the
hundredth of a degree with a 0 entered in the thousandth position.



    3


---

5.   Access Method and Sort for Supplied Data: See #4 above.

6.   Element Names and Definitions: See documentation below.




    4


---
