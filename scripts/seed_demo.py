import argparse, random
from datetime import datetime,timedelta,timezone
from gateway.database import TelemetryDatabase
from gateway.models import Reading
p=argparse.ArgumentParser(); p.add_argument('--database',default='data/telemetry.db'); p.add_argument('--count',type=int,default=20); a=p.parse_args(); db=TelemetryDatabase(a.database); now=datetime.now(timezone.utc)
for i in range(max(1,a.count)):
    db.insert(Reading((now-timedelta(minutes=i)).isoformat(),26+random.random()*3,55+random.random()*10,random.randint(20,70),'seed_demo','env-gw-01'))
