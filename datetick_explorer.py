# -*- coding: utf-8 -*-
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from datetick import datetick


def get_datetime(sliders):
    return datetime.datetime(*[int(s.val) for s in sliders])

def update(val):
    xlow  = get_datetime(sliders_i)
    xhigh = get_datetime(sliders_f)
    print(f"---Update to {xlow.isoformat()} to {xhigh.isoformat()}---")
    plotit(xlow, xhigh)

def reset(event):
    for s in sliders_i + sliders_f:
        s.reset()
    update(None)

def plotit(xlow, xhigh):
    if xlow >= xhigh:
        return
    x = np.array([xlow, xhigh], dtype=object)
    title = xlow.isoformat() + ' to ' + xhigh.isoformat()

    print("---Updating matplotlib plot")
    plt1.set_xdata(x)
    ax1.set_xlim(xlow, xhigh)
    ax1.set_title(title, loc='center', y=1, pad=-14)

    print("---Updating datetick plot")
    plt2.set_xdata(x)
    ax2.set_xlim(xlow, xhigh)


subplots_bottom = 0.25   # fraction of figure height reserved for sliders
slider_left    = 0.15                        # left edge of first slider column
slider_gap     = 0.4                         # horizontal gap between start and end columns
slider_width   = 0.3                         # width of each slider
slider_height  = 0.02                        # height of each slider
n_slider_rows  = 6
slider_row_gap = (subplots_bottom * 0.85) / n_slider_rows   # row spacing fits rows in reserved area
slider_bottom  = 0.1          # bottom margin ≈ half a row gap

reset_left   = 0.47
reset_width  = 0.05
reset_height = 0.02
slider_top   = slider_bottom + (n_slider_rows - 1) * slider_row_gap + slider_height
reset_bottom = slider_top + 0.03   # just above top slider row


ds1 = '1999-01-01T00:00:00'
ds2 = '1999-01-01T02:00:00'
dt1 = datetime.datetime.fromisoformat(ds1)
dt2 = datetime.datetime.fromisoformat(ds2)
x = np.array([dt1, dt2], dtype=object)
y = [0.0, 0.0]

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(16, 9))
plt.subplots_adjust(bottom=subplots_bottom)

plt1, = ax1.plot(x, y, '*')
ax1.set_title('matplotlib', loc='left', y=1, pad=-14)
ax1.set_title(ds1 + ' - ' + ds2, loc='center', y=1, pad=-14)
ax1.grid()

plt2, = ax2.plot(x, y, '*')
ax2.set_title('datetick', loc='left', y=1, pad=-14)
datetick('x', axes=ax2, debug=True)
ax2.grid()

ax3.axis('off')

# Slider definitions: (label, min, max, valinit)
slider_defs_i = [
    ('Year',   1900, 2100, 1999),
    ('Month',  1,    12,   1),
    ('Day',    1,    31,   1),
    ('Hour',   0,    23,   0),
    ('Minute', 0,    59,   0),
    ('Second', 0,    59,   0),
]
slider_defs_f = [
    ('Year',   1900, 2100, 1999),
    ('Month',  1,    12,   1),
    ('Day',    1,    31,   1),
    ('Hour',   0,    23,   2),
    ('Minute', 0,    59,   0),
    ('Second', 0,    59,   0),
]

slider_list = [(slider_defs_i, []), (slider_defs_f, [])]


for col, (defs, sliders) in enumerate(slider_list):
  x0 = slider_left + col * slider_gap
  for row, (label, vmin, vmax, vinit) in enumerate(reversed(defs)):
    ax_s = plt.axes([x0, slider_bottom + row * slider_row_gap, slider_width, slider_height])
    s = Slider(ax_s, label, vmin, vmax, valinit=vinit, valfmt='%0.0f')
    s.on_changed(update)
    sliders.insert(0, s)

sliders_i, sliders_f = slider_list[0][1], slider_list[1][1]

axreset = plt.axes([reset_left, reset_bottom, reset_width, reset_height])
breset = Button(axreset, 'Reset')
breset.on_clicked(reset)

plt.show()
