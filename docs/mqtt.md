# MQTT

## Topics

```text
environment/<device_id>/telemetry
environment/<device_id>/status
environment/<device_id>/alert
```

The reference implementation publishes JSON telemetry on the `telemetry` topic.

Example:

```json
{
  "device_id": "env-gw-01",
  "temperature_c": 27.4,
  "humidity_pct": 61.2,
  "air_quality_index": 43
}
```

## Deployment Guidance

Keep usernames/passwords outside source control. For production-like systems use broker authentication and TLS. MQTT outages should not stop local acquisition or SQLite logging.
