import argparse, logging, signal
from .api import create_app
from .collector import Collector
from .config import load_config
from .database import TelemetryDatabase
from .mqtt_client import MqttPublisher
from .sensors import build_sensor

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config',required=True); args=p.parse_args(); cfg=load_config(args.config)
    logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s: %(message)s')
    db=TelemetryDatabase(cfg['database_path']); sensor=build_sensor(cfg['sensor_mode']); mqtt=MqttPublisher(cfg['mqtt'],cfg['device_id']); collector=Collector(cfg['device_id'],cfg['sample_interval_s'],sensor,db,mqtt); collector.start(); app=create_app(db,collector,mqtt)
    def shutdown(*_): collector.stop(); mqtt.close()
    signal.signal(signal.SIGTERM,shutdown); signal.signal(signal.SIGINT,shutdown)
    app.run(host=cfg['api_host'],port=int(cfg['api_port']),threaded=True)
if __name__=='__main__': main()
