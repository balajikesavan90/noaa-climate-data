## Part 15 - Cloud and Solar Data

Cloud and Solar Data

FLD LEN: 3
    SKY-COVER-LAYER identifier
    The identifier that represents a SKY-COVER-LAYER.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GA1-GA6 An indicator of up to 6 repeating fields of the following items:
    SKY-COVER-LAYER coverage code
    SKY-COVER-LAYER coverage quality code
    SKY-COVER-LAYER base height dimension
    SKY-COVER-LAYER base height quality code
    SKY-COVER-LAYER cloud type code
    SKY-COVER-LAYER cloud type quality code

FLD LEN: 2
    SKY-COVER-LAYER coverage code
    The code that denotes the fraction of the total celestial dome covered by a SKY-COVER-LAYER.
    Note: This is for a discrete cloud layer, as opposed to the cloud later summation data in the GD1-GD6 section.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None, SKC or CLR
    01 = One okta - 1/10 or less but not zero
    02 = Two oktas - 2/10 - 3/10, or FEW
    03 = Three oktas - 4/10
    04 = Four oktas - 5/10, or SCT
    05 = Five oktas - 6/10
    06 = Six oktas - 7/10 - 8/10
    07 = Seven oktas - 9/10 or more but not 10/10, or BKN
    08 = Eight oktas - 10/10, or OVC
    09 = Sky obscured, or cloud amount cannot be estimated
    10 = Partial obscuration
    99 = Missing

FLD LEN: 1
    SKY-COVER-LAYER coverage quality code
    The code that denotes a quality status of the reported SKY-COVER-LAYER coverage.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, from NCEI SURFACE HOURLY
    5 = Passed all quality control checks, from NCEI SURFACE HOURLY
    6 = Suspect, from NCEI SURFACE HOURLY
    7 = Erroneous, from NCEI SURFACE HOURLY
    M = Manual change made to value based on information provided by NWS or FAA
    9 = Passed gross limits check if element is present
FLD LEN: 6
    SKY-COVER-LAYER base height dimension
    The height relative to a VERTICAL-REFERENCE-DATUM of the lowest surface of a cloud.
    MIN: -00400      MAX: +35000       UNITS: Meters
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9), a plus sign (+), and a minus sign (-).
    +99999 = Missing

FLD LEN: 1
    SKY-COVER-LAYER base height quality code
    The code that denotes a quality status of the reported SKY-COVER-LAYER base height.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, from NCEI SURFACE HOURLY
    5 = Passed all quality control checks, from NCEI SURFACE HOURLY
    6 = Suspect, from NCEI SURFACE HOURLY
    7 = Erroneous, from NCEI SURFACE HOURLY
    M = Manual change made to value based on information provided by NWS or FAA


    54


---

9 = Passed gross limits check if element is present

FLD LEN: 2
    SKY-COVER-LAYER cloud type code
    The code that denotes the classification of the clouds that comprise a SKY-COVER-LAYER.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = Cirrus (Ci)
    01 = Cirrocumulus (Cc)
    02 = Cirrostratus (Cs)
    03 = Altocumulus (Ac)
    04 = Altostratus (As)
    05 = Nimbostratus (Ns)
    06 = Stratocumulus (Sc)
    07 = Stratus (St)
    08 = Cumulus (Cu)
    09 = Cumulonimbus (Cb)
    10 = Cloud not visible owing to darkness, fog, duststorm, sandstorm, or other analogous phenonomena/sky
    obcured
    11 = Not used
    12 = Towering Cumulus (Tcu)
    13 = Stratus fractus (Stfra)
    14 = Stratocumulus Lenticular (Scsl)
    15 = Cumulus Fractus (Cufra)
    16 = Cumulonimbus Mammatus (Cbmam)
    17 = Altocumulus Lenticular (Acsl)
    18 = Altocumulus Castellanus (Accas)
    19 = Altocumulus Mammatus (Acmam)
    20 = Cirrocumulus Lenticular (Ccsl)
    21 = Cirrus and/or Cirrocumulus
    22 = jenkins-content-114Stratus and/or Fracto-stratus
    23 = Cumulus and/or Fracto-cumulus
    99 = Missing

FLD LEN: 1
    SKY-COVER-LAYER cloud type quality code
    The code that denotes a quality status of the reported SKY-COVER-LAYER cloud type.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, from NCEI SURFACE HOURLY
    5 = Passed all quality control checks, from NCEI SURFACE HOURLY
    6 = Suspect, from NCEI SURFACE HOURLY
    7 = Erroneous, from NCEI SURFACE HOURLY
    M = Manual change made to value based on information provided by NWS or FAA
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    SKY-COVER-SUMMATION-STATE identifier
    The identifier that denotes the availability of a SKY-COVER-SUMMATION-STATE.
    DOM: A specific domain comprised of the ASCII characters.
    GD1 - GD6 An indicator of up to 6 repeating fields of the following items:
    SKY-COVER-SUMMATION-STATE coverage code
    SKY-COVER-SUMMATION-STATE coverage code #2
    SKY-COVER-SUMMATION-STATE coverage quality code
    SKY-COVER-SUMMATION-STATE height dimension
    SKY-COVER-SUMMATION-STATE height dimension quality code
    SKY-COVER-SUMMATION-STATE characteristic code

FLD LEN: 1
    SKY-COVER-SUMMATION-STATE coverage code
    The code that denotes the portion of the total celestial dome covered by all layers of clouds and other
    obscuring phenomena at or below a given height.
    DOM: A specific domain comprised of the ASCII characters
    0 = Clear - No coverage
    1 = FEW - 2/8 or less coverage (not including zero)



    55


