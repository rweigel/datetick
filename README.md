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


<code>Python-3.12/Matplotlib-3.11.1</code>


## <code>axis=x</code>


1\. (rule change: -1 reverted)

![test/visual_test/latest/20030901000000-20031201000000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20030901000000-20031201000000-6.4in_v1.svg)


2\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v1.svg)


3\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v2.svg)


4\. (rule change: -1 reverted)

![test/visual_test/latest/19991231220000-20000102020000-12.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-12.4in_v1.svg)


5\.

![test/visual_test/latest/19991231220000-20000102020000-3.2in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-3.2in_v1.svg)


6\. (rule change: 1 reverted)

![test/visual_test/latest/19991231220000-20000102020000-1.6in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-1.6in_v1.svg)


7\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg)


8\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg)


9\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg)


10\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg)


11\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg)


12\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg)


13\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg)


14\.

![test/visual_test/latest/20010101000000.0-20010101000000.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.001-6.4in_v1.svg)


15\. Cross second boundary

![test/visual_test/latest/20010101000000.9991-20010101000001.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9991-20010101000001.0001-6.4in_v1.svg)


16\. Cross minute boundary

![test/visual_test/latest/20010101000059.9991-20010101000100.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9991-20010101000100.0001-6.4in_v1.svg)


17\. Cross hour boundary

![test/visual_test/latest/20010101005959.9991-20010101010000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9991-20010101010000.0001-6.4in_v1.svg)


18\. Cross day boundary

![test/visual_test/latest/20010101235959.9991-20010102000000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9991-20010102000000.0001-6.4in_v1.svg)


19\. Cross month boundary

![test/visual_test/latest/20010131235959.9991-20010201000000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9991-20010201000000.0001-6.4in_v1.svg)


20\.

![test/visual_test/latest/20010101000000.0-20010101000000.00125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00125-6.4in_v1.svg)


21\. Cross second boundary

![test/visual_test/latest/20010101000000.998875-20010101000001.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.998875-20010101000001.000125-6.4in_v1.svg)


22\. Cross minute boundary

![test/visual_test/latest/20010101000059.998875-20010101000100.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.998875-20010101000100.000125-6.4in_v1.svg)


23\. Cross hour boundary

![test/visual_test/latest/20010101005959.998875-20010101010000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.998875-20010101010000.000125-6.4in_v1.svg)


24\. Cross day boundary

![test/visual_test/latest/20010101235959.998875-20010102000000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.998875-20010102000000.000125-6.4in_v1.svg)


25\. Cross month boundary

![test/visual_test/latest/20010131235959.998875-20010201000000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.998875-20010201000000.000125-6.4in_v1.svg)


26\.

![test/visual_test/latest/20010101000000.0-20010101000000.0015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0015-6.4in_v1.svg)


27\. Cross second boundary

![test/visual_test/latest/20010101000000.99865-20010101000001.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99865-20010101000001.00015-6.4in_v1.svg)


28\. Cross minute boundary

![test/visual_test/latest/20010101000059.99865-20010101000100.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99865-20010101000100.00015-6.4in_v1.svg)


29\. Cross hour boundary

![test/visual_test/latest/20010101005959.99865-20010101010000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99865-20010101010000.00015-6.4in_v1.svg)


30\. Cross day boundary

![test/visual_test/latest/20010101235959.99865-20010102000000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99865-20010102000000.00015-6.4in_v1.svg)


31\. Cross month boundary

![test/visual_test/latest/20010131235959.99865-20010201000000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99865-20010201000000.00015-6.4in_v1.svg)


32\. (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.00175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00175-6.4in_v1.svg)


33\. Cross second boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.998425-20010101000001.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.998425-20010101000001.000175-6.4in_v1.svg)


34\. Cross minute boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101000059.998425-20010101000100.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.998425-20010101000100.000175-6.4in_v1.svg)


35\. Cross hour boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101005959.998425-20010101010000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.998425-20010101010000.000175-6.4in_v1.svg)


36\. Cross day boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101235959.998425-20010102000000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.998425-20010102000000.000175-6.4in_v1.svg)


37\. Cross month boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010131235959.998425-20010201000000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.998425-20010201000000.000175-6.4in_v1.svg)


38\. (font size change: -2.0 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.002-6.4in_v1.svg)


39\. Cross second boundary (font size change: -2.0 pt)

![test/visual_test/latest/20010101000000.9982-20010101000001.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9982-20010101000001.0002-6.4in_v1.svg)


40\. Cross minute boundary (font size change: -2.0 pt)

![test/visual_test/latest/20010101000059.9982-20010101000100.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9982-20010101000100.0002-6.4in_v1.svg)


41\. Cross hour boundary (font size change: -2.0 pt)

![test/visual_test/latest/20010101005959.9982-20010101010000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9982-20010101010000.0002-6.4in_v1.svg)


42\. Cross day boundary (font size change: -2.0 pt)

![test/visual_test/latest/20010101235959.9982-20010102000000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9982-20010102000000.0002-6.4in_v1.svg)


43\. Cross month boundary (font size change: -2.0 pt)

![test/visual_test/latest/20010131235959.9982-20010201000000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9982-20010201000000.0002-6.4in_v1.svg)


44\. (font size change: -3.0 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.00225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00225-6.4in_v1.svg)


45\. Cross second boundary (font size change: -3.0 pt)

![test/visual_test/latest/20010101000000.997975-20010101000001.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.997975-20010101000001.000225-6.4in_v1.svg)


46\. Cross minute boundary (font size change: -3.0 pt)

![test/visual_test/latest/20010101000059.997975-20010101000100.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.997975-20010101000100.000225-6.4in_v1.svg)


47\. Cross hour boundary (font size change: -3.0 pt)

![test/visual_test/latest/20010101005959.997975-20010101010000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.997975-20010101010000.000225-6.4in_v1.svg)


48\. Cross day boundary (font size change: -3.0 pt)

![test/visual_test/latest/20010101235959.997975-20010102000000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.997975-20010102000000.000225-6.4in_v1.svg)


49\. Cross month boundary (font size change: -3.0 pt)

![test/visual_test/latest/20010131235959.997975-20010201000000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.997975-20010201000000.000225-6.4in_v1.svg)


50\.

![test/visual_test/latest/20010101000000.0-20010101000000.0025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0025-6.4in_v1.svg)


51\. Cross second boundary

![test/visual_test/latest/20010101000000.99775-20010101000001.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99775-20010101000001.00025-6.4in_v1.svg)


52\. Cross minute boundary

![test/visual_test/latest/20010101000059.99775-20010101000100.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99775-20010101000100.00025-6.4in_v1.svg)


53\. Cross hour boundary

![test/visual_test/latest/20010101005959.99775-20010101010000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99775-20010101010000.00025-6.4in_v1.svg)


54\. Cross day boundary

![test/visual_test/latest/20010101235959.99775-20010102000000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99775-20010102000000.00025-6.4in_v1.svg)


55\. Cross month boundary

![test/visual_test/latest/20010131235959.99775-20010201000000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99775-20010201000000.00025-6.4in_v1.svg)


56\.

![test/visual_test/latest/20010101000000.0-20010101000000.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.003-6.4in_v1.svg)


57\. Cross second boundary

![test/visual_test/latest/20010101000000.9973-20010101000001.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9973-20010101000001.0003-6.4in_v1.svg)


58\. Cross minute boundary

![test/visual_test/latest/20010101000059.9973-20010101000100.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9973-20010101000100.0003-6.4in_v1.svg)


59\. Cross hour boundary

![test/visual_test/latest/20010101005959.9973-20010101010000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9973-20010101010000.0003-6.4in_v1.svg)


60\. Cross day boundary

![test/visual_test/latest/20010101235959.9973-20010102000000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9973-20010102000000.0003-6.4in_v1.svg)


61\. Cross month boundary

![test/visual_test/latest/20010131235959.9973-20010201000000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9973-20010201000000.0003-6.4in_v1.svg)


62\.

![test/visual_test/latest/20010101000000.0-20010101000000.0035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0035-6.4in_v1.svg)


63\. Cross second boundary

![test/visual_test/latest/20010101000000.99685-20010101000001.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99685-20010101000001.00035-6.4in_v1.svg)


64\. Cross minute boundary

![test/visual_test/latest/20010101000059.99685-20010101000100.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99685-20010101000100.00035-6.4in_v1.svg)


65\. Cross hour boundary

![test/visual_test/latest/20010101005959.99685-20010101010000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99685-20010101010000.00035-6.4in_v1.svg)


66\. Cross day boundary

![test/visual_test/latest/20010101235959.99685-20010102000000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99685-20010102000000.00035-6.4in_v1.svg)


67\. Cross month boundary

![test/visual_test/latest/20010131235959.99685-20010201000000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99685-20010201000000.00035-6.4in_v1.svg)


68\. (rule change: 1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000000.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.004-6.4in_v1.svg)


