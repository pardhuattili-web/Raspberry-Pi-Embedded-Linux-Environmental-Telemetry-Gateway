import logging, threading
from .models import Reading
logger=logging.getLogger(__name__)
class Collector:
    def __init__(self,device_id,interval_s,sensor,database,mqtt_publisher):
        self.device_id=device_id; self.interval_s=max(0.5,float(interval_s)); self.sensor=sensor; self.database=database; self.mqtt=mqtt_publisher; self.stop_event=threading.Event(); self.thread=None; self.last_error=None
    def start(self): self.thread=threading.Thread(target=self._run,name='collector',daemon=True); self.thread.start()
    def stop(self):
        self.stop_event.set()
        if self.thread: self.thread.join(timeout=self.interval_s+1)
    def _run(self):
        while not self.stop_event.is_set():
            try:
                t,h,a=self.sensor.read(); reading=Reading.now(self.device_id,t,h,a,type(self.sensor).__name__); self.database.insert(reading); self.mqtt.publish(reading.to_dict()); self.last_error=None
                logger.info('reading temperature=%.2fC humidity=%.2f%% aqi=%d',t,h,a)
            except Exception as exc:
                self.last_error=str(exc); logger.exception('collector iteration failed')
            self.stop_event.wait(self.interval_s)