---

    2 = SCATTERED - 3/8-4/8 coverage
    3 = BROKEN - 5/8-7/8 coverage
    4 = OVERCAST - 8/8 coverage
    5 = OBSCURED
    6 = PARTIALLY OBSCURED
    9 = MISSING

FLD LEN: 2
    SKY-COVER-SUMMATION coverage code #2
    The code that denotes the fraction of the total celestial dome covered by a by all layers of clouds and other
    obscuring phenomena at or below a given height, if reported by the station in octas.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None, SKC or CLR
    01 = One okta - 1/10 or less but not zero
    02 = Two oktas - 2/10 - 3/10, or FEW
    03 = Three oktas - 4/10
    04 = Four oktas - 5/10, or SCT
    05 = Five oktas - 6/10
    06 = Six oktas - 7/10 - 8/10
    07 = Seven oktas - 9/10 or more but not 10/10, or BKN
    08 = Eight oktas - 10/10, or OVC
    09 = Sky obscured, or cloud amount cannot be estimated
    10 = Partial Obscuration
    11 = Thin Scattered
    12 = Scattered
    13 = Dark Scattered
    14 = Thin Broken
    15 = Broken
    16 = Dark Broken
    17 = Thin Overcast
    18 = Overcast
    19 = Dark overcast
    99 = Missing

FLD LEN: 1
    SKY-COVER-SUMMATION-STATE coverage quality code
    The code that denotes a quality status of the reported SKY-COVER-SUMMATION-STATE coverage.
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

FLD LEN: 6
    SKY-COVER-SUMMATION-STATE height dimension
    The height above ground level (AGL) of the base of the cloud layer or obscuring phenomena.
    MIN: -00400           MAX: +35000             UNITS: meters
    SCALING FACTOR: 1
    DOM: A general domain compirsed of the ASCII characters 0-9, a plus (+) and a minus sign (-).
    +99999 = Missing

FLD LEN: 1
    SKY-COVER-SUMMATION-STATE height dimension quality code
    The code that denotes a quality status of the reported SKY-COVER-SUMMATION-STATE height dimension.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits checkchec, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present



    56


---

FLD LEN: 1
    SKY-COVER-SUMMATION-STATE characteristic code
    The code that represents a characteristic of a specific cloud or other obscuring phenomena layer.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    1 = Variable height
    2 = Variable amount
    3 = Thin clouds
    4 = Dark layer (reported in data prior to 1950)
    9 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
FLD LEN: 3
    SKY-CONDITION-OBSERVATION identifier
    An indicator that denotes the start of a SKY-CONDITION-OBSERVATION data group.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GE1: An indicator of the occurrence of the following data items:
    SKY-CONDITION-OBSERVATION convective cloud attribute
    SKY-CONDITION-OBSERVATION vertical datum attribute
    SKY-CONDITION-OBSERVATION base height upper range attribute
    SKY-CONDITION-OBSERVATION base height lower range attribute

FLD LEN: 1
    SKY-CONDITION-OBSERVATION convective cloud attribute
    The code that denotes the convective cloud type in an observation.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = None
    1 = ACSL (Altocumulus Standing Lenticular)
    2 = ACCAS (Altocumulus Castelanus)
    3 = TCU (Towering Cumulus)
    4 = MDT CU (Moderate Cumulus)
    5 = CB/CB MAM DISTANT (Cumulonimbus or Cumulonimbus Mammatus in the distance)
    6 = CB/CBMAM (Cumulonimbus or Cumulonimbus Mammatus within 20 nautical miles)
    7 = Unknown
    9 = missing
FLD LEN: 6
    SKY-CONDITION-OBSERVATION vertical datum attribute
    The code that represents a VERTICAL-REFERENCE-DATUM. Under the stewardship of the FDAD for Intelligence.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    AGL: Above Ground Level
    ALAT: Approximate lowest astronomical tide
    AP: Apparent
    CFB: Crest of first berm
    CRD: Columbia River datum
    ESLW: Equatorial Spring low water
    GCLWD: Gulf Coast low water datum
    HAT: Highest astronomical tide
    HHW: Higher high water
    HTWW: High tide wave wash
    HW: High water
    HWFC: High water full and change
    IND: Indefinite
    ISLW: Indian Spring low water
    LAT: Lowest astronomical tide
    LLW: Lowest low water
    LNLW: Lowest normal low water
    LRLW: Lower low water
    LSD: Land survey datum
    LW: Low water
    LWD: Low water datum
    LWFC: Low water full and charge
    MHHW: Mean higher high water
    MHLW: Mean higher low water
    MHW: Mean high water
    MHWN: Mean high water neap
    MHWS: Mean high water spring
    MLHW: Mean lower high water
    MLLW: Mean lower low water
    MLLWS: Mean lower low water springs



    57


---

    MLWN: Mean low water neap
    MLW: Mean low water
    MLWS: Mean low water spring
    MSL: Mean sea level
    MTL: Mean tide level
    NC: No correction
    NT: Neap tide
    ST: Spring tide
    SWA: Storm wave action
    TLLW: Tropic lower low water
    UD: Undetermined
    UK: Unknown
    WGS84E: WGS84 Ellispoid
    WGS84G: WGS84 GEOID
    999999: missing