69\. Cross second boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101000000.9964-20010101000001.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9964-20010101000001.0004-6.4in_v1.svg)


70\. Cross minute boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101000059.9964-20010101000100.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9964-20010101000100.0004-6.4in_v1.svg)


71\. Cross hour boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101005959.9964-20010101010000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9964-20010101010000.0004-6.4in_v1.svg)


72\. Cross day boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101235959.9964-20010102000000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9964-20010102000000.0004-6.4in_v1.svg)


73\. Cross month boundary (rule change: 1 reverted)

![test/visual_test/latest/20010131235959.9964-20010201000000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9964-20010201000000.0004-6.4in_v1.svg)


74\. (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.0045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0045-6.4in_v1.svg)


75\. Cross second boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.99595-20010101000001.00045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99595-20010101000001.00045-6.4in_v1.svg)


76\. Cross minute boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101000059.99595-20010101000100.00045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99595-20010101000100.00045-6.4in_v1.svg)


77\. Cross hour boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101005959.99595-20010101010000.00045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99595-20010101010000.00045-6.4in_v1.svg)


78\. Cross day boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101235959.99595-20010102000000.00045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99595-20010102000000.00045-6.4in_v1.svg)


79\. Cross month boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010131235959.99595-20010201000000.00045-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99595-20010201000000.00045-6.4in_v1.svg)


80\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.01-6.4in_v1.svg)


81\. Cross second boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.991-20010101000001.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.991-20010101000001.001-6.4in_v1.svg)


82\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000059.991-20010101000100.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.991-20010101000100.001-6.4in_v1.svg)


83\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005959.991-20010101010000.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.991-20010101010000.001-6.4in_v1.svg)


84\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235959.991-20010102000000.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.991-20010102000000.001-6.4in_v1.svg)


85\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235959.991-20010201000000.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.991-20010201000000.001-6.4in_v1.svg)


86\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.02-6.4in_v1.svg)


87\. Cross second boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.982-20010101000001.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.982-20010101000001.002-6.4in_v1.svg)


88\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000059.982-20010101000100.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.982-20010101000100.002-6.4in_v1.svg)


89\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005959.982-20010101010000.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.982-20010101010000.002-6.4in_v1.svg)


90\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235959.982-20010102000000.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.982-20010102000000.002-6.4in_v1.svg)


91\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235959.982-20010201000000.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.982-20010201000000.002-6.4in_v1.svg)


92\.

![test/visual_test/latest/20010101000000.0-20010101000000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.03-6.4in_v1.svg)


93\. Cross second boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.973-20010101000001.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.973-20010101000001.003-6.4in_v1.svg)


94\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000059.973-20010101000100.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.973-20010101000100.003-6.4in_v1.svg)


95\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005959.973-20010101010000.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.973-20010101010000.003-6.4in_v1.svg)


96\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235959.973-20010102000000.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.973-20010102000000.003-6.4in_v1.svg)


97\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235959.973-20010201000000.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.973-20010201000000.003-6.4in_v1.svg)


98\.

![test/visual_test/latest/20010101000000.0-20010101000000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.04-6.4in_v1.svg)


99\. Cross second boundary

![test/visual_test/latest/20010101000000.964-20010101000001.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.964-20010101000001.004-6.4in_v1.svg)


100\. Cross minute boundary

![test/visual_test/latest/20010101000059.964-20010101000100.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.964-20010101000100.004-6.4in_v1.svg)


101\. Cross hour boundary

![test/visual_test/latest/20010101005959.964-20010101010000.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.964-20010101010000.004-6.4in_v1.svg)


102\. Cross day boundary

![test/visual_test/latest/20010101235959.964-20010102000000.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.964-20010102000000.004-6.4in_v1.svg)


103\. Cross month boundary

![test/visual_test/latest/20010131235959.964-20010201000000.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.964-20010201000000.004-6.4in_v1.svg)


104\.

![test/visual_test/latest/20010101000000.0-20010101000000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.05-6.4in_v1.svg)


105\. Cross second boundary

![test/visual_test/latest/20010101000000.955-20010101000001.005-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.955-20010101000001.005-6.4in_v1.svg)


106\. Cross minute boundary

![test/visual_test/latest/20010101000059.955-20010101000100.005-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.955-20010101000100.005-6.4in_v1.svg)


107\. Cross hour boundary

![test/visual_test/latest/20010101005959.955-20010101010000.005-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.955-20010101010000.005-6.4in_v1.svg)


108\. Cross day boundary

![test/visual_test/latest/20010101235959.955-20010102000000.005-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.955-20010102000000.005-6.4in_v1.svg)


109\. Cross month boundary

![test/visual_test/latest/20010131235959.955-20010201000000.005-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.955-20010201000000.005-6.4in_v1.svg)


110\.

![test/visual_test/latest/20010101000000.0-20010101000000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.06-6.4in_v1.svg)


111\. Cross second boundary

![test/visual_test/latest/20010101000000.946-20010101000001.006-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.946-20010101000001.006-6.4in_v1.svg)


112\. Cross minute boundary

![test/visual_test/latest/20010101000059.946-20010101000100.006-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.946-20010101000100.006-6.4in_v1.svg)


113\. Cross hour boundary

![test/visual_test/latest/20010101005959.946-20010101010000.006-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.946-20010101010000.006-6.4in_v1.svg)


114\. Cross day boundary

![test/visual_test/latest/20010101235959.946-20010102000000.006-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.946-20010102000000.006-6.4in_v1.svg)


115\. Cross month boundary

![test/visual_test/latest/20010131235959.946-20010201000000.006-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.946-20010201000000.006-6.4in_v1.svg)


116\.

![test/visual_test/latest/20010101000000.0-20010101000000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.07-6.4in_v1.svg)


117\. Cross second boundary

![test/visual_test/latest/20010101000000.937-20010101000001.007-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.937-20010101000001.007-6.4in_v1.svg)


118\. Cross minute boundary

![test/visual_test/latest/20010101000059.937-20010101000100.007-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.937-20010101000100.007-6.4in_v1.svg)


119\. Cross hour boundary

![test/visual_test/latest/20010101005959.937-20010101010000.007-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.937-20010101010000.007-6.4in_v1.svg)


120\. Cross day boundary

![test/visual_test/latest/20010101235959.937-20010102000000.007-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.937-20010102000000.007-6.4in_v1.svg)


121\. Cross month boundary

![test/visual_test/latest/20010131235959.937-20010201000000.007-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.937-20010201000000.007-6.4in_v1.svg)


122\.

![test/visual_test/latest/20010101000000.0-20010101000000.08-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.08-6.4in_v1.svg)


123\. Cross second boundary

![test/visual_test/latest/20010101000000.928-20010101000001.008-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.928-20010101000001.008-6.4in_v1.svg)


124\. Cross minute boundary

![test/visual_test/latest/20010101000059.928-20010101000100.008-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.928-20010101000100.008-6.4in_v1.svg)


125\. Cross hour boundary

![test/visual_test/latest/20010101005959.928-20010101010000.008-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.928-20010101010000.008-6.4in_v1.svg)


126\. Cross day boundary

![test/visual_test/latest/20010101235959.928-20010102000000.008-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.928-20010102000000.008-6.4in_v1.svg)


127\. Cross month boundary

![test/visual_test/latest/20010131235959.928-20010201000000.008-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.928-20010201000000.008-6.4in_v1.svg)


128\.

![test/visual_test/latest/20010101000000.0-20010101000000.09-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.09-6.4in_v1.svg)


129\. Cross second boundary

![test/visual_test/latest/20010101000000.919-20010101000001.009-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.919-20010101000001.009-6.4in_v1.svg)


130\. Cross minute boundary

![test/visual_test/latest/20010101000059.919-20010101000100.009-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.919-20010101000100.009-6.4in_v1.svg)


131\. Cross hour boundary

![test/visual_test/latest/20010101005959.919-20010101010000.009-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.919-20010101010000.009-6.4in_v1.svg)


132\. Cross day boundary

![test/visual_test/latest/20010101235959.919-20010102000000.009-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.919-20010102000000.009-6.4in_v1.svg)


133\. Cross month boundary

![test/visual_test/latest/20010131235959.919-20010201000000.009-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.919-20010201000000.009-6.4in_v1.svg)


134\.

![test/visual_test/latest/20010101000000.0-20010101000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.1-6.4in_v1.svg)


135\. Cross second boundary

![test/visual_test/latest/20010101000000.91-20010101000001.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.91-20010101000001.01-6.4in_v1.svg)


136\. Cross minute boundary

![test/visual_test/latest/20010101000059.91-20010101000100.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.91-20010101000100.01-6.4in_v1.svg)


137\. Cross hour boundary

![test/visual_test/latest/20010101005959.91-20010101010000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.91-20010101010000.01-6.4in_v1.svg)


138\. Cross day boundary

![test/visual_test/latest/20010101235959.91-20010102000000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.91-20010102000000.01-6.4in_v1.svg)


