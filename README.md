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

![test/visual_test/latest/19991231220000-20000102020000-12.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-12.4in_v1.svg)


4\.

![test/visual_test/latest/19991231220000-20000102020000-3.2in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-3.2in_v1.svg)


5\.

![test/visual_test/latest/19991231220000-20000102020000-1.6in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/19991231220000-20000102020000-1.6in_v1.svg)


6\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.svg)


7\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v2.svg)


8\.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v3.svg)


9\. Right label is right aligned in PNG.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.png](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v1.png)


10\. Right label is not right aligned in SVG due to Matplotlib bug.

![test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20000101000000-20000103000000-6.4in_v4.svg)


11\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v1.svg)


12\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v2.svg)


13\.

![test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20001231113000-20010103003000-6.4in_v3.svg)


14\. (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.1-6.4in_v1.svg)


15\. Cross second boundary (rule change: -4)

![test/visual_test/latest/20010101000000.91-20010101000001.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.91-20010101000001.01-6.4in_v1.svg)


16\. Cross minute boundary (rule change: -4)

![test/visual_test/latest/20010101000059.91-20010101000100.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.91-20010101000100.01-6.4in_v1.svg)


17\. Cross hour boundary (rule change: -4)

![test/visual_test/latest/20010101005959.91-20010101010000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.91-20010101010000.01-6.4in_v1.svg)


18\. Cross day boundary (rule change: -4)

![test/visual_test/latest/20010101235959.91-20010102000000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.91-20010102000000.01-6.4in_v1.svg)


19\. Cross month boundary (rule change: -4)

![test/visual_test/latest/20010131235959.91-20010201000000.01-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.91-20010201000000.01-6.4in_v1.svg)


20\.

![test/visual_test/latest/20010101000000.0-20010101000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.125-6.4in_v1.svg)


21\. Cross second boundary (rule change: -4)

![test/visual_test/latest/20010101000000.8875-20010101000001.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.8875-20010101000001.0125-6.4in_v1.svg)


22\. Cross minute boundary (rule change: -4)

![test/visual_test/latest/20010101000059.8875-20010101000100.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.8875-20010101000100.0125-6.4in_v1.svg)


23\. Cross hour boundary (rule change: -4)

![test/visual_test/latest/20010101005959.8875-20010101010000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.8875-20010101010000.0125-6.4in_v1.svg)


24\. Cross day boundary (rule change: -4)

![test/visual_test/latest/20010101235959.8875-20010102000000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.8875-20010102000000.0125-6.4in_v1.svg)


25\. Cross month boundary (rule change: -4)

![test/visual_test/latest/20010131235959.8875-20010201000000.0125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.8875-20010201000000.0125-6.4in_v1.svg)


26\.

![test/visual_test/latest/20010101000000.0-20010101000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.15-6.4in_v1.svg)


27\. Cross second boundary

![test/visual_test/latest/20010101000000.865-20010101000001.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.865-20010101000001.015-6.4in_v1.svg)


28\. Cross minute boundary

![test/visual_test/latest/20010101000059.865-20010101000100.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.865-20010101000100.015-6.4in_v1.svg)


29\. Cross hour boundary

![test/visual_test/latest/20010101005959.865-20010101010000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.865-20010101010000.015-6.4in_v1.svg)


30\. Cross day boundary

![test/visual_test/latest/20010101235959.865-20010102000000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.865-20010102000000.015-6.4in_v1.svg)


31\. Cross month boundary

![test/visual_test/latest/20010131235959.865-20010201000000.015-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.865-20010201000000.015-6.4in_v1.svg)


32\.

![test/visual_test/latest/20010101000000.0-20010101000000.175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.175-6.4in_v1.svg)


33\. Cross second boundary

![test/visual_test/latest/20010101000000.8425-20010101000001.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.8425-20010101000001.0175-6.4in_v1.svg)


34\. Cross minute boundary

![test/visual_test/latest/20010101000059.8425-20010101000100.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.8425-20010101000100.0175-6.4in_v1.svg)


35\. Cross hour boundary

![test/visual_test/latest/20010101005959.8425-20010101010000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.8425-20010101010000.0175-6.4in_v1.svg)


36\. Cross day boundary

![test/visual_test/latest/20010101235959.8425-20010102000000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.8425-20010102000000.0175-6.4in_v1.svg)


37\. Cross month boundary

![test/visual_test/latest/20010131235959.8425-20010201000000.0175-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.8425-20010201000000.0175-6.4in_v1.svg)


38\. (font size change: -1.8 pt)

![test/visual_test/latest/20010101000000.0-20010101000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.2-6.4in_v1.svg)


39\. Cross second boundary

![test/visual_test/latest/20010101000000.82-20010101000001.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.82-20010101000001.02-6.4in_v1.svg)


40\. Cross minute boundary

![test/visual_test/latest/20010101000059.82-20010101000100.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.82-20010101000100.02-6.4in_v1.svg)


41\. Cross hour boundary

![test/visual_test/latest/20010101005959.82-20010101010000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.82-20010101010000.02-6.4in_v1.svg)


42\. Cross day boundary

![test/visual_test/latest/20010101235959.82-20010102000000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.82-20010102000000.02-6.4in_v1.svg)


43\. Cross month boundary

![test/visual_test/latest/20010131235959.82-20010201000000.02-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.82-20010201000000.02-6.4in_v1.svg)


44\.

![test/visual_test/latest/20010101000000.0-20010101000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.25-6.4in_v1.svg)


45\. Cross second boundary (font size change: -1.0 pt)

![test/visual_test/latest/20010101000000.775-20010101000001.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.775-20010101000001.025-6.4in_v1.svg)


46\. Cross minute boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101000059.775-20010101000100.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.775-20010101000100.025-6.4in_v1.svg)


47\. Cross hour boundary (font size change: -0.9 pt)

![test/visual_test/latest/20010101005959.775-20010101010000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.775-20010101010000.025-6.4in_v1.svg)


48\. Cross day boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010101235959.775-20010102000000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.775-20010102000000.025-6.4in_v1.svg)


49\. Cross month boundary (font size change: -1.8 pt)

![test/visual_test/latest/20010131235959.775-20010201000000.025-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.775-20010201000000.025-6.4in_v1.svg)


50\.

![test/visual_test/latest/20010101000000.0-20010101000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.3-6.4in_v1.svg)


51\. Cross second boundary

![test/visual_test/latest/20010101000000.73-20010101000001.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.73-20010101000001.03-6.4in_v1.svg)


52\. Cross minute boundary

![test/visual_test/latest/20010101000059.73-20010101000100.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.73-20010101000100.03-6.4in_v1.svg)


53\. Cross hour boundary

![test/visual_test/latest/20010101005959.73-20010101010000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.73-20010101010000.03-6.4in_v1.svg)


54\. Cross day boundary

![test/visual_test/latest/20010101235959.73-20010102000000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.73-20010102000000.03-6.4in_v1.svg)


55\. Cross month boundary

![test/visual_test/latest/20010131235959.73-20010201000000.03-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.73-20010201000000.03-6.4in_v1.svg)


56\.

![test/visual_test/latest/20010101000000.0-20010101000000.35-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.35-6.4in_v1.svg)