FLD LEN: 6
    SKY-CONDITION-OBSERVATION base height upper range attribute
    The height relative to a VERTICAL-REFERENCE-DATUM for cloud bases reported in a range or the highest theight for a
    variable cloud height report. The concept of a range is to accommodate the WMO practice of reporting a cloud layer by a
    range of heights.
    MIN: -0400              MAX: +15000             UNITS: meters
    DOM: A general domain compirsed of the ASCII characters 0-9, a plus (+) and a minus sign (-).
    +99999 = Missing

FLD LEN: 6
    SKY-CONDITION-OBSERVATION base height lower range attribute
    The height relative to a VERTICAL-REFERENCE-DATUM for cloud bases reported in a range or lowest height for a
    variable cloud height report. The concept of a range is to accommodate the WMO ractice of reporting a cloud layer by
    arange of heights.
    MIN: -0400              MAX: +15000             UNITS: meters
    DOM: A general domain compirsed of the ASCII characters 0-9, a plus (+) and a minus sign (-).
    +99999 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    SKY-CONDITION-OBSERVATION identifier
    An indicator that denotes the start of a SKY-CONDITION-OBSERVATION data group.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GF1: An indicator of the occurrence of the following data items:
    SKY-CONDITION-OBSERVATION total coverage code
    SKY-CONDITION-OBSERVATION total opaque coverage code
    SKY-CONDITION-OBSERVATION quality total coverage code
    SKY-CONDITION-OBSERVATION total lowest cloud cover code
    SKY-CONDITION-OBSERVATION quality total lowest cloud cover code
    SKY-CONDITION-OBSERVATION low cloud genus code
    SKY-CONDITION-OBSERVATION quality low cloud genus code
    SKY-CONDITION-OBSERVATION lowest cloud base height dimension
    SKY-CONDITION-OBSERVATION lowest cloud base height quality code
    SKY-CONDITION-OBSERVATION mid cloud genus code
    SKY-CONDITION-OBSERVATION quality mid cloud genus code
    SKY-CONDITION-OBSERVATION high cloud genus code
    SKY-CONDITION-OBSERVATION quality high cloud genus code

FLD LEN: 2
    SKY-CONDITION-OBSERVATION total coverage code
    The code that denotes the fraction of the total celestial dome covered by clouds or other obscuring phenomena.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None, SKC or CLR
    01 = One okta - 1/10 or less but not zero
    02 = Two oktas - 2/10 - 3/10, or FEW
    03 = Three oktas - 4/10
    04 = Four oktas - 5/10, or SCT
    05 = Five oktas - 6/10
    06 = Six oktas - 7/10 - 8/10
    07 = Seven oktas - 9/10 or more but not 10/10, or BKN
    08 = Eight oktas - 10/10, or OVC
    09 = Sky obscured, or cloud amount cannot be estimated



    58


---

    10 = Partial obscuration
    11 = Thin scattered
    12 = Scattered
    13 = Dark scattered
    14 = Thin broken
    15 = Broken
    16 = Dark broken
    17 = Thin overcast
    18 = Overcast
    19 = Dark overcast
    99 = Missing

FLD LEN: 2
    SKY-CONDITION-OBSERVATION total opaque coverage code
    The code that denotes the fraction of the total celestial dome covered by opaque clouds or other obscuring phenomena.
    Only reported by selected U.S. stations during selected periods.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None, SKC or CLR
    01 = One okta - 1/10 or less but not zero
    02 = Two oktas - 2/10 - 3/10, or FEW
    03 = Three oktas - 4/10
    04 = Four oktas - 5/10, or SCT
    05 = Five oktas - 6/10
    06 = Six oktas - 7/10 - 8/10
    07 = Seven oktas - 9/10 or more but not 10/10, or BKN
    08 = Eight oktas - 10/10, or OVC
    09 = Sky obscured, or cloud amount cannot be estimated
    10 = Partial obscuration
    12 = Scattered
    13 = Dark scattered
    15 = Broken
    16 = Dark broken
    18 = Overcast
    19 = Dark overcast
    99 = Missing

FLD LEN: 1
    SKY-CONDITION-OBSERVATION quality total coverage code
    The code that denotes a quality status of a reported total sky coverage code.
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
    SKY-CONDITION-OBSERVATION total lowest cloud cover code
    The code that represents the fraction of the celestial dome covered by all low clouds present. If
    no low clouds are present; the code denotes the fraction covered by all middle level clouds present.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None
    01 = One okta or 1/10 or less but not zero
    02 = Two oktas or 2/10 - 3/10
    03 = Three oktas or 4/10
    04 = Four oktas or 5/10
    05 = Five oktas or 6/10
    06 = Six oktas or 7/10 - 8/10
    07 = Seven oktas or 9/10 or more but not 10/10
    08 = Eight oktas or 10/10
    09 = Sky obscured, or cloud amount cannot be estimated
    10 = Partial obscuration
    11 = Thin Scattered
    12 = Scattered
    13 = Dark Scattered



    59


---

    14 = Thin Broken
    15 = Broken
    16 = Dark Broken
    17 = Thin Overcast
    18 = Overcast
    19 = Dark overcast
    99 = Missing

