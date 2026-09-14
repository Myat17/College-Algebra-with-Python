# import meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, stations, daily

# Set time period
start = datetime(2026, 8, 1)
end = datetime(2026, 8, 31)

location = Point(13.7563, 100.5018, 25)

# Find the nearest real weather station to this location
nearby = stations.nearby(location, radius=50000, limit=1)
station_id = nearby.index[0]

ts = daily(station_id, start, end)
data = ts.fetch()

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
data.plot(y='temp', ax=ax1, color='green')
data.plot(y='wspd', ax=ax2, color='red')
plt.show()