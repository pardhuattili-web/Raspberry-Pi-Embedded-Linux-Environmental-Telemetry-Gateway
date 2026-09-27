# Test Plan

| ID | Test | Expected result |
|---|---|---|
| T01 | Start simulation mode | Collector starts and records data |
| T02 | `GET /health` | HTTP 200 with component state |
| T03 | Latest endpoint | Newest SQLite row returned |
| T04 | History limit | Returned rows stay within requested bound |
| T05 | Seed demo data | SQLite contains timestamped records |
| T06 | MQTT disabled | Collection continues normally |
| T07 | Invalid sensor mode | Clean startup error |
| T08 | Sensor exception | Error logged; process remains alive |
| T09 | SIGTERM | Collector exits cleanly |
| T10 | systemd restart | Process is restarted after failure |

## Hardware Integration

After simulation validation, enable Raspberry Pi I2C, select a concrete temperature/humidity/air-quality device, implement its adapter, and verify readings against the sensor's documented calibration procedure.

## Validation Status

Software behavior can be exercised in simulation. Physical I2C timing, sensor accuracy, and long-duration deployment remain hardware-validation tasks.