FLD LEN: 1
    SKY-CONDITION-OBSERVATION quality total lowest cloud cover code
    The code that denotes a quality status of a reported total lowest cloud cover code.
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
    SKY-CONDITION-OBSERVATION low cloud genus code
    The code that denotes a type of low cloud.
    DOM: A specific domain comprised of the characters in the ASCII Character set.
    00 = No low clouds
    01 = Cumulus humulis or Cumulus fractus other than of bad weather or both
    02 = Cumulus mediocris or congestus, with or without Cumulus of species fractus or humulis or
    Stratocumulus all having bases at the same level
    03 = Cumulonimbus calvus, with or without Cumulus, Stratocumulus or Stratus
    04 = Stratocumulus cumulogenitus
    05 = Stratocumulus other than Stratocumulus cumulogenitus
    06 = Stratus nebulosus or Stratus fractus other than of bad weather, or both
    07 = Stratus fractus or Cumulus fractus of bad weather, both (pannus) usually below Altostratus or Nimbostratus.
    08 = Cumulus and Stratocumulus other than Stratocumulus cumulogenitus, with bases at different levels
    09 = Cumulonimbus capillatus (often with an anvil), with or without Cumulonimbus calvus,
    Cumulus, Stratocumulus, Stratus or pannus
    99 = Missing

FLD LEN: 1
    SKY-CONDITION-OBSERVATION quality low cloud genus code
    The code that denotes a quality status of a reported low cloud type.
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

FLD LEN: 5
    SKY-CONDITION-OBSERVATION lowest cloud base height dimension
    The height, above ground level (AGL), of the base of the lowest cloud.
    MIN: -0400     MAX: 15000       UNITS: Meters
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    SKY-CONDITION-OBSERVATION lowest cloud base height quality code
    The code that denotes a quality status of a lowest cloud base height.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect



    60


---

    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

FLD LEN: 2
    SKY-CONDITION-OBSERVATION mid cloud genus code
    The code that denotes a type of middle level cloud.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = No middle clouds
    01 = Altostratus translucidus
    02 = Altostratus opacus or Nimbostratus
    03 = Altocumulus translucidus at a single level
    04 = Patches (often lenticulre) of Altocumulus translucidus, continually changing and occurring at one or more
    levels
    05 = Altocumulus translucidus in bands, or one or more layers of Altocumulus translucidus or opacus, progressing
    invading the sky; these Altocumulus clouds generally thicken as a whole
    06 = Altocumulus cumulogentis (or cumulonimbogentus)
    07 = Altocumulus translucidus or opacus in two or more layers, or Altocumulus opacus in a single layer, not
    progressively invading the sky, or Altocumulus with Altostratus or Nimbostratus
    08 = Altocumulus castellanus or floccus
    09 = Altocumulus of a chaotic sky; generally at several levels
    99 = Missing

FLD LEN: 1
    SKY-CONDITION-OBSERVATION quality mid cloud genus code
    The code that denotes a quality status of a reported mid cloud type.
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
    SKY-CONDITION-OBSERVATION high cloud genus code
    The code that denotes a type of high cloud.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = No High Clouds
    01 = Cirrus fibratus, sometimes uncinus, not progressively invading the sky
    02 = Cirrus spissatus, in patches or entangled sheaves, which usually do not increase and sometimes seem to be
    the remains of the upper part of a Cumulonimbus; or Cirrus castellanus or floccus
    03 = Cirrus spissatus cumulonimbogenitus
    04 = Cirrus unicinus or fibratus, or both, progressively invading the sky; they generally thicken as a whole
    05 = Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone, progressively invading the sky; they generally
    thicken as a whole, but the continuous veil does not reach 45 degrees above the horizon
    06 = Cirrus (often in bands) and Cirrostratus, or Cirrostratus alone, progressively invading the sky; they generally
    thicken as a whole; the continuous veil extends more than 45 degrees above the horizon, without the sky
    being totally covered.
    07 = Cirrostratus covering the whole sky
    08 = Cirrostratus not progressively invading the sky and not entirely covering it
    09 = Cirrocumulus alone, or Cirrocumulus predominant among the High clouds
    99 = Missing

FLD LEN: 1
    SKY-CONDITION-OBSERVATION quality high cloud genus code
    The code that denotes a quality status of a reported high cloud type.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    4 = Passed gross limits check, data originate from an NCEI data source



    61


---

    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    BELOW-STATION-CLOUD-LAYER identifier
    The identifier that represents a BELOW-STATION-CLOUD-LAYER.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GG1-GG6 An indicator of up to 6 repeating fields of the following items:
    BELOW-STATION-CLOUD-LAYER coverage code
    BELOW-STATION-CLOUD-LAYER coverage quality code
    BELOW-STATION-CLOUD-LAYER top height dimension
    BELOW-STATION-CLOUD-LAYER top height dimension quality code
    BELOW-STATION-CLOUD-LAYER type code
    BELOW-STATION-CLOUD-LAYER type quality code
    BELOW-STATION-CLOUD-LAYER top code
    BELOW-STATION-CLOUD-LAYER top quality code

FLD LEN: 2
    BELOW-STATION-CLOUD-LAYER coverage code
    The code that denotes the extent of coverage of a BELOW-STATION-CLOUD-LAYER.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = None
    01 = One okta - 1/10 or less but not zero
    02 = Two oktas - 2/10 - 3/10
    03 = Three oktas - 4/10
    04 = Four oktas - 5/10
    05 = Five oktas - 6/10
    06 = Six oktas - 7/10 - 8/10
    07 = Seven oktas - 9/10 or more but not 10/10
    08 = Eight oktas - 10/10
    09 = Sky obscured, or cloud amount cannot be estimated
    10 = Partial obscuration
    99 = Missing

FLD LEN: 1
    BELOW-STATION-CLOUD-LAYER coverage quality code
    The code that denotes a quality status of the reported BELOW-STATION-CLOUD-LAYER coverage.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

