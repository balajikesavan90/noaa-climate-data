# Strict Parse Summary Report

## Token validation rejections
Strict token-level validation detected width/shape mismatches in optional section payloads. These diagnostics did not cause station-level failures or row loss.

- Total token rejections: 4573326
- Affected stations: 73

### By identifier
- CH1: 1650428
- CI1: 137531
- MD1: 225438
- MK1: 37
- OD1: 2185728
- OD2: 157470
- OD3: 34
- SA1: 216660

### By identifier and part
- CH1.part_2: 1650428
- CI1.part_1: 137531
- MD1.part_5: 225438
- MK1.part_2: 23
- MK1.part_5: 14
- OD1.part_3: 1092886
- OD1.part_5: 1092842
- OD2.part_3: 78735
- OD2.part_5: 78735
- OD3.part_3: 17
- OD3.part_5: 17
- SA1.part_1: 216660

### By reason
- token_pattern_mismatch: 37
- token_width_mismatch: 4573289

### Top affected stations
- 99999904141: 1787959
- 06787099999: 352736
- 99737199999: 287737
- 06638099999: 265992
- 91925099999: 216450
- 02081099999: 173456
- 02795099999: 143400
- 86984099999: 130306
- 02773099999: 126808
- 02790099999: 107512

### Examples
- station_id=02081099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=39246, token_sample=0050
- station_id=02081099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=39247, token_sample=0070
- station_id=02081099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=39246, token_sample=999
- station_id=02773099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=41372, token_sample=9999
- station_id=02773099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=41374, token_sample=9999
- station_id=02773099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=41372, token_sample=999
- station_id=02790099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=97282, token_sample=9999
- station_id=02790099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=97690, token_sample=9999
- station_id=02790099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=97282, token_sample=999
- station_id=02795099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=0, token_sample=+022
