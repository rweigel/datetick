# datetick

Sensible numeric time and date tick labels for Matplotlib

# Motivation

Matplotlib's default time tick labels are often poor, and adjusting them requires using [locators and formatters](https://matplotlib.org/stable/api/ticker_api.html) on an ad-hoc basis. In addition, the interfaces for locators and formatters complex and non-intuitive and require study and experimentation.

`datetick()` contains logic for locators and formatters that apply to plots with arbitrary time ranges. One only needs to add the command `datetick()` after the usual Matplotlib `plt.plot(...)` command to have sensible and useable time tick labels.

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
# datetick('x') (use 'y' if y variable is a time)
# or
# datetick('x', axes=plt.gca())
# or
# fig, axes = plt.subplots(2)
# plt.plot([dt1, dt2], [0.0, 1.0])
# datetick('x', axes=axes[0])
```

# Comparison to default Matplotlib


<code>Python-3.13/Matplotlib-3.10.9</code>


## <code>dir=x</code>

![test/visual_test/latest/20010101000000-20010102230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-x.svg)

![test/visual_test/latest/20010101000000-20010102230000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-x_v2.svg)

![test/visual_test/latest/20010101000000-20010102230000-x_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-x_v3.svg)

![test/visual_test/latest/20010101000000-20010102230000-x_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102230000-x_v4.svg)

![test/visual_test/latest/20001231170000-20010102190000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-x.svg)

![test/visual_test/latest/20001231170000-20010102190000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-x_v2.svg)

![test/visual_test/latest/20001231170000-20010102190000-x_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231170000-20010102190000-x_v3.svg)

![test/visual_test/latest/20010101000000.0-20010101000000.9-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.9-x.svg)

![test/visual_test/latest/20010101000000-20010101000001-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000001-x.svg)

![test/visual_test/latest/20010101000000-20010101000002-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000002-x.svg)

![test/visual_test/latest/20010101000000-20010101000003-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000003-x.svg)

![test/visual_test/latest/20010101000000-20010101000004-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000004-x.svg)

![test/visual_test/latest/20010101235958-20010102000002-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000002-x.svg)

![test/visual_test/latest/20010101000000-20010101000005-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000005-x.svg)

![test/visual_test/latest/20010101000000-20010101000006-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000006-x.svg)

![test/visual_test/latest/20010101000000-20010101000007-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000007-x.svg)

![test/visual_test/latest/20010101000000-20010101000009-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000009-x.svg)

![test/visual_test/latest/20010101235958-20010102000005-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000005-x.svg)

![test/visual_test/latest/20010101235959-20010102000005-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959-20010102000005-x.svg)

![test/visual_test/latest/20010101005958-20010101010005-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010005-x.svg)

![test/visual_test/latest/20010101005958-20010101010007-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010007-x.svg)

![test/visual_test/latest/20010101005958-20010101010003-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010003-x.svg)

![test/visual_test/latest/20010101235956-20010102000010-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956-20010102000010-x.svg)

![test/visual_test/latest/20010101235958-20010102000010-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958-20010102000010-x.svg)

![test/visual_test/latest/20010101005956-20010101010010-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010010-x.svg)

![test/visual_test/latest/20010101005956-20010101010015-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010015-x.svg)

![test/visual_test/latest/20010101005956-20010101010006-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956-20010101010006-x.svg)

![test/visual_test/latest/20010101000000-20010101000021-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101000021-x.svg)

![test/visual_test/latest/20010101000000-20010101060000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101060000-x.svg)

![test/visual_test/latest/20010101000000-20010101090000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101090000-x.svg)

![test/visual_test/latest/20010101000000-20010101110000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101110000-x.svg)

![test/visual_test/latest/20010101000000-20010101110000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101110000-x_v2.svg)

![test/visual_test/latest/20010101005958-20010101010028-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958-20010101010028-x.svg)

![test/visual_test/latest/20010101000058-20010101000118-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058-20010101000118-x.svg)

![test/visual_test/latest/20010101000000-20010101180000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101180000-x.svg)

![test/visual_test/latest/20010101000000-20010101120000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101120000-x.svg)

![test/visual_test/latest/20010101000000-20010101230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010101230000-x.svg)

![test/visual_test/latest/20010101020000-20010102010000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101020000-20010102010000-x.svg)

![test/visual_test/latest/20010101000000-20010102010000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010102010000-x.svg)

![test/visual_test/latest/20010101060000-20010102070000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101060000-20010102070000-x.svg)

![test/visual_test/latest/20010101003000-20010102010000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003000-20010102010000-x.svg)

![test/visual_test/latest/20010101000000-20010103000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103000000-x.svg)

![test/visual_test/latest/20010101000000-20010103123000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103123000-x.svg)

![test/visual_test/latest/20010101000000-20010103235959-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010103235959-x.svg)

![test/visual_test/latest/20010101000000-20010105000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010105000000-x.svg)

![test/visual_test/latest/20010101000000-20010105000000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010105000000-x_v2.svg)

![test/visual_test/latest/20010130000000-20010201230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010201230000-x.svg)

![test/visual_test/latest/20011230000000-20020101230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20020101230000-x.svg)

![test/visual_test/latest/20010101000000-20010109000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010109000000-x.svg)

![test/visual_test/latest/20010101000000-20010116230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010116230000-x.svg)

![test/visual_test/latest/20010130000000-20010204230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010204230000-x.svg)

![test/visual_test/latest/20011230000000-20020104230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20020104230000-x.svg)

![test/visual_test/latest/20010101000000-20010131000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010131000000-x.svg)

![test/visual_test/latest/20010101000000-20010116230000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010116230000-x_v2.svg)

![test/visual_test/latest/20010130000000-20010215230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130000000-20010215230000-x.svg)

![test/visual_test/latest/20011230000000-20010115230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011230000000-20010115230000-x.svg)

![test/visual_test/latest/20010101000000-20010202000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010202000000-x.svg)

![test/visual_test/latest/20010101000000-20010227230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010227230000-x.svg)

![test/visual_test/latest/20010115000000-20010216230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010115000000-20010216230000-x.svg)

![test/visual_test/latest/20011231000000-20020226230000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011231000000-20020226230000-x.svg)

![test/visual_test/latest/20010101000000-20010502000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010502000000-x.svg)

![test/visual_test/latest/20010101000000-20010227230000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010227230000-x_v2.svg)

![test/visual_test/latest/20011231000000-20020226230000-x_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011231000000-20020226230000-x_v2.svg)

![test/visual_test/latest/20010101000000-20010702000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20010702000000-x.svg)

![test/visual_test/latest/20010101000000-20011231000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20011231000000-x.svg)

![test/visual_test/latest/20010212000000-20020131000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010212000000-20020131000000-x.svg)

![test/visual_test/latest/20010101000000-20020103000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20020103000000-x.svg)

![test/visual_test/latest/20010101000000-20021231000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20021231000000-x.svg)

![test/visual_test/latest/20010401000000-20020430000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010401000000-20020430000000-x.svg)

![test/visual_test/latest/20011001000000-20031004000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20011001000000-20031004000000-x.svg)

![test/visual_test/latest/20010101000000-20081231000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20081231000000-x.svg)

![test/visual_test/latest/20010101000000-20030104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20030104000000-x.svg)

![test/visual_test/latest/20010101000000-20090104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20090104000000-x.svg)

![test/visual_test/latest/20010101000000-20120104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20120104000000-x.svg)

![test/visual_test/latest/20000101000000-20170104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20170104000000-x.svg)

![test/visual_test/latest/20010101000000-20180104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000-20180104000000-x.svg)

![test/visual_test/latest/20020101000000-20190104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20020101000000-20190104000000-x.svg)

![test/visual_test/latest/20030101000000-20200104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20030101000000-20200104000000-x.svg)

![test/visual_test/latest/20040101000000-20300104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20040101000000-20300104000000-x.svg)

![test/visual_test/latest/19500101000000-20120104000000-x.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19500101000000-20120104000000-x.svg)