"""
  datetick formats the major and minor tick labels.
"""
def datetick(*args,
             axes=None,
             adjust_last_xlabel=False,
             adjust_first_xlabel=False,
             adjust_xrange=False,
             adjust_yrange=False,
             major_font_shrink_factor=0.87,
             major_font_shrink_always=False,
             set_cb=True,
             debug=False):
  """
  datetick() formats the major and minor x-tick labels of the current figure.

  datetick('x') or datetick('y') formats the x- or y- labels

  datetick('x', axes=ax) or datetick('y', axes=ax) formats the given axis `ax`.

  Example:
  --------
    import datetime as dt
    import matplotlib.pyplot as plt
    from datetick import datetick
    d1 = dt.datetime(1900, 1, 2)
    d2 = dt.datetime.fromordinal(10 + dt.datetime.toordinal(d1))
    x = [d1, d2]
    y = [0.0,1.0]
    plt.plot(x, y)
    datetick('x')
    plt.show()

  Keywords:
  --------
  adjust_last_xlabel: If True, adjust last x-label to avoid extending past lower axis limit.
  adjust_first_xlabel: If True, adjust first x-label to avoid extending past upper axis limit.

  adjust_xrange: If True, expand x-range so data are always within a major tick.
  adjust_yrange: If True, expand y-range so data are always within a major tick.

  major_font_shrink_factor: If adjust_first_xlabel or adjust_last_xlabel is True,
                      shrink font size of x-labels without newline by this
                      factor to make it clearer label is attached to tick above
                      it even when not centered.

  major_font_shrink_always: If True, shrink font size of x-labels without newline by
                      major_font_shrink_factor even if adjust_{first,last}_xlabel is False.

  debug: If True, print debug information.
  """

  """
  Based on spacepy/plot/utils.py on 07/10/2017, but many additions.
  See also
    https://github.com/JouleCai/geospacelab/blob/master/geospacelab/visualization/mpl/axis_ticks.py
  and demo use at misc/geospacelab/demo.py

  TODO:
    * Add auto_adjust option that sets adjust_{first,last}_xlabel and
      adjust_{x,y}range as needed.
    * Use _numsize() to determine if figure width and height
      will cause overlap when default number major tick labels is used.
    * If time[0].day > 28, need to make first tick at time[0].day = 28
      as needed.
    * If first data point has fractional seconds, the plot won't have
      a major x-label right below it. This is due to the fact that
      MicrosecondLocator() does not take a keyword argument of
      "bymicroseconds".
    * Adjust lower and upper limits as in 366*8 span
  """

  # Get all kwargs passed using locals
  kwargs = {k: v for k, v in locals().items() if k != 'args'}

  import warnings
  from datetime import datetime

  from matplotlib import pyplot as plt

  import matplotlib.dates as mpld

  from .config import config

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

  fig.canvas.draw()
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
    msg = 'Lower axis limit of %f is not a valid Matplotlib datenum' % lim[0]
    raise ValueError(msg)
  try:
    mpld.num2date(lim[1])
  except:
    msg = 'Upper axis limit of %f is not a valid Matplotlib datenum' % lim[1]
    raise ValueError(msg)

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

  if datamin == datamax:
    if dir == 'x':
      axes.set_xticks([mpld.num2date(datamin)])
      xticklabel = datetime.strftime(mpld.num2date(datamin),'%Y-%m-%dT%H:%M:%S')
      axes.set_xticklabels([xticklabel])
    else:
      axes.set_yticks([mpld.num2date(datamin)])
      yticklabel = datetime.strftime(mpld.num2date(datamin),'%Y-%m-%dT%H:%M:%S')
      axes.set_yticklabels([yticklabel])
    return

  # Need to document why this was used originally. If kept, it creates
  # problems if labels extend beyond the axis limits.
  #tmin = np.min((lim[0], datamin))
  #tmax = np.max((lim[1], datamax))
  tmin = lim[0]
  tmax = lim[1]

  tspan = mpld.num2date((tmin, tmax))

  delta_t = tspan[-1] - tspan[0]
  if debug:
    print("Total seconds: %s" % delta_t.total_seconds())

  if debug:
    print(f'{dir} data min:         {mpld.num2date(datamin)}')
    print(f'Default {dir}lim[0]:    {mpld.num2date(lim[0])}')
    print(f'Default {dir}ticks[0]:  {mpld.num2date(ticks[0])}')
    print(f'{dir} data max:         {mpld.num2date(datamax)}')
    print(f'Default {dir}lim[-1]:   {mpld.num2date(lim[-1])}')
    print(f'Default {dir}ticks[-1]: {mpld.num2date(ticks[-1])}')
    print(f'Default {dir}labels and ticks:')
    labels = _get_labels(dir, axes)
    _print_ticks(dir, axes, ticks, labels)


  """
  major_sub_format contains additional information that is used for the first tick label
  or when there is a major change. For example, if
    major_format = %M:%S and major_sub_format = %H,
  the labels will have only minute and hour and the first tick will have a
  label of %M:%S\n%H. If there is a change in hour somewhere on the axis,
  that label will include the new hour.

  Note that interval=... is specified even when it would seem to be redundant.
  It is needed to workaround the bug discussed at stackoverflow.com/q/31072589
  """

  cfg = config(delta_t, debug=debug)

  if debug:
    print(f'Config for delta_t = {delta_t}:')
    for key, value in cfg.items():
      print(f'  {key}: {value}')

  if cfg['major_locator'] is None:
    if debug:
      print('No locator found for this time span. Using default Matplotlib locator and formatter.')
    ticks, labels, cfg['major_sub_format'] = _manual_labels(dir, axes)
  else:
    if dir == 'x':
      axes.xaxis.set_major_locator(cfg['major_locator'])
      if cfg['major_formatter'] is not None:
        axes.xaxis.set_major_formatter(cfg['major_formatter'])
      if cfg['minor_locator'] is not None:
        axes.xaxis.set_minor_locator(cfg['minor_locator'])
      if cfg['minor_formatter'] is not None:
        axes.xaxis.set_minor_formatter(cfg['minor_formatter'])

      fig.canvas.draw() # Render new labels so updated for next line
      ticks = axes.get_xticks()
    else:
      axes.yaxis.set_major_locator(cfg['major_locator'])
      if cfg['major_formatter'] is not None:
        axes.yaxis.set_major_formatter(cfg['major_formatter'])
      if cfg['minor_locator'] is not None:
        axes.yaxis.set_minor_locator(cfg['minor_locator'])
      if cfg['minor_formatter'] is not None:
        axes.yaxis.set_minor_formatter(cfg['minor_formatter'])

      fig.canvas.draw() # Render new labels so updated for next line
      ticks = axes.get_yticks()

    if debug:
      print(f'{dir}labels and ticks after applying locator:')
      fig.canvas.draw()
      _print_ticks(dir, axes, ticks, _get_labels(dir, axes))
    if adjust_xrange or adjust_yrange:
      _adjust_range(dir, fig, axes, datamin, datamax, debug=debug)
      if debug:
        print(f'{dir}labels and ticks after adjusting range:')
        fig.canvas.draw()
        _print_ticks(dir, axes, ticks, _get_labels(dir, axes))

    fig.canvas.draw()

    labels = _get_labels(dir, axes)

  if len(labels) == 0:
    if debug:
      print('No labels.')
    return

  if debug:
    print(f'{dir}labels and ticks after applying major_formatter:')
    _print_ticks(dir, axes, ticks, labels)

  if cfg['major_sub_format'] != '':
    labels = _add_major_sub_format(dir, cfg['major_sub_format'], cfg['trans'], lim, ticks, labels, debug=False)

    if debug:
      print(f'{dir}labels and ticks after applying major_sub_format:')
      _print_ticks(dir, axes, ticks, labels)

    if dir == 'x':
      # Without the set_xticks(), warning is generated:
      #   UserWarning: set_ticklabels() should only be used.
      # Additional discussion:
      #   https://github.com/matplotlib/matplotlib/issues/18848
      # The correct way to avoid the warning:
      #   https://stackoverflow.com/a/69126185
      # Better: Create custom class:
      #   https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html
      axes.set_xticks(axes.get_xticks())
      axes.set_xticklabels(labels)
      _adjust_xlabels(axes,
        adjust_first_xlabel=adjust_first_xlabel,
        adjust_last_xlabel=adjust_last_xlabel,
        major_font_shrink_factor=major_font_shrink_factor,
        major_font_shrink_always=major_font_shrink_always,
        debug=debug
      )

    if dir == 'y':
      axes.set_yticks(axes.get_yticks())
      axes.set_yticklabels(labels)

  # Trigger update of ticks when limits change due to user interaction.
  if set_cb:
    _set_cb(dir, axes, kwargs, debug=debug)

  return {
          'delta_t': delta_t,
          'ticks': ticks,
          'labels': labels,
          'major_locator': cfg['major_locator'],
          'minor_locator': cfg['minor_locator'],
          'major_formatter': cfg['major_formatter'],
          'minor_formatter': cfg['minor_formatter'],
          'major_sub_format': cfg['major_sub_format'],
          'trans': cfg['trans']
        }


