# datetick

Sensible date/time tick labels for [Matplotlib](https://matplotlib.org/)

# Motivation

`Matplotlib`'s default date/time tick labels are often poor, and adjusting them requires using [locators and formatters](https://matplotlib.org/stable/api/ticker_api.html) on an ad-hoc basis. A method or package for handling arbitrary time ranges does not exist.

In addition, the interfaces for locators and formatters complex and non-intuitive and require study and experimentation (e.g., [[1]](https://github.com/matplotlib/matplotlib/issues/28158), [[2]](https://github.com/matplotlib/matplotlib/issues/15813]), [[3]](https://github.com/matplotlib/matplotlib/issues/9978), [[4]](https://github.com/matplotlib/matplotlib/issues/9978). Tilting labels is an [often-suggested solution](https://github.com/matplotlib/matplotlib/issues/9978), but this should not be needed.

`datetick()` contains logic for locators and formatters that apply to plots with arbitrary time ranges. One only needs to add the command `datetick()` after the usual `plt.plot(...)` command to have sensible and useable time tick labels. The primary configuration is a set of [rules](datetick/rules.json) that account for the time range and an adjustable minimum gap between tick labels.

To prevent overlap and enforce a minimum gap, the font size is automatically reduced to a chosen minimum value. Then the number of ticks are reduced based on rules in [rules.json](datetick/rules.json).

# Usage

```python
import datetime as dt
import matplotlib.pyplot as plt
from datetick import datetick

dt1 = dt.datetime(2011, 1, 2)
dt2 = dt1 + dt.timedelta(days=1, hours=1, minutes=1)

plt.plot([dt1, dt2], [0.0,1.0])
datetick()
plt.show()
# or
# datetick('x') (use 'y' if y variable is datetime-like)
# or
# datetick('x', axes=plt.gca())
# or
# fig, axes = plt.subplots(2)
# plt.plot([dt1, dt2], [0.0, 1.0])
# datetick('x', axes=axes[0])
```

# Comparison to default `Matplotlib`


<code>Python-3.13/Matplotlib-3.10.9</code>


## <code>axis=x</code>

![test/visual_test/latest/20010101000000-20010102230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010102230000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-6.5in_v2.svg)

![test/visual_test/latest/20010101000000-20010102230000-6.5in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-6.5in_v3.svg)

![test/visual_test/latest/20010101000000-20010102230000-6.5in_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-6.5in_v4.svg)

![test/visual_test/latest/20001231170000-20010102190000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-6.5in.svg)

![test/visual_test/latest/20001231170000-20010102190000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-6.5in_v2.svg)

![test/visual_test/latest/20001231170000-20010102190000-6.5in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-6.5in_v3.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.1-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.1-6.5in.svg)

![test/visual_test/latest/20010101000000.91-20010101000001.01-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.91-20010101000001.01-6.5in.svg)

![test/visual_test/latest/20010101000059.91-20010101000100.01-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.91-20010101000100.01-6.5in.svg)

![test/visual_test/latest/20010101005959.91-20010101010000.01-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.91-20010101010000.01-6.5in.svg)

![test/visual_test/latest/20010101235959.91-20010102000000.01-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.91-20010102000000.01-6.5in.svg)

![test/visual_test/latest/20010131235959.91-20010201000000.01-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.91-20010201000000.01-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.15-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.15-6.5in.svg)

![test/visual_test/latest/20010101000000.865-20010101000001.015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.865-20010101000001.015-6.5in.svg)

![test/visual_test/latest/20010101000059.865-20010101000100.015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.865-20010101000100.015-6.5in.svg)

![test/visual_test/latest/20010101005959.865-20010101010000.015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.865-20010101010000.015-6.5in.svg)

![test/visual_test/latest/20010101235959.865-20010102000000.015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.865-20010102000000.015-6.5in.svg)

![test/visual_test/latest/20010131235959.865-20010201000000.015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.865-20010201000000.015-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.2-6.5in.svg)

![test/visual_test/latest/20010101000000.82-20010101000001.02-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.82-20010101000001.02-6.5in.svg)

![test/visual_test/latest/20010101000059.82-20010101000100.02-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.82-20010101000100.02-6.5in.svg)

![test/visual_test/latest/20010101005959.82-20010101010000.02-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.82-20010101010000.02-6.5in.svg)

![test/visual_test/latest/20010101235959.82-20010102000000.02-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.82-20010102000000.02-6.5in.svg)

![test/visual_test/latest/20010131235959.82-20010201000000.02-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.82-20010201000000.02-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.25-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.25-6.5in.svg)

![test/visual_test/latest/20010101000000.775-20010101000001.025-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.775-20010101000001.025-6.5in.svg)

![test/visual_test/latest/20010101000059.775-20010101000100.025-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.775-20010101000100.025-6.5in.svg)

![test/visual_test/latest/20010101005959.775-20010101010000.025-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.775-20010101010000.025-6.5in.svg)

![test/visual_test/latest/20010101235959.775-20010102000000.025-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.775-20010102000000.025-6.5in.svg)

![test/visual_test/latest/20010131235959.775-20010201000000.025-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.775-20010201000000.025-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.3-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.3-6.5in.svg)

![test/visual_test/latest/20010101000000.73-20010101000001.03-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.73-20010101000001.03-6.5in.svg)

![test/visual_test/latest/20010101000059.73-20010101000100.03-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.73-20010101000100.03-6.5in.svg)

![test/visual_test/latest/20010101005959.73-20010101010000.03-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.73-20010101010000.03-6.5in.svg)

![test/visual_test/latest/20010101235959.73-20010102000000.03-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.73-20010102000000.03-6.5in.svg)

![test/visual_test/latest/20010131235959.73-20010201000000.03-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.73-20010201000000.03-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.35-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.35-6.5in.svg)

![test/visual_test/latest/20010101000000.685-20010101000001.035-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.685-20010101000001.035-6.5in.svg)

![test/visual_test/latest/20010101000059.685-20010101000100.035-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.685-20010101000100.035-6.5in.svg)

![test/visual_test/latest/20010101005959.685-20010101010000.035-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.685-20010101010000.035-6.5in.svg)

![test/visual_test/latest/20010101235959.685-20010102000000.035-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.685-20010102000000.035-6.5in.svg)

![test/visual_test/latest/20010131235959.685-20010201000000.035-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.685-20010201000000.035-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.4-6.5in.svg)

![test/visual_test/latest/20010101000000.64-20010101000001.04-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.64-20010101000001.04-6.5in.svg)

![test/visual_test/latest/20010101000059.64-20010101000100.04-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.64-20010101000100.04-6.5in.svg)

![test/visual_test/latest/20010101005959.64-20010101010000.04-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.64-20010101010000.04-6.5in.svg)

![test/visual_test/latest/20010101235959.64-20010102000000.04-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.64-20010102000000.04-6.5in.svg)

![test/visual_test/latest/20010131235959.64-20010201000000.04-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.64-20010201000000.04-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.45-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.45-6.5in.svg)

![test/visual_test/latest/20010101000000.595-20010101000001.045-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.595-20010101000001.045-6.5in.svg)

![test/visual_test/latest/20010101000059.595-20010101000100.045-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.595-20010101000100.045-6.5in.svg)

![test/visual_test/latest/20010101005959.595-20010101010000.045-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.595-20010101010000.045-6.5in.svg)

![test/visual_test/latest/20010101235959.595-20010102000000.045-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.595-20010102000000.045-6.5in.svg)

![test/visual_test/latest/20010131235959.595-20010201000000.045-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.595-20010201000000.045-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.5-6.5in.svg)

![test/visual_test/latest/20010101000000.55-20010101000001.05-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.55-20010101000001.05-6.5in.svg)

![test/visual_test/latest/20010101000059.55-20010101000100.05-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.55-20010101000100.05-6.5in.svg)

![test/visual_test/latest/20010101005959.55-20010101010000.05-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.55-20010101010000.05-6.5in.svg)

![test/visual_test/latest/20010101235959.55-20010102000000.05-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.55-20010102000000.05-6.5in.svg)

![test/visual_test/latest/20010131235959.55-20010201000000.05-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.55-20010201000000.05-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.6-6.5in.svg)

![test/visual_test/latest/20010101000000.46-20010101000001.06-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.46-20010101000001.06-6.5in.svg)

![test/visual_test/latest/20010101000059.46-20010101000100.06-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.46-20010101000100.06-6.5in.svg)

![test/visual_test/latest/20010101005959.46-20010101010000.06-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.46-20010101010000.06-6.5in.svg)

![test/visual_test/latest/20010101235959.46-20010102000000.06-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.46-20010102000000.06-6.5in.svg)

![test/visual_test/latest/20010131235959.46-20010201000000.06-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.46-20010201000000.06-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.7-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.7-6.5in.svg)

![test/visual_test/latest/20010101000000.37-20010101000001.07-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.37-20010101000001.07-6.5in.svg)

![test/visual_test/latest/20010101000059.37-20010101000100.07-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.37-20010101000100.07-6.5in.svg)

![test/visual_test/latest/20010101005959.37-20010101010000.07-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.37-20010101010000.07-6.5in.svg)

![test/visual_test/latest/20010101235959.37-20010102000000.07-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.37-20010102000000.07-6.5in.svg)

![test/visual_test/latest/20010131235959.37-20010201000000.07-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.37-20010201000000.07-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.8-6.5in.svg)

![test/visual_test/latest/20010101000000.28-20010101000001.08-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.28-20010101000001.08-6.5in.svg)

![test/visual_test/latest/20010101000059.28-20010101000100.08-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.28-20010101000100.08-6.5in.svg)

![test/visual_test/latest/20010101005959.28-20010101010000.08-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.28-20010101010000.08-6.5in.svg)

![test/visual_test/latest/20010101235959.28-20010102000000.08-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.28-20010102000000.08-6.5in.svg)

![test/visual_test/latest/20010131235959.28-20010201000000.08-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.28-20010201000000.08-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.9-6.5in.svg)

![test/visual_test/latest/20010101000000.19-20010101000001.09-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.19-20010101000001.09-6.5in.svg)

![test/visual_test/latest/20010101000059.19-20010101000100.09-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.19-20010101000100.09-6.5in.svg)

![test/visual_test/latest/20010101005959.19-20010101010000.09-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.19-20010101010000.09-6.5in.svg)

![test/visual_test/latest/20010101235959.19-20010102000000.09-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.19-20010102000000.09-6.5in.svg)

![test/visual_test/latest/20010131235959.19-20010201000000.09-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.19-20010201000000.09-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000001.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.0-6.5in.svg)

![test/visual_test/latest/20010101000059.1-20010101000100.1-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.1-20010101000100.1-6.5in.svg)

![test/visual_test/latest/20010101005959.1-20010101010000.1-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.1-20010101010000.1-6.5in.svg)

![test/visual_test/latest/20010101235959.1-20010102000000.1-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.1-20010102000000.1-6.5in.svg)

![test/visual_test/latest/20010131235959.1-20010201000000.1-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.1-20010201000000.1-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000001.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.5-6.5in.svg)

![test/visual_test/latest/20010101000058.65-20010101000100.15-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.65-20010101000100.15-6.5in.svg)

![test/visual_test/latest/20010101005958.65-20010101010000.15-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.65-20010101010000.15-6.5in.svg)

![test/visual_test/latest/20010101235958.65-20010102000000.15-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.65-20010102000000.15-6.5in.svg)

![test/visual_test/latest/20010131235958.65-20010201000000.15-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.65-20010201000000.15-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000002.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.0-6.5in.svg)

![test/visual_test/latest/20010101000058.2-20010101000100.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.2-20010101000100.2-6.5in.svg)

![test/visual_test/latest/20010101005958.2-20010101010000.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.2-20010101010000.2-6.5in.svg)

![test/visual_test/latest/20010101235958.2-20010102000000.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.2-20010102000000.2-6.5in.svg)

![test/visual_test/latest/20010131235958.2-20010201000000.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.2-20010201000000.2-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000002.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.5-6.5in.svg)

![test/visual_test/latest/20010101000057.75-20010101000100.25-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.75-20010101000100.25-6.5in.svg)

![test/visual_test/latest/20010101005957.75-20010101010000.25-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.75-20010101010000.25-6.5in.svg)

![test/visual_test/latest/20010101235957.75-20010102000000.25-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.75-20010102000000.25-6.5in.svg)

![test/visual_test/latest/20010131235957.75-20010201000000.25-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.75-20010201000000.25-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000003.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000003.0-6.5in.svg)

![test/visual_test/latest/20010101000057.3-20010101000100.3-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.3-20010101000100.3-6.5in.svg)

![test/visual_test/latest/20010101005957.3-20010101010000.3-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.3-20010101010000.3-6.5in.svg)

![test/visual_test/latest/20010101235957.3-20010102000000.3-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.3-20010102000000.3-6.5in.svg)

![test/visual_test/latest/20010131235957.3-20010201000000.3-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.3-20010201000000.3-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000003.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000003.5-6.5in.svg)

![test/visual_test/latest/20010101000056.85-20010101000100.35-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000056.85-20010101000100.35-6.5in.svg)

![test/visual_test/latest/20010101005956.85-20010101010000.35-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956.85-20010101010000.35-6.5in.svg)

![test/visual_test/latest/20010101235956.85-20010102000000.35-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956.85-20010102000000.35-6.5in.svg)

![test/visual_test/latest/20010131235956.85-20010201000000.35-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235956.85-20010201000000.35-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000004.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000004.0-6.5in.svg)

![test/visual_test/latest/20010101000056.4-20010101000100.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000056.4-20010101000100.4-6.5in.svg)

![test/visual_test/latest/20010101005956.4-20010101010000.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956.4-20010101010000.4-6.5in.svg)

![test/visual_test/latest/20010101235956.4-20010102000000.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956.4-20010102000000.4-6.5in.svg)

![test/visual_test/latest/20010131235956.4-20010201000000.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235956.4-20010201000000.4-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000004.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000004.5-6.5in.svg)

![test/visual_test/latest/20010101000055.95-20010101000100.45-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000055.95-20010101000100.45-6.5in.svg)

![test/visual_test/latest/20010101005955.95-20010101010000.45-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005955.95-20010101010000.45-6.5in.svg)

![test/visual_test/latest/20010101235955.95-20010102000000.45-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235955.95-20010102000000.45-6.5in.svg)

![test/visual_test/latest/20010131235955.95-20010201000000.45-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235955.95-20010201000000.45-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000005.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000005.0-6.5in.svg)

![test/visual_test/latest/20010101000055.5-20010101000100.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000055.5-20010101000100.5-6.5in.svg)

![test/visual_test/latest/20010101005955.5-20010101010000.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005955.5-20010101010000.5-6.5in.svg)

![test/visual_test/latest/20010101235955.5-20010102000000.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235955.5-20010102000000.5-6.5in.svg)

![test/visual_test/latest/20010131235955.5-20010201000000.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235955.5-20010201000000.5-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000006.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000006.0-6.5in.svg)

![test/visual_test/latest/20010101000054.6-20010101000100.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000054.6-20010101000100.6-6.5in.svg)

![test/visual_test/latest/20010101005954.6-20010101010000.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005954.6-20010101010000.6-6.5in.svg)

![test/visual_test/latest/20010101235954.6-20010102000000.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235954.6-20010102000000.6-6.5in.svg)

![test/visual_test/latest/20010131235954.6-20010201000000.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235954.6-20010201000000.6-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000007.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000007.0-6.5in.svg)

![test/visual_test/latest/20010101000053.7-20010101000100.7-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000053.7-20010101000100.7-6.5in.svg)

![test/visual_test/latest/20010101005953.7-20010101010000.7-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005953.7-20010101010000.7-6.5in.svg)

![test/visual_test/latest/20010101235953.7-20010102000000.7-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235953.7-20010102000000.7-6.5in.svg)

![test/visual_test/latest/20010131235953.7-20010201000000.7-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235953.7-20010201000000.7-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000008.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000008.0-6.5in.svg)

![test/visual_test/latest/20010101000052.8-20010101000100.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000052.8-20010101000100.8-6.5in.svg)

![test/visual_test/latest/20010101005952.8-20010101010000.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005952.8-20010101010000.8-6.5in.svg)

![test/visual_test/latest/20010101235952.8-20010102000000.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235952.8-20010102000000.8-6.5in.svg)

![test/visual_test/latest/20010131235952.8-20010201000000.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235952.8-20010201000000.8-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000009.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000009.0-6.5in.svg)

![test/visual_test/latest/20010101000051.9-20010101000100.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000051.9-20010101000100.9-6.5in.svg)

![test/visual_test/latest/20010101005951.9-20010101010000.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005951.9-20010101010000.9-6.5in.svg)

![test/visual_test/latest/20010101235951.9-20010102000000.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235951.9-20010102000000.9-6.5in.svg)

![test/visual_test/latest/20010131235951.9-20010201000000.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235951.9-20010201000000.9-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000010.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000010.0-6.5in.svg)

![test/visual_test/latest/20010101000051.0-20010101000101.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000051.0-20010101000101.0-6.5in.svg)

![test/visual_test/latest/20010101005951.0-20010101010001.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005951.0-20010101010001.0-6.5in.svg)

![test/visual_test/latest/20010101235951.0-20010102000001.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235951.0-20010102000001.0-6.5in.svg)

![test/visual_test/latest/20010131235951.0-20010201000001.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235951.0-20010201000001.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000012.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000012.0-6.5in.svg)

![test/visual_test/latest/20010101000049.2-20010101000101.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000049.2-20010101000101.2-6.5in.svg)

![test/visual_test/latest/20010101005949.2-20010101010001.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005949.2-20010101010001.2-6.5in.svg)

![test/visual_test/latest/20010101235949.2-20010102000001.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235949.2-20010102000001.2-6.5in.svg)

![test/visual_test/latest/20010131235949.2-20010201000001.2-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235949.2-20010201000001.2-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000014.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000014.0-6.5in.svg)

![test/visual_test/latest/20010101000047.4-20010101000101.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000047.4-20010101000101.4-6.5in.svg)

![test/visual_test/latest/20010101005947.4-20010101010001.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005947.4-20010101010001.4-6.5in.svg)

![test/visual_test/latest/20010101235947.4-20010102000001.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235947.4-20010102000001.4-6.5in.svg)

![test/visual_test/latest/20010131235947.4-20010201000001.4-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235947.4-20010201000001.4-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000016.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000016.0-6.5in.svg)

![test/visual_test/latest/20010101000045.6-20010101000101.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000045.6-20010101000101.6-6.5in.svg)

![test/visual_test/latest/20010101005945.6-20010101010001.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005945.6-20010101010001.6-6.5in.svg)

![test/visual_test/latest/20010101235945.6-20010102000001.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235945.6-20010102000001.6-6.5in.svg)

![test/visual_test/latest/20010131235945.6-20010201000001.6-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235945.6-20010201000001.6-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000018.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000018.0-6.5in.svg)

![test/visual_test/latest/20010101000043.8-20010101000101.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000043.8-20010101000101.8-6.5in.svg)

![test/visual_test/latest/20010101005943.8-20010101010001.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005943.8-20010101010001.8-6.5in.svg)

![test/visual_test/latest/20010101235943.8-20010102000001.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235943.8-20010102000001.8-6.5in.svg)

![test/visual_test/latest/20010131235943.8-20010201000001.8-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235943.8-20010201000001.8-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000020.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000020.0-6.5in.svg)

![test/visual_test/latest/20010101000042.0-20010101000102.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000042.0-20010101000102.0-6.5in.svg)

![test/visual_test/latest/20010101005942.0-20010101010002.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005942.0-20010101010002.0-6.5in.svg)

![test/visual_test/latest/20010101235942.0-20010102000002.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235942.0-20010102000002.0-6.5in.svg)

![test/visual_test/latest/20010131235942.0-20010201000002.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235942.0-20010201000002.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000025.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000025.0-6.5in.svg)

![test/visual_test/latest/20010101000037.5-20010101000102.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000037.5-20010101000102.5-6.5in.svg)

![test/visual_test/latest/20010101005937.5-20010101010002.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005937.5-20010101010002.5-6.5in.svg)

![test/visual_test/latest/20010101235937.5-20010102000002.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235937.5-20010102000002.5-6.5in.svg)

![test/visual_test/latest/20010131235937.5-20010201000002.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235937.5-20010201000002.5-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000030.0-6.5in.svg)

![test/visual_test/latest/20010101000033.0-20010101000103.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000033.0-20010101000103.0-6.5in.svg)

![test/visual_test/latest/20010101005933.0-20010101010003.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005933.0-20010101010003.0-6.5in.svg)

![test/visual_test/latest/20010101235933.0-20010102000003.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235933.0-20010102000003.0-6.5in.svg)

![test/visual_test/latest/20010131235933.0-20010201000003.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235933.0-20010201000003.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000040.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000040.0-6.5in.svg)

![test/visual_test/latest/20010101000024.0-20010101000104.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000024.0-20010101000104.0-6.5in.svg)

![test/visual_test/latest/20010101005924.0-20010101010004.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005924.0-20010101010004.0-6.5in.svg)

![test/visual_test/latest/20010101235924.0-20010102000004.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235924.0-20010102000004.0-6.5in.svg)

![test/visual_test/latest/20010131235924.0-20010201000004.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235924.0-20010201000004.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000050.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000050.0-6.5in.svg)

![test/visual_test/latest/20010101000015.0-20010101000105.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000015.0-20010101000105.0-6.5in.svg)

![test/visual_test/latest/20010101005915.0-20010101010005.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005915.0-20010101010005.0-6.5in.svg)

![test/visual_test/latest/20010101235915.0-20010102000005.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235915.0-20010102000005.0-6.5in.svg)

![test/visual_test/latest/20010131235915.0-20010201000005.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235915.0-20010201000005.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000100.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000100.0-6.5in.svg)

![test/visual_test/latest/20010101005906.0-20010101010006.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005906.0-20010101010006.0-6.5in.svg)

![test/visual_test/latest/20010101235906.0-20010102000006.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235906.0-20010102000006.0-6.5in.svg)

![test/visual_test/latest/20010131235906.0-20010201000006.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235906.0-20010201000006.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000120.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000120.0-6.5in.svg)

![test/visual_test/latest/20010101005848.0-20010101010008.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005848.0-20010101010008.0-6.5in.svg)

![test/visual_test/latest/20010101235848.0-20010102000008.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235848.0-20010102000008.0-6.5in.svg)

![test/visual_test/latest/20010131235848.0-20010201000008.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235848.0-20010201000008.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000140.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000140.0-6.5in.svg)

![test/visual_test/latest/20010101005830.0-20010101010010.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005830.0-20010101010010.0-6.5in.svg)

![test/visual_test/latest/20010101235830.0-20010102000010.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235830.0-20010102000010.0-6.5in.svg)

![test/visual_test/latest/20010131235830.0-20010201000010.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235830.0-20010201000010.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000200.0-6.5in.svg)

![test/visual_test/latest/20010101005812.0-20010101010012.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005812.0-20010101010012.0-6.5in.svg)

![test/visual_test/latest/20010101235812.0-20010102000012.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235812.0-20010102000012.0-6.5in.svg)

![test/visual_test/latest/20010131235812.0-20010201000012.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235812.0-20010201000012.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000220.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000220.0-6.5in.svg)

![test/visual_test/latest/20010101005754.0-20010101010014.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005754.0-20010101010014.0-6.5in.svg)

![test/visual_test/latest/20010101235754.0-20010102000014.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235754.0-20010102000014.0-6.5in.svg)

![test/visual_test/latest/20010131235754.0-20010201000014.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235754.0-20010201000014.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000240.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000240.0-6.5in.svg)

![test/visual_test/latest/20010101005736.0-20010101010016.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005736.0-20010101010016.0-6.5in.svg)

![test/visual_test/latest/20010101235736.0-20010102000016.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235736.0-20010102000016.0-6.5in.svg)

![test/visual_test/latest/20010131235736.0-20010201000016.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235736.0-20010201000016.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000300.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000300.0-6.5in.svg)

![test/visual_test/latest/20010101005718.0-20010101010018.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005718.0-20010101010018.0-6.5in.svg)

![test/visual_test/latest/20010101235718.0-20010102000018.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235718.0-20010102000018.0-6.5in.svg)

![test/visual_test/latest/20010131235718.0-20010201000018.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235718.0-20010201000018.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000330.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000330.0-6.5in.svg)

![test/visual_test/latest/20010101005651.0-20010101010021.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005651.0-20010101010021.0-6.5in.svg)

![test/visual_test/latest/20010101235651.0-20010102000021.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235651.0-20010102000021.0-6.5in.svg)

![test/visual_test/latest/20010131235651.0-20010201000021.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235651.0-20010201000021.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000400.0-6.5in.svg)

![test/visual_test/latest/20010101005624.0-20010101010024.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005624.0-20010101010024.0-6.5in.svg)

![test/visual_test/latest/20010101235624.0-20010102000024.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235624.0-20010102000024.0-6.5in.svg)

![test/visual_test/latest/20010131235624.0-20010201000024.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235624.0-20010201000024.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000430.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000430.0-6.5in.svg)

![test/visual_test/latest/20010101005557.0-20010101010027.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005557.0-20010101010027.0-6.5in.svg)

![test/visual_test/latest/20010101235557.0-20010102000027.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235557.0-20010102000027.0-6.5in.svg)

![test/visual_test/latest/20010131235557.0-20010201000027.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235557.0-20010201000027.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000500.0-6.5in.svg)

![test/visual_test/latest/20010101005530.0-20010101010030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005530.0-20010101010030.0-6.5in.svg)

![test/visual_test/latest/20010101235530.0-20010102000030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235530.0-20010102000030.0-6.5in.svg)

![test/visual_test/latest/20010131235530.0-20010201000030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235530.0-20010201000030.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000600.0-6.5in.svg)

![test/visual_test/latest/20010101005436.0-20010101010036.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005436.0-20010101010036.0-6.5in.svg)

![test/visual_test/latest/20010101235436.0-20010102000036.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235436.0-20010102000036.0-6.5in.svg)

![test/visual_test/latest/20010131235436.0-20010201000036.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235436.0-20010201000036.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000700.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000700.0-6.5in.svg)

![test/visual_test/latest/20010101005342.0-20010101010042.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005342.0-20010101010042.0-6.5in.svg)

![test/visual_test/latest/20010101235342.0-20010102000042.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235342.0-20010102000042.0-6.5in.svg)

![test/visual_test/latest/20010131235342.0-20010201000042.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235342.0-20010201000042.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000800.0-6.5in.svg)

![test/visual_test/latest/20010101005248.0-20010101010048.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005248.0-20010101010048.0-6.5in.svg)

![test/visual_test/latest/20010101235248.0-20010102000048.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235248.0-20010102000048.0-6.5in.svg)

![test/visual_test/latest/20010131235248.0-20010201000048.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235248.0-20010201000048.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000900.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000900.0-6.5in.svg)

![test/visual_test/latest/20010101005154.0-20010101010054.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005154.0-20010101010054.0-6.5in.svg)

![test/visual_test/latest/20010101235154.0-20010102000054.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235154.0-20010102000054.0-6.5in.svg)

![test/visual_test/latest/20010131235154.0-20010201000054.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235154.0-20010201000054.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101001000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001000.0-6.5in.svg)

![test/visual_test/latest/20010101005100.0-20010101010100.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005100.0-20010101010100.0-6.5in.svg)

![test/visual_test/latest/20010101235100.0-20010102000100.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235100.0-20010102000100.0-6.5in.svg)

![test/visual_test/latest/20010131235100.0-20010201000100.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235100.0-20010201000100.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101001200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001200.0-6.5in.svg)

![test/visual_test/latest/20010101004912.0-20010101010112.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004912.0-20010101010112.0-6.5in.svg)

![test/visual_test/latest/20010101234912.0-20010102000112.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234912.0-20010102000112.0-6.5in.svg)

![test/visual_test/latest/20010131234912.0-20010201000112.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234912.0-20010201000112.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101001400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001400.0-6.5in.svg)

![test/visual_test/latest/20010101004724.0-20010101010124.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004724.0-20010101010124.0-6.5in.svg)

![test/visual_test/latest/20010101234724.0-20010102000124.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234724.0-20010102000124.0-6.5in.svg)

![test/visual_test/latest/20010131234724.0-20010201000124.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234724.0-20010201000124.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101001600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001600.0-6.5in.svg)

![test/visual_test/latest/20010101004536.0-20010101010136.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004536.0-20010101010136.0-6.5in.svg)

![test/visual_test/latest/20010101234536.0-20010102000136.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234536.0-20010102000136.0-6.5in.svg)

![test/visual_test/latest/20010131234536.0-20010201000136.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234536.0-20010201000136.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101001800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001800.0-6.5in.svg)

![test/visual_test/latest/20010101004348.0-20010101010148.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004348.0-20010101010148.0-6.5in.svg)

![test/visual_test/latest/20010101234348.0-20010102000148.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234348.0-20010102000148.0-6.5in.svg)

![test/visual_test/latest/20010131234348.0-20010201000148.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234348.0-20010201000148.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101002000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002000.0-6.5in.svg)

![test/visual_test/latest/20010101004200.0-20010101010200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004200.0-20010101010200.0-6.5in.svg)

![test/visual_test/latest/20010101234200.0-20010102000200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234200.0-20010102000200.0-6.5in.svg)

![test/visual_test/latest/20010131234200.0-20010201000200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234200.0-20010201000200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101002500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002500.0-6.5in.svg)

![test/visual_test/latest/20010101003730.0-20010101010230.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003730.0-20010101010230.0-6.5in.svg)

![test/visual_test/latest/20010101233730.0-20010102000230.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233730.0-20010102000230.0-6.5in.svg)

![test/visual_test/latest/20010131233730.0-20010201000230.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233730.0-20010201000230.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101003000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101003000.0-6.5in.svg)

![test/visual_test/latest/20010101003300.0-20010101010300.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003300.0-20010101010300.0-6.5in.svg)

![test/visual_test/latest/20010101233300.0-20010102000300.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233300.0-20010102000300.0-6.5in.svg)

![test/visual_test/latest/20010131233300.0-20010201000300.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233300.0-20010201000300.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101004000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101004000.0-6.5in.svg)

![test/visual_test/latest/20010101002400.0-20010101010400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101002400.0-20010101010400.0-6.5in.svg)

![test/visual_test/latest/20010101232400.0-20010102000400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101232400.0-20010102000400.0-6.5in.svg)

![test/visual_test/latest/20010131232400.0-20010201000400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131232400.0-20010201000400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101005000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101005000.0-6.5in.svg)

![test/visual_test/latest/20010101001500.0-20010101010500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101001500.0-20010101010500.0-6.5in.svg)

![test/visual_test/latest/20010101231500.0-20010102000500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101231500.0-20010102000500.0-6.5in.svg)

![test/visual_test/latest/20010131231500.0-20010201000500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131231500.0-20010201000500.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101010000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101010000.0-6.5in.svg)

![test/visual_test/latest/20010101230600.0-20010102000600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101230600.0-20010102000600.0-6.5in.svg)

![test/visual_test/latest/20010131230600.0-20010201000600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131230600.0-20010201000600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101011500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101011500.0-6.5in.svg)

![test/visual_test/latest/20010101225230.0-20010102000730.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101225230.0-20010102000730.0-6.5in.svg)

![test/visual_test/latest/20010131225230.0-20010201000730.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131225230.0-20010201000730.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101013000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101013000.0-6.5in.svg)

![test/visual_test/latest/20010101223900.0-20010102000900.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101223900.0-20010102000900.0-6.5in.svg)

![test/visual_test/latest/20010131223900.0-20010201000900.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131223900.0-20010201000900.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101014500.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101014500.0-6.5in.svg)

![test/visual_test/latest/20010101222530.0-20010102001030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101222530.0-20010102001030.0-6.5in.svg)

![test/visual_test/latest/20010131222530.0-20010201001030.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131222530.0-20010201001030.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101020000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101020000.0-6.5in.svg)

![test/visual_test/latest/20010101221200.0-20010102001200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101221200.0-20010102001200.0-6.5in.svg)

![test/visual_test/latest/20010131221200.0-20010201001200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131221200.0-20010201001200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101022000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101022000.0-6.5in.svg)

![test/visual_test/latest/20010101215400.0-20010102001400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101215400.0-20010102001400.0-6.5in.svg)

![test/visual_test/latest/20010131215400.0-20010201001400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131215400.0-20010201001400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101024000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101024000.0-6.5in.svg)

![test/visual_test/latest/20010101213600.0-20010102001600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101213600.0-20010102001600.0-6.5in.svg)

![test/visual_test/latest/20010131213600.0-20010201001600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131213600.0-20010201001600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101030000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101030000.0-6.5in.svg)

![test/visual_test/latest/20010101211800.0-20010102001800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101211800.0-20010102001800.0-6.5in.svg)

![test/visual_test/latest/20010131211800.0-20010201001800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131211800.0-20010201001800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101032000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101032000.0-6.5in.svg)

![test/visual_test/latest/20010101210000.0-20010102002000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101210000.0-20010102002000.0-6.5in.svg)

![test/visual_test/latest/20010131210000.0-20010201002000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131210000.0-20010201002000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101034000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101034000.0-6.5in.svg)

![test/visual_test/latest/20010101204200.0-20010102002200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101204200.0-20010102002200.0-6.5in.svg)

![test/visual_test/latest/20010131204200.0-20010201002200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131204200.0-20010201002200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101040000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101040000.0-6.5in.svg)

![test/visual_test/latest/20010101202400.0-20010102002400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101202400.0-20010102002400.0-6.5in.svg)

![test/visual_test/latest/20010131202400.0-20010201002400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131202400.0-20010201002400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101050000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101050000.0-6.5in.svg)

![test/visual_test/latest/20010101193000.0-20010102003000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101193000.0-20010102003000.0-6.5in.svg)

![test/visual_test/latest/20010131193000.0-20010201003000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131193000.0-20010201003000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101060000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101060000.0-6.5in.svg)

![test/visual_test/latest/20010101183600.0-20010102003600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101183600.0-20010102003600.0-6.5in.svg)

![test/visual_test/latest/20010131183600.0-20010201003600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131183600.0-20010201003600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101080000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101080000.0-6.5in.svg)

![test/visual_test/latest/20010101164800.0-20010102004800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101164800.0-20010102004800.0-6.5in.svg)

![test/visual_test/latest/20010131164800.0-20010201004800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131164800.0-20010201004800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101100000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101100000.0-6.5in.svg)

![test/visual_test/latest/20010101150000.0-20010102010000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101150000.0-20010102010000.0-6.5in.svg)

![test/visual_test/latest/20010131150000.0-20010201010000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131150000.0-20010201010000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101120000.0-6.5in.svg)

![test/visual_test/latest/20010101131200.0-20010102011200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101131200.0-20010102011200.0-6.5in.svg)

![test/visual_test/latest/20010131131200.0-20010201011200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131131200.0-20010201011200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101150000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101150000.0-6.5in.svg)

![test/visual_test/latest/20010101103000.0-20010102013000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101103000.0-20010102013000.0-6.5in.svg)

![test/visual_test/latest/20010131103000.0-20010201013000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131103000.0-20010201013000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101180000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101180000.0-6.5in.svg)

![test/visual_test/latest/20010101074800.0-20010102014800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101074800.0-20010102014800.0-6.5in.svg)

![test/visual_test/latest/20010131074800.0-20010201014800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131074800.0-20010201014800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101210000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101210000.0-6.5in.svg)

![test/visual_test/latest/20010101050600.0-20010102020600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101050600.0-20010102020600.0-6.5in.svg)

![test/visual_test/latest/20010131050600.0-20010201020600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131050600.0-20010201020600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102000000.0-6.5in.svg)

![test/visual_test/latest/20010131022400.0-20010201022400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131022400.0-20010201022400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102040000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102040000.0-6.5in.svg)

![test/visual_test/latest/20010130224800.0-20010201024800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130224800.0-20010201024800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102080000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102080000.0-6.5in.svg)

![test/visual_test/latest/20010130191200.0-20010201031200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130191200.0-20010201031200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102120000.0-6.5in.svg)

![test/visual_test/latest/20010130153600.0-20010201033600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130153600.0-20010201033600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102160000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102160000.0-6.5in.svg)

![test/visual_test/latest/20010130120000.0-20010201040000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130120000.0-20010201040000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010102200000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102200000.0-6.5in.svg)

![test/visual_test/latest/20010130082400.0-20010201042400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130082400.0-20010201042400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010103000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103000000.0-6.5in.svg)

![test/visual_test/latest/20010130044800.0-20010201044800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130044800.0-20010201044800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010103060000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103060000.0-6.5in.svg)

![test/visual_test/latest/20010129232400.0-20010201052400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129232400.0-20010201052400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010103120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103120000.0-6.5in.svg)

![test/visual_test/latest/20010129180000.0-20010201060000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129180000.0-20010201060000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010103180000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103180000.0-6.5in.svg)

![test/visual_test/latest/20010129123600.0-20010201063600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129123600.0-20010201063600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010104000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104000000.0-6.5in.svg)

![test/visual_test/latest/20010129071200.0-20010201071200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129071200.0-20010201071200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010104120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104120000.0-6.5in.svg)

![test/visual_test/latest/20010128202400.0-20010201082400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128202400.0-20010201082400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010105000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010105000000.0-6.5in.svg)

![test/visual_test/latest/20010128093600.0-20010201093600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128093600.0-20010201093600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010106000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010106000000.0-6.5in.svg)

![test/visual_test/latest/20010127120000.0-20010201120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010127120000.0-20010201120000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010107000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010107000000.0-6.5in.svg)

![test/visual_test/latest/20010126142400.0-20010201142400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010126142400.0-20010201142400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010108000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010108000000.0-6.5in.svg)

![test/visual_test/latest/20010125164800.0-20010201164800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010125164800.0-20010201164800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010109000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010109000000.0-6.5in.svg)

![test/visual_test/latest/20010124191200.0-20010201191200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010124191200.0-20010201191200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010110000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010110000000.0-6.5in.svg)

![test/visual_test/latest/20010123213600.0-20010201213600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010123213600.0-20010201213600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010111000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010111000000.0-6.5in.svg)

![test/visual_test/latest/20010123000000.0-20010202000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010123000000.0-20010202000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010112000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010112000000.0-6.5in.svg)

![test/visual_test/latest/20010122022400.0-20010202022400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010122022400.0-20010202022400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010113000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010113000000.0-6.5in.svg)

![test/visual_test/latest/20010121044800.0-20010202044800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010121044800.0-20010202044800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010114000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010114000000.0-6.5in.svg)

![test/visual_test/latest/20010120071200.0-20010202071200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010120071200.0-20010202071200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010115000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010115000000.0-6.5in.svg)

![test/visual_test/latest/20010119093600.0-20010202093600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010119093600.0-20010202093600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010116000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010116000000.0-6.5in.svg)

![test/visual_test/latest/20010118120000.0-20010202120000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010118120000.0-20010202120000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010117000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010117000000.0-6.5in.svg)

![test/visual_test/latest/20010117142400.0-20010202142400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010117142400.0-20010202142400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010120000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010120000000.0-6.5in.svg)

![test/visual_test/latest/20010114213600.0-20010202213600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010114213600.0-20010202213600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010121000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010121000000.0-6.5in.svg)

![test/visual_test/latest/20010114000000.0-20010203000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010114000000.0-20010203000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010124000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010124000000.0-6.5in.svg)

![test/visual_test/latest/20010111071200.0-20010203071200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010111071200.0-20010203071200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010125000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010125000000.0-6.5in.svg)

![test/visual_test/latest/20010110093600.0-20010203093600.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010110093600.0-20010203093600.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010128000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010128000000.0-6.5in.svg)

![test/visual_test/latest/20010107164800.0-20010203164800.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010107164800.0-20010203164800.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010129000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010129000000.0-6.5in.svg)

![test/visual_test/latest/20010106191200.0-20010203191200.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010106191200.0-20010203191200.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010201000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010201000000.0-6.5in.svg)

![test/visual_test/latest/20010104022400.0-20010204022400.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010104022400.0-20010204022400.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010205000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010205000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010208000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010208000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010215000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010215000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010222000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010222000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010301000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010301000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010303000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010303000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010331000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010331000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010401000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010401000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010402000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010402000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010403000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010403000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010501000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010501000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010503000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010503000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010531000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010531000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010601000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010601000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010701000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010701000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010703000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010703000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010704000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010704000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010801000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010801000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010803000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010803000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010831000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010831000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010901000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010901000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010902000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010902000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010903000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010903000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011001000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011001000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011003000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011003000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011031000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011031000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011103000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011103000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20011201000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011201000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020301000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020301000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020303000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020303000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020304000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020304000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020501000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020501000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020503000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020503000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020504000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020504000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020701000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020701000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020704000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020704000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020901000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020901000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20020903000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020903000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20021101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20021103000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021103000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20030101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20030101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20040101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20040102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20050101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20050101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20060101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20060102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20070101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20070102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20080101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20080102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20090101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20090101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20100101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20100101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20100102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20100102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20110101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20110102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20120101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20120101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20120102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20120102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20130101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20130101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20140101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20140101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20150101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20150101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20160101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20160101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20210101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20210101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20260101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20260102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20310101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20310102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20360101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20360102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20401231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20401231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20410101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20410101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20510101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20510102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20601231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20601231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20610101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20610101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20710101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20710102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20801231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20801231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20810101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20810101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20910101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20910102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21201231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21201231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21210101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21210101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21401231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21401231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21410101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21410101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21601231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21601231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21610101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21610101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21801231000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21801231000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-21810101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21810101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-22010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-22010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-22210101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22210101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-22410101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22410101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-23010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-23010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-24010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-24010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-25010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-25010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-30010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-30010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-35010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-35010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-35010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-35010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-40010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-40010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-45010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-45010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-45010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-45010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-50010101000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-50010101000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-50010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-50010102000000.0-6.5in.svg)

![test/visual_test/latest/20010101000000.0-55010102000000.0-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-55010102000000.0-6.5in.svg)