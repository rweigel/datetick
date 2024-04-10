import dateutil.parser
import matplotlib.pyplot as plt
import numpy as np

from datetick import datetick

ds1 = '2000-01-01T00:00:00Z'
ds2 = '2017-01-04T00:00:00Z'

# Plots two points separated by varying time ranges.
# For testing date/time tick labeling code datetick.py.
dt1 = dateutil.parser.parse(ds1)
dt2 = dateutil.parser.parse(ds2)
x = np.array([dt1,dt2], dtype=object)
y = [0.0,0.0]
plt.figure(figsize=(8,2))
plt.plot(x, y, '*')
plt.title(ds1 + ' - ' + ds2)
datetick('x')
plt.grid()
plt.show()