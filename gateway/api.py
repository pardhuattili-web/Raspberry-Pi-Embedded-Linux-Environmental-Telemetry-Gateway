from flask import Flask, jsonify, request

def create_app(database,collector,mqtt):
    app=Flask(__name__)
    @app.get('/health')
    def health(): return jsonify({'status':'ok','sensor_mode':type(collector.sensor).__name__,'mqtt_connected':mqtt.connected,'last_error':collector.last_error})
    @app.get('/api/v1/readings/latest')
    def latest():
        r=database.latest()
        return (jsonify(r),200) if r else (jsonify({'error':'no readings available'}),404)
    @app.get('/api/v1/readings')
    def history():
        try: n=int(request.args.get('limit',100))
        except ValueError: return jsonify({'error':'limit must be an integer'}),400
        return jsonify(database.history(n))
    @app.get('/api/v1/status')
    def status(): return jsonify({'device_id':collector.device_id,'sensor':type(collector.sensor).__name__,'mqtt_connected':mqtt.connected,'last_reading':database.latest(),'collector_error':collector.last_error})
    return app
