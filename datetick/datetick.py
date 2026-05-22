"""
  datetick formats the major and minor tick labels.
"""
import datetime
import matplotlib
# In case lazy import is implemented:
import matplotlib.dates
import matplotlib.pyplot

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
             rule_idx_change=None,
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

  from . import adjust, util
  from .rules import rule as select_rule

  axis = 'x' if len(args) == 0 else args[0]
  if axis not in ['x', 'y']:
    raise ValueError(f"Invalid axis={axis!r}. Expected 'x' or 'y'.")

  axes = _check_axes(kwargs)

  bbox = axes.dataLim
  if axis == 'x':
    lim_data = (bbox.x0, bbox.x1)
    lim_axis = axes.get_xlim()
    ticks = axes.get_xticks()
  else:
    lim_data = (bbox.y0, bbox.y1)
    lim_axis = axes.get_ylim()
    ticks = axes.get_yticks()

  ok = _check_bounds(lim_data, lim_axis, axis, debug=debug)
  if not ok:
    return None

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

  data_tspan = matplotlib.dates.num2date((lim_data[0], lim_data[1]))
  delta_t_data = data_tspan[-1] - data_tspan[0]

  axis_tspan = matplotlib.dates.num2date((lim_axis[0], lim_axis[1]))
  delta_t_axis = axis_tspan[-1] - axis_tspan[0]
  delta_t = delta_t_axis # max(delta_t_data, delta_t_axis)
  if debug:
    print("Data total seconds: %s" % delta_t_data.total_seconds())
    print("Axis total seconds: %s" % delta_t_axis.total_seconds())
    print("Rule total seconds: %s" % delta_t.total_seconds())
    print(f'{axis} data min:         {matplotlib.dates.num2date(lim_data[0])}')
    print(f'Default {axis}lim[0]:    {matplotlib.dates.num2date(lim_axis[0])}')
    print(f'Default {axis}ticks[0]:  {matplotlib.dates.num2date(ticks[0])}')
    print(f'{axis} data max:         {matplotlib.dates.num2date(lim_data[-1])}')
    print(f'Default {axis}lim[-1]:   {matplotlib.dates.num2date(lim_axis[-1])}')
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
    return {
      'delta_t': delta_t,
      'ticks': ticks,
      'labels': labels,
      'rule': rule
    }


  if rule['major']['locator'] is None:
    if debug:
      msg = 'No major locator rule for this time span. '
      msg += 'Using default Matplotlib locator and formatter.'
      print(msg)
    labels = adjust.millis(labels, min_digits=1)
    if debug:
      print(f'{axis}labels and ticks after modifying millis:')
      util.print_ticks(axis, axes, ticks, labels)
  else:
    ticks, labels = _apply_rule(axis, axes, rule, lim_data, debug=debug)
    if debug:
      print(f'{axis}labels and ticks after applying locators and formatters:')
      util.print_ticks(axis, axes, ticks, labels)
    labels = adjust.millis(labels, min_digits=2)
    if debug:
      print(f'{axis}labels and ticks after modifying millis:')
      util.print_ticks(axis, axes, ticks, labels)


  if len(labels) == 0:
    if debug:
      print('No labels. Returning without applying major_sub_format or set_cb.')
    return

  if adjust_range:
    if debug:
      print(f'Adjusting {axis}-range')
    adjust.time_range(axis, axes, lim_data, debug=debug)
    if debug:
      print(f'{axis}labels and ticks after adjusting range:')
      axes.figure.canvas.draw()
      ticks = util.get_ticks(axis, axes)
      labels = util.get_ticklabels(axis, axes)
      util.print_ticks(axis, axes, ticks, labels)


  if rule['major']['sub_format'] == '':
    _update_labels(axis, axes, ticks, labels)
    if debug:
      print(f'{axis}labels and ticks after updating plot:')
      util.print_ticks(axis, axes, ticks, labels)
  else:
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

    _update_labels(axis, axes, ticks, labels)
    if debug:
      print(f'{axis}labels and ticks after updating plot:')
      util.print_ticks(axis, axes, ticks, labels)

    adjusted = adjust.first_last_labels(axes,
      adjust_first_xlabel=adjust_first_xlabel,
      adjust_last_xlabel=adjust_last_xlabel,
      debug=debug
    )

    if adjusted or major_font_shrink_always:
      adjust.non_sub_label_font_size(axes, major_font_shrink_factor, debug=debug)


  font_size_change = 0
  rule_idx_change = 0
  font_size_change_warning = None
  rule_idx_change_warning = None
  if kwargs['rule_idx_change'] is None:
    font_size_change, font_size_change_warning = \
      adjust.font_size_for_overlap(axis, axes, min_gap_warn, debug=debug)

    rule_idx_change, rule_idx_change_warning = \
      adjust.rule(axis, axes, rule_idx_change, debug=debug)
    if rule_idx_change != 0:
      if debug:
        print(f'Font size overlap exists after font size adjustment. Re-running datetick() with rule_idx_change = {rule_idx_change}.\n')
      kwargs['rule_idx_change'] = rule_idx_change
      kwargs['axes'] = axes
      return datetick(axis, **kwargs)


  # Trigger update of ticks when limits change due to user interaction.
  if set_cb and util.backend_is_interactive():
    _set_cb(axis, axes, kwargs, debug=debug)

  return {
          'delta_t': delta_t,
          'ticks': ticks,
          'labels': labels,
          'rule': rule,
          'rule_idx_change': kwargs['rule_idx'],
          'rule_idx_change_warning': rule_idx_change_warning,
          'font_size_change': font_size_change,
          'font_size_change_warning': font_size_change_warning
        }