57\. Cross second boundary

![test/visual_test/latest/20010101000000.685-20010101000001.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.685-20010101000001.035-6.4in_v1.svg)


58\. Cross minute boundary

![test/visual_test/latest/20010101000059.685-20010101000100.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.685-20010101000100.035-6.4in_v1.svg)


59\. Cross hour boundary

![test/visual_test/latest/20010101005959.685-20010101010000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.685-20010101010000.035-6.4in_v1.svg)


60\. Cross day boundary

![test/visual_test/latest/20010101235959.685-20010102000000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.685-20010102000000.035-6.4in_v1.svg)


61\. Cross month boundary

![test/visual_test/latest/20010131235959.685-20010201000000.035-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.685-20010201000000.035-6.4in_v1.svg)


62\.

![test/visual_test/latest/20010101000000.0-20010101000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.4-6.4in_v1.svg)


63\. Cross second boundary

![test/visual_test/latest/20010101000000.64-20010101000001.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.64-20010101000001.04-6.4in_v1.svg)


64\. Cross minute boundary

![test/visual_test/latest/20010101000059.64-20010101000100.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.64-20010101000100.04-6.4in_v1.svg)


65\. Cross hour boundary

![test/visual_test/latest/20010101005959.64-20010101010000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.64-20010101010000.04-6.4in_v1.svg)


66\. Cross day boundary

![test/visual_test/latest/20010101235959.64-20010102000000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.64-20010102000000.04-6.4in_v1.svg)


67\. Cross month boundary

![test/visual_test/latest/20010131235959.64-20010201000000.04-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.64-20010201000000.04-6.4in_v1.svg)


68\.

![test/visual_test/latest/20010101000000.0-20010101000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.5-6.4in_v1.svg)


69\. Cross second boundary

![test/visual_test/latest/20010101000000.55-20010101000001.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.55-20010101000001.05-6.4in_v1.svg)


70\. Cross minute boundary

![test/visual_test/latest/20010101000059.55-20010101000100.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.55-20010101000100.05-6.4in_v1.svg)


71\. Cross hour boundary

![test/visual_test/latest/20010101005959.55-20010101010000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.55-20010101010000.05-6.4in_v1.svg)


72\. Cross day boundary

![test/visual_test/latest/20010101235959.55-20010102000000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.55-20010102000000.05-6.4in_v1.svg)


73\. Cross month boundary

![test/visual_test/latest/20010131235959.55-20010201000000.05-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.55-20010201000000.05-6.4in_v1.svg)


74\.

![test/visual_test/latest/20010101000000.0-20010101000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.6-6.4in_v1.svg)


75\. Cross second boundary

![test/visual_test/latest/20010101000000.46-20010101000001.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.46-20010101000001.06-6.4in_v1.svg)


76\. Cross minute boundary

![test/visual_test/latest/20010101000059.46-20010101000100.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.46-20010101000100.06-6.4in_v1.svg)


77\. Cross hour boundary

![test/visual_test/latest/20010101005959.46-20010101010000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.46-20010101010000.06-6.4in_v1.svg)


78\. Cross day boundary

![test/visual_test/latest/20010101235959.46-20010102000000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.46-20010102000000.06-6.4in_v1.svg)


79\. Cross month boundary

![test/visual_test/latest/20010131235959.46-20010201000000.06-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.46-20010201000000.06-6.4in_v1.svg)


80\.

![test/visual_test/latest/20010101000000.0-20010101000000.7-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000000.7-6.4in_v1.svg)


81\. Cross second boundary

![test/visual_test/latest/20010101000000.37-20010101000001.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.37-20010101000001.07-6.4in_v1.svg)


82\. Cross minute boundary

![test/visual_test/latest/20010101000059.37-20010101000100.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.37-20010101000100.07-6.4in_v1.svg)


83\. Cross hour boundary

![test/visual_test/latest/20010101005959.37-20010101010000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.37-20010101010000.07-6.4in_v1.svg)


84\. Cross day boundary

![test/visual_test/latest/20010101235959.37-20010102000000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.37-20010102000000.07-6.4in_v1.svg)


85\. Cross month boundary

![test/visual_test/latest/20010131235959.37-20010201000000.07-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.37-20010201000000.07-6.4in_v1.svg)


86\. (font size change: -0.5 pt)

![test/visual_test/latest/20010101000000.0-20010101000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.0-6.4in_v1.svg)


87\. Cross minute boundary

![test/visual_test/latest/20010101000059.1-20010101000100.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000059.1-20010101000100.1-6.4in_v1.svg)


88\. Cross hour boundary

![test/visual_test/latest/20010101005959.1-20010101010000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005959.1-20010101010000.1-6.4in_v1.svg)


89\. Cross day boundary

![test/visual_test/latest/20010101235959.1-20010102000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235959.1-20010102000000.1-6.4in_v1.svg)


90\. Cross month boundary

![test/visual_test/latest/20010131235959.1-20010201000000.1-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235959.1-20010201000000.1-6.4in_v1.svg)


91\.

![test/visual_test/latest/20010101000000.0-20010101000001.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.25-6.4in_v1.svg)


92\. Cross minute boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010101000058.875-20010101000100.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.875-20010101000100.125-6.4in_v1.svg)


93\. Cross hour boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010101005958.875-20010101010000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.875-20010101010000.125-6.4in_v1.svg)


94\. Cross day boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010101235958.875-20010102000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.875-20010102000000.125-6.4in_v1.svg)


95\. Cross month boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010131235958.875-20010201000000.125-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.875-20010201000000.125-6.4in_v1.svg)


96\.

![test/visual_test/latest/20010101000000.0-20010101000001.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000001.5-6.4in_v1.svg)


97\. Cross minute boundary

![test/visual_test/latest/20010101000058.65-20010101000100.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.65-20010101000100.15-6.4in_v1.svg)


98\. Cross hour boundary

![test/visual_test/latest/20010101005958.65-20010101010000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.65-20010101010000.15-6.4in_v1.svg)


99\. Cross day boundary

![test/visual_test/latest/20010101235958.65-20010102000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.65-20010102000000.15-6.4in_v1.svg)


100\. Cross month boundary

![test/visual_test/latest/20010131235958.65-20010201000000.15-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.65-20010201000000.15-6.4in_v1.svg)


101\. (font size change: -1.8 pt)

![test/visual_test/latest/20010101000000.0-20010101000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.0-6.4in_v1.svg)


102\. Cross minute boundary

![test/visual_test/latest/20010101000058.2-20010101000100.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000058.2-20010101000100.2-6.4in_v1.svg)


103\. Cross hour boundary

![test/visual_test/latest/20010101005958.2-20010101010000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005958.2-20010101010000.2-6.4in_v1.svg)


104\. Cross day boundary

![test/visual_test/latest/20010101235958.2-20010102000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235958.2-20010102000000.2-6.4in_v1.svg)


105\. Cross month boundary

![test/visual_test/latest/20010131235958.2-20010201000000.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235958.2-20010201000000.2-6.4in_v1.svg)


106\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010101000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000002.5-6.4in_v1.svg)


107\. Cross minute boundary

![test/visual_test/latest/20010101000057.75-20010101000100.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.75-20010101000100.25-6.4in_v1.svg)