139\. Cross month boundary

![test/visual_test/latest/20010131235959.91-20010201000000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.91-20010201000000.01-6.4in_v1.svg)


140\.

![test/visual_test/latest/20010101000000.0-20010101000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.125-6.4in_v1.svg)


141\. Cross second boundary

![test/visual_test/latest/20010101000000.8875-20010101000001.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.8875-20010101000001.0125-6.4in_v1.svg)


142\. Cross minute boundary

![test/visual_test/latest/20010101000059.8875-20010101000100.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.8875-20010101000100.0125-6.4in_v1.svg)


143\. Cross hour boundary

![test/visual_test/latest/20010101005959.8875-20010101010000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.8875-20010101010000.0125-6.4in_v1.svg)


144\. Cross day boundary

![test/visual_test/latest/20010101235959.8875-20010102000000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.8875-20010102000000.0125-6.4in_v1.svg)


145\. Cross month boundary

![test/visual_test/latest/20010131235959.8875-20010201000000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.8875-20010201000000.0125-6.4in_v1.svg)


146\.

![test/visual_test/latest/20010101000000.0-20010101000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.15-6.4in_v1.svg)


147\. Cross second boundary

![test/visual_test/latest/20010101000000.865-20010101000001.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.865-20010101000001.015-6.4in_v1.svg)


148\. Cross minute boundary

![test/visual_test/latest/20010101000059.865-20010101000100.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.865-20010101000100.015-6.4in_v1.svg)


149\. Cross hour boundary

![test/visual_test/latest/20010101005959.865-20010101010000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.865-20010101010000.015-6.4in_v1.svg)


150\. Cross day boundary

![test/visual_test/latest/20010101235959.865-20010102000000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.865-20010102000000.015-6.4in_v1.svg)


151\. Cross month boundary

![test/visual_test/latest/20010131235959.865-20010201000000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.865-20010201000000.015-6.4in_v1.svg)


152\.

![test/visual_test/latest/20010101000000.0-20010101000000.175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.175-6.4in_v1.svg)


153\. Cross second boundary

![test/visual_test/latest/20010101000000.8425-20010101000001.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.8425-20010101000001.0175-6.4in_v1.svg)


154\. Cross minute boundary

![test/visual_test/latest/20010101000059.8425-20010101000100.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.8425-20010101000100.0175-6.4in_v1.svg)


155\. Cross hour boundary

![test/visual_test/latest/20010101005959.8425-20010101010000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.8425-20010101010000.0175-6.4in_v1.svg)


156\. Cross day boundary

![test/visual_test/latest/20010101235959.8425-20010102000000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.8425-20010102000000.0175-6.4in_v1.svg)


157\. Cross month boundary

![test/visual_test/latest/20010131235959.8425-20010201000000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.8425-20010201000000.0175-6.4in_v1.svg)


158\.

![test/visual_test/latest/20010101000000.0-20010101000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.2-6.4in_v1.svg)


159\. Cross second boundary

![test/visual_test/latest/20010101000000.82-20010101000001.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.82-20010101000001.02-6.4in_v1.svg)


160\. Cross minute boundary

![test/visual_test/latest/20010101000059.82-20010101000100.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.82-20010101000100.02-6.4in_v1.svg)


161\. Cross hour boundary

![test/visual_test/latest/20010101005959.82-20010101010000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.82-20010101010000.02-6.4in_v1.svg)


162\. Cross day boundary

![test/visual_test/latest/20010101235959.82-20010102000000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.82-20010102000000.02-6.4in_v1.svg)


163\. Cross month boundary

![test/visual_test/latest/20010131235959.82-20010201000000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.82-20010201000000.02-6.4in_v1.svg)


164\.

![test/visual_test/latest/20010101000000.0-20010101000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.25-6.4in_v1.svg)


165\. Cross second boundary

![test/visual_test/latest/20010101000000.775-20010101000001.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.775-20010101000001.025-6.4in_v1.svg)


166\. Cross minute boundary

![test/visual_test/latest/20010101000059.775-20010101000100.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.775-20010101000100.025-6.4in_v1.svg)


167\. Cross hour boundary

![test/visual_test/latest/20010101005959.775-20010101010000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.775-20010101010000.025-6.4in_v1.svg)


168\. Cross day boundary

![test/visual_test/latest/20010101235959.775-20010102000000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.775-20010102000000.025-6.4in_v1.svg)


169\. Cross month boundary

![test/visual_test/latest/20010131235959.775-20010201000000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.775-20010201000000.025-6.4in_v1.svg)


170\.

![test/visual_test/latest/20010101000000.0-20010101000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.3-6.4in_v1.svg)


171\. Cross second boundary

![test/visual_test/latest/20010101000000.73-20010101000001.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.73-20010101000001.03-6.4in_v1.svg)


172\. Cross minute boundary

![test/visual_test/latest/20010101000059.73-20010101000100.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.73-20010101000100.03-6.4in_v1.svg)


173\. Cross hour boundary

![test/visual_test/latest/20010101005959.73-20010101010000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.73-20010101010000.03-6.4in_v1.svg)


174\. Cross day boundary

![test/visual_test/latest/20010101235959.73-20010102000000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.73-20010102000000.03-6.4in_v1.svg)


175\. Cross month boundary

![test/visual_test/latest/20010131235959.73-20010201000000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.73-20010201000000.03-6.4in_v1.svg)


176\.

![test/visual_test/latest/20010101000000.0-20010101000000.35-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.35-6.4in_v1.svg)


177\. Cross second boundary

![test/visual_test/latest/20010101000000.685-20010101000001.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.685-20010101000001.035-6.4in_v1.svg)


178\. Cross minute boundary

![test/visual_test/latest/20010101000059.685-20010101000100.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.685-20010101000100.035-6.4in_v1.svg)


179\. Cross hour boundary

![test/visual_test/latest/20010101005959.685-20010101010000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.685-20010101010000.035-6.4in_v1.svg)


180\. Cross day boundary

![test/visual_test/latest/20010101235959.685-20010102000000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.685-20010102000000.035-6.4in_v1.svg)


181\. Cross month boundary

![test/visual_test/latest/20010131235959.685-20010201000000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.685-20010201000000.035-6.4in_v1.svg)


182\.

![test/visual_test/latest/20010101000000.0-20010101000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.4-6.4in_v1.svg)


183\. Cross second boundary

![test/visual_test/latest/20010101000000.64-20010101000001.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.64-20010101000001.04-6.4in_v1.svg)


184\. Cross minute boundary

![test/visual_test/latest/20010101000059.64-20010101000100.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.64-20010101000100.04-6.4in_v1.svg)


185\. Cross hour boundary

![test/visual_test/latest/20010101005959.64-20010101010000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.64-20010101010000.04-6.4in_v1.svg)


186\. Cross day boundary

![test/visual_test/latest/20010101235959.64-20010102000000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.64-20010102000000.04-6.4in_v1.svg)


187\. Cross month boundary

![test/visual_test/latest/20010131235959.64-20010201000000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.64-20010201000000.04-6.4in_v1.svg)


188\.

![test/visual_test/latest/20010101000000.0-20010101000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.5-6.4in_v1.svg)


189\. Cross second boundary

![test/visual_test/latest/20010101000000.55-20010101000001.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.55-20010101000001.05-6.4in_v1.svg)


190\. Cross minute boundary

![test/visual_test/latest/20010101000059.55-20010101000100.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.55-20010101000100.05-6.4in_v1.svg)


191\. Cross hour boundary

![test/visual_test/latest/20010101005959.55-20010101010000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.55-20010101010000.05-6.4in_v1.svg)


192\. Cross day boundary

![test/visual_test/latest/20010101235959.55-20010102000000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.55-20010102000000.05-6.4in_v1.svg)


193\. Cross month boundary

![test/visual_test/latest/20010131235959.55-20010201000000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.55-20010201000000.05-6.4in_v1.svg)


194\.

![test/visual_test/latest/20010101000000.0-20010101000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.6-6.4in_v1.svg)


195\. Cross second boundary

![test/visual_test/latest/20010101000000.46-20010101000001.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.46-20010101000001.06-6.4in_v1.svg)


196\. Cross minute boundary

![test/visual_test/latest/20010101000059.46-20010101000100.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.46-20010101000100.06-6.4in_v1.svg)


197\. Cross hour boundary

![test/visual_test/latest/20010101005959.46-20010101010000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.46-20010101010000.06-6.4in_v1.svg)


198\. Cross day boundary

![test/visual_test/latest/20010101235959.46-20010102000000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.46-20010102000000.06-6.4in_v1.svg)


199\. Cross month boundary

![test/visual_test/latest/20010131235959.46-20010201000000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.46-20010201000000.06-6.4in_v1.svg)


200\.

![test/visual_test/latest/20010101000000.0-20010101000000.7-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.7-6.4in_v1.svg)


201\. Cross second boundary

![test/visual_test/latest/20010101000000.37-20010101000001.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.37-20010101000001.07-6.4in_v1.svg)


