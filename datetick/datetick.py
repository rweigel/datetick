"""
  datetick formats the major and minor tick labels.
"""
import datetime
import logging

import matplotlib
import matplotlib.dates # In case lazy import is implemented in future.

logger = logging.getLogger(__name__)

def datetick(*args,
             axes=None,
             adjust_range=False,
             adjust_range_tight=False,
             adjust_last_xlabel=False,
             adjust_first_xlabel=False,
             font_shrink_factor=0.87,
             font_shrink_always=False,
             min_font_size=6,
             min_gap_warn=False,
             rule_idx=None,
             rule_idx_change=None,
             set_cb=True):
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
  adjust_range: If True, expand axis range so data are always within a major tick.

  adjust_last_xlabel: If True, adjust last x-label to avoid extending past lower axis limit.
                      If 'offset', use the offset method. If 'custom', use one
                      custom multiline text artist. If 'custom_split', use
                      separate custom text artists for each line (default when
                      adjust_last_xlabel = True).

  adjust_first_xlabel: The same string options as adjust_last_xlabel are also accepted.

  font_shrink_factor: If adjust_first_xlabel or adjust_last_xlabel is True,
                      shrink font size of x-labels without newline by this
                      factor to make it clearer label is attached to tick above
                      it even when not centered.

  font_shrink_always: If True, shrink font size of x-labels without newline by
                      font_shrink_factor even if adjust_{first,last}_xlabel is False.
  """

  """
  TODO:
    * Add auto_adjust option that sets adjust_{first,last}_xlabel and
      adjust_range as needed.
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
  from . import adjust, util, rules

  axis = 'x' if len(args) == 0 else args[0]
  if axis not in ['x', 'y']:
    raise ValueError(f"Invalid axis={axis!r}. Expected 'x' or 'y'.")

  axes = util.check_axes(kwargs)

  bbox = axes.dataLim
  if axis == 'x':
    lim_data = (bbox.x0, bbox.x1)
    lim_axis = axes.get_xlim()
    ticks = axes.get_xticks()
  else:
    lim_data = (bbox.y0, bbox.y1)
    lim_axis = axes.get_ylim()
    ticks = axes.get_yticks()

  ok = util.check_bounds(lim_data, lim_axis, axis)
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

  labels = util.get_ticklabels(axis, axes)

  data_tspan = matplotlib.dates.num2date((lim_data[0], lim_data[1]))
  delta_t_data = data_tspan[-1] - data_tspan[0]

  axis_tspan = matplotlib.dates.num2date((lim_axis[0], lim_axis[1]))
  delta_t_axis = axis_tspan[-1] - axis_tspan[0]
  delta_t = delta_t_axis # max(delta_t_data, delta_t_axis)
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Data total seconds: %s', delta_t_data.total_seconds())
    logger.debug('Axis total seconds: %s', delta_t_axis.total_seconds())
    logger.debug('Rule total seconds: %s', delta_t.total_seconds())
    logger.debug('%s data min:         %s', axis, matplotlib.dates.num2date(lim_data[0]))
    logger.debug('Default %slim[0]:    %s', axis, matplotlib.dates.num2date(lim_axis[0]))
    logger.debug('Default %sticks[0]:  %s', axis, matplotlib.dates.num2date(ticks[0]))
    logger.debug('%s data max:         %s', axis, matplotlib.dates.num2date(lim_data[-1]))
    logger.debug('Default %slim[-1]:   %s', axis, matplotlib.dates.num2date(lim_axis[-1]))
    logger.debug('Default %sticks[-1]: %s', axis, matplotlib.dates.num2date(ticks[-1]))
    logger.debug('Default %slabels and ticks:', axis)
    util.print_ticks(axis, axes, ticks, labels)


  rule = rules.rule(delta_t, rule_idx_change=kwargs['rule_idx_change'])
  if rule is not None:
    logger.debug('Matched rule: %s', rule)
  else:
    msg = f'No config rule matched delta_t = {util.format_delta(delta_t)}. '
    msg += 'Using default Matplotlib locator and formatter.'
    util.warn(msg)
    return {
      'delta_t': delta_t,
      'ticks': ticks,
      'labels': labels,
      'rule': None,
      'rule_idx_change': None,
      'font_size_change': None
    }

  if kwargs['rule_idx_change'] is not None:
    # Reset rule_idx_change to None so starting labels don't have datetick()
    # formatting.
    ticks, labels = util.reset(axis, axes)

  if rule['major']['locator'] is None:

    logger.debug('No major locator rule for this time span. Using default Matplotlib locator and formatter.')
    labels = adjust.millis(labels, min_digits=1)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after modifying millis:', axis)
      util.print_ticks(axis, axes, ticks, labels)

  else:
    ticks, labels = _apply_rule(axis, axes, rule, lim_data)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after applying locators and formatters:', axis)
      util.print_ticks(axis, axes, ticks, labels)

    labels = adjust.millis(labels, min_digits=2)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after modifying millis:', axis)
      util.print_ticks(axis, axes, ticks, labels)


  if len(labels) == 0:
    logger.debug('No labels. Returning without applying major_sub_format or set_cb.')
    return

  # If font size was changed before rule change applied, font size on
  # some labels persist.
  orig_font_size = getattr(axes, '_datetick_font_size', None)
  if orig_font_size is not None:
    logger.debug('  Found _datetick_font_size. Setting all labels to have this font size.')
    for label in labels:
      label.set_fontsize(orig_font_size)
  else:
    getattr(axes, '_datetick_font_size', util.get_font_size(axis, axes))


  if adjust_range or adjust_range_tight:
    logger.debug('Adjusting %s-range', axis)

    ticks, labels = adjust.time_range(axis, axes, lim_data, adjust_range_tight)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after adjusting range:', axis)
      util.print_ticks(axis, axes, ticks, labels)


  if rule['major']['sub_format'] == '':
    ticks, labels = _update_labels(axis, axes, ticks, labels)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after updating plot:', axis)
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

    labels = _add_major_sub_string(*args)

    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after applying major_sub_format:', axis)
      util.print_ticks(axis, axes, ticks, labels)

    ticks, labels = _update_labels(axis, axes, ticks, labels)
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('%slabels and ticks after updating plot:', axis)
      util.print_ticks(axis, axes, ticks, labels)

    adjusted = adjust.first_last_labels(axes,
      adjust_first_xlabel=adjust_first_xlabel,
      adjust_last_xlabel=adjust_last_xlabel,
      edge_label_mode='custom',
      edge_label_split=True)

    if adjusted or font_shrink_always:
      adjust.non_sub_label_font_size(axes, font_shrink_factor)

  font_size_change = adjust.font_size_for_overlap(axis, axes, min_font_size, min_gap_warn)

  rule_idx_change = adjust.rule(axis, axes, rule_idx_change)

  if abs(rule_idx_change) > 3 or len(labels) < 3:
    logger.debug('Max rule_idx_change exceeded. No further rule adjustments will be made.')
  else:
    if rule_idx_change != 0:
      if rule_idx_change > 0:
        msg = 'Label overlap. '
      else:
        msg = 'Large gap between labels. '
      msg += 'Re-running datetick() with rule_idx_change = %s.\n'
      logger.debug(msg, rule_idx_change)
      kwargs['rule_idx_change'] = rule_idx_change
      kwargs['axes'] = axes
      return datetick(axis, **kwargs)


  # Trigger update of ticks when limits change due to user interaction.
  if set_cb and util.backend_is_interactive():
    _set_cb(axis, axes, kwargs)


  return {
          'delta_t': delta_t,
          'ticks': ticks,
          'labels': labels,
          'rule': rule,
          'rule_idx_change': rule_idx_change,
          'font_size_change': font_size_change
        }


