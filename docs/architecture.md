# Architecture

```text
+----------------------+
| Sensor / Simulator   |
+----------+-----------+
           |
           v
+----------------------+
| Collector Thread     |
| acquire + validate   |
+----------+-----------+
           |
      +----+-----+
      |          |
      v          v
   SQLite      MQTT
      |
      v
+----------------------+
| Flask REST API       |
+----------------------+
```

## Responsibilities

- `sensors.py` hides hardware-specific acquisition behind `SensorProvider`.
- `collector.py` is responsible for periodic sampling and persistence.
- `database.py` is the local historical store.
- `mqtt_client.py` forwards telemetry without blocking the collector design.
- `api.py` exposes current/history/status data.
- `systemd` supervises the long-running process.

## Failure Strategy

Sensor exceptions are logged and do not terminate the collector thread.

MQTT is optional; local persistence continues when the broker is unavailable.

The API exposes `last_error` so operators can see the most recent acquisition failure.