202\. Cross minute boundary

![test/visual_test/latest/20010101000059.37-20010101000100.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.37-20010101000100.07-6.4in_v1.svg)


203\. Cross hour boundary

![test/visual_test/latest/20010101005959.37-20010101010000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.37-20010101010000.07-6.4in_v1.svg)


204\. Cross day boundary

![test/visual_test/latest/20010101235959.37-20010102000000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.37-20010102000000.07-6.4in_v1.svg)


205\. Cross month boundary

![test/visual_test/latest/20010131235959.37-20010201000000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.37-20010201000000.07-6.4in_v1.svg)


206\.

![test/visual_test/latest/20010101000000.0-20010101000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.0-6.4in_v1.svg)


207\. Cross minute boundary

![test/visual_test/latest/20010101000059.1-20010101000100.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.1-20010101000100.1-6.4in_v1.svg)


208\. Cross hour boundary

![test/visual_test/latest/20010101005959.1-20010101010000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.1-20010101010000.1-6.4in_v1.svg)


209\. Cross day boundary

![test/visual_test/latest/20010101235959.1-20010102000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.1-20010102000000.1-6.4in_v1.svg)


210\. Cross month boundary

![test/visual_test/latest/20010131235959.1-20010201000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.1-20010201000000.1-6.4in_v1.svg)


211\.

![test/visual_test/latest/20010101000000.0-20010101000001.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.25-6.4in_v1.svg)


212\. Cross minute boundary

![test/visual_test/latest/20010101000058.875-20010101000100.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.875-20010101000100.125-6.4in_v1.svg)


213\. Cross hour boundary

![test/visual_test/latest/20010101005958.875-20010101010000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.875-20010101010000.125-6.4in_v1.svg)


214\. Cross day boundary

![test/visual_test/latest/20010101235958.875-20010102000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.875-20010102000000.125-6.4in_v1.svg)


215\. Cross month boundary

![test/visual_test/latest/20010131235958.875-20010201000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.875-20010201000000.125-6.4in_v1.svg)


216\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000001.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.5-6.4in_v1.svg)


217\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000058.65-20010101000100.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.65-20010101000100.15-6.4in_v1.svg)


218\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005958.65-20010101010000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.65-20010101010000.15-6.4in_v1.svg)


219\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235958.65-20010102000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.65-20010102000000.15-6.4in_v1.svg)


220\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235958.65-20010201000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.65-20010201000000.15-6.4in_v1.svg)


221\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.0-6.4in_v1.svg)


222\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000058.2-20010101000100.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.2-20010101000100.2-6.4in_v1.svg)


223\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005958.2-20010101010000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.2-20010101010000.2-6.4in_v1.svg)


224\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235958.2-20010102000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.2-20010102000000.2-6.4in_v1.svg)


225\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235958.2-20010201000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.2-20010201000000.2-6.4in_v1.svg)


226\.

![test/visual_test/latest/20010101000000.0-20010101000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.5-6.4in_v1.svg)


227\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000057.75-20010101000100.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.75-20010101000100.25-6.4in_v1.svg)


228\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005957.75-20010101010000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.75-20010101010000.25-6.4in_v1.svg)


229\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235957.75-20010102000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.75-20010102000000.25-6.4in_v1.svg)


230\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235957.75-20010201000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.75-20010201000000.25-6.4in_v1.svg)


231\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000003.0-6.4in_v1.svg)


232\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000057.3-20010101000100.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.3-20010101000100.3-6.4in_v1.svg)


233\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005957.3-20010101010000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.3-20010101010000.3-6.4in_v1.svg)


234\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235957.3-20010102000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.3-20010102000000.3-6.4in_v1.svg)


235\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235957.3-20010201000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.3-20010201000000.3-6.4in_v1.svg)


236\.

![test/visual_test/latest/20010101000000.0-20010101000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000004.0-6.4in_v1.svg)


237\. Cross minute boundary

![test/visual_test/latest/20010101000056.4-20010101000100.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000056.4-20010101000100.4-6.4in_v1.svg)


238\. Cross hour boundary

![test/visual_test/latest/20010101005956.4-20010101010000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956.4-20010101010000.4-6.4in_v1.svg)


239\. Cross day boundary

![test/visual_test/latest/20010101235956.4-20010102000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956.4-20010102000000.4-6.4in_v1.svg)


240\. Cross month boundary

![test/visual_test/latest/20010131235956.4-20010201000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235956.4-20010201000000.4-6.4in_v1.svg)


241\.

![test/visual_test/latest/20010101000000.0-20010101000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000005.0-6.4in_v1.svg)


242\. Cross minute boundary

![test/visual_test/latest/20010101000055.5-20010101000100.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000055.5-20010101000100.5-6.4in_v1.svg)


243\. Cross hour boundary

![test/visual_test/latest/20010101005955.5-20010101010000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005955.5-20010101010000.5-6.4in_v1.svg)


244\. Cross day boundary

![test/visual_test/latest/20010101235955.5-20010102000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235955.5-20010102000000.5-6.4in_v1.svg)


245\. Cross month boundary

![test/visual_test/latest/20010131235955.5-20010201000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235955.5-20010201000000.5-6.4in_v1.svg)


246\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000006.0-6.4in_v1.svg)


247\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000054.6-20010101000100.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000054.6-20010101000100.6-6.4in_v1.svg)


248\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005954.6-20010101010000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005954.6-20010101010000.6-6.4in_v1.svg)


249\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235954.6-20010102000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235954.6-20010102000000.6-6.4in_v1.svg)


250\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235954.6-20010201000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235954.6-20010201000000.6-6.4in_v1.svg)


251\.

![test/visual_test/latest/20010101000000.0-20010101000008.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000008.0-6.4in_v1.svg)


252\. Cross minute boundary

![test/visual_test/latest/20010101000052.8-20010101000100.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000052.8-20010101000100.8-6.4in_v1.svg)


253\. Cross hour boundary

![test/visual_test/latest/20010101005952.8-20010101010000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005952.8-20010101010000.8-6.4in_v1.svg)


254\. Cross day boundary

![test/visual_test/latest/20010101235952.8-20010102000000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235952.8-20010102000000.8-6.4in_v1.svg)


255\. Cross month boundary

![test/visual_test/latest/20010131235952.8-20010201000000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235952.8-20010201000000.8-6.4in_v1.svg)


256\.

![test/visual_test/latest/20010101000000.0-20010101000010.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000010.0-6.4in_v1.svg)


257\. Cross minute boundary

![test/visual_test/latest/20010101000051.0-20010101000101.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000051.0-20010101000101.0-6.4in_v1.svg)


258\. Cross hour boundary

![test/visual_test/latest/20010101005951.0-20010101010001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005951.0-20010101010001.0-6.4in_v1.svg)


259\. Cross day boundary

![test/visual_test/latest/20010101235951.0-20010102000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235951.0-20010102000001.0-6.4in_v1.svg)


260\. Cross month boundary

![test/visual_test/latest/20010131235951.0-20010201000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235951.0-20010201000001.0-6.4in_v1.svg)


261\.

![test/visual_test/latest/20010101000000.0-20010101000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000012.0-6.4in_v1.svg)


262\. Cross minute boundary

![test/visual_test/latest/20010101000049.2-20010101000101.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000049.2-20010101000101.2-6.4in_v1.svg)


263\. Cross hour boundary

![test/visual_test/latest/20010101005949.2-20010101010001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005949.2-20010101010001.2-6.4in_v1.svg)


264\. Cross day boundary

![test/visual_test/latest/20010101235949.2-20010102000001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235949.2-20010102000001.2-6.4in_v1.svg)


265\. Cross month boundary

![test/visual_test/latest/20010131235949.2-20010201000001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235949.2-20010201000001.2-6.4in_v1.svg)


266\.

![test/visual_test/latest/20010101000000.0-20010101000014.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000014.0-6.4in_v1.svg)


267\. Cross minute boundary

![test/visual_test/latest/20010101000047.4-20010101000101.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000047.4-20010101000101.4-6.4in_v1.svg)


268\. Cross hour boundary

![test/visual_test/latest/20010101005947.4-20010101010001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005947.4-20010101010001.4-6.4in_v1.svg)


269\. Cross day boundary

![test/visual_test/latest/20010101235947.4-20010102000001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235947.4-20010102000001.4-6.4in_v1.svg)


270\. Cross month boundary

![test/visual_test/latest/20010131235947.4-20010201000001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235947.4-20010201000001.4-6.4in_v1.svg)


271\.

![test/visual_test/latest/20010101000000.0-20010101000016.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000016.0-6.4in_v1.svg)


272\. Cross minute boundary

![test/visual_test/latest/20010101000045.6-20010101000101.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000045.6-20010101000101.6-6.4in_v1.svg)


273\. Cross hour boundary

![test/visual_test/latest/20010101005945.6-20010101010001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005945.6-20010101010001.6-6.4in_v1.svg)


274\. Cross day boundary