108\. Cross hour boundary

![test/visual_test/latest/20010101005957.75-20010101010000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.75-20010101010000.25-6.4in_v1.svg)


109\. Cross day boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010101235957.75-20010102000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.75-20010102000000.25-6.4in_v1.svg)


110\. Cross month boundary (font size change: -0.8 pt)

![test/visual_test/latest/20010131235957.75-20010201000000.25-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.75-20010201000000.25-6.4in_v1.svg)


111\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010101000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000003.0-6.4in_v1.svg)


112\. Cross minute boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010101000057.3-20010101000100.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000057.3-20010101000100.3-6.4in_v1.svg)


113\. Cross hour boundary

![test/visual_test/latest/20010101005957.3-20010101010000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005957.3-20010101010000.3-6.4in_v1.svg)


114\. Cross day boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010101235957.3-20010102000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235957.3-20010102000000.3-6.4in_v1.svg)


115\. Cross month boundary (font size change: -0.5 pt)

![test/visual_test/latest/20010131235957.3-20010201000000.3-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235957.3-20010201000000.3-6.4in_v1.svg)


116\.

![test/visual_test/latest/20010101000000.0-20010101000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000004.0-6.4in_v1.svg)


117\. Cross minute boundary

![test/visual_test/latest/20010101000056.4-20010101000100.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000056.4-20010101000100.4-6.4in_v1.svg)


118\. Cross hour boundary

![test/visual_test/latest/20010101005956.4-20010101010000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005956.4-20010101010000.4-6.4in_v1.svg)


119\. Cross day boundary

![test/visual_test/latest/20010101235956.4-20010102000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235956.4-20010102000000.4-6.4in_v1.svg)


120\. Cross month boundary

![test/visual_test/latest/20010131235956.4-20010201000000.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235956.4-20010201000000.4-6.4in_v1.svg)


121\.

![test/visual_test/latest/20010101000000.0-20010101000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000005.0-6.4in_v1.svg)


122\. Cross minute boundary

![test/visual_test/latest/20010101000055.5-20010101000100.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000055.5-20010101000100.5-6.4in_v1.svg)


123\. Cross hour boundary

![test/visual_test/latest/20010101005955.5-20010101010000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005955.5-20010101010000.5-6.4in_v1.svg)


124\. Cross day boundary

![test/visual_test/latest/20010101235955.5-20010102000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235955.5-20010102000000.5-6.4in_v1.svg)


125\. Cross month boundary

![test/visual_test/latest/20010131235955.5-20010201000000.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235955.5-20010201000000.5-6.4in_v1.svg)


126\.

![test/visual_test/latest/20010101000000.0-20010101000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000006.0-6.4in_v1.svg)


127\. Cross minute boundary

![test/visual_test/latest/20010101000054.6-20010101000100.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000054.6-20010101000100.6-6.4in_v1.svg)


128\. Cross hour boundary

![test/visual_test/latest/20010101005954.6-20010101010000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005954.6-20010101010000.6-6.4in_v1.svg)


129\. Cross day boundary

![test/visual_test/latest/20010101235954.6-20010102000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235954.6-20010102000000.6-6.4in_v1.svg)


130\. Cross month boundary

![test/visual_test/latest/20010131235954.6-20010201000000.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235954.6-20010201000000.6-6.4in_v1.svg)


131\.

![test/visual_test/latest/20010101000000.0-20010101000008.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000008.0-6.4in_v1.svg)


132\. Cross minute boundary

![test/visual_test/latest/20010101000052.8-20010101000100.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000052.8-20010101000100.8-6.4in_v1.svg)


133\. Cross hour boundary

![test/visual_test/latest/20010101005952.8-20010101010000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005952.8-20010101010000.8-6.4in_v1.svg)


134\. Cross day boundary

![test/visual_test/latest/20010101235952.8-20010102000000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235952.8-20010102000000.8-6.4in_v1.svg)


135\. Cross month boundary

![test/visual_test/latest/20010131235952.8-20010201000000.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235952.8-20010201000000.8-6.4in_v1.svg)


136\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101000010.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000010.0-6.4in_v1.svg)


137\. Cross minute boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101000051.0-20010101000101.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000051.0-20010101000101.0-6.4in_v1.svg)


138\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101005951.0-20010101010001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005951.0-20010101010001.0-6.4in_v1.svg)


139\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101235951.0-20010102000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235951.0-20010102000001.0-6.4in_v1.svg)


140\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131235951.0-20010201000001.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235951.0-20010201000001.0-6.4in_v1.svg)


141\.

![test/visual_test/latest/20010101000000.0-20010101000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000012.0-6.4in_v1.svg)


142\. Cross minute boundary

![test/visual_test/latest/20010101000049.2-20010101000101.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000049.2-20010101000101.2-6.4in_v1.svg)


143\. Cross hour boundary

![test/visual_test/latest/20010101005949.2-20010101010001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005949.2-20010101010001.2-6.4in_v1.svg)


144\. Cross day boundary

![test/visual_test/latest/20010101235949.2-20010102000001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235949.2-20010102000001.2-6.4in_v1.svg)


145\. Cross month boundary

![test/visual_test/latest/20010131235949.2-20010201000001.2-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235949.2-20010201000001.2-6.4in_v1.svg)


146\.

![test/visual_test/latest/20010101000000.0-20010101000014.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000014.0-6.4in_v1.svg)


147\. Cross minute boundary

![test/visual_test/latest/20010101000047.4-20010101000101.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000047.4-20010101000101.4-6.4in_v1.svg)


148\. Cross hour boundary

![test/visual_test/latest/20010101005947.4-20010101010001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005947.4-20010101010001.4-6.4in_v1.svg)


149\. Cross day boundary

![test/visual_test/latest/20010101235947.4-20010102000001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235947.4-20010102000001.4-6.4in_v1.svg)


150\. Cross month boundary

![test/visual_test/latest/20010131235947.4-20010201000001.4-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235947.4-20010201000001.4-6.4in_v1.svg)


151\.

![test/visual_test/latest/20010101000000.0-20010101000016.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000016.0-6.4in_v1.svg)


152\. Cross minute boundary

![test/visual_test/latest/20010101000045.6-20010101000101.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000045.6-20010101000101.6-6.4in_v1.svg)


153\. Cross hour boundary

![test/visual_test/latest/20010101005945.6-20010101010001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005945.6-20010101010001.6-6.4in_v1.svg)


154\. Cross day boundary

![test/visual_test/latest/20010101235945.6-20010102000001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235945.6-20010102000001.6-6.4in_v1.svg)


155\. Cross month boundary

![test/visual_test/latest/20010131235945.6-20010201000001.6-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235945.6-20010201000001.6-6.4in_v1.svg)


156\.

![test/visual_test/latest/20010101000000.0-20010101000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000018.0-6.4in_v1.svg)


157\. Cross minute boundary

![test/visual_test/latest/20010101000043.8-20010101000101.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000043.8-20010101000101.8-6.4in_v1.svg)


158\. Cross hour boundary

![test/visual_test/latest/20010101005943.8-20010101010001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005943.8-20010101010001.8-6.4in_v1.svg)