FLD LEN: 5
    BELOW-STATION-CLOUD-LAYER top height dimension
    The height above mean sea level (MSL) of the top of a BELOW-STATION-CLOUD-LAYER.
    MIN: 00000     MAX: 35000      UNITS: Meters
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing

FLD LEN: 1
    BELOW-STATION-CLOUD-LAYER top height dimension quality code
    The code that denotes a quality status of the reported BELOW-STATION-CLOUD-LAYER top height dimension.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present




    62


---

FLD LEN: 2
    BELOW-STATION-CLOUD-LAYER type code
    The code that denotes the classification of the clouds that comprise a BELOW-STATION-CLOUD-LAYER.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = Cirrus (Ci)
    01 = Cirrocumulus (Cc)
    02 = Cirrostratus (Cs)
    03 = Altocumulus (Ac)
    04 = Altostratus (As)
    05 = Nimbostratus (Ns)
    06 = Stratocumulus (Sc)
    07 = Stratus (St)
    08 = Cumulus (Cu)
    09 = Cumulonimbus (Cb)
    10: Cloud not visible owing to darkness, fog, dust storm, sandstorm, or other analogous phenomena
    99 = Missing

FLD LEN: 1
    BELOW-STATION-CLOUD-LAYER type quality code
    The code that denotes a quality status of the reported BELOW-STATION-CLOUD-LAYER type.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

FLD LEN: 2
    BELOW-STATION-CLOUD-LAYER top code
    The code that denotes the characteristics of the upper surface of a BELOW-STATION-CLOUD-LAYER
    DOM: A specific domain comprised of the characters in the ASCII character set.
    00 = Isolated cloud or fragments of clouds
    01 = Continuous flat tops
    02 = Broken cloud - small breaks, flat tops
    03 = Broken cloud - large breaks, flat tops
    04 = Continuous cloud, undulation tops
    05 = Broken cloud - small breaks, undulating tops
    06 = Broken cloud - large breaks, undulating tops
    07 = Continuous or almost continuous with towering clouds above the top of the layer
    08 = Groups of waves with towering clouds above the top of the layer
    09 = Two of more layers at different levels
    99 = Missing

FLD LEN: 1
    BELOW-STATION-CLOUD-LAYER top quality code
    The code that denotes a quality status of the reported BELOW-STATION-CLOUD-LAYER top.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Passed gross limits check if element is present

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Hourly Solar Radiation Section identifier
    The identifier that indicates an hourly observation of solar radiation. This section appears in the last ISD record of
    the hour.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GH1 An indicator of the following items:
    SOLARAD hourly average solar radiation
    SOLARAD_QC quality code
    SOLARAD_FLAG quality code
    SOLARAD_MIN minimum solar radiation
    SOLARAD_MIN_QC quality code
    SOLARAD_MIN_FLAG quality code
    SOLARAD_MAX maximum solar radiation
    SOLARAD_MAX_QC quality code



    63


---

    SOLARAD_MAX_FLAG quality code
    SOLARAD_STD solar radiation standard deviation
    SOLARAD_STD_QC quality code
    SOLARAD_STD_FLAG quality code

FLD LEN: 5
    SOLARAD hourly average solar radiation
    The hourly average solar radiation.
    MIN: 0000      MAX: 99998        UNITS: watts per square meter
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    SOLARAD_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly average solar radiation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SOLARAD_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly average solar radiation. Most
    users will find the preceding quality code SOLARAD_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 5
    SOLARAD_MIN minimum solar radiation
    The minimum 10 second solar radiation for the hour.
    MIN: 00000     MAX: 99998       UNITS: watts per square meter
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    SOLARAD_MIN_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly minimum solar radiation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SOLARAD_MIN_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of the hourly minimum solar radiation. Most
    users will find the preceding quality code SOLARAD_MIN_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 5
    SOLARAD_MAX maximum solar radiation
    The maximum 10 second solar radiation for the hour.
    MIN: 00000     MAX: 99998      UNITS: watts per square meter
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    SOLARAD_MAX_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly maximum solar radiation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SOLARAD_MAX_FLAG quality code



    64


---

    The code that indicates the network’s internal evaluation of the quality status of the hourly maximum solar radiation.
    Most users will find the preceding quality code SOLARAD_MAX_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

FLD LEN: 5
    SOLARAD_STD solar radiation standard deviation
    The hourly 10 second hourly solar radiation standard deviation.
    MIN: 00000      MAX: 99998
    SCALING FACTOR: 10
    DOM: A general domain comprised of the numeric characters (0-9).
    99999 = Missing.

FLD LEN: 1
    SOLARAD_STD_QC quality code
    The code that indicates ISD’s evaluation of the quality status of the hourly solar radiation standard deviation.
    DOM: A specific domain comprised of the numeric characters (0-9).
    1 = Passed all quality control checks
    3 = Failed all quality control checks
    9 = Missing

FLD LEN: 1
    SOLARAD_STD_FLAG quality code
    The code that indicates the network’s internal evaluation of the quality status of hourly solar radiation standard deviation. Most
    users will find the preceding quality code SOLARAD_STD_QC to be the simplest and most useful quality indicator.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed all quality control checks
    other – Did not pass all quality checks

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


FLD LEN: 3
    SUNSHINE-OBSERVATION identifier
    The identifier that denotes the availability of sunshine information.
    DOM: A specific domain comprised of the ASCII characters
    GJ1 An indicator of the occurrence of the following items:
    SUNSHINE-OBSERVATION sunshine duration quantity
    SUNSHINE-OBSERVATION sunshine duration quality code


