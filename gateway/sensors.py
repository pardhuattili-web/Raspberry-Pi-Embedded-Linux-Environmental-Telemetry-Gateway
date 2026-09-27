import math, random, time
from abc import ABC, abstractmethod

class SensorProvider(ABC):
    @abstractmethod
    def read(self): raise NotImplementedError

class SimulationSensor(SensorProvider):
    def __init__(self): self._start=time.monotonic()
    def read(self):
        t=time.monotonic()-self._start
        return (27.0+2.0*math.sin(t/60.0)+random.uniform(-0.2,0.2), 60.0+5.0*math.sin(t/90.0)+random.uniform(-0.5,0.5), int(max(0,min(500,45+10*math.sin(t/45.0)+random.uniform(-2,2)))))

class I2CSensor(SensorProvider):
    def read(self): raise RuntimeError('I2CSensor is a hardware integration point; select a real sensor model and implement its adapter.')

def build_sensor(mode):
    if mode.lower()=='simulation': return SimulationSensor()
    if mode.lower()=='i2c': return I2CSensor()
    raise ValueError(f'Unsupported sensor mode: {mode}')
