# Raspberry Pi Embedded Linux Environmental Telemetry Gateway

> **Embedded Linux / IoT project | Raspberry Pi + I2C + SQLite + REST + MQTT**

A Raspberry Pi based Embedded Linux gateway that collects environmental measurements, stores timestamped telemetry locally, exposes the latest data through a REST API, and publishes updates through MQTT.

The design follows a small production-style edge architecture: sensor collection, local persistence, HTTP access, MQTT forwarding, structured logging, and systemd deployment.

## Architecture

```text
Sensors / Simulator
       |
       v
  Collector Service
       |
       +-------> SQLite
       |
       +-------> MQTT Publisher
       |
       v
    REST API
       |
       v
   Local / Remote Clients
```

## Target Platform

| Component | Choice |
|---|---|
| Hardware | Raspberry Pi Zero 2 W / Raspberry Pi 4 |
| OS | Raspberry Pi OS / Embedded Linux |
| Language | Python |
| Sensor bus | I2C |
| Storage | SQLite |
| API | HTTP/REST |
| Telemetry | MQTT |
| Service manager | systemd |

## Features

- I2C sensor abstraction
- Simulation mode for development without hardware
- Timestamped SQLite telemetry
- REST API for live and historical readings
- MQTT telemetry publishing
- Network/sensor recovery handling
- systemd deployment
- Structured logs
- Hardware-independent application logic

## Repository Structure

```text
Raspberry-Pi-Embedded-Linux-Environmental-Telemetry-Gateway/
├── README.md
├── requirements.txt
├── config/
│   └── gateway.example.json
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── mqtt.md
│   └── test_plan.md
├── gateway/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── database.py
│   ├── sensors.py
│   ├── collector.py
│   ├── mqtt_client.py
│   └── api.py
├── scripts/
│   └── seed_demo.py
└── deploy/
    └── environmental-gateway.service
```

## Data Model

```json
{
  "timestamp": "2026-09-28T03:00:00Z",
  "temperature_c": 27.4,
  "humidity_pct": 61.2,
  "air_quality_index": 43
}
```

## REST API

- `GET /health`
- `GET /api/v1/readings/latest`
- `GET /api/v1/readings?limit=100`
- `GET /api/v1/status`

See `docs/api.md` for response formats.

## MQTT

```text
environment/<device_id>/telemetry
environment/<device_id>/status
environment/<device_id>/alert
```

Credentials are kept in local configuration/environment variables and are not committed.

## Sensor Modes

**Simulation:** generates deterministic environmental data for development and testing.

**Hardware:** accesses a selected sensor through Linux I2C. The sensor adapter is intentionally isolated so the gateway can support different devices.

## Installation

```bash
git clone https://github.com/pardhuattili-web/Raspberry-Pi-Embedded-Linux-Environmental-Telemetry-Gateway.git
cd Raspberry-Pi-Embedded-Linux-Environmental-Telemetry-Gateway
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config/gateway.example.json config/gateway.json
python -m gateway.main --config config/gateway.json
```

Check the service locally:

```bash
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/api/v1/readings/latest
```

## systemd

```bash
sudo cp deploy/environmental-gateway.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now environmental-gateway
journalctl -u environmental-gateway -f
```

## Validation

Start with simulation mode, verify SQLite persistence and API responses, test MQTT reconnect behavior, exercise sensor failures, and then switch to physical I2C hardware.

Physical sensor accuracy should only be claimed after the chosen sensor/front-end has been calibrated and tested.

## Portfolio Skills

- Embedded Linux
- I2C device access
- SQLite
- REST APIs
- MQTT
- systemd
- Edge telemetry
- Fault recovery
- Structured logging

## Status

**Architecture + reference implementation scaffold**

## Author

**Pardhu Attili**