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

fig, (ax1, ax2) = plt.subplots(2, figsize=(8,4) )
ax1.set_title(ds1 + ' - ' + ds2)
ax1.plot(x, y, '*')
ax1.text(x[0], 0.04, 'matplotlib')
ax1.grid()

ax2.plot(x, y, '*')
ax2.text(x[0], 0.04, 'datetick')
datetick('x', axes=ax2)
ax2.grid()

plt.show()
