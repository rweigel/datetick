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