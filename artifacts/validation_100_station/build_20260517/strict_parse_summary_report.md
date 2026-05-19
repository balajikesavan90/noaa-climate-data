# Strict Parse Summary Report

## Token validation rejections
Strict token-level validation detected width/shape mismatches in optional section payloads. These diagnostics did not cause station-level failures or row loss.

- Total token rejections: 2681534
- Affected stations: 70

### By identifier
- MD1: 309043
- MK1: 34
- OD1: 1824771
- OD2: 367710
- OD3: 128752
- SA1: 51224

### By identifier and part
- MD1.part_5: 309043
- MK1.part_2: 16
- MK1.part_5: 18
- OD1.part_3: 912391
- OD1.part_5: 912380
- OD2.part_3: 183855
- OD2.part_5: 183855
- OD3.part_3: 64376
- OD3.part_5: 64376
- SA1.part_1: 51224

### By reason
- token_pattern_mismatch: 34
- token_width_mismatch: 2681500

### Top affected stations
- 06375099999: 692821
- 06633099999: 367220
- 99848399999: 217775
- 99420099999: 202238
- 27277099999: 130794
- 07315099999: 121930
- 42165099999: 113230
- 01441099999: 97706
- 86609099999: 84216
- 41594099999: 65797

### Examples
- station_id=01059099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=13229, token_sample=-021
- station_id=01059099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=3108, token_sample=+005
- station_id=01059099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=5534, token_sample=+002
- station_id=01059099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=12, token_sample=0110
- station_id=01059099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=123969, token_sample=0060
- station_id=01059099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=123980, token_sample=0080
- station_id=01059099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=29, token_sample=0160
- station_id=01059099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=12, token_sample=999
- station_id=01059099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=123969, token_sample=999
- station_id=01066099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=4191, token_sample=+023