![test/visual_test/latest/20010101235945.6-20010102000001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235945.6-20010102000001.6-6.4in_v1.svg)


275\. Cross month boundary

![test/visual_test/latest/20010131235945.6-20010201000001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235945.6-20010201000001.6-6.4in_v1.svg)


276\. (rule change: 1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000018.0-6.4in_v1.svg)


277\. Cross minute boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101000043.8-20010101000101.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000043.8-20010101000101.8-6.4in_v1.svg)


278\. Cross hour boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101005943.8-20010101010001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005943.8-20010101010001.8-6.4in_v1.svg)


279\. Cross day boundary (rule change: 1 reverted)

![test/visual_test/latest/20010101235943.8-20010102000001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235943.8-20010102000001.8-6.4in_v1.svg)


280\. Cross month boundary (rule change: 1 reverted)

![test/visual_test/latest/20010131235943.8-20010201000001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235943.8-20010201000001.8-6.4in_v1.svg)


281\.

![test/visual_test/latest/20010101000000.0-20010101000020.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000020.0-6.4in_v1.svg)


282\. Cross minute boundary

![test/visual_test/latest/20010101000042.0-20010101000102.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000042.0-20010101000102.0-6.4in_v1.svg)


283\. Cross hour boundary

![test/visual_test/latest/20010101005942.0-20010101010002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005942.0-20010101010002.0-6.4in_v1.svg)


284\. Cross day boundary

![test/visual_test/latest/20010101235942.0-20010102000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235942.0-20010102000002.0-6.4in_v1.svg)


285\. Cross month boundary

![test/visual_test/latest/20010131235942.0-20010201000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235942.0-20010201000002.0-6.4in_v1.svg)


286\.

![test/visual_test/latest/20010101000000.0-20010101000025.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000025.0-6.4in_v1.svg)


287\. Cross minute boundary

![test/visual_test/latest/20010101000037.5-20010101000102.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000037.5-20010101000102.5-6.4in_v1.svg)


288\. Cross hour boundary

![test/visual_test/latest/20010101005937.5-20010101010002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005937.5-20010101010002.5-6.4in_v1.svg)


289\. Cross day boundary

![test/visual_test/latest/20010101235937.5-20010102000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235937.5-20010102000002.5-6.4in_v1.svg)


290\. Cross month boundary

![test/visual_test/latest/20010131235937.5-20010201000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235937.5-20010201000002.5-6.4in_v1.svg)


291\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000030.0-6.4in_v1.svg)


292\. Cross minute boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101000033.0-20010101000103.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000033.0-20010101000103.0-6.4in_v1.svg)


293\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101005933.0-20010101010003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005933.0-20010101010003.0-6.4in_v1.svg)


294\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101235933.0-20010102000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235933.0-20010102000003.0-6.4in_v1.svg)


295\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131235933.0-20010201000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235933.0-20010201000003.0-6.4in_v1.svg)


296\.

![test/visual_test/latest/20010101000000.0-20010101000040.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000040.0-6.4in_v1.svg)


297\. Cross minute boundary

![test/visual_test/latest/20010101000024.0-20010101000104.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000024.0-20010101000104.0-6.4in_v1.svg)


298\. Cross hour boundary

![test/visual_test/latest/20010101005924.0-20010101010004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005924.0-20010101010004.0-6.4in_v1.svg)


299\. Cross day boundary

![test/visual_test/latest/20010101235924.0-20010102000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235924.0-20010102000004.0-6.4in_v1.svg)


300\. Cross month boundary

![test/visual_test/latest/20010131235924.0-20010201000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235924.0-20010201000004.0-6.4in_v1.svg)


301\.

![test/visual_test/latest/20010101000000.0-20010101000050.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000050.0-6.4in_v1.svg)


302\. Cross minute boundary

![test/visual_test/latest/20010101000015.0-20010101000105.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000015.0-20010101000105.0-6.4in_v1.svg)


303\. Cross hour boundary

![test/visual_test/latest/20010101005915.0-20010101010005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005915.0-20010101010005.0-6.4in_v1.svg)


304\. Cross day boundary

![test/visual_test/latest/20010101235915.0-20010102000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235915.0-20010102000005.0-6.4in_v1.svg)


305\. Cross month boundary

![test/visual_test/latest/20010131235915.0-20010201000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235915.0-20010201000005.0-6.4in_v1.svg)


306\.

![test/visual_test/latest/20010101000000.0-20010101000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000100.0-6.4in_v1.svg)


307\. Cross hour boundary

![test/visual_test/latest/20010101005906.0-20010101010006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005906.0-20010101010006.0-6.4in_v1.svg)


308\. Cross day boundary

![test/visual_test/latest/20010101235906.0-20010102000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235906.0-20010102000006.0-6.4in_v1.svg)


309\. Cross month boundary

![test/visual_test/latest/20010131235906.0-20010201000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235906.0-20010201000006.0-6.4in_v1.svg)


310\.

![test/visual_test/latest/20010101000000.0-20010101000110.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000110.0-6.4in_v1.svg)


311\. Cross hour boundary

![test/visual_test/latest/20010101005857.0-20010101010007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005857.0-20010101010007.0-6.4in_v1.svg)


312\. Cross day boundary

![test/visual_test/latest/20010101235857.0-20010102000007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235857.0-20010102000007.0-6.4in_v1.svg)


313\. Cross month boundary

![test/visual_test/latest/20010131235857.0-20010201000007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235857.0-20010201000007.0-6.4in_v1.svg)


314\.

![test/visual_test/latest/20010101000000.0-20010101000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000200.0-6.4in_v1.svg)


315\. Cross hour boundary

![test/visual_test/latest/20010101005812.0-20010101010012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005812.0-20010101010012.0-6.4in_v1.svg)


316\. Cross day boundary

![test/visual_test/latest/20010101235812.0-20010102000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235812.0-20010102000012.0-6.4in_v1.svg)


317\. Cross month boundary

![test/visual_test/latest/20010131235812.0-20010201000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235812.0-20010201000012.0-6.4in_v1.svg)


318\.

![test/visual_test/latest/20010101000000.0-20010101000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000230.0-6.4in_v1.svg)


319\. Cross hour boundary

![test/visual_test/latest/20010101005745.0-20010101010015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005745.0-20010101010015.0-6.4in_v1.svg)


320\. Cross day boundary

![test/visual_test/latest/20010101235745.0-20010102000015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235745.0-20010102000015.0-6.4in_v1.svg)


321\. Cross month boundary

![test/visual_test/latest/20010131235745.0-20010201000015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235745.0-20010201000015.0-6.4in_v1.svg)


322\.

![test/visual_test/latest/20010101000000.0-20010101000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000300.0-6.4in_v1.svg)


323\. Cross hour boundary

![test/visual_test/latest/20010101005718.0-20010101010018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005718.0-20010101010018.0-6.4in_v1.svg)


324\. Cross day boundary

![test/visual_test/latest/20010101235718.0-20010102000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235718.0-20010102000018.0-6.4in_v1.svg)


325\. Cross month boundary

![test/visual_test/latest/20010131235718.0-20010201000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235718.0-20010201000018.0-6.4in_v1.svg)


326\.

![test/visual_test/latest/20010101000000.0-20010101000330.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000330.0-6.4in_v1.svg)


327\. Cross hour boundary

![test/visual_test/latest/20010101005651.0-20010101010021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005651.0-20010101010021.0-6.4in_v1.svg)


328\. Cross day boundary

![test/visual_test/latest/20010101235651.0-20010102000021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235651.0-20010102000021.0-6.4in_v1.svg)


329\. Cross month boundary

![test/visual_test/latest/20010131235651.0-20010201000021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235651.0-20010201000021.0-6.4in_v1.svg)


330\.

![test/visual_test/latest/20010101000000.0-20010101000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000400.0-6.4in_v1.svg)


331\. Cross hour boundary

![test/visual_test/latest/20010101005624.0-20010101010024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005624.0-20010101010024.0-6.4in_v1.svg)


332\. Cross day boundary

![test/visual_test/latest/20010101235624.0-20010102000024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235624.0-20010102000024.0-6.4in_v1.svg)


333\. Cross month boundary

![test/visual_test/latest/20010131235624.0-20010201000024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235624.0-20010201000024.0-6.4in_v1.svg)


334\.

![test/visual_test/latest/20010101000000.0-20010101000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000500.0-6.4in_v1.svg)


335\. Cross hour boundary

![test/visual_test/latest/20010101005530.0-20010101010030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005530.0-20010101010030.0-6.4in_v1.svg)


336\. Cross day boundary

![test/visual_test/latest/20010101235530.0-20010102000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235530.0-20010102000030.0-6.4in_v1.svg)


337\. Cross month boundary

![test/visual_test/latest/20010131235530.0-20010201000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235530.0-20010201000030.0-6.4in_v1.svg)


338\.

![test/visual_test/latest/20010101000000.0-20010101000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000600.0-6.4in_v1.svg)


