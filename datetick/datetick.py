"""
  datetick formats the major and minor tick labels.
"""
import datetime
import matplotlib

def datetick(*args,
             axes=None,
             adjust_last_xlabel=False,
             adjust_first_xlabel=False,
             adjust_xrange=False,
             adjust_yrange=False,
             major_font_shrink_factor=0.87,
             major_font_shrink_always=False,
             min_font_size=6,
             warn_on_min_gap=False,
             set_cb=True,
             debug=False):
  """
  datetick() formats the major and minor x-tick labels of the current figure.

  datetick('x') or datetick('y') formats the x- or y- labels

  datetick('x', axes=ax) or datetick('y', axes=ax) formats the given axis `ax`.

  Example:
  --------
    import datetime as dt
    import matplotlib.pyplot
    from datetick import datetick
    d1 = dt.datetime(1900, 1, 2)
    d2 = dt.datetime.fromordinal(10 + dt.datetime.toordinal(d1))
    x = [d1, d2]
    y = [0.0,1.0]
    matplotlib.pyplot.plot(x, y)
    datetick('x')
    matplotlib.pyplot.show()

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

  from . import adjust, compute, rules, util

  dir = 'x' if len(args) == 0 else args[0]

  if kwargs.get('axes', None) is not None:
    axes = kwargs['axes']
    if not isinstance(axes, matplotlib.pyplot.Axes):
      raise ValueError(f"Invalid axes argument (axes={axes}) provided. Not an instance of matplotlib.pyplot.Axes.")
    try:
      fig = axes.figure
    except:
      raise ValueError(f"Invalid axes argument (axes={axes}) provided. Execution of axes.figure failed.")
  else:
    if matplotlib.pyplot.get_fignums() == []:
      util.warn("No current figure.")
      return None
    try:
      fig = matplotlib.pyplot.gcf()
    except Exception as e:
      raise ValueError("matplotlib.pyplot.gcf() failed: {e}")
    try:
      axes = matplotlib.pyplot.gca()
    except Exception as e:
      raise ValueError(f"matplotlib.pyplot.gca() failed: {e}")

  try:
    fig.canvas.draw()
  except Exception as e:
    raise ValueError(f"fig.canvas.draw() failed: {e}")

  if not hasattr(axes, 'dataLim'):
    raise ValueError("axes does not have dataLim attribute. Cannot use datetick().")

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

  # If all values are NaN, datamin = np.inf and datamax = -np.inf.
  try:
    matplotlib.dates.num2date(datamin)
  except:
    msg = f"matplotlib.dates.num2date(axes.dataLim.{dir}x0) failed. Cannot use datetick()."
    #_warn(msg)
    return
  try:
    matplotlib.dates.num2date(datamax)
  except:
    msg = f"matplotlib.dates.num2date(axes.dataLim.{dir}x1) failed. Cannot use datetick()."
    #_warn(msg)
    return

  try:
    matplotlib.dates.num2date(lim[0])
  except:
    msg = f"axes.get_{dir}lim()[0] = {lim[0]} is not a valid Matplotlib datenum."
    raise ValueError(msg)
  try:
    matplotlib.dates.num2date(lim[1])
  except:
    msg = f"axes.get_{dir}lim()[0] = {lim[1]} is not a valid Matplotlib datenum."
    raise ValueError(msg)

  if datamin == datamax:
    if dir == 'x':
      axes.set_xticks([matplotlib.dates.num2date(datamin)])
      xticklabel = datetime.datetime.strftime(matplotlib.dates.num2date(datamin),'%Y-%m-%dT%H:%M:%S')
      axes.set_xticklabels([xticklabel])
    else:
      axes.set_yticks([matplotlib.dates.num2date(datamin)])
      yticklabel = datetime.datetime.strftime(matplotlib.dates.num2date(datamin),'%Y-%m-%dT%H:%M:%S')
      axes.set_yticklabels([yticklabel])
    return

  # Need to document why np.{min,max} was used originally. If kept, it creates
  # problems if labels extend beyond the axis limits.
  #tmin = np.min((lim[0], datamin))
  #tmax = np.max((lim[1], datamax))
  tmin = lim[0]
  tmax = lim[1]

  tspan = matplotlib.dates.num2date((tmin, tmax))

  delta_t = tspan[-1] - tspan[0]
  if debug:
    print("Total seconds: %s" % delta_t.total_seconds())

  if debug:
    print(f'{dir} data min:         {matplotlib.dates.num2date(datamin)}')
    print(f'Default {dir}lim[0]:    {matplotlib.dates.num2date(lim[0])}')
    print(f'Default {dir}ticks[0]:  {matplotlib.dates.num2date(ticks[0])}')
    print(f'{dir} data max:         {matplotlib.dates.num2date(datamax)}')
    print(f'Default {dir}lim[-1]:   {matplotlib.dates.num2date(lim[-1])}')
    print(f'Default {dir}ticks[-1]: {matplotlib.dates.num2date(ticks[-1])}')
    print(f'Default {dir}labels and ticks:')
    labels = _get_labels(dir, axes)
    util.print_ticks(dir, axes, ticks, labels)


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

  rule = rules.rule(delta_t, debug=debug)

  if rule is None:
    util.warn(f'No config rule matched delta_t={delta_t}. Using default Matplotlib locator and formatter.')
    ticks, labels, major_sub_format = _manual_labels(dir, axes)
    return {
      'delta_t': delta_t,
      'ticks': ticks,
      'labels': labels,
      'rule': rule
    }

  if debug:
    print(f'Rule for delta_t = {delta_t}:')
    for key, value in rule.items():
      print(f'  {key}: {value}')

  if rule['major']['locator'] is None:
    if debug:
      print('No major locator found for this time span. Using default Matplotlib locator and formatter.')
    ticks, labels, rule['major']['sub_format'] = _manual_labels(dir, axes)
  else:
    if dir == 'x':
      axis = axes.xaxis
    else:
      axis = axes.yaxis

    axis.set_major_locator(util.make_locator(rule['major']['locator']))
    if rule['major']['formatter'] is not None:
      axis.set_major_formatter(util.make_formatter(rule['major']['formatter']))
    if rule['minor']['locator'] is not None:
      axis.set_minor_locator(util.make_locator(rule['minor']['locator']))
    if rule['minor']['formatter'] is not None:
      axis.set_minor_formatter(util.make_formatter(rule['minor']['formatter']))

    fig.canvas.draw() # Render new labels so updated for next line
    ticks = axes.get_xticks() if dir == 'x' else axes.get_yticks()

    if debug:
      print(f'{dir}labels and ticks after applying locators and formatters:')
      fig.canvas.draw()
      util.print_ticks(dir, axes, ticks, _get_labels(dir, axes))

    if adjust_xrange or adjust_yrange:
      adjust.time_range(dir, fig, axes, datamin, datamax, debug=debug)
      if debug:
        print(f'{dir}labels and ticks after adjusting range:')
        fig.canvas.draw()
        util.print_ticks(dir, axes, ticks, _get_labels(dir, axes))

    fig.canvas.draw()

    labels = _get_labels(dir, axes)

  if len(labels) == 0:
    if debug:
      print('No labels. Returning without applying major_sub_format or set_cb.')
    return

  if rule['major']['sub_format'] != '':
    labels = _add_major_sub_string(dir, rule['major']['sub_format'], rule['major']['sub_transition'], lim, ticks, labels, debug=False)

    if debug:
      print(f'{dir}labels and ticks after applying major_sub_format:')
      util.print_ticks(dir, axes, ticks, labels)

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
      adjust.xlabels(axes,
        adjust_first_xlabel=adjust_first_xlabel,
        adjust_last_xlabel=adjust_last_xlabel,
        major_font_shrink_factor=major_font_shrink_factor,
        major_font_shrink_always=major_font_shrink_always,
        debug=debug
      )

    if dir == 'y':
      axes.set_yticks(axes.get_yticks())
      axes.set_yticklabels(labels)

  min_gap = compute.min_gap(axes, dir, debug=debug)
  if min_gap < min_font_size:
    min_gap = adjust.font_size(fig, axes, dir, min_gap, min_font_size, debug=debug)
    if min_gap < min_font_size and warn_on_min_gap:
      util.warn(f'Minimum gap between labels is {min_gap:.1f} px after reducing font size to min_font_size = {min_font_size} px.')

  # Trigger update of ticks when limits change due to user interaction.
  if set_cb and util.backend_is_interactive():
    _set_cb(dir, axes, kwargs, debug=debug)

  return {
          'delta_t': delta_t,
          'ticks': ticks,
          'labels': labels,
          'rule': rule
        }


def _set_cb(dir, axes, kwargs, debug=False):
  def on_xlims_change(ax):
    if debug:
      print('xlims changed. Updating datetick plot.')
    ax.xaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
    ax.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    datetick('x', **{**kwargs, 'set_cb': False})

  def on_ylims_change(ax):
    if debug:
      print('xlims changed. Updating datetick plot.')
    ax.yaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
    ax.yaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
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


def _add_major_sub_string(dir, major_sub_format, major_sub_transition, lim, ticks, labels, debug=False):

  time = matplotlib.dates.num2date(ticks)

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
    print(f'Applying major_sub_format to first tick label at {matplotlib.dates.num2date(ticks[first])}.')
  labels[first] = '%s\n%s' % (labels[first], datetime.datetime.strftime(time[first], major_sub_format))

  major_sub_format_len = len(datetime.datetime.strftime(time[first], major_sub_format))

  if major_sub_transition is None:
    return labels

  for i in range(first+1, len(time)):
    # First major label will always have major_sub_format applied.
    # Modify major labels after first under certain conditions.
    modify = False
    if debug:
      print(f'Checking if major_sub_format should be applied to tick label at {matplotlib.dates.num2date(ticks[i])}.')
      print(f'  major_sub_transition = {major_sub_transition}')
      print(f'  time[{i-1}] = {time[i-1]}')
      print(f'  time[{i}] = {time[i]}')

    if major_sub_transition == 'year' and time[i].year != time[i-1].year:
      if debug:
        print(f'  Year changed: {time[i-1].year} -> {time[i].year}')
      modify = True
    if major_sub_transition == 'month' and time[i].month != time[i-1].month:
      if debug:
        print(f'  Month changed: {time[i-1].month} -> {time[i].month}')
      modify = True
    if major_sub_transition == 'day' and time[i].day != time[i-1].day:
      if debug:
        print(f'  Day changed: {time[i-1].day} -> {time[i].day}')
      modify = True
    if major_sub_transition == 'hour' and time[i].hour != time[i-1].hour:
      if debug:
        print(f'  Hour changed: {time[i-1].hour} -> {time[i].hour}')
      modify = True
    if major_sub_transition == 'minute' and time[i].minute !=time[i-1].minute:
      if debug:
        print(f'  Minute changed: {time[i-1].minute} -> {time[i].minute}')
      modify = True
    if major_sub_transition == 'second' and time[i].second != time[i-1].second:
      if debug:
        print(f'  Second changed: {time[i-1].second} -> {time[i].second}')
      modify = True

    if not modify:
      continue

    if i == first + 1 and dir == 'x':
      # If first two major tick labels have major_sub_format applied, the will
      # likely run together. This keeps major_sub_format label for second major
      # tick.

      if major_sub_format_len > 7 and major_sub_transition in ['month', 'day', 'hour', 'minute', 'second']:
        if debug:
          print(f'Removing major_sub_format to first tick label at {matplotlib.dates.num2date(ticks[first])} to avoid overlap with second label.')
        labels[first] = labels[first].split('\n')[0]
      if debug:
        print(f'Applying major_sub_format to tick label at       {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))
    else:
      if debug:
        print(f'Applying major_sub_format to tick label at       {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))

  return labels


def _manual_labels(dir, axes):

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

  return ticks, labels