159\. Cross day boundary

![test/visual_test/latest/20010101235943.8-20010102000001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235943.8-20010102000001.8-6.4in_v1.svg)


160\. Cross month boundary

![test/visual_test/latest/20010131235943.8-20010201000001.8-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235943.8-20010201000001.8-6.4in_v1.svg)


161\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101000020.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000020.0-6.4in_v1.svg)


162\. Cross minute boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101000042.0-20010101000102.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000042.0-20010101000102.0-6.4in_v1.svg)


163\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101005942.0-20010101010002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005942.0-20010101010002.0-6.4in_v1.svg)


164\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101235942.0-20010102000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235942.0-20010102000002.0-6.4in_v1.svg)


165\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131235942.0-20010201000002.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235942.0-20010201000002.0-6.4in_v1.svg)


166\. (font size change: -3.5 pt)

![test/visual_test/latest/20010101000000.0-20010101000025.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000025.0-6.4in_v1.svg)


167\. Cross minute boundary (font size change: -3.5 pt)

![test/visual_test/latest/20010101000037.5-20010101000102.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000037.5-20010101000102.5-6.4in_v1.svg)


168\. Cross hour boundary (font size change: -3.4 pt)

![test/visual_test/latest/20010101005937.5-20010101010002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005937.5-20010101010002.5-6.4in_v1.svg)


169\. Cross day boundary (font size change: -3.4 pt)

![test/visual_test/latest/20010101235937.5-20010102000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235937.5-20010102000002.5-6.4in_v1.svg)


170\. Cross month boundary (font size change: -3.4 pt)

![test/visual_test/latest/20010131235937.5-20010201000002.5-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235937.5-20010201000002.5-6.4in_v1.svg)


171\.

![test/visual_test/latest/20010101000000.0-20010101000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000030.0-6.4in_v1.svg)


172\. Cross minute boundary

![test/visual_test/latest/20010101000033.0-20010101000103.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000033.0-20010101000103.0-6.4in_v1.svg)


173\. Cross hour boundary

![test/visual_test/latest/20010101005933.0-20010101010003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005933.0-20010101010003.0-6.4in_v1.svg)


174\. Cross day boundary

![test/visual_test/latest/20010101235933.0-20010102000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235933.0-20010102000003.0-6.4in_v1.svg)


175\. Cross month boundary

![test/visual_test/latest/20010131235933.0-20010201000003.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235933.0-20010201000003.0-6.4in_v1.svg)


176\.

![test/visual_test/latest/20010101000000.0-20010101000040.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000040.0-6.4in_v1.svg)


177\. Cross minute boundary

![test/visual_test/latest/20010101000024.0-20010101000104.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000024.0-20010101000104.0-6.4in_v1.svg)


178\. Cross hour boundary

![test/visual_test/latest/20010101005924.0-20010101010004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005924.0-20010101010004.0-6.4in_v1.svg)


179\. Cross day boundary

![test/visual_test/latest/20010101235924.0-20010102000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235924.0-20010102000004.0-6.4in_v1.svg)


180\. Cross month boundary

![test/visual_test/latest/20010131235924.0-20010201000004.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235924.0-20010201000004.0-6.4in_v1.svg)


181\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101000050.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000050.0-6.4in_v1.svg)


182\. Cross minute boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101000015.0-20010101000105.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000015.0-20010101000105.0-6.4in_v1.svg)


183\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101005915.0-20010101010005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005915.0-20010101010005.0-6.4in_v1.svg)


184\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101235915.0-20010102000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235915.0-20010102000005.0-6.4in_v1.svg)


185\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131235915.0-20010201000005.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235915.0-20010201000005.0-6.4in_v1.svg)


186\.

![test/visual_test/latest/20010101000000.0-20010101000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000100.0-6.4in_v1.svg)


187\. Cross hour boundary

![test/visual_test/latest/20010101005906.0-20010101010006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005906.0-20010101010006.0-6.4in_v1.svg)


188\. Cross day boundary

![test/visual_test/latest/20010101235906.0-20010102000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235906.0-20010102000006.0-6.4in_v1.svg)


189\. Cross month boundary

![test/visual_test/latest/20010131235906.0-20010201000006.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235906.0-20010201000006.0-6.4in_v1.svg)


190\.

![test/visual_test/latest/20010101000000.0-20010101000110.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000110.0-6.4in_v1.svg)


191\. Cross hour boundary

![test/visual_test/latest/20010101005857.0-20010101010007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005857.0-20010101010007.0-6.4in_v1.svg)


192\. Cross day boundary

![test/visual_test/latest/20010101235857.0-20010102000007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235857.0-20010102000007.0-6.4in_v1.svg)


193\. Cross month boundary

![test/visual_test/latest/20010131235857.0-20010201000007.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235857.0-20010201000007.0-6.4in_v1.svg)


194\. (font size change: -3.1 pt)

![test/visual_test/latest/20010101000000.0-20010101000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000200.0-6.4in_v1.svg)


195\. Cross hour boundary (rule change: -2)

![test/visual_test/latest/20010101005812.0-20010101010012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005812.0-20010101010012.0-6.4in_v1.svg)


196\. Cross day boundary (rule change: -2)

![test/visual_test/latest/20010101235812.0-20010102000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235812.0-20010102000012.0-6.4in_v1.svg)


197\. Cross month boundary (rule change: -2)

![test/visual_test/latest/20010131235812.0-20010201000012.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235812.0-20010201000012.0-6.4in_v1.svg)


198\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010101000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000230.0-6.4in_v1.svg)


199\. Cross hour boundary (font size change: -3.9 pt)

![test/visual_test/latest/20010101005745.0-20010101010015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005745.0-20010101010015.0-6.4in_v1.svg)


200\. Cross day boundary (font size change: -3.9 pt)

![test/visual_test/latest/20010101235745.0-20010102000015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235745.0-20010102000015.0-6.4in_v1.svg)


201\. Cross month boundary (font size change: -3.9 pt)

![test/visual_test/latest/20010131235745.0-20010201000015.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235745.0-20010201000015.0-6.4in_v1.svg)


202\.

![test/visual_test/latest/20010101000000.0-20010101000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000300.0-6.4in_v1.svg)


203\. Cross hour boundary

![test/visual_test/latest/20010101005718.0-20010101010018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005718.0-20010101010018.0-6.4in_v1.svg)


204\. Cross day boundary

![test/visual_test/latest/20010101235718.0-20010102000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235718.0-20010102000018.0-6.4in_v1.svg)


205\. Cross month boundary

![test/visual_test/latest/20010131235718.0-20010201000018.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235718.0-20010201000018.0-6.4in_v1.svg)


206\.

![test/visual_test/latest/20010101000000.0-20010101000330.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000330.0-6.4in_v1.svg)


207\. Cross hour boundary

![test/visual_test/latest/20010101005651.0-20010101010021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005651.0-20010101010021.0-6.4in_v1.svg)


208\. Cross day boundary

![test/visual_test/latest/20010101235651.0-20010102000021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235651.0-20010102000021.0-6.4in_v1.svg)


209\. Cross month boundary

![test/visual_test/latest/20010131235651.0-20010201000021.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235651.0-20010201000021.0-6.4in_v1.svg)


