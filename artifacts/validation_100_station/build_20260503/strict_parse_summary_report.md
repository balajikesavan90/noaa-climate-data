# Strict Parse Summary Report

## Token validation rejections
Strict token-level validation detected width/shape mismatches in optional section payloads. These diagnostics did not cause station-level failures or row loss.

- Total token rejections: 2352988
- Affected stations: 70

### By identifier
- GO1: 172493
- MD1: 519678
- MK1: 12
- OD1: 1374882
- OD2: 91158
- SA1: 194765

### By identifier and part
- GO1.part_4: 110561
- GO1.part_6: 61932
- MD1.part_5: 519678
- MK1.part_2: 7
- MK1.part_5: 5
- OD1.part_3: 687468
- OD1.part_5: 687414
- OD2.part_3: 45587
- OD2.part_5: 45571
- SA1.part_1: 194765

### By reason
- token_pattern_mismatch: 12
- token_width_mismatch: 2352976

### Top affected stations
- 99731599999: 289662
- 99847599999: 283876
- 06618099999: 243874
- 99730899999: 189365
- 99999994045: 172493
- 86720099999: 145222
- 26134099999: 124379
- 43150099999: 100862
- 03544099999: 83672
- 48900099999: 81377

### Examples
- station_id=03541399999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=18706, token_sample=+000
- station_id=03541399999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=74558, token_sample=+999
- station_id=03541399999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=75364, token_sample=+999
- station_id=03544099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=154109, token_sample=+999
- station_id=03544099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=154110, token_sample=+999
- station_id=03544099999, identifier=SA1, part_index=1, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=154778, token_sample=+999
- station_id=06618099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=545, token_sample=0026
- station_id=06618099999, identifier=OD1, part_index=3, reason=token_width_mismatch, actual_width=4, expected_width=3, row_index=650, token_sample=0041
- station_id=06618099999, identifier=OD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=1, row_index=545, token_sample=999
- station_id=10253099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=104539, token_sample=+127