FLD LEN: 4
    SUNSHINE-OBSERVATION sunshine duration quantity
    The quantity of time sunshine occurred over the reporting period.
    MIN: 0000        MAX: 6000      UNITS: minutes
    DOM: A general domain comprised of the ASCII characters 0-9.
    9999 = Missing

FLD LEN: 1
    SUNSHINE-OBSERVATION sunshine duration quality code
    The code that denotes a quality status of the reported SUNSHINE-OBSERVATION sunshine duration.
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




    65


---

FLD LEN: 3
    SUNSHINE-OBSERVATION identifier
    The identifier that denotes the availability of percent of possible sunshine information.
    DOM: A specific domain comprised of the ASCII characters
    GK1 An indicator of the occurrence of the following items:
    SUNSHINE-OBSERVATION percent of possible sunshine quantity
    SUNSHINE-OBSERVATION percent of possible sunshine quality code

FLD LEN: 3
    SUNSHINE-OBSERVATION percent of possible sunshine quantity
    The percent of possible sunshine that occurred over the previous 24-hour period.
    MIN: 000       MAX: 100       UNITS: percentage
    DOM: A general domain comprised of the ASCII characters 0-9.
    999 = Missing.

FLD LEN: 1
    SUNSHINE-OBSERVATION percent of possible sunshine quality code
    The code that denotes a quality status of the reported SUNSHINE-OBSERVATION percent of possible sunshine.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    4 = Passed gross limits check, data originate from an NCEI data source
    5 = Passed all quality control checks, data originate from an NCEI data source
    6 = Suspect, data originate from an NCEI data source
    7 = Erroneous, data originate from an NCEI data source
    M = Manual change made to value based on information provided by NWS or FAA
    9 = Passed gross limits check if element is present


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    SUNSHINE-OBSERVATION FOR THE MONTH identifier
    The identifier that denotes the availability of sunshine information.
    DOM: A specific domain comprised of the ASCII characters
    GL1 An indicator of the occurrence of the following items:
    SUNSHINE-OBSERVATION sunshine duration quantity
    SUNSHINE-OBSERVATION sunshine duration quality code

FLD LEN: 5
    SUNSHINE-OBSERVATION FOR THE MONTH sunshine duration quantity
    The quantity of time sunshine occurred over the reporting period.
    MIN: 00000        MAX: 30000       UNITS: minutes
    DOM: A general domain comprised of the ASCII characters 0-9.
    99999 = Missing

FLD LEN: 1
    SUNSHINE-OBSERVATION FOR THE MONTH sunshine duration quality code
    The code that denotes a quality status of the reported SUNSHINE-OBSERVATION sunshine duration.
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
    Solar Irradiance Section identifier
    The identifier that indicates an observation of solar irradiance data integrated over the specified time period.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GM1 An indicator of the following items:
    Solar irradiance data time period
    Global irradiance
    Global irradiance data flag
    Global irradiance quality code
    Direct beam irradiance
    Direct beam irradiance data flag
    Direct beam irradiance quality code


    66


---

    Diffuse irradiance
    Diffuse irradiance data flag
    Diffuse irradiance quality code
    UVB global irradiance
    UVB global irradiance data flag
    UVB global irradiance quality code

FLD LEN: 4
    Time period in minutes, for which the data in this section (GM1) pertains—eg, 0060 = 60 minutes (1 hour).
    MIN: 0001         MAX: 9998        UNITS: Minutes
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 4
    Global irradiance
    Global horizontal irradiance measured using a pyranometer. Unit is watts per square meter
    (W/m2) in whole values. Waveband ranges from 0.4 - 2.3 micrometers.
    MIN: 0000      MAX: 9998        UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 2
    Global irradiance data flag
    The code that provides additional information regarding the global irradiance data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    00 = Untested (raw data)
    01 = Passed one-component test; data fall within max-min limits of Kt, Kn, or Kd
    02 = Passed two-component test; data fall within 0.03 of the Gompertz boundaries
    03 = Passed three-component test; data come within + 0.03 of satisfying Kt = Kn + Kd
    04 = Passed visual inspection: not used by SERI_QC1
    05 = Failed visual inspection: not used by SERI_QC1
    06 = Value estimated; passes all pertinent SERI_QC tests
    07 = Failed one-component test; lower than allowed minimum
    08 = Failed one-component test; higher than allowed maximum
    09 = Passed three-component test but failed two-component test by 0.05
    10-93 = Failed two- or three- component tests in one of four ways.
    94-97 = Data fails into physically impossible region where Kn > Kt by K-space distances of 0.05 to 0.10 (94), 0.10
    to 0.15 (95), 0.15 to 0.20 (96), and > 0.20 (97).
    98 = Not used
    99 = Missing data

FLD LEN: 1
    Global irradiance quality code
    The code that denotes a quality status of the reported global irradiance value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Direct beam irradiance
    Direct beam irradiance measured using a pyrheliometer or other instrument. Unit is watts per square meter (W/m2) in
    whole values. Waveband ranges from 0.4 - 2.3 micrometers.
    MIN: 0000       MAX: 9998     UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.




    67


---

