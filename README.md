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


1\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v1.svg)


2\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v2.svg)


3\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v3.svg)


4\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v4.svg)


5\.

![test/visual_test/latest/19991231220000-20000102020000-6.4in_v5.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-6.4in_v5.svg)


6\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg)


7\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg)


8\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg)


9\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg)


10\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg)


11\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg)


12\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg)


13\.

![test/visual_test/latest/20010101000000.0-20010101000000.001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.001-6.4in_v1.svg)


14\. Cross second boundary

![test/visual_test/latest/20010101000000.9991-20010101000001.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9991-20010101000001.0001-6.4in_v1.svg)


15\. Cross minute boundary

![test/visual_test/latest/20010101000059.9991-20010101000100.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9991-20010101000100.0001-6.4in_v1.svg)


16\. Cross hour boundary

![test/visual_test/latest/20010101005959.9991-20010101010000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9991-20010101010000.0001-6.4in_v1.svg)


17\. Cross day boundary

![test/visual_test/latest/20010101235959.9991-20010102000000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9991-20010102000000.0001-6.4in_v1.svg)


18\. Cross month boundary

![test/visual_test/latest/20010131235959.9991-20010201000000.0001-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9991-20010201000000.0001-6.4in_v1.svg)


19\.

![test/visual_test/latest/20010101000000.0-20010101000000.00125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00125-6.4in_v1.svg)


20\. Cross second boundary

![test/visual_test/latest/20010101000000.998875-20010101000001.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.998875-20010101000001.000125-6.4in_v1.svg)


21\. Cross minute boundary

![test/visual_test/latest/20010101000059.998875-20010101000100.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.998875-20010101000100.000125-6.4in_v1.svg)


22\. Cross hour boundary

![test/visual_test/latest/20010101005959.998875-20010101010000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.998875-20010101010000.000125-6.4in_v1.svg)


23\. Cross day boundary

![test/visual_test/latest/20010101235959.998875-20010102000000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.998875-20010102000000.000125-6.4in_v1.svg)


24\. Cross month boundary

![test/visual_test/latest/20010131235959.998875-20010201000000.000125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.998875-20010201000000.000125-6.4in_v1.svg)


25\.

![test/visual_test/latest/20010101000000.0-20010101000000.0015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0015-6.4in_v1.svg)


26\. Cross second boundary

![test/visual_test/latest/20010101000000.99865-20010101000001.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99865-20010101000001.00015-6.4in_v1.svg)


27\. Cross minute boundary

![test/visual_test/latest/20010101000059.99865-20010101000100.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99865-20010101000100.00015-6.4in_v1.svg)


28\. Cross hour boundary

![test/visual_test/latest/20010101005959.99865-20010101010000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99865-20010101010000.00015-6.4in_v1.svg)


29\. Cross day boundary

![test/visual_test/latest/20010101235959.99865-20010102000000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99865-20010102000000.00015-6.4in_v1.svg)


30\. Cross month boundary

![test/visual_test/latest/20010131235959.99865-20010201000000.00015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99865-20010201000000.00015-6.4in_v1.svg)


31\. (font size change: -0.8 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.00175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00175-6.4in_v1.svg)


32\. Cross second boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010101000000.998425-20010101000001.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.998425-20010101000001.000175-6.4in_v1.svg)


33\. Cross minute boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010101000059.998425-20010101000100.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.998425-20010101000100.000175-6.4in_v1.svg)


34\. Cross hour boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010101005959.998425-20010101010000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.998425-20010101010000.000175-6.4in_v1.svg)


35\. Cross day boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010101235959.998425-20010102000000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.998425-20010102000000.000175-6.4in_v1.svg)


36\. Cross month boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010131235959.998425-20010201000000.000175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.998425-20010201000000.000175-6.4in_v1.svg)


37\. (font size change: -1.8 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.002-6.4in_v1.svg)


38\. Cross second boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101000000.9982-20010101000001.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9982-20010101000001.0002-6.4in_v1.svg)


39\. Cross minute boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101000059.9982-20010101000100.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9982-20010101000100.0002-6.4in_v1.svg)


40\. Cross hour boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101005959.9982-20010101010000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9982-20010101010000.0002-6.4in_v1.svg)


41\. Cross day boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101235959.9982-20010102000000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9982-20010102000000.0002-6.4in_v1.svg)


42\. Cross month boundary (font size change: -1.9 pt)

![test/visual_test/latest/20010131235959.9982-20010201000000.0002-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9982-20010201000000.0002-6.4in_v1.svg)


43\. (font size change: -2.8 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.00225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.00225-6.4in_v1.svg)


44\. Cross second boundary (font size change: -2.8 pt)