def _set_cb(axis, axes, kwargs):

  def refresh(axis_name):
    if axis_name == 'x':
      axes.xaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
      axes.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    else:
      axes.yaxis.set_minor_locator(matplotlib.dates.AutoDateLocator())
      axes.yaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
    datetick(axis_name, **{**kwargs, 'set_cb': False})


  def on_xlims_change(ax):
    logger.debug('xlims changed. Updating datetick plot.')
    refresh('x')

  def on_ylims_change(ax):
    logger.debug('ylims changed. Updating datetick plot.')
    refresh('y')

  def on_resize(event):
    logger.debug('figure size changed. Updating datetick plot.')
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

  logger.debug('%slim_changed callbacks registered: %s', axis, len(axes.callbacks.callbacks.get(f'{axis}lim_changed', {})))

  disconect()

  if axis == 'x':
    cid = axes.callbacks.connect('xlim_changed', on_xlims_change)
    axes._datetick_cb_x = cid
  else:
    cid = axes.callbacks.connect('ylim_changed', on_ylims_change)
    axes._datetick_cb_y = cid

  resize_cid = axes.figure.canvas.mpl_connect('resize_event', on_resize)
  setattr(axes, f'_datetick_resize_cb_{axis}', resize_cid)


def _add_major_sub_string(axis, lim_axis, ticks, labels, major_sub_format, major_sub_transition):

  time = matplotlib.dates.num2date(ticks)
  logger.debug('Adding major_sub_format to select labels.')

  first = 0
  if False and ticks[0] < lim_axis[0]:
    if logger.isEnabledFor(logging.DEBUG):
      msg = 'First tick is less than lower axis limit. Applying major_sub_format to second tick label.'
      logger.debug(msg)
    # Work-around for bug in Matplotlib where left-most tick is less than
    # lower x-limit. Could more than one tick be less than lower x-limit?
    while first < len(ticks) and ticks[first] < lim_axis[0]:
      first += 1
    if first == len(ticks):
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('All ticks are less than lower axis limit. Applying major_sub_format to last tick label.')
      first = len(ticks) - 1

  # Always apply major_sub_format to first tick label
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Applying major_sub_format to first tick label at %s.', matplotlib.dates.num2date(ticks[first]))
  labels[first] = '%s\n%s' % (labels[first], datetime.datetime.strftime(time[first], major_sub_format))

  major_sub_format_len = len(datetime.datetime.strftime(time[first], major_sub_format))

  if major_sub_transition is None:
    return labels

  for i in range(first+1, len(time)):
    # First major label will always have major_sub_format applied.
    # Modify major labels after first under certain conditions.
    modify = False
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('Checking if major_sub_format should be applied to tick label at %s.', matplotlib.dates.num2date(ticks[i]))
      logger.debug('  major_sub_transition = %s', major_sub_transition)
      logger.debug('  time[%s] = %s', i-1, time[i-1])
      logger.debug('  time[%s] = %s', i, time[i])

    if major_sub_transition == 'year' and time[i].year != time[i-1].year:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Year changed: %s -> %s', time[i-1].year, time[i].year)
      modify = True
    if major_sub_transition == 'month' and time[i].month != time[i-1].month:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Month changed: %s -> %s', time[i-1].month, time[i].month)
      modify = True
    if major_sub_transition == 'day' and time[i].day != time[i-1].day:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Day changed: %s -> %s', time[i-1].day, time[i].day)
      modify = True
    if major_sub_transition == 'hour' and time[i].hour != time[i-1].hour:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Hour changed: %s -> %s', time[i-1].hour, time[i].hour)
      modify = True
    if major_sub_transition == 'minute' and time[i].minute !=time[i-1].minute:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Minute changed: %s -> %s', time[i-1].minute, time[i].minute)
      modify = True
    if major_sub_transition == 'second' and time[i].second != time[i-1].second:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Second changed: %s -> %s', time[i-1].second, time[i].second)
      modify = True

    if not modify:
      continue

    if i == first + 1 and axis == 'x':
      # If first two major tick labels have major_sub_format applied, the will
      # likely run together. This keeps major_sub_format label for second major
      # tick.

      if major_sub_format_len > 7 and major_sub_transition in ['month', 'day', 'hour', 'minute', 'second']:
        if logger.isEnabledFor(logging.DEBUG):
          logger.debug('  Removing major_sub_format to first tick label at %s to avoid overlap with second label.', matplotlib.dates.num2date(ticks[first]))
        labels[first] = labels[first].split('\n')[0]
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Applying major_sub_format to tick label at %s.', matplotlib.dates.num2date(ticks[i]))
      labels[i] = '%s\n%s' % (labels[i], datetime.datetime.strftime(matplotlib.dates.num2date(ticks[i]), major_sub_format))
    else:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('  Applying major_sub_format to tick label at %s.', matplotlib.dates.num2date(ticks[i]))
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
  from . import util
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

  axes.figure.canvas.draw()
  ticks = util.get_ticks(axis, axes)
  labels = util.get_ticklabels(axis, axes)

  return ticks, labels


def _apply_rule(axis, axes, rule, lim_data):

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
