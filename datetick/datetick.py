def datetick(*args,
             axes=None,
             set_cb=True,
             adjust_last_xlabel=False,
             adjust_first_xlabel=False,
             debug=False, **kwargs):
  """
  datetick('x') or datetick('y') formats the major and minor tick labels
  of the current figure.

  datetick('x', axes=ax) or datetick('y', axes=ax) formats the given axes `ax`.

  Example:
  --------
    import datetime as dt
    import matplotlib.pyplot as plt
    from datetick import datetick
    d1 = dt.datetime(1900, 1, 2)
    d2 = dt.datetime.fromordinal(10 + dt.datetime.toordinal(d1))
    x = [d1, d2]
    y = [0.0,1.0]
    plt.clf()
    plt.plot(x, y)
    datetick('x')
  """

  # Based on spacepy/plot/utils.py on 07/10/2017, but many additions.
  # See also https://github.com/JouleCai/geospacelab/blob/master/geospacelab/visualization/mpl/axis_ticks.py

  # TODO: Use numsize() to determine if figure width and height
  #       will cause overlap when default number major tick labels is used.
  # TODO: If time[0].day > 28, need to make first tick at time[0].day = 28
  #       as needed.
  # TODO: If first data point has fractional seconds, the plot won't have
  #       a major x-label right below it. This is due to the fact that
  #       MicrosecondLocator() does not take a keyword argument of
  #       "bymicroseconds".
  # TODO: Adjust lower and upper limits as in 366*8 span

  # Get all kwargs passed using locals
  kwargs = {k: v for k, v in locals().items() if k != 'args'}

  import warnings
  from datetime import datetime

  import matplotlib
  import matplotlib.dates as mpld

  if matplotlib.get_backend() == 'MacOSX':
    # With MacOSX backend, draw() does not update the ticks. See warning at
    # https://matplotlib.org/3.3.0/tutorials/advanced/blitting.html
    import sys
    if sys.version_info[0:2] < (3, 6):
      # warnings.filterwarnings("ignore", '.*backend.*', category=UserWarning)
      # the above should work and is better because more specific.
      warnings.simplefilter("ignore", category=UserWarning)
    gui_env = ['Qt5Agg', 'QT4Agg', 'GTKAgg', 'TKAgg', 'WXAgg']
    for gui in gui_env:
      cmd = f"matplotlib.use('{gui}', force=True)"
      try:
        if debug:
          print(f"Trying {cmd}")
        matplotlib.use(gui, force=True)
        import matplotlib.pyplot as plt
        if debug:
          print("  Success.")
        break
      except:
        if debug:
          print(" Failure.")
        continue
  else:
    try:
      import matplotlib.pyplot as plt
    except:
      print('Failed: import matplotlib.pyplot as plt')
      gui_env = ['Qt5Agg','QT4Agg','GTKAgg','TKAgg','WXAgg']
      cmd = f"matplotlib.use('{gui}', force=True)"
      for gui in gui_env:
        try:
          if debug:
            print(f"Trying {cmd}")
          matplotlib.use(gui, force=True)
          import matplotlib.pyplot as plt
          if debug:
            print("  Success.")
          break
        except:
          if debug:
            print(" Failure.")
          continue

  def millis(x, pos):
    x = matplotlib.dates.num2date(x)
    label = x.strftime('.%f')
    label = label[0:3]
    #label = label.rstrip(".")
    return label

  def on_xlims_change(ax):
    datetick('x', **{**kwargs, 'set_cb': False})

  def on_ylims_change(ax):
    datetick('y', **{**kwargs, 'set_cb': False})

  def draw(fig):
    fig.canvas.draw()

  if len(args) == 0:
    dir = 'x'
  else:
    dir = args[0]

  if 'axes' in kwargs:
    axes = kwargs['axes']
    fig = axes.figure
  else:
    axes = plt.gca()
    fig = plt.gcf()

  draw(fig)
  bbox = axes.dataLim

  if dir == 'x':
    datamin = bbox.x0
    datamax = bbox.x1
    lim = axes.get_xlim()
    ticks = axes.get_xticks()
  else:
    datamin = bbox.y0
    datamax = bbox.y1
    lim = axes.get_ylim()
    ticks = axes.get_yticks()

  try:
    mpld.num2date(lim[0])
  except:
    raise ValueError('Lower axis limit of %f is not a valid Matplotlib datenum' % lim[0])
  try:
    mpld.num2date(lim[1])
  except:
    raise ValueError('Upper axis limit of %f is not a valid Matplotlib datenum' % lim[1])

  # If all values are NaN, datamin = np.inf and datamax = -np.inf.
  msg = "is not a valid Matplotlib datenum. Are all data values NaN? Cannot use datetick()"
  try:
    mpld.num2date(datamin)
  except:
    warnings.warn(f'Minimum value of %f {msg}' % datamin)
    return
  try:
    mpld.num2date(datamax)
  except:
    warnings.warn(f'Maximum value of %f {msg}' % datamax)
    return

  # Need to document why this was used. It creates
  # problems if labels extend beyond the axis limits.
  #tmin = np.min((lim[0], datamin))
  #tmax = np.max((lim[1], datamax))
  tmin = lim[0]
  tmax = lim[1]

  time = mpld.num2date((tmin,tmax))

  if datamin == datamax:
    axes.set_xticks([mpld.num2date(datamin)])
    axes.set_xticklabels([datetime.strftime(mpld.num2date(datamin),'%Y-%m-%dT%H:%M:%S')])
    return

  deltaT = time[-1] - time[0]
  nDays  = deltaT.days
  nHours = deltaT.days * 24.0 + deltaT.seconds/3600.0
  nSecs  = deltaT.total_seconds()
  if debug:
    print("Total seconds: %s" % deltaT.total_seconds())

  """
  fmt1 is format of the tick labels

  fmt2 contains additional information that is used for the first tick label
  or when there is a major change. For example, if
    fmt1 = %M:%S and fmt2 = %H,
  the labels will have only minute and hour and the first tick will have a
  label of %M:%S\n%H. If there is a change in hour somewhere on the axis,
  that label will include the new hour.

  Note that interval=... is specified even when it would seem to be redundant.
  It is needed to workaround the bug discussed at stackoverflow.com/q/31072589
  """

  if deltaT.total_seconds() < 0.1:
    # < 0.1 second
    Mtick = mpld.MicrosecondLocator(interval=10000)
    mtick = mpld.MicrosecondLocator(interval=2000)
    fmt1 = matplotlib.ticker.FuncFormatter(millis)
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
  if deltaT.total_seconds() < 0.5:
    # < 0.5 seconds
    # Locators don't locate at this resolution.
    # Need to do this manually. See comment above.
    Mtick = mpld.MicrosecondLocator(interval=50000)
    mtick = mpld.MicrosecondLocator(interval=10000)
    fmt1 = matplotlib.ticker.FuncFormatter(millis)
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
  if deltaT.total_seconds() < 1:
    # < 1 second
    # https://matplotlib.org/api/dates_api.html#matplotlib.dates.MicrosecondLocator
    # MircosecondLocator() does not have a "bymicrosecond" option. If
    # first point is not at zero microseconds, it won't be labeled.
    Mtick = mpld.MicrosecondLocator(interval=100000)
    mtick = mpld.MicrosecondLocator(interval=20000)
    fmt1 = matplotlib.ticker.FuncFormatter(millis)
    #fmt1  = mpld.DateFormatter('%M:%S.%f')
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
  elif deltaT.total_seconds() < 5:
    # < 5 seconds
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    mtick = mpld.MicrosecondLocator(interval=200000)
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 10:
    # < 10 seconds
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    mtick = mpld.MicrosecondLocator(interval=500000)
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 20:
    # < 20 seconds
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 2)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 30:
    # < 30 seconds
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60:
    # < 1 minute
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 10)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 2)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*2:
    # < 2 minutes
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 20)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*3:
    # < 3 minutes
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 20)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*5:
    # < 5 minutes
    Mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 30)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 10)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*10:
    # < 10 minutes
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 1)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 15)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*20:
    # < 20 minutes
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 2)) )
    mtick = mpld.SecondLocator(bysecond=list(range(0, 60, 30)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
  elif deltaT.total_seconds() < 60*30:
    # < 30 minutes
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif deltaT.total_seconds() < 60*60:
    # < 60 minutes
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 10)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 2)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif nHours < 2:
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 15)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif nHours < 4:
    Mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 20)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif nHours < 6:
    Mtick = mpld.HourLocator(byhour=list(range(0,24,1)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 10)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif nHours < 12:
    Mtick = mpld.HourLocator(byhour=list(range(0,24,2)) )
    mtick = mpld.MinuteLocator(byminute=list(range(0, 60, 30)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
  elif nHours < 24:
    # < 1 day
    Mtick = mpld.HourLocator(byhour=list(range(0, 24, 3)) )
    mtick = mpld.HourLocator(byhour=list(range(0, 24, 1)) )
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
  elif nHours < 48:
    # < 2 days
    Mtick = mpld.HourLocator(byhour=list(range(0, 24, 4)) )
    mtick = mpld.HourLocator(byhour=list(range(0, 24, 2)) )
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
  elif nHours < 72:
    # < 3 days
    Mtick = mpld.HourLocator(byhour = list(range(0, 24, 6)))
    mtick = mpld.HourLocator(byhour = list(range(0, 24, 3)))
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
  elif nHours < 96:
    # < 4 days
    Mtick = mpld.HourLocator(byhour = list(range(0, 24, 12)))
    mtick = mpld.HourLocator(byhour = list(range(0, 24, 3)))
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
  elif deltaT.days < 8:
    Mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    mtick = mpld.HourLocator(byhour=list(range(0, 24, 4)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
  elif deltaT.days < 16:
    Mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
  elif deltaT.days < 32:
    Mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 4)))
    mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
  elif deltaT.days < 60:
    Mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 7)))
    mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
  elif deltaT.days < 183:
    Mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    mtick = mpld.DayLocator(bymonthday=list(range(1, 32, 7)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
  elif deltaT.days < 367:
    Mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
  elif deltaT.days < 366*2:
    Mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 2)))
    mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
  elif deltaT.days < 366*8:
    Mtick = mpld.YearLocator(1)
    mtick = mpld.MonthLocator(bymonth=list(range(1, 13, 4)))
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
  elif deltaT.days < 366*15:
    to = axes.lines[0].get_xdata()[0]
    tf = axes.lines[0].get_xdata()[-1]
    # Ideally would set byyear=list(range(to.year, tf.year,2)) but
    # byyear is not a kwarg. Would need to something like
    # https://stackoverflow.com/questions/48428729/matplotlib-dates-yearlocator-with-odd-intervals
    Mtick = mpld.YearLocator(1)
    mtick = mpld.YearLocator(1)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    if False:
      xl = axes.get_xlim()
      a = mpld.num2date(xl[0])
      print(a)
      import pdb;pdb.set_trace()
      a = mpld.date2num(a.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0))
      b = mpld.num2date(xl[1])
      b = mpld.date2num(b.replace(year=(b.year+1), month=1, day=1, hour=0, minute=0, second=0, microsecond=0))
      axes.set_xlim([a, b])
  elif deltaT.days < 366*40:
    Mtick = mpld.YearLocator(5)
    mtick = mpld.YearLocator(1)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
  elif deltaT.days < 366*100:
    Mtick = mpld.YearLocator(10)
    mtick = mpld.YearLocator(2)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
  elif deltaT.days < 366*200:
    Mtick = mpld.YearLocator(20)
    mtick = mpld.YearLocator(5)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
  else:
    Mtick = mpld.YearLocator(50)
    mtick = mpld.YearLocator(10)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''

  if debug:
    print(f'{dir} data min:         {mpld.num2date(datamin)}')
    print(f'Default {dir}lim[0]:    {mpld.num2date(lim[0])}')
    print(f'Default {dir}ticks[0]:  {mpld.num2date(ticks[0])}')
    print(f'{dir} data max:         {mpld.num2date(datamax)}')
    print(f'Default {dir}lim[-1]:   {mpld.num2date(lim[-1])}')
    print(f'Default {dir}ticks[-1]: {mpld.num2date(ticks[-1])}')
    print(f'Default {dir}ticks:')
    for i in range(0,len(ticks)):
      print(f' {mpld.num2date(ticks[i])}')

  if dir == 'x':
    axes.xaxis.set_major_locator(Mtick)
    axes.xaxis.set_minor_locator(mtick)
    axes.xaxis.set_major_formatter(fmt1)
    draw(fig) # Render new labels so updated for next line
    labels = [item.get_text() for item in axes.get_xticklabels()]
    ticks = axes.get_xticks()
    time = mpld.num2date(ticks)
  else:
    axes.yaxis.set_major_locator(Mtick)
    axes.yaxis.set_minor_locator(mtick)
    axes.yaxis.set_major_formatter(fmt1)
    draw(fig) # Render new labels so updated for next line
    labels = [item.get_text() for item in axes.get_yticklabels()]
    ticks = axes.get_yticks()
    time = mpld.num2date(ticks)

  if debug:
    xl = axes.get_xlim()
    print(f'New {dir}ticks:')
    for i in range(0,len(ticks)):
      note = ''
      if ticks[i] < xl[0] or ticks[i] > xl[1]:
        note = ' (will be clipped by mpl b/c outside of axis limits)'
      print(f' {mpld.num2date(ticks[i])} {note}')

  if len(labels) == 0:
    if debug:
      print('No labels to format')
    return

  if fmt2 != '':
    first = 0
    if ticks[0] < lim[0]:
      # Work-around for bug in Matplotlib where left-most tick is less than
      # lower x-limit.
      first = 1

    # Always apply fmt2 to first tick label
    labels[first] = '%s\n%s' % (labels[first], datetime.strftime(time[first], fmt2))

    for i in range(first+1, len(time)):
      # First label will always have fmt1 applied.
      # Modify labels after first under certain conditions.
      modify = False

      if time[i].year > time[i-1].year:
        modify = True
      if nDays < 60 and time[i].month > time[i-1].month:
        modify = True
      if nDays < 4 and time[i].day > time[i-1].day:
        modify = True
      if nSecs < 60*30 and time[i].hour > time[i-1].hour:
        modify = True
      if nSecs < 1 and time[i].minute > time[i-1].minute:
        modify = True
      if nSecs < 1 and time[i].second > time[i-1].second:
        modify = True

      if not modify:
        continue

      if i == first + 1 and dir == 'x':
        # If first two major tick labels have fmt2 applied, the will
        # likely run together. This keeps fmt2 label for second major
        # tick.
        #labels[i] = '%s\n%s' % (labels[i], datetime.strftime(mpld.num2date(ticks[i]), fmt2))
        pass
      else:
        labels[i] = '%s\n%s' % (labels[i], datetime.strftime(mpld.num2date(ticks[i]), fmt2))

    # Without the set_xticks(), warning is generated:
    #   UserWarning: set_ticklabels() should only be used.
    # Additional discussion: https://github.com/matplotlib/matplotlib/issues/18848
    # The correct way to avoid the warning: https://stackoverflow.com/a/69126185
    # Better: Create custom class:
    #   https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html
    if dir == 'x':
      axes.set_xticks(axes.get_xticks())
      axes.set_xticklabels(labels)
    if dir == 'y':
      axes.set_yticks(axes.get_yticks())
      axes.set_yticklabels(labels)

    if dir == 'x':
      xticklabels = axes.get_xticklabels()
      lastlabel_text = xticklabels[-1].get_text()
      firstlabel_text = xticklabels[0].get_text()
      adjusted = False

      if adjust_first_xlabel and '\n' in firstlabel_text:
        if len(firstlabel_text.split('\n')[-1]) > 7:
          if debug:
            print(f'Adjusting first x-label: "{firstlabel_text.replace("\n", "\\n")}"')
          adjusted = True
          # If fmt1 in first label longer than YYYY-MM, set justification to left.
          xticklabels[0].set_ha('left')
          # Shift to right by 1/2 width of fmt1 in first label.
          first_fmt1 = firstlabel_text.split('\n')[0]
          offset = numsize(axes, first_fmt1, +1, debug=debug)
          xticklabels[0].set_transform(xticklabels[0].get_transform() - offset)

      if adjust_last_xlabel and '\n' in lastlabel_text:
        if len(lastlabel_text.split('\n')[-1]) > 7:
          if debug:
            print(f'Adjusting last x-label: "{lastlabel_text.replace("\n", "\\n")}"')
          adjusted = True
          # If fmt1 iin last label longer than YYYY-MM, set justification to right.
          xticklabels[-1].set_ha('right')
          # Shift to left by 1/2 width of fmt1 in last label.
          last_fmt1 = lastlabel_text.split('\n')[0]
          offset = numsize(axes, last_fmt1, -1, debug=debug)
          xticklabels[-1].set_transform(xticklabels[-1].get_transform() - offset)

      if adjusted:
        # Make all labels without newline slightly smaller than default fontsize 
        # so it is clearer that fmt2 applies to larger number.
        if debug:
          print('Adjusting font size of x-labels without newline')
        for label in xticklabels:
          if '\n' not in label.get_text():
            label.set_fontsize(label.get_fontsize()*0.85)

  # Trigger update of ticks when limits change due to user interaction.
  if 'set_cb':
    if dir == 'x':
      axes.callbacks.connect('xlim_changed', on_xlims_change)
    else:
      axes.callbacks.connect('ylim_changed', on_ylims_change)