FLD LEN: 2
    Direct beam irradiance data flag
    The code that provides additional information regarding the direct beam irradiance data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    00 = Untested (raw data)
    01 = Passed one-component test; data fall within max-min limits of Kt, Kn, or Kd
    02 = Passed two-component test; data fall within 0.03 of the Gompertz boundaries
    03 = Passed three-component test; data come within + 0.03 of satisfying Kt = Kn + Kd
    04 = Passed visual inspection: not used by SERI_QC1
    05 = Failed visual inspection: not used by SERI_QC1
    06 = Value estimated; passes all pertinent SERI_QC tests
    07 = Failed one-component test; lower than allowed minimum
    08 = Failed one-component test; higher than allowed maximum
    09 = Passed three-component test but failed two-component test by 0.05
    10-93 = Failed two- or three- component tests in one of four ways.
    94-97 = Data fails into physically impossible region where Kn > Kt by K-space distances of 0.05 to 0.10 (94),
    0.10 to 0.15 (95), 0.15 to 0.20 (96), and > 0.20 (97).
    98 = Not used
    99 = Missing data

FLD LEN: 1
    Direct beam irradiance quality code
    The code that denotes a quality status of the reported direct beam irradiance value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Diffuse irradiance
    Diffuse irradiance measured using a pyranometer under a shading device. Unit is watts per square meter (W/m2) in
    whole values. Waveband ranges from 0.4 - 2.3 micrometers. Instrument is mounted under a shadowband.
    MIN: 0000       MAX: 9998      UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 2
    Diffuse irradiance data flag
    The code that provides additional information regarding the diffuse irradiance data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    00 = Untested (raw data)
    01 = Passed one-component test; data fall within max-min limits of Kt, Kn, or Kd
    02 = Passed two-component test; data fall within 0.03 of the Gompertz boundaries
    03 = Passed three-component test; data come within + 0.03 of satisfying Kt = Kn + Kd
    04 = Passed visual inspection: not used by SERI_QC1
    05 = Failed visual inspection: not used by SERI_QC1
    06 = Value estimated; passes all pertinent SERI_QC tests
    07 = Failed one-component test; lower than allowed minimum
    08 = Failed one-component test; higher than allowed maximum
    09 = Passed three-component test but failed two-component test by 0.05
    10-93 = Failed two- or three- component tests in one of four ways.
    94-97 = Data fails into physically impossible region where Kn > Kt by K-space distances of 0.05 to 0.10 (94), 0.10 to
    0.15 (95), 0.15 to 0.20 (96), and > 0.20 (97).
    98 = Not used
    99 = Missing data

FLD LEN: 1
    Diffuse irradiance quality code
    The code that denotes a quality status of the reported diffuse irradiance value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    UVB global irradiance
    Ultra-violet global irradiance measured using a Ultra-violet Biometer (Solar Light). Unit is milli-watts per square


    68


---

    meter (mW/m2) of erythema effective irradiance in whole values. Waveband ranges from 290-320 nanometers.
    MIN: 0000     MAX: 9998      UNITS: milli-watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

   FLD LEN: 1
    UVB global irradiance quality code
    The code that denotes a quality status of the reported UVB global irradiance value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

   FLD LEN: 3
    Solar Radiation Section identifier
    The identifier that indicates an observation of solar radiation data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GN1 An indicator of the following items:
    Solar radiation data time period
    Upwelling global solar radiation
    Upwelling global solar radiation quality code
    Downwelling thermal infrared radiation
    Downwelling thermal infrared radiation quality code
    Upwelling thermal infrared radiation
    Upwelling thermal infrared radiation quality code
    Photosynthetically active radiation
    Photosynthetically active radiation quality code
    Solar zenith angle
    Solar zenith angle quality code

   FLD LEN: 4
    Time period in minutes, for which the data in this section (GN1) pertains—eg, 0060 = 60 minutes (1 hour).
    MIN: 0001         MAX: 9998        UNITS: Minutes
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

   FLD LEN: 4
    Upwelling global solar radiation
    Global radiation measured using an Epply Precision Spectral Pyranometer mounted upside down ten meters above the
    surface on a meteorological tower. Unit is milli-watts per square meter (mW/m2). Waveband ranges from 270 to 3000
    nanometers.
    MIN: 0000       MAX: 9998      UNITS: milli-watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

   FLD LEN: 1
    Upwelling global solar radiation quality code
    The code that denotes a quality status of the reported upwelling global solar radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing




    69


---

    FLD LEN: 4
    Downwelling thermal infrared radiation
    Infrared radiation measured using an Epply Precision Infrared Radiometer mounted upright ten meters above the surface
    on a meteorological tower. Unit is milli-watts per square meter (mW/m2). Waveband ranges from 3000 to 50,000
    nanometers.
    MIN: 0000        MAX: 9998       UNITS: milli-watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

    FLD LEN: 1
    Downwelling thermal infrared radiation quality code
    The code that denotes a quality status of the reported downwelling thermal infrared radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

    FLD LEN: 4
    Upwelling thermal infrared radiation
    Infrared radiation measured using an Epply Precision Infrared Radiometer mounted upside-down ten meters above the
    surface on a meteorological tower. Unit is Watts per meter per meter (mW/m2). Waveband ranges from 3000 to 50,000
    nanometers.
    MIN: 0000        MAX: 9998      UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

    FLD LEN: 1
    Upwelling thermal infrared radiation quality code
    The code that denotes a quality status of the reported upwelling thermal infrared radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

    FLD LEN: 4
    Photosynthetically active radiation
    The PAR sensor measures global solar radiation from 400 to 700 nm in Watts per square meter (mW/m2), which
    approximates the spectral band active in photosynthesis.
    MIN: 0000      MAX: 9998       UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

    FLD LEN: 1
    Photosynthetically active radiation quality code
    The code that denotes a quality status of the reported photosynthetically active radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

    FLD LEN: 3
    Solar zenith angle
    The Solar Zenith Angle is the angle in degrees between the sun and the perpendicular to the earth’s surface. At sunrise it is
    90 degrees, at noon it is a function of latitude, and at sunset it is again 90 degrees. Below the horizon value is 100. Values
    are reported to the nearest tens of degrees (eg, 090).
    MIN: 000       MAX: 998        UNITS: angular degrees
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing.