339\. Cross hour boundary

![test/visual_test/latest/20010101005436.0-20010101010036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005436.0-20010101010036.0-6.4in_v1.svg)


340\. Cross day boundary

![test/visual_test/latest/20010101235436.0-20010102000036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235436.0-20010102000036.0-6.4in_v1.svg)


341\. Cross month boundary

![test/visual_test/latest/20010131235436.0-20010201000036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235436.0-20010201000036.0-6.4in_v1.svg)


342\.

![test/visual_test/latest/20010101000000.0-20010101000700.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000700.0-6.4in_v1.svg)


343\. Cross hour boundary

![test/visual_test/latest/20010101005342.0-20010101010042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005342.0-20010101010042.0-6.4in_v1.svg)


344\. Cross day boundary

![test/visual_test/latest/20010101235342.0-20010102000042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235342.0-20010102000042.0-6.4in_v1.svg)


345\. Cross month boundary

![test/visual_test/latest/20010131235342.0-20010201000042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235342.0-20010201000042.0-6.4in_v1.svg)


346\.

![test/visual_test/latest/20010101000000.0-20010101000800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000800.0-6.4in_v1.svg)


347\. Cross hour boundary

![test/visual_test/latest/20010101005248.0-20010101010048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005248.0-20010101010048.0-6.4in_v1.svg)


348\. Cross day boundary

![test/visual_test/latest/20010101235248.0-20010102000048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235248.0-20010102000048.0-6.4in_v1.svg)


349\. Cross month boundary

![test/visual_test/latest/20010131235248.0-20010201000048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235248.0-20010201000048.0-6.4in_v1.svg)


350\.

![test/visual_test/latest/20010101000000.0-20010101001000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001000.0-6.4in_v1.svg)


351\. Cross hour boundary

![test/visual_test/latest/20010101005100.0-20010101010100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005100.0-20010101010100.0-6.4in_v1.svg)


352\. Cross day boundary

![test/visual_test/latest/20010101235100.0-20010102000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235100.0-20010102000100.0-6.4in_v1.svg)


353\. Cross month boundary

![test/visual_test/latest/20010131235100.0-20010201000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235100.0-20010201000100.0-6.4in_v1.svg)


354\.

![test/visual_test/latest/20010101000000.0-20010101001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001200.0-6.4in_v1.svg)


355\. Cross hour boundary

![test/visual_test/latest/20010101004912.0-20010101010112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004912.0-20010101010112.0-6.4in_v1.svg)


356\. Cross day boundary

![test/visual_test/latest/20010101234912.0-20010102000112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234912.0-20010102000112.0-6.4in_v1.svg)


357\. Cross month boundary

![test/visual_test/latest/20010131234912.0-20010201000112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234912.0-20010201000112.0-6.4in_v1.svg)


358\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001500.0-6.4in_v1.svg)


359\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101004630.0-20010101010130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004630.0-20010101010130.0-6.4in_v1.svg)


360\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101234630.0-20010102000130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234630.0-20010102000130.0-6.4in_v1.svg)


361\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131234630.0-20010201000130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234630.0-20010201000130.0-6.4in_v1.svg)


362\.

![test/visual_test/latest/20010101000000.0-20010101002000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002000.0-6.4in_v1.svg)


363\. Cross hour boundary

![test/visual_test/latest/20010101004200.0-20010101010200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004200.0-20010101010200.0-6.4in_v1.svg)


364\. Cross day boundary

![test/visual_test/latest/20010101234200.0-20010102000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234200.0-20010102000200.0-6.4in_v1.svg)


365\. Cross month boundary

![test/visual_test/latest/20010131234200.0-20010201000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234200.0-20010201000200.0-6.4in_v1.svg)


366\.

![test/visual_test/latest/20010101000000.0-20010101002500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002500.0-6.4in_v1.svg)


367\. Cross hour boundary

![test/visual_test/latest/20010101003730.0-20010101010230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003730.0-20010101010230.0-6.4in_v1.svg)


368\. Cross day boundary

![test/visual_test/latest/20010101233730.0-20010102000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233730.0-20010102000230.0-6.4in_v1.svg)


369\. Cross month boundary

![test/visual_test/latest/20010131233730.0-20010201000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233730.0-20010201000230.0-6.4in_v1.svg)


370\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101003000.0-6.4in_v1.svg)


371\. Cross hour boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101003300.0-20010101010300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003300.0-20010101010300.0-6.4in_v1.svg)


372\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101233300.0-20010102000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233300.0-20010102000300.0-6.4in_v1.svg)


373\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131233300.0-20010201000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233300.0-20010201000300.0-6.4in_v1.svg)


374\.

![test/visual_test/latest/20010101000000.0-20010101004000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101004000.0-6.4in_v1.svg)


375\. Cross hour boundary

![test/visual_test/latest/20010101002400.0-20010101010400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101002400.0-20010101010400.0-6.4in_v1.svg)


376\. Cross day boundary

![test/visual_test/latest/20010101232400.0-20010102000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101232400.0-20010102000400.0-6.4in_v1.svg)


377\. Cross month boundary

![test/visual_test/latest/20010131232400.0-20010201000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131232400.0-20010201000400.0-6.4in_v1.svg)


378\.

![test/visual_test/latest/20010101000000.0-20010101005000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101005000.0-6.4in_v1.svg)


379\. Cross hour boundary

![test/visual_test/latest/20010101001500.0-20010101010500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101001500.0-20010101010500.0-6.4in_v1.svg)


380\. Cross day boundary

![test/visual_test/latest/20010101231500.0-20010102000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101231500.0-20010102000500.0-6.4in_v1.svg)


381\. Cross month boundary

![test/visual_test/latest/20010131231500.0-20010201000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131231500.0-20010201000500.0-6.4in_v1.svg)


382\.

![test/visual_test/latest/20010101000000.0-20010101010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101010000.0-6.4in_v1.svg)


383\. Cross day boundary

![test/visual_test/latest/20010101230600.0-20010102000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101230600.0-20010102000600.0-6.4in_v1.svg)


384\. Cross month boundary

![test/visual_test/latest/20010131230600.0-20010201000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131230600.0-20010201000600.0-6.4in_v1.svg)


385\.

![test/visual_test/latest/20010101000000.0-20010101011500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101011500.0-6.4in_v1.svg)


386\. Cross day boundary

![test/visual_test/latest/20010101225230.0-20010102000730.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101225230.0-20010102000730.0-6.4in_v1.svg)


387\. Cross month boundary

![test/visual_test/latest/20010131225230.0-20010201000730.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131225230.0-20010201000730.0-6.4in_v1.svg)


388\.

![test/visual_test/latest/20010101000000.0-20010101013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101013000.0-6.4in_v1.svg)


389\. Cross day boundary

![test/visual_test/latest/20010101223900.0-20010102000900.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101223900.0-20010102000900.0-6.4in_v1.svg)


390\. Cross month boundary

![test/visual_test/latest/20010131223900.0-20010201000900.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131223900.0-20010201000900.0-6.4in_v1.svg)


391\.

![test/visual_test/latest/20010101000000.0-20010101014500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101014500.0-6.4in_v1.svg)


392\. Cross day boundary

![test/visual_test/latest/20010101222530.0-20010102001030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101222530.0-20010102001030.0-6.4in_v1.svg)


393\. Cross month boundary

![test/visual_test/latest/20010131222530.0-20010201001030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131222530.0-20010201001030.0-6.4in_v1.svg)


394\.

![test/visual_test/latest/20010101000000.0-20010101020000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101020000.0-6.4in_v1.svg)


395\. Cross day boundary

![test/visual_test/latest/20010101221200.0-20010102001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101221200.0-20010102001200.0-6.4in_v1.svg)


396\. Cross month boundary

![test/visual_test/latest/20010131221200.0-20010201001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131221200.0-20010201001200.0-6.4in_v1.svg)


397\.

![test/visual_test/latest/20010101000000.0-20010101023000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101023000.0-6.4in_v1.svg)


398\. Cross day boundary

![test/visual_test/latest/20010101214500.0-20010102001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101214500.0-20010102001500.0-6.4in_v1.svg)


399\. Cross month boundary

![test/visual_test/latest/20010131214500.0-20010201001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131214500.0-20010201001500.0-6.4in_v1.svg)


400\.

![test/visual_test/latest/20010101000000.0-20010101030000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101030000.0-6.4in_v1.svg)


401\. Cross day boundary

![test/visual_test/latest/20010101211800.0-20010102001800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101211800.0-20010102001800.0-6.4in_v1.svg)


402\. Cross month boundary

![test/visual_test/latest/20010131211800.0-20010201001800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131211800.0-20010201001800.0-6.4in_v1.svg)


403\.

![test/visual_test/latest/20010101000000.0-20010101033000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101033000.0-6.4in_v1.svg)


404\. Cross day boundary

![test/visual_test/latest/20010101205100.0-20010102002100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101205100.0-20010102002100.0-6.4in_v1.svg)


