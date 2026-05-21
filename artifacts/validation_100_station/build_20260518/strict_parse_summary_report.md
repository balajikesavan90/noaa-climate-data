# Strict Parse Summary Report

## Token validation rejections
Strict token-level validation detected width/shape mismatches in optional section payloads. These diagnostics did not cause station-level failures or row loss.

- Total token rejections: 4438272
- Affected stations: 71

### By identifier
- CH1: 1595282
- CI1: 133306
- MD1: 191141
- MK1: 24
- OD1: 1972573
- OD2: 440989
- OD3: 102956
- SA1: 2001

### By identifier and part
- CH1.part_2: 1595282
- CI1.part_1: 133306
- MD1.part_5: 191141
- MK1.part_2: 11
- MK1.part_5: 13
- OD1.part_3: 986418
- OD1.part_5: 986155
- OD2.part_3: 220617
- OD2.part_5: 220372
- OD3.part_3: 51478
- OD3.part_5: 51478
- SA1.part_1: 2001

### By reason
- token_pattern_mismatch: 24
- token_width_mismatch: 4438248

### Top affected stations
- 99999923906: 1728588
- 06240099999: 661119
- 06635099999: 280664
- 99418099999: 228709
- 08301099999: 145485
- 02831099999: 142562
- 02209099999: 127471
- 86995099999: 123566
- 56964099999: 113283
- 03214099999: 90289

### Examples
- station_id=01182099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=581, token_sample=+014
- station_id=01182099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=392, token_sample=+055
- station_id=01182099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=402, token_sample=+040
- station_id=02209099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=17746, token_sample=+999
- station_id=02209099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=17973, token_sample=+999
- station_id=02209099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=18116, token_sample=+999
- station_id=02255099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=2417, token_sample=+001
- station_id=02831099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=68589, token_sample=9999
- station_id=02831099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=69594, token_sample=9999
- station_id=02831099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=68589, token_sample=999
