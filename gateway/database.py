import sqlite3
from pathlib import Path

class TelemetryDatabase:
    def __init__(self, path):
        p=Path(path); p.parent.mkdir(parents=True, exist_ok=True); self.path=str(p); self._init_schema()
    def _connect(self):
        c=sqlite3.connect(self.path); c.row_factory=sqlite3.Row; return c
    def _init_schema(self):
        with self._connect() as c:
            c.execute('CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL, temperature_c REAL NOT NULL, humidity_pct REAL NOT NULL, air_quality_index INTEGER NOT NULL, source TEXT NOT NULL, device_id TEXT NOT NULL)')
    def insert(self, reading):
        with self._connect() as c:
            c.execute('INSERT INTO readings (timestamp,temperature_c,humidity_pct,air_quality_index,source,device_id) VALUES (?,?,?,?,?,?)',(reading.timestamp,reading.temperature_c,reading.humidity_pct,reading.air_quality_index,reading.source,reading.device_id))
    def latest(self):
        with self._connect() as c:
            row=c.execute('SELECT * FROM readings ORDER BY id DESC LIMIT 1').fetchone()
        return dict(row) if row else None
    def history(self, limit=100):
        n=max(1,min(int(limit),1000))
        with self._connect() as c: rows=c.execute('SELECT * FROM readings ORDER BY id DESC LIMIT ?',(n,)).fetchall()
        return [dict(r) for r in rows]