405\. Cross month boundary

![test/visual_test/latest/20010131205100.0-20010201002100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131205100.0-20010201002100.0-6.4in_v1.svg)


406\.

![test/visual_test/latest/20010101000000.0-20010101040000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101040000.0-6.4in_v1.svg)


407\. Cross day boundary

![test/visual_test/latest/20010101202400.0-20010102002400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101202400.0-20010102002400.0-6.4in_v1.svg)


408\. Cross month boundary

![test/visual_test/latest/20010131202400.0-20010201002400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131202400.0-20010201002400.0-6.4in_v1.svg)


409\.

![test/visual_test/latest/20010101000000.0-20010101050000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101050000.0-6.4in_v1.svg)


410\. Cross day boundary

![test/visual_test/latest/20010101193000.0-20010102003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101193000.0-20010102003000.0-6.4in_v1.svg)


411\. Cross month boundary

![test/visual_test/latest/20010131193000.0-20010201003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131193000.0-20010201003000.0-6.4in_v1.svg)


412\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101060000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101060000.0-6.4in_v1.svg)


413\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101183600.0-20010102003600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101183600.0-20010102003600.0-6.4in_v1.svg)


414\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131183600.0-20010201003600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131183600.0-20010201003600.0-6.4in_v1.svg)


415\.

![test/visual_test/latest/20010101000000.0-20010101080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101080000.0-6.4in_v1.svg)


416\. Cross day boundary

![test/visual_test/latest/20010101164800.0-20010102004800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101164800.0-20010102004800.0-6.4in_v1.svg)


417\. Cross month boundary

![test/visual_test/latest/20010131164800.0-20010201004800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131164800.0-20010201004800.0-6.4in_v1.svg)


418\.

![test/visual_test/latest/20010101000000.0-20010101100000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101100000.0-6.4in_v1.svg)


419\. Cross day boundary

![test/visual_test/latest/20010101150000.0-20010102010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101150000.0-20010102010000.0-6.4in_v1.svg)


420\. Cross month boundary

![test/visual_test/latest/20010131150000.0-20010201010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131150000.0-20010201010000.0-6.4in_v1.svg)


421\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010101120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101120000.0-6.4in_v1.svg)


422\. Cross day boundary (rule change: -1 reverted)

![test/visual_test/latest/20010101131200.0-20010102011200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101131200.0-20010102011200.0-6.4in_v1.svg)


423\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010131131200.0-20010201011200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131131200.0-20010201011200.0-6.4in_v1.svg)


424\.

![test/visual_test/latest/20010101000000.0-20010101150000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101150000.0-6.4in_v1.svg)


425\. Cross day boundary

![test/visual_test/latest/20010101103000.0-20010102013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101103000.0-20010102013000.0-6.4in_v1.svg)


426\. Cross month boundary

![test/visual_test/latest/20010131103000.0-20010201013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131103000.0-20010201013000.0-6.4in_v1.svg)


427\.

![test/visual_test/latest/20010101000000.0-20010101180000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101180000.0-6.4in_v1.svg)


428\. Cross day boundary

![test/visual_test/latest/20010101074800.0-20010102014800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101074800.0-20010102014800.0-6.4in_v1.svg)


429\. Cross month boundary

![test/visual_test/latest/20010131074800.0-20010201014800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131074800.0-20010201014800.0-6.4in_v1.svg)


430\.

![test/visual_test/latest/20010101000000.0-20010101210000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101210000.0-6.4in_v1.svg)


431\. Cross day boundary

![test/visual_test/latest/20010101050600.0-20010102020600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101050600.0-20010102020600.0-6.4in_v1.svg)


432\. Cross month boundary

![test/visual_test/latest/20010131050600.0-20010201020600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131050600.0-20010201020600.0-6.4in_v1.svg)


433\.

![test/visual_test/latest/20010101000000.0-20010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102000000.0-6.4in_v1.svg)


434\. Cross month boundary

![test/visual_test/latest/20010131022400.0-20010201022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131022400.0-20010201022400.0-6.4in_v1.svg)


435\.

![test/visual_test/latest/20010101000000.0-20010102040000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102040000.0-6.4in_v1.svg)


436\. Cross month boundary

![test/visual_test/latest/20010130224800.0-20010201024800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130224800.0-20010201024800.0-6.4in_v1.svg)


437\.

![test/visual_test/latest/20010101000000.0-20010102080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102080000.0-6.4in_v1.svg)


438\. Cross month boundary

![test/visual_test/latest/20010130191200.0-20010201031200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130191200.0-20010201031200.0-6.4in_v1.svg)


439\.

![test/visual_test/latest/20010101000000.0-20010102120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102120000.0-6.4in_v1.svg)


440\. Cross month boundary

![test/visual_test/latest/20010130153600.0-20010201033600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130153600.0-20010201033600.0-6.4in_v1.svg)


441\.

![test/visual_test/latest/20010101000000.0-20010102180000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102180000.0-6.4in_v1.svg)


442\. Cross month boundary

![test/visual_test/latest/20010130101200.0-20010201041200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130101200.0-20010201041200.0-6.4in_v1.svg)


443\.

![test/visual_test/latest/20010101000000.0-20010103000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103000000.0-6.4in_v1.svg)


444\. Cross month boundary

![test/visual_test/latest/20010130044800.0-20010201044800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130044800.0-20010201044800.0-6.4in_v1.svg)


445\.

![test/visual_test/latest/20010101000000.0-20010103080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103080000.0-6.4in_v1.svg)


446\. Cross month boundary

![test/visual_test/latest/20010129213600.0-20010201053600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129213600.0-20010201053600.0-6.4in_v1.svg)


447\.

![test/visual_test/latest/20010101000000.0-20010103160000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103160000.0-6.4in_v1.svg)


448\. Cross month boundary

![test/visual_test/latest/20010129142400.0-20010201062400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129142400.0-20010201062400.0-6.4in_v1.svg)


449\.

![test/visual_test/latest/20010101000000.0-20010104000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104000000.0-6.4in_v1.svg)


450\. Cross month boundary

![test/visual_test/latest/20010129071200.0-20010201071200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129071200.0-20010201071200.0-6.4in_v1.svg)


451\.

![test/visual_test/latest/20010101000000.0-20010104120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104120000.0-6.4in_v1.svg)


452\. Cross month boundary

![test/visual_test/latest/20010128202400.0-20010201082400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128202400.0-20010201082400.0-6.4in_v1.svg)


453\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010105000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010105000000.0-6.4in_v1.svg)


454\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010128093600.0-20010201093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128093600.0-20010201093600.0-6.4in_v1.svg)


455\.

![test/visual_test/latest/20010101000000.0-20010106000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010106000000.0-6.4in_v1.svg)


456\. Cross month boundary

![test/visual_test/latest/20010127120000.0-20010201120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010127120000.0-20010201120000.0-6.4in_v1.svg)


457\.

![test/visual_test/latest/20010101000000.0-20010107000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010107000000.0-6.4in_v1.svg)


458\. Cross month boundary

![test/visual_test/latest/20010126142400.0-20010201142400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010126142400.0-20010201142400.0-6.4in_v1.svg)


459\.

![test/visual_test/latest/20010101000000.0-20010108000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010108000000.0-6.4in_v1.svg)


460\. Cross month boundary

![test/visual_test/latest/20010125164800.0-20010201164800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010125164800.0-20010201164800.0-6.4in_v1.svg)


461\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010109000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010109000000.0-6.4in_v1.svg)


462\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010124191200.0-20010201191200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010124191200.0-20010201191200.0-6.4in_v1.svg)


463\.

![test/visual_test/latest/20010101000000.0-20010111000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010111000000.0-6.4in_v1.svg)


464\. Cross month boundary

![test/visual_test/latest/20010123000000.0-20010202000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010123000000.0-20010202000000.0-6.4in_v1.svg)


465\.

![test/visual_test/latest/20010101000000.0-20010113000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010113000000.0-6.4in_v1.svg)


466\. Cross month boundary

![test/visual_test/latest/20010121044800.0-20010202044800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010121044800.0-20010202044800.0-6.4in_v1.svg)


467\.

![test/visual_test/latest/20010101000000.0-20010115000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010115000000.0-6.4in_v1.svg)


468\. Cross month boundary

![test/visual_test/latest/20010119093600.0-20010202093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010119093600.0-20010202093600.0-6.4in_v1.svg)


469\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010118000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010118000000.0-6.4in_v1.svg)


470\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010116164800.0-20010202164800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010116164800.0-20010202164800.0-6.4in_v1.svg)


471\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010122000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010122000000.0-6.4in_v1.svg)


472\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010113022400.0-20010203022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010113022400.0-20010203022400.0-6.4in_v1.svg)


473\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010125000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010125000000.0-6.4in_v1.svg)


474\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010110093600.0-20010203093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010110093600.0-20010203093600.0-6.4in_v1.svg)


475\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010129000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010129000000.0-6.4in_v1.svg)


