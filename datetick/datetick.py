"""
  datetick formats the major and minor tick labels.
"""
import datetime
import matplotlib

def datetick(*args,
             axes=None,
             adjust_range=False,
             adjust_last_xlabel=False,
             adjust_first_xlabel=False,
             major_font_shrink_factor=0.87,
             major_font_shrink_always=False,
             min_font_size=6,
             min_gap_warn=False,
             rule_idx=None,
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

  adjust_range: If True, expand axis range so data are always within a major tick.

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

  from . import adjust, compute, util
  from .rules import rule as select_rule

  axis = 'x' if len(args) == 0 else args[0]

  _check_plt(kwargs)

  bbox = axes.dataLim
  if axis == 'x':
    lim_data = (bbox.x0, bbox.x1)
    lim_axis = axes.get_xlim()
    ticks = axes.get_xticks()
  else:
    lim_data = (bbox.y0, bbox.y1)
    lim_axis = axes.get_ylim()
    ticks = axes.get_yticks()

  _check_bounds(lim_data, lim_axis, ticks, axis, debug=debug)

  if lim_data[0] == lim_data[1]:
    datamin_date = matplotlib.dates.num2date(lim_data[0])
    ticklabel = datetime.datetime.strftime(datamin_date,'%Y-%m-%dT%H:%M:%S')
    if axis == 'x':
      axes.set_xticks([datamin_date])
      axes.set_xticklabels([ticklabel])
    else:
      axes.set_yticks([datamin_date])
      axes.set_yticklabels([ticklabel])
    return

  # Need to document why np.{min,max} was used originally. If kept, it creates
  # problems if labels extend beyond the axis limits.
  #tmin = np.min((lim[0], datamin))
  #tmax = np.max((lim[1], datamax))
  #tmin = lim[0]
  #tmax = lim[1]
  tmin = lim_data[0]
  tmax = lim_data[1]

  tspan = matplotlib.dates.num2date((tmin, tmax))

  delta_t = tspan[-1] - tspan[0]
  if debug:
    print("Total seconds: %s" % delta_t.total_seconds())
    print(f'{axis} data min:         {matplotlib.dates.num2date(lim_data[0])}')
    print(f'Default {axis}lim[0]:    {matplotlib.dates.num2date(lim_data[0])}')
    print(f'Default {axis}ticks[0]:  {matplotlib.dates.num2date(ticks[0])}')
    print(f'{axis} data max:         {matplotlib.dates.num2date(lim_data[-1])}')
    print(f'Default {axis}lim[-1]:   {matplotlib.dates.num2date(lim_data[-1])}')
    print(f'Default {axis}ticks[-1]: {matplotlib.dates.num2date(ticks[-1])}')
    print(f'Default {axis}labels and ticks:')
    labels = util.get_ticklabels(axis, axes)
    util.print_ticks(axis, axes, ticks, labels)

  rule = select_rule(delta_t, rule_idx=kwargs['rule_idx'], debug=debug)

  if rule is None:
    delta_t_str = util.format_delta(delta_t)
    msg = f'No config rule matched delta_t={delta_t_str}. '
    msg += 'Using default Matplotlib locator and formatter.'
    util.warn(msg)
    ticks, labels = _manual_labels(axis, axes)
    return {
      'delta_t': delta_t,
      'ticks': ticks,
      'labels': labels,
      'rule': rule
    }


  if rule['major']['locator'] is None:
    if debug:
      msg = 'No major locator found for this time span. '
      msg += 'Using default Matplotlib locator and formatter.'
      print(msg)
    ticks, labels = _manual_labels(axis, axes)
  else:
    ticks, labels = _locator_labels(axis, axes, rule, lim_data, adjust_range, debug=debug)

  if len(labels) == 0:
    if debug:
      print('No labels. Returning without applying major_sub_format or set_cb.')
    return


  if rule['major']['sub_format'] != '':
    args = [
      axis,
      lim_axis,
      ticks,
      labels,
      rule['major']['sub_format'],
      rule['major']['sub_transition']
    ]
    labels = _add_major_sub_string(*args, debug=debug)

    if debug:
      print(f'{axis}labels and ticks after applying major_sub_format:')
      util.print_ticks(axis, axes, ticks, labels)

    args = [axis,
            axes,
            labels,
            adjust_first_xlabel,
            adjust_last_xlabel,
            major_font_shrink_factor,
            major_font_shrink_always
    ]
    _apply_major_sub_string(*args, debug=debug)


  # Adjust font size if overlap in labels.
  min_gap = compute.min_gap(axis, axes, debug=debug)
  adjust_warning = None
  font_size = util.get_font_size(axis, axes)
  font_size_change = 0
  if min_gap < min_font_size:
    adjust_warning = adjust.font_size(axis, axes, min_gap, min_font_size, debug=debug)
    if adjust_warning is not None and min_gap_warn:
      util.warn(adjust_warning)
    font_size_change = util.get_font_size(axis, axes) - font_size

  if adjust_warning is not None:
    # Adjust rule if overlap in labels after shrinking font size.
    # Try to use next rule so fewer labels are used.
    max_attempts = 3
    if kwargs['rule_idx'] is None:
      kwargs['rule_idx'] = 0

    if debug:
      msg = '\nAttempting to use datetick with previous rule. '
      msg += f'Attempt {kwargs["rule_idx"] + 1} of {max_attempts}.\n'
      print(msg)

    if False:
      kwargs['rule_idx'] += 1

      if kwargs['rule_idx'] < max_attempts:
        kwargs['axes'] = axes
        return datetick(axis, **kwargs)
      else:
        adjust_warning += f' Tried to use {max_attempts} rules but minimum gap is '
        adjust_warning += f'still less than min_font_size = {min_font_size} px.'


  # Trigger update of ticks when limits change due to user interaction.
  if set_cb and util.backend_is_interactive():
    _set_cb(axis, axes, kwargs, debug=debug)

  return {
          'delta_t': delta_t,
          'ticks': ticks,
          'labels': labels,
          'rule': rule,
          'rule_idx': kwargs['rule_idx'],
          'font_size_change': font_size_change,
          'warning': adjust_warning
        }


def _check_plt(kwargs):
  from . import util

  if kwargs.get('axes', None) is not None:
    axes = kwargs['axes']
    if not isinstance(axes, matplotlib.pyplot.Axes):
      msg = f"Invalid axes argument axes={axes} is not an instance of matplotlib.pyplot.Axes."
      raise ValueError(msg)
    try:
      fig = axes.figure
    except Exception as e:
      msg = f"Invalid axes argument axes={axes} - execution of axes.figure failed: {e}"
      raise ValueError(msg)
  else:
    if matplotlib.pyplot.get_fignums() == []:
      util.warn("No current figure.")
      return None
    try:
      fig = matplotlib.pyplot.gcf()
    except Exception as e:
      raise ValueError(f"matplotlib.pyplot.gcf() failed: {e}")
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


def _check_bounds(lim_data, lim_axis, ticks, axis, debug=False):

  # If all values are NaN, datamin = np.inf and datamax = -np.inf.
  try:
    matplotlib.dates.num2date(lim_data[0])
  except:
    msg = f"matplotlib.dates.num2date(axes.dataLim.{axis}x0) failed. Cannot use datetick()."
    #_warn(msg)
    return
  try:
    matplotlib.dates.num2date(lim_data[1])
  except:
    msg = f"matplotlib.dates.num2date(axes.dataLim.{axis}x1) failed. Cannot use datetick()."
    #_warn(msg)
    return

  try:
    matplotlib.dates.num2date(lim_axis[0])
  except:
    msg = f"axes.get_{axis}lim()[0] = {lim_axis[0]} is not a valid Matplotlib datenum."
    raise ValueError(msg)
  try:
    matplotlib.dates.num2date(lim_axis[1])
  except:
    msg = f"axes.get_{axis}lim()[0] = {lim_axis[1]} is not a valid Matplotlib datenum."
    raise ValueError(msg)


def _set_cb(axis, axes, kwargs, debug=False):
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
    prev = getattr(axes, f'_datetick_cb_{axis}', None)
    if prev is not None:
      """
      This catches case where user calls datetick('x', axes=ax, use_cb=True)
      multiple times on same axes. It also allows user to call datetick() with
      use_cb=False to disable callback after it has been enabled.
      """
      axes.callbacks.disconnect(prev)

  if debug:
    n = len(axes.callbacks.callbacks.get(f'{axis}lim_changed', {}))
    print(f'{axis}lim_changed callbacks registered: {n}')

  disconect()

  if axis == 'x':
    cid = axes.callbacks.connect('xlim_changed', on_xlims_change)
    axes._datetick_cb_x = cid
  else:
    cid = axes.callbacks.connect('ylim_changed', on_ylims_change)
    axes._datetick_cb_y = cid


def _add_major_sub_string(axis, lim_axis, ticks, labels, major_sub_format, major_sub_transition, debug=False):

  time = matplotlib.dates.num2date(ticks)

  first = 0
  if False and ticks[0] < lim_axis[0]:
    if debug:
      msg = 'First tick is less than lower axis limit. Applying major_sub_format to second tick label.'
      print(msg)
    # Work-around for bug in Matplotlib where left-most tick is less than
    # lower x-limit. Could more than one tick be less than lower x-limit?
    while first < len(ticks) and ticks[first] < lim_axis[0]:
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

    if i == first + 1 and axis == 'x':
      # If first two major tick labels have major_sub_format applied, the will
      # likely run together. This keeps major_sub_format label for second major
      # tick.

      if major_sub_format_len > 7 and major_sub_transition in ['month', 'day', 'hour', 'minute', 'second']:
        if debug:
          print(f'Removing major_sub_format to first tick label at {matplotlib.dates.num2date(ticks[first])} to avoid overlap with second label.')
        labels[first] = labels[first].split('\n')[0]
      if debug:
        print(f'Applying major_sub_format to tick label at {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))
    else:
      if debug:
        print(f'Applying major_sub_format to tick label at {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))


  # Look for labels with two newlines. If third row has been seen before, remove.
  third_row = None
  for idx, label in enumerate(labels):
    parts = label.split('\n')
    if len(parts) != 3:
      continue
    if third_row is None:
      third_row = parts[2]
      continue
    if parts[2] == third_row:
      labels[idx] = '\n'.join(parts[0:2])
    else:
      third_row = parts[2]

  return labels


def _apply_major_sub_string(axis, axes, labels, adjust_first_xlabel, adjust_last_xlabel, major_font_shrink_factor, major_font_shrink_always, debug=False):
  from . import adjust
  if axis == 'x':
    """
      Without the set_xticks(), warning is generated:
        UserWarning: set_ticklabels() should only be used.
      Additional discussion:
        https://github.com/matplotlib/matplotlib/issues/18848
      The correct way to avoid the warning:
        https://stackoverflow.com/a/69126185
      Better: Create custom class:
        https://matplotlib.org/stable/gallery/ticks/date_index_formatter.html
    """
    axes.set_xticks(axes.get_xticks())
    axes.set_xticklabels(labels)
    adjust.xlabels(axes,
      adjust_first_xlabel=adjust_first_xlabel,
      adjust_last_xlabel=adjust_last_xlabel,
      major_font_shrink_factor=major_font_shrink_factor,
      major_font_shrink_always=major_font_shrink_always,
      debug=debug
    )

  if axis == 'y':
    axes.set_yticks(axes.get_yticks())
    axes.set_yticklabels(labels)


def _manual_labels(axis, axes):

  from . import util

  ticks = util.get_ticks(axis, axes, strings=False)
  labels = util.get_ticklabels(axis, axes)
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


def _locator_labels(axis, axes, rule, lim_data, adjust_range, debug=False):
  from . import adjust, util
  if axis == 'x':
    axis_obj = axes.xaxis
  else:
    axis_obj = axes.yaxis

  axis_obj.set_major_locator(util.make_locator(rule['major']['locator']))
  if rule['major']['formatter'] is not None:
    axis_obj.set_major_formatter(util.make_formatter(rule['major']['formatter']))
  if rule['minor']['locator'] is not None:
    axis_obj.set_minor_locator(util.make_locator(rule['minor']['locator']))
  if rule['minor']['formatter'] is not None:
    axis_obj.set_minor_formatter(util.make_formatter(rule['minor']['formatter']))

  fig = axes.figure

  fig.canvas.draw() # Render new labels so updated for next line
  ticks = util.get_ticks(axis, axes)

  labels = util.get_ticklabels(axis, axes)
  if debug:
    print(f'{axis}labels and ticks after applying locators and formatters:')
    fig.canvas.draw()
    util.print_ticks(axis, axes, ticks, labels)

  if adjust_range:
    adjust.time_range(axis, axes, lim_data, debug=debug)
    if debug:
      print(f'{axis}labels and ticks after adjusting range:')
      fig.canvas.draw()
      util.print_ticks(axis, axes, ticks, labels)

  fig.canvas.draw()
  ticks = util.get_ticks(axis, axes)
  labels = util.get_ticklabels(axis, axes)

  return ticks, labels