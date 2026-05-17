# Strict Parse Summary Report

## Token validation rejections
Strict token-level validation detected width/shape mismatches in optional section payloads. These diagnostics did not cause station-level failures or row loss.

- Total token rejections: 7347677
- Affected stations: 70

### By identifier
- CH1: 4871002
- CI1: 402647
- MD1: 156447
- MK1: 46
- OD1: 1704737
- OD2: 129958
- SA1: 82840

### By identifier and part
- CH1.part_2: 4871002
- CI1.part_1: 402647
- MD1.part_5: 156447
- MK1.part_2: 19
- MK1.part_5: 27
- OD1.part_3: 852369
- OD1.part_5: 852368
- OD2.part_3: 64979
- OD2.part_5: 64979
- SA1.part_1: 82840

### By reason
- token_pattern_mismatch: 46
- token_width_mismatch: 7347631

### Top affected stations
- 99999903048: 1768193
- 99999923907: 1763346
- 99999903733: 1635339
- 07481099999: 332561
- 02836099999: 162889
- 15460099999: 150844
- 86891099999: 146044
- 02992099999: 141480
- 86796099999: 134532
- 86798099999: 122016

### Examples
- station_id=01121099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=31919, token_sample=-073
- station_id=01121099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=31922, token_sample=-006
- station_id=01121099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=6720, token_sample=+008
- station_id=02471099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=2464, token_sample=-024
- station_id=02471099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=3129, token_sample=+024
- station_id=02471099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=55, token_sample=+000
- station_id=02836099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=3307, token_sample=+045
- station_id=02836099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=3333, token_sample=+008
- station_id=02836099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=3588, token_sample=-013
- station_id=02982099999, identifier=MD1, part_index=5, reason=token_width_mismatch, actual_width=3, expected_width=4, row_index=5558, token_sample=+012