FLD LEN: 1
    Solar zenith angle quality code
    The code that denotes a quality status of the reported solar zenith angle value.


    70


---

    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing


▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Net Solar Radiation Section identifier
    The identifier that indicates an observation of net solar radiation data.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GO1 An indicator of the following items:
    Net solar radiation data time period
    Net solar radiation
    Net solar radiation quality code
    Net infrared radiation
    Net infrared radiation quality code
    Net radiation
    Net radiation quality code

FLD LEN: 4
    Time period in minutes, for which the data in this section (GO1) pertains—eg, 0060 = 60 minutes (1 hour).
    MIN: 0001         MAX: 9998        UNITS: Minutes
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 4
    Net solar radiation
    The difference between global radiation and upwelling global radiation measured in Watts per square meter (W/m2). If
    negative, left most position contains a "-" sign.
    MIN: -999       MAX: 9998        UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    Net solar radiation quality code
    The code that denotes a quality status of the reported net solar radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Net infrared radiation
    The difference between downwelling infrared and upwelling infrared measured in Watts per square meter (W/m2). If
    negative, left most position contains a "-" sign.
    MIN: -999       MAX: 9998        UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    Net infrared radiation quality code
    The code that denotes a quality status of the reported net infrared radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

FLD LEN: 4
    Net radiation
    The total of Net Solar and Net Infrared radiation measured in Watts per square meter (W/m2).
    MIN: -999      MAX: 9998        UNITS: watts per square meter
    SCALING FACTOR: 1


    71


---

    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 1
    Net radiation quality code
    The code that denotes a quality status of the reported net radiation value.
    DOM: A specific domain comprised of the numeric characters (0-9).
    0 = Passed gross limits check
    1 = Passed all quality control checks
    2 = Suspect
    3 = Erroneous
    9 = Missing

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

FLD LEN: 3
    Modeled Solar Irradiance Section identifier
    The identifier that indicates modeled broadband solar irradiance data integrated over the specified time period.
    DOM: A specific domain comprised of the characters in the ASCII character set.
    GP1 An indicator of the following items:
    Modeled solar irradiance data time period
    Modeled global horizontal
    Modeled global horizontal source flag
    Modeled global horizontal uncertainty
    Modeled direct normal
    Modeled direct normal source flag
    Modeled direct normal uncertainty
    Modeled diffuse horizontal
    Modeled diffuse horizontal source flag
    Modeled diffuse horizontal uncertainty

FLD LEN: 4
    Time period in minutes, for which the data in this section pertains—eg, 0060 = 60 minutes (1 hour).
    MAX: 9998      UNITS: Minutes
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 4
    Modeled global horizontal
    Total amount of direct and diffuse solar radiation (modeled) received on a horizontal surface. Unit is watts per
    square meter (W/m2) in whole values.
    MIN: 0000      MAX: 9998         UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 2
    Modeled global horizontal source flag
    The code that provides source information regarding the global horizontal data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    01 = Value modeled from METSTAT model
    02 = Value time-shifted from SUNY satellite model
    03 = Value time-shifted from SUNY satellite model, adjusted to a minimum low-diffuse envelope
    99 = Missing data

FLD LEN: 3
    Modeled global horizontal uncertainty
    The uncertainty values are based on model type and quality of input data.
    MIN: 000        MAX: 100       UNITS: Percent
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing data

FLD LEN: 4
    Modeled direct normal
    The amount of solar radiation (modeled) on a surface normal to the sun. Unit is watts per square meter (W/m2) in
    whole values.
    MIN: 0000     MAX: 9998         UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.



    72


---

FLD LEN: 2
    Modeled direct normal source flag
    The code that provides source information regarding the direct normal data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    01 = Value modeled from METSTAT model
    02 = Value time-shifted from SUNY satellite model
    03 = Value time-shifted from SUNY satellite model, adjusted to a minimum low-diffuse envelope
    99 = Missing data

FLD LEN: 3
    Modeled direct normal uncertainty
    The uncertainty values are based on model type and quality of input data.
    MIN: 000        MAX: 100       UNITS: Percent
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    999 = Missing data

FLD LEN: 4
    Modeled diffuse horizontal
    The amount of solar radiation (modeled) received from the sky (excluding the solar disk) on a horizontal surface.
    Unit is watts per square meter (W/m2) in whole values. Waveband ranges from 0.4 - 2.3 micrometers.
    MIN: 0000       MAX: 9998       UNITS: watts per square meter
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9).
    9999 = Missing.

FLD LEN: 2
    Modeled diffuse horizontal source flag
    The code that provides source information regarding the diffuse horizontal data.
    DOM: A specific domain comprised of the numeric characters (00-99).
    01 = Value modeled from METSTAT model
    02 = Value time-shifted from SUNY satellite model
    03 = Value time-shifted from SUNY satellite model, adjusted to a minimum low-diffuse envelope
    99 = Missing data

FLD LEN: 3
    Modeled diffuse horizontal uncertainty
    The uncertainty values are based on model type and quality of input data.
    MIN: 000        MAX: 100       UNITS: Percent
    SCALING FACTOR: 1
    DOM: A general domain comprised of the numeric characters (0-9)
    999 = Missing data

▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
