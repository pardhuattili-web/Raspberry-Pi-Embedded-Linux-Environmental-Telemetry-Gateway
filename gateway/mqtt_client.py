import json, logging
logger=logging.getLogger(__name__)
try: import paho.mqtt.client as mqtt
except ImportError: mqtt=None

class MqttPublisher:
    def __init__(self,cfg,device_id):
        self.enabled=bool(cfg.get('enabled',False)); self.client=None; self.device_id=device_id; self.prefix=cfg.get('topic_prefix','environment')
        if not self.enabled: return
        if mqtt is None: raise RuntimeError('paho-mqtt is not installed')
        self.client=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        if cfg.get('username'): self.client.username_pw_set(cfg['username'],cfg.get('password',''))
        self.client.connect_async(cfg.get('host','127.0.0.1'),int(cfg.get('port',1883)),30); self.client.loop_start()
    @property
    def connected(self): return bool(self.client and self.client.is_connected())
    def publish(self, reading):
        if not self.enabled or not self.client: return False
        topic=f'{self.prefix}/{self.device_id}/telemetry'; result=self.client.publish(topic,json.dumps(reading),qos=1,retain=False); return result.rc==0
    def close(self):
        if self.client: self.client.loop_stop(); self.client.disconnect()