def numsize(ax, num, sign, debug=False):
  '''Returns (width, height) of str(num) in pixels.

  If ax is given, measures against that axes' renderer and DPI (correct).
  Otherwise creates a temporary figure using rcParams figure.dpi.
  '''
  import re
  import matplotlib
  import matplotlib.figure
  import matplotlib.backends.backend_agg

  num = str(num)

  #dpi = ax.figure.get_dpi() if ax is not None else matplotlib.rcParams['figure.dpi']
  dpi = 72 # Why not use above dpi? On OS-X when dpi = 200 is returned, offset is wrong.
  fig = matplotlib.figure.Figure(dpi=dpi)
  canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(fig)
  ax_tmp = fig.add_subplot(111)
  renderer = canvas.get_renderer()
  fontsize = matplotlib.rcParams['xtick.labelsize']
  t = ax_tmp.text(0.5, 0.5, num, fontsize=fontsize)

  w, h, d = renderer.get_text_width_height_descent(num, t.get_fontproperties(), ismath=False)
  dpi = ax.figure.get_dpi() if ax is not None else matplotlib.rcParams['figure.dpi']
  delta = w/len(num)
  # It seems like sign should not be needed, but does not work if
  # + offset instead of - offset is used code that uses offset.
  offset =  matplotlib.transforms.ScaledTranslation(sign*delta/dpi, 0, ax.figure.dpi_scale_trans)

  if debug:
    print('numsize():')
    print(f'  num      = "{num}"')
    print(f'  fontsize = {fontsize}')
    print(f'  dpi      = {dpi}')
    print(f'  width    = {w}')
    print(f'  height   = {h}')
    print(f'  descent  = {d}')
    print(f'  delta    = {delta}')
    print(f'  offset   = {re.sub(r"\n\s+", "", str(offset))}')

  return offset