def _set_cb(dir, axes, kwargs, debug=False):
  import matplotlib.dates as mpld

  def on_xlims_change(ax):
    if debug:
      print('xlims changed. Updating datetick plot.')
    ax.xaxis.set_minor_locator(mpld.AutoDateLocator())
    ax.xaxis.set_major_locator(mpld.AutoDateLocator())
    datetick('x', **{**kwargs, 'set_cb': False})

  def on_ylims_change(ax):
    if debug:
      print('xlims changed. Updating datetick plot.')
    ax.yaxis.set_minor_locator(mpld.AutoDateLocator())
    ax.yaxis.set_major_locator(mpld.AutoDateLocator())
    datetick('y', **{**kwargs, 'set_cb': False})

  def disconect():
    prev = getattr(axes, f'_datetick_cb_{dir}', None)
    if prev is not None:
      """
      This catches case where user calls datetick('x', axes=ax, use_cb=True)
      multiple times on same axes. It also allows user to call datetick() with
      use_cb=False to disable callback after it has been enabled.
      """
      axes.callbacks.disconnect(prev)

  if debug:
    n = len(axes.callbacks.callbacks.get(f'{dir}lim_changed', {}))
    print(f'{dir}lim_changed callbacks registered: {n}')

  disconect()

  if dir == 'x':
    cid = axes.callbacks.connect('xlim_changed', on_xlims_change)
    axes._datetick_cb_x = cid
  else:
    cid = axes.callbacks.connect('ylim_changed', on_ylims_change)
    axes._datetick_cb_y = cid


