import datetime as dt
import matplotlib.pyplot as plt
from datetick import datetick
dt1 = dt.datetime(2011, 1, 2)
dt2 = dt1 + dt.timedelta(days=1, hours=1, minutes=1)
x = [dt1, dt2]
y = [0.0,1.0]

method = 4
if method == 1:
  plt.plot(x, y)
  datetick()
if method == 2:
  plt.plot(x, y)
  datetick('x')
if method == 3:
  plt.plot(x, y)
  datetick('x', axes=plt.gca())
if method == 4:
  fig, axes = plt.subplots(2, figsize=(8,6))
  axes[0].plot(x, y)
  axes[1].plot(x, y)
  datetick('x', axes=axes[0])
  datetick('x', axes=axes[1])

plt.show()