210\.

![test/visual_test/latest/20010101000000.0-20010101000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000400.0-6.4in_v1.svg)


211\. Cross hour boundary

![test/visual_test/latest/20010101005624.0-20010101010024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005624.0-20010101010024.0-6.4in_v1.svg)


212\. Cross day boundary

![test/visual_test/latest/20010101235624.0-20010102000024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235624.0-20010102000024.0-6.4in_v1.svg)


213\. Cross month boundary

![test/visual_test/latest/20010131235624.0-20010201000024.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235624.0-20010201000024.0-6.4in_v1.svg)


214\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000500.0-6.4in_v1.svg)


215\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101005530.0-20010101010030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005530.0-20010101010030.0-6.4in_v1.svg)


216\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101235530.0-20010102000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235530.0-20010102000030.0-6.4in_v1.svg)


217\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131235530.0-20010201000030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235530.0-20010201000030.0-6.4in_v1.svg)


218\.

![test/visual_test/latest/20010101000000.0-20010101000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000600.0-6.4in_v1.svg)


219\. Cross hour boundary

![test/visual_test/latest/20010101005436.0-20010101010036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005436.0-20010101010036.0-6.4in_v1.svg)


220\. Cross day boundary

![test/visual_test/latest/20010101235436.0-20010102000036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235436.0-20010102000036.0-6.4in_v1.svg)


221\. Cross month boundary

![test/visual_test/latest/20010131235436.0-20010201000036.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235436.0-20010201000036.0-6.4in_v1.svg)


222\.

![test/visual_test/latest/20010101000000.0-20010101000700.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000700.0-6.4in_v1.svg)


223\. Cross hour boundary

![test/visual_test/latest/20010101005342.0-20010101010042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005342.0-20010101010042.0-6.4in_v1.svg)


224\. Cross day boundary

![test/visual_test/latest/20010101235342.0-20010102000042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235342.0-20010102000042.0-6.4in_v1.svg)


225\. Cross month boundary

![test/visual_test/latest/20010131235342.0-20010201000042.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235342.0-20010201000042.0-6.4in_v1.svg)


226\.

![test/visual_test/latest/20010101000000.0-20010101000800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101000800.0-6.4in_v1.svg)


227\. Cross hour boundary

![test/visual_test/latest/20010101005248.0-20010101010048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005248.0-20010101010048.0-6.4in_v1.svg)


228\. Cross day boundary

![test/visual_test/latest/20010101235248.0-20010102000048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235248.0-20010102000048.0-6.4in_v1.svg)


229\. Cross month boundary

![test/visual_test/latest/20010131235248.0-20010201000048.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235248.0-20010201000048.0-6.4in_v1.svg)


230\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101001000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001000.0-6.4in_v1.svg)


231\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101005100.0-20010101010100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101005100.0-20010101010100.0-6.4in_v1.svg)


232\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101235100.0-20010102000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101235100.0-20010102000100.0-6.4in_v1.svg)


233\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131235100.0-20010201000100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131235100.0-20010201000100.0-6.4in_v1.svg)


234\.

![test/visual_test/latest/20010101000000.0-20010101001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001200.0-6.4in_v1.svg)


235\. Cross hour boundary

![test/visual_test/latest/20010101004912.0-20010101010112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004912.0-20010101010112.0-6.4in_v1.svg)


236\. Cross day boundary

![test/visual_test/latest/20010101234912.0-20010102000112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234912.0-20010102000112.0-6.4in_v1.svg)


237\. Cross month boundary

![test/visual_test/latest/20010131234912.0-20010201000112.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234912.0-20010201000112.0-6.4in_v1.svg)


238\.

![test/visual_test/latest/20010101000000.0-20010101001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101001500.0-6.4in_v1.svg)


239\. Cross hour boundary

![test/visual_test/latest/20010101004630.0-20010101010130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004630.0-20010101010130.0-6.4in_v1.svg)


240\. Cross day boundary

![test/visual_test/latest/20010101234630.0-20010102000130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234630.0-20010102000130.0-6.4in_v1.svg)


241\. Cross month boundary

![test/visual_test/latest/20010131234630.0-20010201000130.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234630.0-20010201000130.0-6.4in_v1.svg)


242\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101002000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002000.0-6.4in_v1.svg)


243\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101004200.0-20010101010200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101004200.0-20010101010200.0-6.4in_v1.svg)


244\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101234200.0-20010102000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101234200.0-20010102000200.0-6.4in_v1.svg)


245\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131234200.0-20010201000200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131234200.0-20010201000200.0-6.4in_v1.svg)


246\. (font size change: -3.5 pt)

![test/visual_test/latest/20010101000000.0-20010101002500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101002500.0-6.4in_v1.svg)


247\. Cross hour boundary (font size change: -3.5 pt)

![test/visual_test/latest/20010101003730.0-20010101010230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003730.0-20010101010230.0-6.4in_v1.svg)


248\. Cross day boundary (font size change: -3.5 pt)

![test/visual_test/latest/20010101233730.0-20010102000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233730.0-20010102000230.0-6.4in_v1.svg)


249\. Cross month boundary (font size change: -3.5 pt)

![test/visual_test/latest/20010131233730.0-20010201000230.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233730.0-20010201000230.0-6.4in_v1.svg)


250\.

![test/visual_test/latest/20010101000000.0-20010101003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101003000.0-6.4in_v1.svg)


251\. Cross hour boundary

![test/visual_test/latest/20010101003300.0-20010101010300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101003300.0-20010101010300.0-6.4in_v1.svg)


252\. Cross day boundary

![test/visual_test/latest/20010101233300.0-20010102000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101233300.0-20010102000300.0-6.4in_v1.svg)


253\. Cross month boundary

![test/visual_test/latest/20010131233300.0-20010201000300.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131233300.0-20010201000300.0-6.4in_v1.svg)


254\.

![test/visual_test/latest/20010101000000.0-20010101004000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101004000.0-6.4in_v1.svg)


255\. Cross hour boundary

![test/visual_test/latest/20010101002400.0-20010101010400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101002400.0-20010101010400.0-6.4in_v1.svg)


256\. Cross day boundary

![test/visual_test/latest/20010101232400.0-20010102000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101232400.0-20010102000400.0-6.4in_v1.svg)


257\. Cross month boundary

![test/visual_test/latest/20010131232400.0-20010201000400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131232400.0-20010201000400.0-6.4in_v1.svg)


258\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101005000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101005000.0-6.4in_v1.svg)


259\. Cross hour boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101001500.0-20010101010500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101001500.0-20010101010500.0-6.4in_v1.svg)


260\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101231500.0-20010102000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101231500.0-20010102000500.0-6.4in_v1.svg)


261\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131231500.0-20010201000500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131231500.0-20010201000500.0-6.4in_v1.svg)


262\.

![test/visual_test/latest/20010101000000.0-20010101010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101010000.0-6.4in_v1.svg)


263\. Cross day boundary

![test/visual_test/latest/20010101230600.0-20010102000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101230600.0-20010102000600.0-6.4in_v1.svg)


264\. Cross month boundary

![test/visual_test/latest/20010131230600.0-20010201000600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131230600.0-20010201000600.0-6.4in_v1.svg)