def _get_labels(dir, axes):
  if dir == 'x':
    return [item.get_text() for item in axes.get_xticklabels()]
  else:
    return [item.get_text() for item in axes.get_yticklabels()]


def _adjust_range(dir, fig, axes, datamin, datamax, debug=False):
  import matplotlib.dates as mpld
  if dir == 'x':
    ticks = axes.get_xticks()
  else:
    ticks = axes.get_yticks()
  if len(ticks) >= 2:
    fig.canvas.draw()
    dt = ticks[1] - ticks[0]
    pad = 0.05 * dt
    first_candidates  = ticks[ticks <= datamin]
    last_candidates = ticks[ticks >= datamax]
    first  = first_candidates[-1]  if len(first_candidates) > 0 else ticks[0] - dt
    last = last_candidates[0]  if len(last_candidates) > 0 else ticks[-1] + dt
    if debug:
      print(f'_adjust_range(): Setting lower limit to {mpld.num2date(first-pad)} and upper limit to {mpld.num2date(last+pad)}')
    if dir == 'x':
      axes.set_xlim(first - pad, last + pad)
    else:
      axes.set_ylim(first - pad, last + pad)


def _add_major_sub_format(dir, major_sub_format, trans, lim, ticks, labels, debug=False):
  from datetime import datetime
  import matplotlib.dates as mpld

  time = mpld.num2date(ticks)

  first = 0
  if ticks[0] < lim[0]:
    if debug:
      msg = 'First tick is less than lower axis limit. Applying major_sub_format to second tick label.'
      print(msg)
    # Work-around for bug in Matplotlib where left-most tick is less than
    # lower x-limit. Could more than one tick be less than lower x-limit?
    while first < len(ticks) and ticks[first] < lim[0]:
      first += 1
    if first == len(ticks):
      if debug:
        print('All ticks are less than lower axis limit. Applying major_sub_format to last tick label.')
      first = len(ticks) - 1

  # Always apply major_sub_format to first tick label
  if debug:
    print(f'Applying major_sub_format to first tick label at {mpld.num2date(ticks[first])}.')
  labels[first] = '%s\n%s' % (labels[first], datetime.strftime(time[first], major_sub_format))

  major_sub_format_len = len(datetime.strftime(time[first], major_sub_format))

  if trans is None:
    return labels

  for i in range(first+1, len(time)):
    # First major label will always have major_sub_format applied.
    # Modify major labels after first under certain conditions.
    modify = False
    if debug:
      print(f'Checking if major_sub_format should be applied to tick label at {mpld.num2date(ticks[i])}.')
      print(f'  trans = {trans}')
      print(f'  time[{i-1}] = {time[i-1]}')
      print(f'  time[{i}] = {time[i]}')

    if trans == 'year' and time[i].year != time[i-1].year:
      if debug:
        print(f'  Year changed: {time[i-1].year} -> {time[i].year}')
      modify = True
    if trans == 'month' and time[i].month != time[i-1].month:
      if debug:
        print(f'  Month changed: {time[i-1].month} -> {time[i].month}')
      modify = True
    if trans == 'day' and time[i].day != time[i-1].day:
      if debug:
        print(f'  Day changed: {time[i-1].day} -> {time[i].day}')
      modify = True
    if trans == 'hour' and time[i].hour != time[i-1].hour:
      if debug:
        print(f'  Hour changed: {time[i-1].hour} -> {time[i].hour}')
      modify = True
    if trans == 'minute' and time[i].minute !=time[i-1].minute:
      if debug:
        print(f'  Minute changed: {time[i-1].minute} -> {time[i].minute}')
      modify = True
    if trans == 'second' and time[i].second != time[i-1].second:
      if debug:
        print(f'  Second changed: {time[i-1].second} -> {time[i].second}')
      modify = True

    if not modify:
      continue

    if i == first + 1 and dir == 'x':
      # If first two major tick labels have major_sub_format applied, the will
      # likely run together. This keeps major_sub_format label for second major
      # tick.

      if major_sub_format_len > 7 and trans in ['month', 'day', 'hour', 'minute', 'second']:
        if debug:
          print(f'Removing major_sub_format to first tick label at {mpld.num2date(ticks[first])} to avoid overlap with second label.')
        labels[first] = labels[first].split('\n')[0]
      if debug:
        print(f'Applying major_sub_format to tick label at       {mpld.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.strftime(mpld.num2date(ticks[i]), major_sub_format))
    else:
      if debug:
        print(f'Applying major_sub_format to tick label at       {mpld.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.strftime(mpld.num2date(ticks[i]), major_sub_format))

  return labels


def _adjust_xlabels(axes, adjust_first_xlabel=False, adjust_last_xlabel=False, major_font_shrink_factor=0.9, major_font_shrink_always=False, debug=False):
  xticklabels = axes.get_xticklabels()
  lastlabel_text = xticklabels[-1].get_text()
  firstlabel_text = xticklabels[0].get_text()
  adjusted = False

  if adjust_first_xlabel and '\n' in firstlabel_text:
    if len(firstlabel_text.split('\n')[-1]) > 7:
      if debug:
        _first = firstlabel_text.replace("\n", "\\n")
        print(f'Adjusting first x-label: "{_first}"')
      adjusted = True
      # If fmt1 in first label longer than YYYY-MM, set justification to left.
      xticklabels[0].set_ha('left')
      # Shift to right by 1/2 width of fmt1 in first label.
      first_fmt1 = firstlabel_text.split('\n')[0]
      offset = _numsize(axes, first_fmt1, +1, debug=debug)
      xticklabels[0].set_transform(xticklabels[0].get_transform() - offset)

  if adjust_last_xlabel and '\n' in lastlabel_text:
    if len(lastlabel_text.split('\n')[-1]) > 7:
      if debug:
        _last = lastlabel_text.replace("\n", "\\n")
        print(f'Adjusting last x-label: "{_last}"')
      adjusted = True
      # If fmt1 iin last label longer than YYYY-MM, set justification to right.
      xticklabels[-1].set_ha('right')
      # Shift to left by 1/2 width of fmt1 in last label.
      last_fmt1 = lastlabel_text.split('\n')[0]
      offset = _numsize(axes, last_fmt1, -1, debug=debug)
      xticklabels[-1].set_transform(xticklabels[-1].get_transform() - offset)

  if adjusted or major_font_shrink_always:
    # Make all labels without newline slightly smaller than default fontsize 
    # so it is clearer that major_sub_format applies to larger number.
    if debug:
      print('Adjusting font size of x-labels without newline')
    for label in xticklabels:
      if '\n' not in label.get_text():
        label.set_fontsize(label.get_fontsize()*major_font_shrink_factor)


def _numsize(ax, num, sign, debug=False):
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
    print('_numsize():')
    print(f'  num      = "{num}"')
    print(f'  fontsize = {fontsize}')
    print(f'  dpi      = {dpi}')
    print(f'  width    = {w}')
    print(f'  height   = {h}')
    print(f'  descent  = {d}')
    print(f'  delta    = {delta}')
    _offset = re.sub(r"\n\s+", "", str(offset))
    print(f'  offset   = {_offset}')

  return offset


def _print_ticks(dir, axes, ticks, labels):
  import matplotlib.dates as mpld
  lim = axes.get_xlim() if dir == 'x' else axes.get_ylim()
  for i in range(0, len(ticks)):
    note = ''
    if ticks[i] < lim[0] or ticks[i] > lim[1]:
      note = ' (may be clipped by mpl b/c outside of axis limits)'
    label = str(labels[i]).replace("\n", "\\n")
    print(f' {label}    {mpld.num2date(ticks[i])} {note}')


def _manual_labels(dir, axes):

  major_sub_format = '%Y-%m-%d'
  ticks = axes.get_xticks() if dir == 'x' else axes.get_yticks()
  labels = _get_labels(dir, axes)
  # Make all labels have the same number of decimal places as one
  # with the most decimal places.
  n_places = 0
  for i in range(0, len(labels)):
    # Remove trailing zeros.
    n_places = max(n_places, len(labels[i].rstrip("0").split(".")[-1]))
  for i in range(0, len(labels)):
    parts = labels[i].split(".")
    labels[i] = parts[0]
    if len(parts) > 1:
      fractional = parts[1][0:n_places]
    if n_places > 0:
      labels[i] += "." + fractional

  return ticks, labels, major_sub_format