476\. Cross month boundary (rule change: -1 reverted)

![test/visual_test/latest/20010106191200.0-20010203191200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010106191200.0-20010203191200.0-6.4in_v1.svg)


477\. (rule change: -2 reverted)

![test/visual_test/latest/20010101000000.0-20010201000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010201000000.0-6.4in_v1.svg)


478\. Cross month boundary (rule change: -2 reverted)

![test/visual_test/latest/20010104022400.0-20010204022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010104022400.0-20010204022400.0-6.4in_v1.svg)


479\.

![test/visual_test/latest/20010101000000.0-20010205000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010205000000.0-6.4in_v1.svg)


480\.

![test/visual_test/latest/20010101000000.0-20010208000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010208000000.0-6.4in_v1.svg)


481\.

![test/visual_test/latest/20010101000000.0-20010215000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010215000000.0-6.4in_v1.svg)


482\.

![test/visual_test/latest/20010101000000.0-20010222000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010222000000.0-6.4in_v1.svg)


483\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010301000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010301000000.0-6.4in_v1.svg)


484\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010303000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010303000000.0-6.4in_v1.svg)


485\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010331000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010331000000.0-6.4in_v1.svg)


486\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010401000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010401000000.0-6.4in_v1.svg)


487\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010402000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010402000000.0-6.4in_v1.svg)


488\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010403000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010403000000.0-6.4in_v1.svg)


489\.

![test/visual_test/latest/20010101000000.0-20010501000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010501000000.0-6.4in_v1.svg)


490\.

![test/visual_test/latest/20010101000000.0-20010503000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010503000000.0-6.4in_v1.svg)


491\.

![test/visual_test/latest/20010101000000.0-20010531000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010531000000.0-6.4in_v1.svg)


492\.

![test/visual_test/latest/20010101000000.0-20010601000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010601000000.0-6.4in_v1.svg)


493\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010701000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010701000000.0-6.4in_v1.svg)


494\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010704000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010704000000.0-6.4in_v1.svg)


495\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20010901000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010901000000.0-6.4in_v1.svg)


496\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20011003000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011003000000.0-6.4in_v1.svg)


497\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20020101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020101000000.0-6.4in_v1.svg)


498\.

![test/visual_test/latest/20010101000000.0-20020401000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020401000000.0-6.4in_v1.svg)


499\.

![test/visual_test/latest/20010101000000.0-20020402000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020402000000.0-6.4in_v1.svg)


500\.

![test/visual_test/latest/20010101000000.0-20020403000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020403000000.0-6.4in_v1.svg)


501\.

![test/visual_test/latest/20010101000000.0-20020701000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020701000000.0-6.4in_v1.svg)


502\.

![test/visual_test/latest/20010101000000.0-20020703000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020703000000.0-6.4in_v1.svg)


503\.

![test/visual_test/latest/20010101000000.0-20020704000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020704000000.0-6.4in_v1.svg)


504\.

![test/visual_test/latest/20010101000000.0-20021001000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021001000000.0-6.4in_v1.svg)


505\.

![test/visual_test/latest/20010101000000.0-20021003000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021003000000.0-6.4in_v1.svg)


506\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20030101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20030101000000.0-6.4in_v1.svg)


507\. (rule change: -2 reverted)

![test/visual_test/latest/20010101000000.0-20040101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040101000000.0-6.4in_v1.svg)


508\. (rule change: -2 reverted)

![test/visual_test/latest/20010101000000.0-20040102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040102000000.0-6.4in_v1.svg)


509\.

![test/visual_test/latest/20010101000000.0-20050101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20050101000000.0-6.4in_v1.svg)


510\.

![test/visual_test/latest/20010101000000.0-20060101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060101000000.0-6.4in_v1.svg)


511\.

![test/visual_test/latest/20010101000000.0-20060102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060102000000.0-6.4in_v1.svg)


512\.

![test/visual_test/latest/20010101000000.0-20070101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070101000000.0-6.4in_v1.svg)


513\.

![test/visual_test/latest/20010101000000.0-20070102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070102000000.0-6.4in_v1.svg)


514\.

![test/visual_test/latest/20010101000000.0-20080101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080101000000.0-6.4in_v1.svg)


515\.

![test/visual_test/latest/20010101000000.0-20080102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080102000000.0-6.4in_v1.svg)


516\.

![test/visual_test/latest/20010101000000.0-20090101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20090101000000.0-6.4in_v1.svg)


517\.

![test/visual_test/latest/20010101000000.0-20100101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20100101000000.0-6.4in_v1.svg)


518\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20110101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110101000000.0-6.4in_v1.svg)


519\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20110102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110102000000.0-6.4in_v1.svg)


520\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20160101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20160101000000.0-6.4in_v1.svg)


521\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-20160102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20160102000000.0-6.4in_v1.svg)


522\.

![test/visual_test/latest/20010101000000.0-20210101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20210101000000.0-6.4in_v1.svg)


523\.

![test/visual_test/latest/20010101000000.0-20260101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260101000000.0-6.4in_v1.svg)


524\.

![test/visual_test/latest/20010101000000.0-20260102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260102000000.0-6.4in_v1.svg)


525\.

![test/visual_test/latest/20010101000000.0-20310101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310101000000.0-6.4in_v1.svg)


526\.

![test/visual_test/latest/20010101000000.0-20310102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310102000000.0-6.4in_v1.svg)


527\.

![test/visual_test/latest/20010101000000.0-20360101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360101000000.0-6.4in_v1.svg)


528\.

![test/visual_test/latest/20010101000000.0-20360102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360102000000.0-6.4in_v1.svg)


529\.

![test/visual_test/latest/20010101000000.0-20401231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20401231000000.0-6.4in_v1.svg)


530\.

![test/visual_test/latest/20010101000000.0-20410101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20410101000000.0-6.4in_v1.svg)


531\.

![test/visual_test/latest/20010101000000.0-20510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510101000000.0-6.4in_v1.svg)


532\.

![test/visual_test/latest/20010101000000.0-20510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510102000000.0-6.4in_v1.svg)


533\.

![test/visual_test/latest/20010101000000.0-20601231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20601231000000.0-6.4in_v1.svg)


534\.

![test/visual_test/latest/20010101000000.0-20610101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20610101000000.0-6.4in_v1.svg)


535\.

![test/visual_test/latest/20010101000000.0-20710101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710101000000.0-6.4in_v1.svg)


536\.

![test/visual_test/latest/20010101000000.0-20710102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710102000000.0-6.4in_v1.svg)


537\.

![test/visual_test/latest/20010101000000.0-20801231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20801231000000.0-6.4in_v1.svg)


538\.

![test/visual_test/latest/20010101000000.0-20810101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20810101000000.0-6.4in_v1.svg)


539\. (rule change: 1 reverted)

![test/visual_test/latest/20010101000000.0-20910101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910101000000.0-6.4in_v1.svg)


540\. (rule change: 1 reverted)

![test/visual_test/latest/20010101000000.0-20910102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910102000000.0-6.4in_v1.svg)


541\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-21010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010101000000.0-6.4in_v1.svg)


542\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-21010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010102000000.0-6.4in_v1.svg)


543\.

![test/visual_test/latest/20010101000000.0-21510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21510101000000.0-6.4in_v1.svg)


544\.

![test/visual_test/latest/20010101000000.0-21510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21510102000000.0-6.4in_v1.svg)


545\.

![test/visual_test/latest/20010101000000.0-22010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010101000000.0-6.4in_v1.svg)


546\.

![test/visual_test/latest/20010101000000.0-22010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010102000000.0-6.4in_v1.svg)


547\.

![test/visual_test/latest/20010101000000.0-23010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010101000000.0-6.4in_v1.svg)


548\.

![test/visual_test/latest/20010101000000.0-23010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010102000000.0-6.4in_v1.svg)


549\.

![test/visual_test/latest/20010101000000.0-24010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-24010101000000.0-6.4in_v1.svg)


550\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-25010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010101000000.0-6.4in_v1.svg)


551\. (rule change: -1 reverted)

![test/visual_test/latest/20010101000000.0-25010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010102000000.0-6.4in_v1.svg)


552\.

![test/visual_test/latest/20010101000000.0-27510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-27510102000000.0-6.4in_v1.svg)


553\.

![test/visual_test/latest/20010101000000.0-30010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010101000000.0-6.4in_v1.svg)


554\.

![test/visual_test/latest/20010101000000.0-30010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010102000000.0-6.4in_v1.svg)


555\.

![test/visual_test/latest/20010101000000.0-32510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-32510101000000.0-6.4in_v1.svg)


556\.

![test/visual_test/latest/20010101000000.0-32510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-32510102000000.0-6.4in_v1.svg)


557\.

![test/visual_test/latest/20010101000000.0-35010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-35010102000000.0-6.4in_v1.svg)


558\.

![test/visual_test/latest/20010101000000.0-37510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-37510102000000.0-6.4in_v1.svg)