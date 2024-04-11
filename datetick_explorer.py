# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:09:42 2018

@author: Brendan
"""

import dateutil.parser
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import datetime

from datetick import datetick

def update(val):

    YI = sYearI.val
    mI = sMonthI.val
    DI = sDayI.val
    HI = sHourI.val
    MI = sMinuteI.val
    SI = sSecondI.val

    YF = sYearF.val
    mF = sMonthF.val
    DF = sDayF.val
    HF = sHourF.val
    MF = sMinuteF.val
    SF = sSecondF.val

    xlow = datetime.datetime(int(YI), int(mI), int(DI), int(HI), int(MI), int(SI))
    xhigh = datetime.datetime(int(YF), int(mF), int(DF), int(HF), int(MF), int(SF))
    print(f"---Update to {xlow.isoformat()} to {xhigh.isoformat()}---")
    plotit(xlow,xhigh)

def reset(event):
    sYearI.reset()
    sMonthI.reset()
    sDayI.reset()
    sHourI.reset()
    sMinuteI.reset()
    sSecondI.reset()

    sYearF.reset()
    sMonthF.reset()
    sDayF.reset()
    sHourF.reset()
    sMinuteF.reset()
    sSecondF.reset()

    YI = sYearI.val
    mI = sMonthI.val
    DI = sDayI.val
    HI = sHourI.val
    MI = sMinuteI.val
    SI = sSecondI.val

    YF = sYearF.val
    mF = sMonthF.val
    DF = sDayF.val
    HF = sHourF.val
    MF = sMinuteF.val
    SF = sSecondF.val

    xlow = datetime.datetime(int(YI), int(mI), int(DI), int(HI), int(MI), int(SI))
    xhigh = datetime.datetime(int(YF), int(mF), int(DF), int(HF), int(MF), int(SF))
    plotit(xlow,xhigh)

def plotit(xlow, xhigh):
    global ax1,ax2,plt1,plt2

    if xlow >= xhigh:
        return

    x = np.array([xlow, xhigh], dtype=object)

    print(f"---Updating matplotlib plot")
    ax1.set_title(xlow.isoformat() + " to " + xhigh.isoformat(), loc='center', y=1, pad=-14)
    ax1.set_title('matplotlib', loc='left', y=1, pad=-14)

    plt1.set_xdata(x)
    ax1.set_xlim(xlow, xhigh)

    print(f"---Updating datetick plot")
    plt2.set_xdata(x)
    ax2.set_title('datetick', loc='left', y=1, pad=-14)
    ax2.set_xlim(xlow, xhigh)

# Globals
ax1 = None
t1 = None


y = [0.0, 0.0]

ds1 = '1999-01-01T00:00:00Z'
ds2 = '1999-01-01T02:00:00Z'
dt1 = dateutil.parser.parse(ds1)
dt2 = dateutil.parser.parse(ds2)
x = np.array([dt1,dt2], dtype=object)

plt.subplots_adjust(bottom=0.4)
fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(16,9))

plt1, = ax1.plot(x, y, '*')
ax1.set_title('matplotlib', loc='left', y=1, pad=-14)
ax1.set_title(ds1 + ' - ' + ds2, loc='center', y=1, pad=-14)
ax1.grid()

plt2, = ax2.plot(x, y, '*')
ax2.set_title('datetick', loc='left', y=1, pad=-14)
datetick('x', axes=ax2, debug=True)
ax2.grid()

ax3.axis('off')

# designate axes object for sliders
axYearI = plt.axes([0.15, 0.23, 0.3, 0.02])
axMonthI = plt.axes([0.15, 0.19, 0.3, 0.02])
axDayI = plt.axes([0.15, 0.15, 0.3, 0.02])
axHourI = plt.axes([0.15, 0.11, 0.3, 0.02])
axMinuteI = plt.axes([0.15, 0.07, 0.3, 0.02])
axSecondI = plt.axes([0.15, 0.03, 0.3, 0.02])

axYearF = plt.axes([0.55, 0.23, 0.3, 0.02])
axMonthF = plt.axes([0.55, 0.19, 0.3, 0.02])
axDayF = plt.axes([0.55, 0.15, 0.3, 0.02])
axHourF = plt.axes([0.55, 0.11, 0.3, 0.02])
axMinuteF = plt.axes([0.55, 0.07, 0.3, 0.02])
axSecondF = plt.axes([0.55, 0.03, 0.3, 0.02])

axStart = plt.axes([0.23, 0.27, 0.15, 0.03])
axEnd = plt.axes([0.63, 0.27, 0.15, 0.03])

axreset = plt.axes([0.47, 0.29, 0.05, 0.05])

# make sliders and add update function
sYearI = Slider(axYearI, 'Year', 1900, 2100, valinit=1999, valfmt='%0.0f')
sYearI.on_changed(update)
sMonthI = Slider(axMonthI, 'Month', 1, 12, valinit=1, valfmt='%0.0f')
sMonthI.on_changed(update)
sDayI = Slider(axDayI, 'Day', 1, 31, valinit=1, valfmt='%0.0f')
sDayI.on_changed(update)
sHourI = Slider(axHourI, 'Hour', 0, 23, valinit=1, valfmt='%0.0f')
sHourI.on_changed(update)
sMinuteI = Slider(axMinuteI, 'Minute', 0, 59, valinit=0, valfmt='%0.0f')
sMinuteI.on_changed(update)
sSecondI = Slider(axSecondI, 'Second', 0, 59, valinit=0, valfmt='%0.0f')
sSecondI.on_changed(update)

sYearF = Slider(axYearF, 'Year', 1900, 2100, valinit=1999, valfmt='%0.0f')
sYearF.on_changed(update)
sMonthF = Slider(axMonthF, 'Month', 1, 12, valinit=1, valfmt='%0.0f')
sMonthF.on_changed(update)
sDayF = Slider(axDayF, 'Day', 1, 31, valinit=1, valfmt='%0.0f')
sDayF.on_changed(update)
sHourF = Slider(axHourF, 'Hour', 0, 23, valinit=2, valfmt='%0.0f')
sHourF.on_changed(update)
sMinuteF = Slider(axMinuteF, 'Minute', 0, 59, valinit=0, valfmt='%0.0f')
sMinuteF.on_changed(update)
sSecondF = Slider(axSecondF, 'Second', 0, 59, valinit=0, valfmt='%0.0f')
sSecondF.on_changed(update)

bStart = Button(axStart, 'Start',color='1.0',hovercolor='1.0')
bEnd = Button(axEnd, 'End',color='1.0',hovercolor='1.0')

breset = Button(axreset, 'Reset')
breset.on_clicked(reset)
plt.show()