265\.

![test/visual_test/latest/20010101000000.0-20010101011500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101011500.0-6.4in_v1.svg)


266\. Cross day boundary

![test/visual_test/latest/20010101225230.0-20010102000730.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101225230.0-20010102000730.0-6.4in_v1.svg)


267\. Cross month boundary

![test/visual_test/latest/20010131225230.0-20010201000730.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131225230.0-20010201000730.0-6.4in_v1.svg)


268\.

![test/visual_test/latest/20010101000000.0-20010101013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101013000.0-6.4in_v1.svg)


269\. Cross day boundary

![test/visual_test/latest/20010101223900.0-20010102000900.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101223900.0-20010102000900.0-6.4in_v1.svg)


270\. Cross month boundary

![test/visual_test/latest/20010131223900.0-20010201000900.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131223900.0-20010201000900.0-6.4in_v1.svg)


271\.

![test/visual_test/latest/20010101000000.0-20010101014500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101014500.0-6.4in_v1.svg)


272\. Cross day boundary

![test/visual_test/latest/20010101222530.0-20010102001030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101222530.0-20010102001030.0-6.4in_v1.svg)


273\. Cross month boundary

![test/visual_test/latest/20010131222530.0-20010201001030.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131222530.0-20010201001030.0-6.4in_v1.svg)


274\.

![test/visual_test/latest/20010101000000.0-20010101020000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101020000.0-6.4in_v1.svg)


275\. Cross day boundary

![test/visual_test/latest/20010101221200.0-20010102001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101221200.0-20010102001200.0-6.4in_v1.svg)


276\. Cross month boundary

![test/visual_test/latest/20010131221200.0-20010201001200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131221200.0-20010201001200.0-6.4in_v1.svg)


277\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101023000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101023000.0-6.4in_v1.svg)


278\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101214500.0-20010102001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101214500.0-20010102001500.0-6.4in_v1.svg)


279\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131214500.0-20010201001500.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131214500.0-20010201001500.0-6.4in_v1.svg)


280\.

![test/visual_test/latest/20010101000000.0-20010101030000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101030000.0-6.4in_v1.svg)


281\. Cross day boundary

![test/visual_test/latest/20010101211800.0-20010102001800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101211800.0-20010102001800.0-6.4in_v1.svg)


282\. Cross month boundary

![test/visual_test/latest/20010131211800.0-20010201001800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131211800.0-20010201001800.0-6.4in_v1.svg)


283\.

![test/visual_test/latest/20010101000000.0-20010101033000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101033000.0-6.4in_v1.svg)


284\. Cross day boundary

![test/visual_test/latest/20010101205100.0-20010102002100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101205100.0-20010102002100.0-6.4in_v1.svg)


285\. Cross month boundary

![test/visual_test/latest/20010131205100.0-20010201002100.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131205100.0-20010201002100.0-6.4in_v1.svg)


286\.

![test/visual_test/latest/20010101000000.0-20010101040000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101040000.0-6.4in_v1.svg)


287\. Cross day boundary

![test/visual_test/latest/20010101202400.0-20010102002400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101202400.0-20010102002400.0-6.4in_v1.svg)


288\. Cross month boundary

![test/visual_test/latest/20010131202400.0-20010201002400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131202400.0-20010201002400.0-6.4in_v1.svg)


289\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101050000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101050000.0-6.4in_v1.svg)


290\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101193000.0-20010102003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101193000.0-20010102003000.0-6.4in_v1.svg)


291\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131193000.0-20010201003000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131193000.0-20010201003000.0-6.4in_v1.svg)


292\.

![test/visual_test/latest/20010101000000.0-20010101060000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101060000.0-6.4in_v1.svg)


293\. Cross day boundary

![test/visual_test/latest/20010101183600.0-20010102003600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101183600.0-20010102003600.0-6.4in_v1.svg)


294\. Cross month boundary

![test/visual_test/latest/20010131183600.0-20010201003600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131183600.0-20010201003600.0-6.4in_v1.svg)


295\.

![test/visual_test/latest/20010101000000.0-20010101080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101080000.0-6.4in_v1.svg)


296\. Cross day boundary

![test/visual_test/latest/20010101164800.0-20010102004800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101164800.0-20010102004800.0-6.4in_v1.svg)


297\. Cross month boundary

![test/visual_test/latest/20010131164800.0-20010201004800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131164800.0-20010201004800.0-6.4in_v1.svg)


298\. (font size change: -1.2 pt)

![test/visual_test/latest/20010101000000.0-20010101100000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101100000.0-6.4in_v1.svg)


299\. Cross day boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010101150000.0-20010102010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101150000.0-20010102010000.0-6.4in_v1.svg)


300\. Cross month boundary (font size change: -1.2 pt)

![test/visual_test/latest/20010131150000.0-20010201010000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131150000.0-20010201010000.0-6.4in_v1.svg)


301\.

![test/visual_test/latest/20010101000000.0-20010101120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101120000.0-6.4in_v1.svg)


302\. Cross day boundary

![test/visual_test/latest/20010101131200.0-20010102011200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101131200.0-20010102011200.0-6.4in_v1.svg)


303\. Cross month boundary

![test/visual_test/latest/20010131131200.0-20010201011200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131131200.0-20010201011200.0-6.4in_v1.svg)


304\.

![test/visual_test/latest/20010101000000.0-20010101150000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101150000.0-6.4in_v1.svg)


305\. Cross day boundary

![test/visual_test/latest/20010101103000.0-20010102013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101103000.0-20010102013000.0-6.4in_v1.svg)


306\. Cross month boundary

![test/visual_test/latest/20010131103000.0-20010201013000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131103000.0-20010201013000.0-6.4in_v1.svg)


307\.

![test/visual_test/latest/20010101000000.0-20010101180000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101180000.0-6.4in_v1.svg)


308\. Cross day boundary

![test/visual_test/latest/20010101074800.0-20010102014800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101074800.0-20010102014800.0-6.4in_v1.svg)


309\. Cross month boundary

![test/visual_test/latest/20010131074800.0-20010201014800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131074800.0-20010201014800.0-6.4in_v1.svg)


310\.

![test/visual_test/latest/20010101000000.0-20010101210000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010101210000.0-6.4in_v1.svg)


311\. Cross day boundary

![test/visual_test/latest/20010101050600.0-20010102020600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101050600.0-20010102020600.0-6.4in_v1.svg)


312\. Cross month boundary

![test/visual_test/latest/20010131050600.0-20010201020600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131050600.0-20010201020600.0-6.4in_v1.svg)


313\.

![test/visual_test/latest/20010101000000.0-20010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102000000.0-6.4in_v1.svg)


314\. Cross month boundary

![test/visual_test/latest/20010131022400.0-20010201022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010131022400.0-20010201022400.0-6.4in_v1.svg)


315\.

![test/visual_test/latest/20010101000000.0-20010102040000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102040000.0-6.4in_v1.svg)


316\. Cross month boundary

![test/visual_test/latest/20010130224800.0-20010201024800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130224800.0-20010201024800.0-6.4in_v1.svg)


317\.

![test/visual_test/latest/20010101000000.0-20010102080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102080000.0-6.4in_v1.svg)


