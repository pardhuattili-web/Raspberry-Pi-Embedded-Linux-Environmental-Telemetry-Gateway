from dataclasses import asdict, dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class Reading:
    timestamp: str
    temperature_c: float
    humidity_pct: float
    air_quality_index: int
    source: str
    device_id: str

    @staticmethod
    def now(device_id: str, temperature_c: float, humidity_pct: float, air_quality_index: int, source: str):
        return Reading(datetime.now(timezone.utc).isoformat(), float(temperature_c), float(humidity_pct), int(air_quality_index), source, device_id)

    def to_dict(self):
        return asdict(self)
