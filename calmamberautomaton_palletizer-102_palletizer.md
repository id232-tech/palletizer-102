# Model calmamberautomaton:palletizer-102:palletizer

Packs boxes from the pick-station onto the pallet in a configurable pattern.

## Configuration

The following attribute template can be used to configure this model:

```json
{
  "columns": <int>,
  "rows": <int>,
  "layers": <int>,
  "box_height_mm": <float>
}
```

### Attributes

The following attributes are available for this model:

| Name | Type | Inclusion | Description |
|------|------|-----------|-------------|
| `columns` | int | Required | Boxes across the pallet |
| `rows` | int | Required | Boxes deep |
| `layers` | int | Required | Stacked layers |
| `box_height_mm` | float | Required | Box height, above zero |

### Example Configuration

```json
{
  "columns": 2,
  "rows": 2,
  "layers": 2,
  "box_height_mm": 100
}
```

## DoCommand

This model is driven through `DoCommand`. Every command names its verb with the `command` key.

| Verb | Does | Answers |
|------|------|---------|
| `status` | Reports the resources it resolved | `{"resources": {...}, "boxes_packed": <int>}` |
| `clear` | Empties the pallet, the scene, and the record | `{"cleared": true}` |
| `pick` | Picks the next box off the pick-station | `{"picked": true}` |
| `place` | Places the held box in the next slot | `{"slot": <int>}` |
| `pack` | Packs the whole pattern, from empty | `{"placed": <int>}` |

An unrecognized verb answers `{"error": "unknown command: <verb>"}`.

### Example DoCommand

```json
{
  "command": "pack"
}
```
