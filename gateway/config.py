import json
from pathlib import Path

DEFAULTS = {"device_id":"env-gw-01","sensor_mode":"simulation","sample_interval_s":10,"database_path":"data/telemetry.db","api_host":"0.0.0.0","api_port":8080,"mqtt":{"enabled":False,"host":"127.0.0.1","port":1883,"username":"","password":"","topic_prefix":"environment"}}

def load_config(path):
    loaded = json.loads(Path(path).read_text(encoding="utf-8"))
    data = DEFAULTS.copy()
    data.update(loaded)
    mqtt = DEFAULTS["mqtt"].copy(); mqtt.update(loaded.get("mqtt", {})); data["mqtt"] = mqtt
    return data