![test/visual_test/latest/20010101000000.997975-20010101000001.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.997975-20010101000001.000225-6.4in_v1.svg)


45\. Cross minute boundary (font size change: -2.8 pt)

![test/visual_test/latest/20010101000059.997975-20010101000100.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.997975-20010101000100.000225-6.4in_v1.svg)


46\. Cross hour boundary (font size change: -2.8 pt)

![test/visual_test/latest/20010101005959.997975-20010101010000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.997975-20010101010000.000225-6.4in_v1.svg)


47\. Cross day boundary (font size change: -2.8 pt)

![test/visual_test/latest/20010101235959.997975-20010102000000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.997975-20010102000000.000225-6.4in_v1.svg)


48\. Cross month boundary (font size change: -2.8 pt)

![test/visual_test/latest/20010131235959.997975-20010201000000.000225-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.997975-20010201000000.000225-6.4in_v1.svg)


49\.

![test/visual_test/latest/20010101000000.0-20010101000000.0025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0025-6.4in_v1.svg)


50\. Cross second boundary

![test/visual_test/latest/20010101000000.99775-20010101000001.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99775-20010101000001.00025-6.4in_v1.svg)


51\. Cross minute boundary

![test/visual_test/latest/20010101000059.99775-20010101000100.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99775-20010101000100.00025-6.4in_v1.svg)


52\. Cross hour boundary

![test/visual_test/latest/20010101005959.99775-20010101010000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99775-20010101010000.00025-6.4in_v1.svg)


53\. Cross day boundary

![test/visual_test/latest/20010101235959.99775-20010102000000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99775-20010102000000.00025-6.4in_v1.svg)


54\. Cross month boundary

![test/visual_test/latest/20010131235959.99775-20010201000000.00025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99775-20010201000000.00025-6.4in_v1.svg)


55\.

![test/visual_test/latest/20010101000000.0-20010101000000.003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.003-6.4in_v1.svg)


56\. Cross second boundary

![test/visual_test/latest/20010101000000.9973-20010101000001.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9973-20010101000001.0003-6.4in_v1.svg)


57\. Cross minute boundary

![test/visual_test/latest/20010101000059.9973-20010101000100.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9973-20010101000100.0003-6.4in_v1.svg)


58\. Cross hour boundary

![test/visual_test/latest/20010101005959.9973-20010101010000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9973-20010101010000.0003-6.4in_v1.svg)


59\. Cross day boundary

![test/visual_test/latest/20010101235959.9973-20010102000000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9973-20010102000000.0003-6.4in_v1.svg)


60\. Cross month boundary

![test/visual_test/latest/20010131235959.9973-20010201000000.0003-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9973-20010201000000.0003-6.4in_v1.svg)


61\.

![test/visual_test/latest/20010101000000.0-20010101000000.0035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.0035-6.4in_v1.svg)


62\. Cross second boundary

![test/visual_test/latest/20010101000000.99685-20010101000001.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.99685-20010101000001.00035-6.4in_v1.svg)


63\. Cross minute boundary

![test/visual_test/latest/20010101000059.99685-20010101000100.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.99685-20010101000100.00035-6.4in_v1.svg)


64\. Cross hour boundary

![test/visual_test/latest/20010101005959.99685-20010101010000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.99685-20010101010000.00035-6.4in_v1.svg)


65\. Cross day boundary

![test/visual_test/latest/20010101235959.99685-20010102000000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.99685-20010102000000.00035-6.4in_v1.svg)


66\. Cross month boundary

![test/visual_test/latest/20010131235959.99685-20010201000000.00035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.99685-20010201000000.00035-6.4in_v1.svg)


67\.

![test/visual_test/latest/20010101000000.0-20010101000000.004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.004-6.4in_v1.svg)


68\. Cross second boundary (rule change: 1)

![test/visual_test/latest/20010101000000.9964-20010101000001.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.9964-20010101000001.0004-6.4in_v1.svg)


69\. Cross minute boundary (rule change: 1)

![test/visual_test/latest/20010101000059.9964-20010101000100.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.9964-20010101000100.0004-6.4in_v1.svg)


70\. Cross hour boundary (rule change: 1)

![test/visual_test/latest/20010101005959.9964-20010101010000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.9964-20010101010000.0004-6.4in_v1.svg)


71\. Cross day boundary (rule change: 1)

![test/visual_test/latest/20010101235959.9964-20010102000000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.9964-20010102000000.0004-6.4in_v1.svg)


72\. Cross month boundary (rule change: 1)

![test/visual_test/latest/20010131235959.9964-20010201000000.0004-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.9964-20010201000000.0004-6.4in_v1.svg)