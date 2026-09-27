# REST API

## `GET /health`

Returns gateway liveness and component status.

```json
{
  "status": "ok",
  "sensor_mode": "SimulationSensor",
  "mqtt_connected": false,
  "last_error": null
}
```

## `GET /api/v1/readings/latest`

Returns the latest persisted reading, or HTTP 404 when no data exists.

## `GET /api/v1/readings?limit=100`

Returns the newest readings. The server clamps the requested limit to 1–1000.

## `GET /api/v1/status`

Returns device identity, sensor implementation, MQTT state, latest reading, and collector error state.