318\. Cross month boundary

![test/visual_test/latest/20010130191200.0-20010201031200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130191200.0-20010201031200.0-6.4in_v1.svg)


319\.

![test/visual_test/latest/20010101000000.0-20010102120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102120000.0-6.4in_v1.svg)


320\. Cross month boundary

![test/visual_test/latest/20010130153600.0-20010201033600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130153600.0-20010201033600.0-6.4in_v1.svg)


321\.

![test/visual_test/latest/20010101000000.0-20010102180000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010102180000.0-6.4in_v1.svg)


322\. Cross month boundary

![test/visual_test/latest/20010130101200.0-20010201041200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130101200.0-20010201041200.0-6.4in_v1.svg)


323\.

![test/visual_test/latest/20010101000000.0-20010103000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103000000.0-6.4in_v1.svg)


324\. Cross month boundary

![test/visual_test/latest/20010130044800.0-20010201044800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010130044800.0-20010201044800.0-6.4in_v1.svg)


325\.

![test/visual_test/latest/20010101000000.0-20010103080000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103080000.0-6.4in_v1.svg)


326\. Cross month boundary

![test/visual_test/latest/20010129213600.0-20010201053600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129213600.0-20010201053600.0-6.4in_v1.svg)


327\.

![test/visual_test/latest/20010101000000.0-20010103160000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010103160000.0-6.4in_v1.svg)


328\. Cross month boundary

![test/visual_test/latest/20010129142400.0-20010201062400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129142400.0-20010201062400.0-6.4in_v1.svg)


329\.

![test/visual_test/latest/20010101000000.0-20010104000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104000000.0-6.4in_v1.svg)


330\. Cross month boundary

![test/visual_test/latest/20010129071200.0-20010201071200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010129071200.0-20010201071200.0-6.4in_v1.svg)


331\.

![test/visual_test/latest/20010101000000.0-20010104120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010104120000.0-6.4in_v1.svg)


332\. Cross month boundary

![test/visual_test/latest/20010128202400.0-20010201082400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128202400.0-20010201082400.0-6.4in_v1.svg)


333\.

![test/visual_test/latest/20010101000000.0-20010105000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010105000000.0-6.4in_v1.svg)


334\. Cross month boundary

![test/visual_test/latest/20010128093600.0-20010201093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010128093600.0-20010201093600.0-6.4in_v1.svg)


335\.

![test/visual_test/latest/20010101000000.0-20010106000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010106000000.0-6.4in_v1.svg)


336\. Cross month boundary

![test/visual_test/latest/20010127120000.0-20010201120000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010127120000.0-20010201120000.0-6.4in_v1.svg)


337\. (font size change: -1.9 pt)

![test/visual_test/latest/20010101000000.0-20010107000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010107000000.0-6.4in_v1.svg)


338\. Cross month boundary (font size change: -1.9 pt)

![test/visual_test/latest/20010126142400.0-20010201142400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010126142400.0-20010201142400.0-6.4in_v1.svg)


339\.

![test/visual_test/latest/20010101000000.0-20010108000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010108000000.0-6.4in_v1.svg)


340\. Cross month boundary

![test/visual_test/latest/20010125164800.0-20010201164800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010125164800.0-20010201164800.0-6.4in_v1.svg)


341\.

![test/visual_test/latest/20010101000000.0-20010109000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010109000000.0-6.4in_v1.svg)


342\. Cross month boundary

![test/visual_test/latest/20010124191200.0-20010201191200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010124191200.0-20010201191200.0-6.4in_v1.svg)


343\.

![test/visual_test/latest/20010101000000.0-20010111000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010111000000.0-6.4in_v1.svg)


344\. Cross month boundary

![test/visual_test/latest/20010123000000.0-20010202000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010123000000.0-20010202000000.0-6.4in_v1.svg)


345\.

![test/visual_test/latest/20010101000000.0-20010113000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010113000000.0-6.4in_v1.svg)


346\. Cross month boundary

![test/visual_test/latest/20010121044800.0-20010202044800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010121044800.0-20010202044800.0-6.4in_v1.svg)


347\.

![test/visual_test/latest/20010101000000.0-20010115000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010115000000.0-6.4in_v1.svg)


348\. Cross month boundary

![test/visual_test/latest/20010119093600.0-20010202093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010119093600.0-20010202093600.0-6.4in_v1.svg)


349\.

![test/visual_test/latest/20010101000000.0-20010118000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010118000000.0-6.4in_v1.svg)


350\. Cross month boundary

![test/visual_test/latest/20010116164800.0-20010202164800.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010116164800.0-20010202164800.0-6.4in_v1.svg)


351\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010122000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010122000000.0-6.4in_v1.svg)


352\. Cross month boundary

![test/visual_test/latest/20010113022400.0-20010203022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010113022400.0-20010203022400.0-6.4in_v1.svg)


353\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010125000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010125000000.0-6.4in_v1.svg)


354\. Cross month boundary

![test/visual_test/latest/20010110093600.0-20010203093600.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010110093600.0-20010203093600.0-6.4in_v1.svg)


355\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010129000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010129000000.0-6.4in_v1.svg)


356\. Cross month boundary

![test/visual_test/latest/20010106191200.0-20010203191200.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010106191200.0-20010203191200.0-6.4in_v1.svg)


357\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010201000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010201000000.0-6.4in_v1.svg)


358\. Cross month boundary

![test/visual_test/latest/20010104022400.0-20010204022400.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010104022400.0-20010204022400.0-6.4in_v1.svg)


359\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010205000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010205000000.0-6.4in_v1.svg)


360\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010208000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010208000000.0-6.4in_v1.svg)


361\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010215000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010215000000.0-6.4in_v1.svg)


362\.

![test/visual_test/latest/20010101000000.0-20010222000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010222000000.0-6.4in_v1.svg)


363\.

![test/visual_test/latest/20010101000000.0-20010301000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010301000000.0-6.4in_v1.svg)


364\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010303000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010303000000.0-6.4in_v1.svg)


365\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010331000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010331000000.0-6.4in_v1.svg)


366\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010401000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010401000000.0-6.4in_v1.svg)


367\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010402000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010402000000.0-6.4in_v1.svg)


368\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010403000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010403000000.0-6.4in_v1.svg)


369\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010501000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010501000000.0-6.4in_v1.svg)


370\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010503000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010503000000.0-6.4in_v1.svg)


371\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010531000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010531000000.0-6.4in_v1.svg)


372\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20010601000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010601000000.0-6.4in_v1.svg)


373\.

![test/visual_test/latest/20010101000000.0-20010701000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010701000000.0-6.4in_v1.svg)


374\.

![test/visual_test/latest/20010101000000.0-20010704000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010704000000.0-6.4in_v1.svg)


375\.

![test/visual_test/latest/20010101000000.0-20010901000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20010901000000.0-6.4in_v1.svg)


376\.

![test/visual_test/latest/20010101000000.0-20011003000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20011003000000.0-6.4in_v1.svg)


377\.

![test/visual_test/latest/20010101000000.0-20020101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020101000000.0-6.4in_v1.svg)


378\.

![test/visual_test/latest/20010101000000.0-20020401000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020401000000.0-6.4in_v1.svg)