def _check_axes(kwargs):

  if kwargs.get('axes', None) is not None:
    axes = kwargs['axes']
    if not hasattr(axes, 'figure'):
      msg = f"Invalid axes argument axes={axes} does not have a figure attribute."
      raise ValueError(msg)
    try:
      fig = axes.figure
    except Exception as e:
      msg = f"Invalid axes argument axes={axes} - execution of axes.figure failed: {e}"
      raise ValueError(msg)
    if fig is None:
      raise ValueError(f"Invalid axes argument axes={axes} has figure=None.")
  else:
    if matplotlib.pyplot.get_fignums() == []:
      raise ValueError("No current figure. Cannot use datetick() without axes.")
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

  return axes


def _check_bounds(lim_data, lim_axis, axis, debug=False):
  import math
  from . import util

  # If all values are NaN, datamin = np.inf and datamax = -np.inf.
  if math.isinf(lim_data[0]) or math.isinf(lim_data[1]):
    util.warn("At least of one the data limits is NaN or +/-infinity. Cannot use datetick().")
    return None

  try:
    matplotlib.dates.num2date(lim_data[0])
  except Exception as e:
    dim = 'x0' if axis == 'x' else 'y0'
    msg = f"matplotlib.dates.num2date(axes.dataLim.{dim}) failed. Cannot use datetick(): {e}"
    util.warn(msg)
    return False
  try:
    matplotlib.dates.num2date(lim_data[1])
  except Exception as e:
    dim = 'x1' if axis == 'x' else 'y1'
    msg = f"matplotlib.dates.num2date(axes.dataLim.{dim}) failed. Cannot use datetick(): {e}"
    util.warn(msg)
    return False

  try:
    matplotlib.dates.num2date(lim_axis[0])
  except Exception as e:
    msg = f"axes.get_{axis}lim()[0] = {lim_axis[0]} is not a valid Matplotlib datenum. Cannot use datetick(): {e}"
    util.warn(msg)
    return False
  try:
    matplotlib.dates.num2date(lim_axis[1])
  except Exception as e:
    msg = f"axes.get_{axis}lim()[1] = {lim_axis[1]} is not a valid Matplotlib datenum. Cannot use datetick(): {e}"
    util.warn(msg)
    return False

  return True


