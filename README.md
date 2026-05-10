# datetick

Sensible date/time tick labels for [Matplotlib](https://matplotlib.org/)

# Motivation

`Matplotlib`'s default date/time tick labels are often poor, and adjusting them requires using [locators and formatters](https://matplotlib.org/stable/api/ticker_api.html) on an ad-hoc basis. A method or package for handling arbitrary time ranges does not exist.

In addition, the interfaces for locators and formatters complex and non-intuitive and require study and experimentation (e.g., [[1]](https://github.com/matplotlib/matplotlib/issues/28158), [[2]](https://github.com/matplotlib/matplotlib/issues/15813]), [[3]](https://github.com/matplotlib/matplotlib/issues/9978), [[4]](https://github.com/matplotlib/matplotlib/issues/9978). Tilting labels is an [often-suggested solution](https://github.com/matplotlib/matplotlib/issues/9978), but this should not be needed.

`datetick()` contains logic for locators and formatters that apply to plots with arbitrary time ranges. One only needs to add the command `datetick()` after the usual `plt.plot(...)` command to have sensible and useable time tick labels. The primary configuration is a set of [rules](datetick/rules.json) that account for the time range and an adjustable minimum gap between tick labels.

To prevent overlap and enforce a minimum gap, the font size is automatically reduced to a chosen minimum value. Then the number of ticks are reduced based on rules in [rules.json](datetick/rules.json).

# Usage

```
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

![test/visual_test/latest/20010101000000.0-20010101000000.5-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.5-6.5in.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.9-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.9-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000001-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000001-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000002-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000002-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000003-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000003-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000004-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000004-6.5in.svg)

![test/visual_test/latest/20010101235958-20010102000002-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000002-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000005-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000005-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000006-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000006-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000007-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000007-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000009-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000009-6.5in.svg)

![test/visual_test/latest/20010101235958-20010102000005-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000005-6.5in.svg)

![test/visual_test/latest/20010101235959-20010102000005-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959-20010102000005-6.5in.svg)

![test/visual_test/latest/20010101005958-20010101010005-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010005-6.5in.svg)

![test/visual_test/latest/20010101005958-20010101010007-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010007-6.5in.svg)

![test/visual_test/latest/20010101005958-20010101010003-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010003-6.5in.svg)

![test/visual_test/latest/20010101235956-20010102000010-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956-20010102000010-6.5in.svg)

![test/visual_test/latest/20010101235958-20010102000010-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000010-6.5in.svg)

![test/visual_test/latest/20010101005956-20010101010010-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010010-6.5in.svg)

![test/visual_test/latest/20010101005956-20010101010015-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010015-6.5in.svg)

![test/visual_test/latest/20010101005956-20010101010006-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010006-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101000021-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000021-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101060000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101060000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101090000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101090000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101110000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101110000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101110000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101110000-6.5in_v2.svg)

![test/visual_test/latest/20010101005958-20010101010028-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010028-6.5in.svg)

![test/visual_test/latest/20010101000058-20010101000118-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058-20010101000118-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101120000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101120000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101180000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101180000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010101230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101230000-6.5in.svg)

![test/visual_test/latest/20010101020000-20010102010000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101020000-20010102010000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010102010000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102010000-6.5in.svg)

![test/visual_test/latest/20010101060000-20010102070000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101060000-20010102070000-6.5in.svg)

![test/visual_test/latest/20010101003000-20010102010000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003000-20010102010000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010103000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010103123000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103123000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010103235959-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103235959-6.5in.svg)

![test/visual_test/latest/20010101000000-20010105000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010105000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010105000000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010105000000-6.5in_v2.svg)

![test/visual_test/latest/20010130000000-20010201230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010201230000-6.5in.svg)

![test/visual_test/latest/20011230000000-20020101230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20020101230000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010109000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010109000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010116230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010116230000-6.5in.svg)

![test/visual_test/latest/20010130000000-20010204230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010204230000-6.5in.svg)

![test/visual_test/latest/20011230000000-20020104230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20020104230000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010116230000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010116230000-6.5in_v2.svg)

![test/visual_test/latest/20010101000000-20010131000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010131000000-6.5in.svg)

![test/visual_test/latest/20010130000000-20010215230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010215230000-6.5in.svg)

![test/visual_test/latest/20011230000000-20020115230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20020115230000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010202000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010202000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010227230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010227230000-6.5in.svg)

![test/visual_test/latest/20010115000000-20010216230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010115000000-20010216230000-6.5in.svg)

![test/visual_test/latest/20011231000000-20020226230000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011231000000-20020226230000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010502000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010502000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20010227230000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010227230000-6.5in_v2.svg)

![test/visual_test/latest/20011231000000-20020226230000-6.5in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011231000000-20020226230000-6.5in_v2.svg)

![test/visual_test/latest/20010101000000-20010702000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010702000000-6.5in.svg)

![test/visual_test/latest/20010212000000-20020131000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010212000000-20020131000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20011231000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20011231000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20020103000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20020103000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20021231000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20021231000000-6.5in.svg)

![test/visual_test/latest/20010401000000-20020430000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010401000000-20020430000000-6.5in.svg)

![test/visual_test/latest/20011001000000-20031004000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011001000000-20031004000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20081231000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20081231000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20090104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20090104000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20120104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20120104000000-6.5in.svg)

![test/visual_test/latest/20000101000000-20170104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20170104000000-6.5in.svg)

![test/visual_test/latest/20010101000000-20180104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20180104000000-6.5in.svg)

![test/visual_test/latest/20030101000000-20200104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20030101000000-20200104000000-6.5in.svg)

![test/visual_test/latest/20040101000000-20300104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20040101000000-20300104000000-6.5in.svg)

![test/visual_test/latest/19500101000000-20120104000000-6.5in.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19500101000000-20120104000000-6.5in.svg)