379\.

![test/visual_test/latest/20010101000000.0-20020402000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020402000000.0-6.4in_v1.svg)


380\.

![test/visual_test/latest/20010101000000.0-20020403000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020403000000.0-6.4in_v1.svg)


381\.

![test/visual_test/latest/20010101000000.0-20020701000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020701000000.0-6.4in_v1.svg)


382\.

![test/visual_test/latest/20010101000000.0-20020703000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020703000000.0-6.4in_v1.svg)


383\.

![test/visual_test/latest/20010101000000.0-20020704000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20020704000000.0-6.4in_v1.svg)


384\.

![test/visual_test/latest/20010101000000.0-20021001000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021001000000.0-6.4in_v1.svg)


385\.

![test/visual_test/latest/20010101000000.0-20021003000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20021003000000.0-6.4in_v1.svg)


386\.

![test/visual_test/latest/20010101000000.0-20030101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20030101000000.0-6.4in_v1.svg)


387\. (font size change: -0.4 pt)

![test/visual_test/latest/20010101000000.0-20040101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040101000000.0-6.4in_v1.svg)


388\. (font size change: -0.4 pt)

![test/visual_test/latest/20010101000000.0-20040102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20040102000000.0-6.4in_v1.svg)


389\. (font size change: -3.2 pt)

![test/visual_test/latest/20010101000000.0-20050101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20050101000000.0-6.4in_v1.svg)


390\.

![test/visual_test/latest/20010101000000.0-20060101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060101000000.0-6.4in_v1.svg)


391\.

![test/visual_test/latest/20010101000000.0-20060102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20060102000000.0-6.4in_v1.svg)


392\.

![test/visual_test/latest/20010101000000.0-20070101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070101000000.0-6.4in_v1.svg)


393\.

![test/visual_test/latest/20010101000000.0-20070102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20070102000000.0-6.4in_v1.svg)


394\.

![test/visual_test/latest/20010101000000.0-20080101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080101000000.0-6.4in_v1.svg)


395\.

![test/visual_test/latest/20010101000000.0-20080102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20080102000000.0-6.4in_v1.svg)


396\.

![test/visual_test/latest/20010101000000.0-20090101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20090101000000.0-6.4in_v1.svg)


397\.

![test/visual_test/latest/20010101000000.0-20100101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20100101000000.0-6.4in_v1.svg)


398\. (font size change: -3.5 pt)

![test/visual_test/latest/20010101000000.0-20110101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110101000000.0-6.4in_v1.svg)


399\. (font size change: -3.5 pt)

![test/visual_test/latest/20010101000000.0-20110102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20110102000000.0-6.4in_v1.svg)


400\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20160101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20160101000000.0-6.4in_v1.svg)


401\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20160102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20160102000000.0-6.4in_v1.svg)


402\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-20210101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20210101000000.0-6.4in_v1.svg)


403\.

![test/visual_test/latest/20010101000000.0-20260101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260101000000.0-6.4in_v1.svg)


404\.

![test/visual_test/latest/20010101000000.0-20260102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20260102000000.0-6.4in_v1.svg)


405\.

![test/visual_test/latest/20010101000000.0-20310101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310101000000.0-6.4in_v1.svg)


406\.

![test/visual_test/latest/20010101000000.0-20310102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20310102000000.0-6.4in_v1.svg)


407\.

![test/visual_test/latest/20010101000000.0-20360101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360101000000.0-6.4in_v1.svg)


408\.

![test/visual_test/latest/20010101000000.0-20360102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20360102000000.0-6.4in_v1.svg)


409\.

![test/visual_test/latest/20010101000000.0-20401231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20401231000000.0-6.4in_v1.svg)


410\.

![test/visual_test/latest/20010101000000.0-20410101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20410101000000.0-6.4in_v1.svg)


411\.

![test/visual_test/latest/20010101000000.0-20510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510101000000.0-6.4in_v1.svg)


412\.

![test/visual_test/latest/20010101000000.0-20510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20510102000000.0-6.4in_v1.svg)


413\.

![test/visual_test/latest/20010101000000.0-20601231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20601231000000.0-6.4in_v1.svg)


414\.

![test/visual_test/latest/20010101000000.0-20610101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20610101000000.0-6.4in_v1.svg)


415\.

![test/visual_test/latest/20010101000000.0-20710101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710101000000.0-6.4in_v1.svg)


416\.

![test/visual_test/latest/20010101000000.0-20710102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20710102000000.0-6.4in_v1.svg)


417\.

![test/visual_test/latest/20010101000000.0-20801231000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20801231000000.0-6.4in_v1.svg)


418\.

![test/visual_test/latest/20010101000000.0-20810101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20810101000000.0-6.4in_v1.svg)


419\. (font size change: -0.1 pt)

![test/visual_test/latest/20010101000000.0-20910101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910101000000.0-6.4in_v1.svg)


420\. (font size change: -0.1 pt)

![test/visual_test/latest/20010101000000.0-20910102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-20910102000000.0-6.4in_v1.svg)


421\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-21010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010101000000.0-6.4in_v1.svg)


422\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-21010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21010102000000.0-6.4in_v1.svg)


423\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-21510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21510101000000.0-6.4in_v1.svg)


424\. (font size change: -3.9 pt)

![test/visual_test/latest/20010101000000.0-21510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-21510102000000.0-6.4in_v1.svg)


425\.

![test/visual_test/latest/20010101000000.0-22010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010101000000.0-6.4in_v1.svg)


426\.

![test/visual_test/latest/20010101000000.0-22010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-22010102000000.0-6.4in_v1.svg)


427\.

![test/visual_test/latest/20010101000000.0-23010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010101000000.0-6.4in_v1.svg)


428\.

![test/visual_test/latest/20010101000000.0-23010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-23010102000000.0-6.4in_v1.svg)


429\.

![test/visual_test/latest/20010101000000.0-24010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-24010101000000.0-6.4in_v1.svg)


430\. (font size change: -0.1 pt)

![test/visual_test/latest/20010101000000.0-25010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010101000000.0-6.4in_v1.svg)


431\. (font size change: -0.1 pt)

![test/visual_test/latest/20010101000000.0-25010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-25010102000000.0-6.4in_v1.svg)


432\. (font size change: -2.0 pt)

![test/visual_test/latest/20010101000000.0-27510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-27510102000000.0-6.4in_v1.svg)


433\.

![test/visual_test/latest/20010101000000.0-30010101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010101000000.0-6.4in_v1.svg)


434\.

![test/visual_test/latest/20010101000000.0-30010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-30010102000000.0-6.4in_v1.svg)


435\.

![test/visual_test/latest/20010101000000.0-32510101000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-32510101000000.0-6.4in_v1.svg)


436\.

![test/visual_test/latest/20010101000000.0-32510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-32510102000000.0-6.4in_v1.svg)


437\.

![test/visual_test/latest/20010101000000.0-35010102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-35010102000000.0-6.4in_v1.svg)


438\.

![test/visual_test/latest/20010101000000.0-37510102000000.0-6.4in_v1.svg](https://raw.githubusercontent.com/rweigel/datetick/main/test/visual_test/latest/20010101000000.0-37510102000000.0-6.4in_v1.svg)