def _set_cb(axis, axes, kwargs, debug=False):

  def refresh(axis_name):
    if axis_name == 'x':
      axes.xaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
      axes.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    else:
      axes.yaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
      axes.yaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    datetick(axis_name, **{**kwargs, 'set_cb': False})


  def on_xlims_change(ax):
    if debug:
      print('xlims changed. Updating datetick plot.')
    refresh('x')

  def on_ylims_change(ax):
    if debug:
      print('ylims changed. Updating datetick plot.')
    refresh('y')

  def on_resize(event):
    if debug:
      print('figure size changed. Updating datetick plot.')
    refresh(axis)

  def disconect():
    prev = getattr(axes, f'_datetick_cb_{axis}', None)
    if prev is not None:
      """
      This catches case where user calls datetick('x', axes=ax, use_cb=True)
      multiple times on same axes. It also allows user to call datetick() with
      use_cb=False to disable callback after it has been enabled.
      """
      axes.callbacks.disconnect(prev)
    prev_resize = getattr(axes, f'_datetick_resize_cb_{axis}', None)
    if prev_resize is not None:
      axes.figure.canvas.mpl_disconnect(prev_resize)

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

  resize_cid = axes.figure.canvas.mpl_connect('resize_event', on_resize)
  setattr(axes, f'_datetick_resize_cb_{axis}', resize_cid)


def _add_major_sub_string(axis, lim_axis, ticks, labels, major_sub_format, major_sub_transition, debug=False):

  time = matplotlib.dates.num2date(ticks)
  print('Adding major_sub_format to select labels.')

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
          print(f'  Removing major_sub_format to first tick label at {matplotlib.dates.num2date(ticks[first])} to avoid overlap with second label.')
        labels[first] = labels[first].split('\n')[0]
      if debug:
        print(f'  Applying major_sub_format to tick label at {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))
    else:
      if debug:
        print(f'  Applying major_sub_format to tick label at {matplotlib.dates.num2date(ticks[i])}.')
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))


  # If a trailing row repeats on later labels, drop the repeated trailing row.
  second_row = None
  third_row = None
  for idx, label in enumerate(labels):
    parts = label.split('\n')
    if len(parts) == 2:
      if second_row is None:
        second_row = parts[1]
        continue
      if parts[1] == second_row:
        labels[idx] = parts[0]
      else:
        second_row = parts[1]
      continue
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


def _update_labels(axis, axes, ticks, labels):
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
    axes.set_xticks(ticks)
    axes.set_xticklabels(labels)

  if axis == 'y':
    axes.set_yticks(ticks)
    axes.set_yticklabels(labels)


def _apply_rule(axis, axes, rule, lim_data, debug=False):

  from . import util

  if axis == 'x':
    axis_obj = axes.xaxis
  else:
    axis_obj = axes.yaxis

  use_auto_date_locator = False

  if rule['major']['locator'] is not None:
    axis_obj.set_major_locator(util.make_locator(rule['major']['locator']))
    if use_auto_date_locator:
      import matplotlib.dates as mdates
      locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
      axis_obj.set_major_locator(locator)

  if rule['major']['formatter'] is not None:
    axis_obj.set_major_formatter(util.make_formatter(rule['major']['formatter']))
  else:
    axis_obj.set_major_formatter(matplotlib.ticker.NullFormatter())
  if rule['minor']['locator'] is not None:
    axis_obj.set_minor_locator(util.make_locator(rule['minor']['locator']))
  if rule['minor']['formatter'] is not None:
    axis_obj.set_minor_formatter(util.make_formatter(rule['minor']['formatter']))
  else:
    axis_obj.set_minor_formatter(matplotlib.ticker.NullFormatter())

  axes.figure.canvas.draw()
  ticks = util.get_ticks(axis, axes)
  labels = util.get_ticklabels(axis, axes)

  return ticks, labels
