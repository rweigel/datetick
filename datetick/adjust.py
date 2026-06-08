import logging
import matplotlib

from . import util
from . import compute

logger = logging.getLogger(__name__)

def rule(axis, axes, rule_idx_change):
  """
  Adjust rule if overlap in labels after shrinking font size.
  Try to use next rule so fewer labels are used.
  """
  font_size = util.get_font_size(axis, axes)
  min_gap = compute.min_gap(axis, axes)

  a = min_gap < font_size
  b = min_gap > 8*font_size
  if not a and not b:
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('No adjustment needed for rule_idx_change.')
    return 0

  # Adjust rule if overlap in labels after reducing font size.
  # Try to use next rule so fewer or more labels are used.
  logger.debug('Last rule_idx_change = %s', rule_idx_change)
  if rule_idx_change is None:
    rule_idx_change = 0
  rule_idx_change_last = rule_idx_change
  if a:
    rule_idx_change += 1
  else:
    rule_idx_change -= 1
  logger.debug('New rule_idx_change = %s', rule_idx_change)

  # Stop if the retry direction reverses; that means the previous retry overshot
  # and continuing would oscillate between neighboring rule offsets.
  if rule_idx_change_last != 0 and abs(rule_idx_change) < abs(rule_idx_change_last):
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug(
        'rule_idx_change reversed from %s to %s. Resetting to 0.',
        rule_idx_change_last,
        rule_idx_change,
      )
    return 0

  # Check that sign of rule_idx_change = sign of rule_idx_change_last
  if rule_idx_change != 0 and rule_idx_change_last * rule_idx_change < 0:
    if logger.isEnabledFor(logging.DEBUG):
      logger.debug('rule_idx_change = %s has opposite sign of previous rule_idx_change = %s. Resetting to 0.', rule_idx_change, rule_idx_change_last)
    return 0

  return rule_idx_change


def font_size_for_overlap(axis, axes, min_font_size, min_gap_warn):
  adjust_warning = None
  # Adjust font size if overlap in labels.

  font_size = util.get_font_size(axis, axes)
  min_gap = compute.min_gap(axis, axes)

  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Minimum gap between %s-tick labels: %.1f px.', axis, min_gap)

  adjust_warning = None
  font_size = util.get_font_size(axis, axes)
  font_size_change = 0
  if min_gap < font_size:
    if font_size is not None:
      adjust_warning = _reduce_font_size(axis, axes, min_gap, min_font_size)
      if adjust_warning is not None and min_gap_warn:
        util.warn(adjust_warning)
      font_size_change = util.get_font_size(axis, axes) - font_size

  return font_size_change


def _reduce_font_size(axis, axes, min_gap, font_size_min):

  ticklabels = util.get_ticklabels(axis, axes, strings=False)

  font_size_orig = util.get_font_size(axis, axes)

  if logger.isEnabledFor(logging.DEBUG):
    msg = f'Minimum gap of {min_gap:.1f} px bewteen labels is less than font size of '
    msg += f'{font_size_orig} pt. Shrinking font size to avoid overlap.'
    logger.debug(msg)

  if logger.isEnabledFor(logging.DEBUG):
    # Print size info in pixels for debugging purposes.
    inch = axes.figure.get_size_inches()[0]
    px = inch * axes.figure.dpi
    logger.debug('  Figure width: %.2f inch, %.1f px', inch, px)
    logger.debug('  axes.figure.dpi: %s dpi', axes.figure.dpi)

  font_size = ticklabels[0].get_fontsize() if len(ticklabels) > 0 else matplotlib.rcParams['xtick.labelsize']

  if isinstance(font_size, str):
    font_size = matplotlib.font_manager.FontProperties(size=font_size).get_size_in_points()

  new_font_size = _fit_font_size(axis, axes, font_size, font_size_min, font_size)
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('  Trying font size %.2f pt.', new_font_size)
  matplotlib.pyplot.setp(ticklabels, fontsize=new_font_size)

  min_gap = compute.min_gap(axis, axes)

  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('  After changing font size, minimum gap between labels is %.1f px.', min_gap)

  min_gap_warning = None
  if min_gap < font_size_min:
    lim_axis = axes.get_xlim() if axis == 'x' else axes.get_ylim()
    lim_axis_str = f"{matplotlib.dates.num2date(lim_axis[0])}/"
    lim_axis_str += f"{matplotlib.dates.num2date(lim_axis[1])}"

    min_gap_warning = f'for axis limits {lim_axis_str}, minimum gap between labels is '
    min_gap_warning += f'{min_gap:.1f} px after reducing font size from {font_size_orig} pt to '
    min_gap_warning += f'min_font_size = {font_size_min} pt.'

  return min_gap_warning


def _fit_font_size(axis, axes, target_gap, font_size_min, font_size):
  """Find a tick-label font size with rendered minimum gap is near target_gap.

  Search over font size in points. At each step it
  renders the current tick labels, measures the minimum separation between
  adjacent label bounding boxes with compute.min_gap(), and keeps the size that gets
  closest to target_gap in pixels.
  """

  ticklabels = util.get_ticklabels(axis, axes, strings=False)

  lo = font_size_min
  hi = float(font_size)
  best = hi
  best_err = abs(compute.min_gap(axis, axes) - target_gap)

  for _ in range(8):
    mid = 0.5 * (lo + hi)
    matplotlib.pyplot.setp(ticklabels, fontsize=mid)
    gap = compute.min_gap(axis, axes)
    err = abs(gap - target_gap)
    if err < best_err:
      best = mid
      best_err = err
    if gap < target_gap:
      hi = mid
    else:
      lo = mid

  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('  Using font size %.2f to target minimum gap of %.1f px.', best, target_gap)

  return best


def millis(labels, min_digits=2):
  """
  Remove redundant trailing zeros in fractional part of milliseconds in labels.

  Example:
    1.100000, 1.200000
  becomes, if min_digits = 1,
    1.1, 1.2
  If min_digits = 2
    1.10, 1.20

  Example:
    1.150000, 1.200000
  becomes, if min_digits = 1,
    1.15, 1.20
  If min_digits = 3
    1.150, 1.200
  """

  def _split_label(label):
    if '\n' not in label:
      return label, ''
    first_line, remainder = label.split('\n', 1)
    return first_line, '\n' + remainder

  # Find max significant (non-trailing-zero) decimal places across all first lines.
  n_sig = 0
  for label in labels:
    first_line, _ = _split_label(label)
    if "." in first_line:
      n_sig = max(n_sig, len(first_line.rstrip("0").split(".")[-1]))

  n_places = max(min_digits, n_sig) if min_digits is not None else n_sig

  for i in range(len(labels)):
    first_line, remainder = _split_label(labels[i])
    if "." in first_line:
      whole, frac = first_line.split(".", 1)
      frac = frac.ljust(n_places, "0")[0:n_places]
      first_line = whole + ("." + frac if n_places > 0 else "")
      labels[i] = first_line + remainder

  return labels


def time_range(axis, axes, lim_data, tight):
  ticks = util.get_ticks(axis, axes)
  labels = util.get_ticklabels(axis, axes)

  if len(ticks) >= 2:
    fig = axes.figure
    fig.canvas.draw()
    dt = ticks[1] - ticks[0]
    if tight:
      pad = 0.0
    else:
      pad = 0.05 * dt
    first_candidates = ticks[ticks <= lim_data[0]]
    last_candidates = ticks[ticks >= lim_data[1]]
    first  = first_candidates[-1]  if len(first_candidates) > 0 else ticks[0] - dt
    last = last_candidates[0]  if len(last_candidates) > 0 else ticks[-1] + dt
    if logger.isEnabledFor(logging.DEBUG):
      lower = matplotlib.dates.num2date(first-pad)
      upper = matplotlib.dates.num2date(last+pad)
      logger.debug('adjust.time_range(): Setting lower limit to %s and upper limit to %s', lower, upper)
    if axis == 'x':
      axes.set_xlim(first - pad, last + pad)
    else:
      axes.set_ylim(first - pad, last + pad)

    axes.figure.canvas.draw()
    ticks = util.get_ticks(axis, axes)
    labels = util.get_ticklabels(axis, axes)

  return ticks, labels


def first_last_labels(axes, adjust_first_xlabel=False, adjust_last_xlabel=False, edge_label_mode='custom', edge_label_split=True):

  # Remove existing custom first/last labels if they exist.
  for which in ['first', 'last']:
    custom_labels = getattr(axes, f'_datetick_custom_{which}_xlabel', None)
    if custom_labels is not None:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('Removing existing custom %s x-label', which)
      if not isinstance(custom_labels, (list, tuple)):
        custom_labels = [custom_labels]
      for custom_label in custom_labels:
        try:
          custom_label.remove()
        except ValueError:
          pass
      delattr(axes, f'_datetick_custom_{which}_xlabel')


  xticklabels = axes.get_xticklabels()
  _restore_edge_label(axes, xticklabels[0], which='first')
  _restore_edge_label(axes, xticklabels[-1], which='last')

  original_first_alpha = getattr(axes, '_datetick_first_xlabel_alpha', xticklabels[0].get_alpha())
  original_last_alpha = getattr(axes, '_datetick_last_xlabel_alpha', xticklabels[-1].get_alpha())
  xticklabels[0].set_alpha(original_first_alpha)
  xticklabels[-1].set_alpha(original_last_alpha)

  default_first = _edge_label_options(adjust_first_xlabel, edge_label_mode=edge_label_mode, split=edge_label_split)
  default_last = _edge_label_options(adjust_last_xlabel, edge_label_mode=edge_label_mode, split=edge_label_split)

  adjusted = False

  if default_first['enabled']:
    firstlabel_text = xticklabels[0].get_text()
    if '\n' in firstlabel_text:
      if len(firstlabel_text.split('\n')[-1]) > 7:
        if logger.isEnabledFor(logging.DEBUG):
          _first = firstlabel_text.replace("\n", "\\n")
          logger.debug('Adjusting first x-label: "%s"', _first)

        adjusted = True
        xticklabels[0].set_ha('left')
        xticklabels[0].set_multialignment('left')

        if default_first['edge_label_mode'] == 'custom':
          axes._datetick_first_xlabel_alpha = xticklabels[0].get_alpha()
          xticklabels[0].set_alpha(0)
          _custom_label(axes, xticklabels[0], which='first', split=default_first['split'])
        else:
          _offset_edge_label(axes, xticklabels[0], which='first')

      else:
        if logger.isEnabledFor(logging.DEBUG):
          logger.debug('First x-label does not have newline; no adjustment needed.')

  if default_last['enabled']:
    lastlabel_text = xticklabels[-1].get_text()
    if '\n' in lastlabel_text:
      if len(lastlabel_text.split('\n')[-1]) > 7:
        if logger.isEnabledFor(logging.DEBUG):
          _last = lastlabel_text.replace("\n", "\\n")
          logger.debug('Adjusting last x-label: "%s"', _last)

        adjusted = True
        xticklabels[-1].set_ha('right')
        xticklabels[-1].set_multialignment('right')

        if default_last['edge_label_mode'] == 'custom':
          axes._datetick_last_xlabel_alpha = xticklabels[-1].get_alpha()
          xticklabels[-1].set_alpha(0)
          _custom_label(axes, xticklabels[-1], which='last', split=default_last['split'])
        else:
          _offset_edge_label(axes, xticklabels[-1], which='last')

      else:
        if logger.isEnabledFor(logging.DEBUG):
          logger.debug('Last x-label does not have newline; no adjustment needed.')

  return adjusted


def _edge_label_options(value, edge_label_mode='custom', split=True):
  if isinstance(value, str):
    if value == 'offset':
      return {'enabled': True, 'edge_label_mode': 'offset', 'split': False}
    if value == 'custom':
      return {'enabled': True, 'edge_label_mode': 'custom', 'split': False}
    if value in ('custom_split', 'custom+'):
      return {'enabled': True, 'edge_label_mode': 'custom', 'split': True}
    raise ValueError(
      f"Invalid edge-label option {value!r}. Expected True, False, 'offset', 'custom', 'custom+', or 'custom_split'."
    )

  if edge_label_mode not in ('custom', 'offset'):
    raise ValueError(f"Invalid edge_label_mode={edge_label_mode!r}. Expected 'custom' or 'offset'.")

  return {
    'enabled': bool(value),
    'edge_label_mode': edge_label_mode,
    'split': split,
  }


def _restore_edge_label(axes, label, which):
  original_transform = getattr(axes, f'_datetick_{which}_xlabel_transform', None)
  if original_transform is not None:
    label.set_transform(original_transform)
    delattr(axes, f'_datetick_{which}_xlabel_transform')

  original_ha = getattr(axes, f'_datetick_{which}_xlabel_ha', None)
  if original_ha is not None:
    label.set_ha(original_ha)
    delattr(axes, f'_datetick_{which}_xlabel_ha')

  original_multialignment = getattr(axes, f'_datetick_{which}_xlabel_multialignment', None)
  if original_multialignment is not None:
    label.set_multialignment(original_multialignment)
    delattr(axes, f'_datetick_{which}_xlabel_multialignment')


def _get_multialignment(label):
  if hasattr(label, 'get_multialignment'):
    return label.get_multialignment()
  return getattr(label, '_multialignment', label.get_ha())


def _offset_edge_label(axes, label, which):

  axes.figure.canvas.draw()
  renderer = axes.figure.canvas.get_renderer()

  first_line_text = label.get_text().split('\n')[0]
  font_props = label.get_fontproperties().copy()
  first_line_width_px, _, _ = renderer.get_text_width_height_descent(
    first_line_text, font_props, ismath=False
  )

  if not hasattr(axes, f'_datetick_{which}_xlabel_transform'):
    setattr(axes, f'_datetick_{which}_xlabel_transform', label.get_transform())
    setattr(axes, f'_datetick_{which}_xlabel_ha', label.get_ha())
    setattr(axes, f'_datetick_{which}_xlabel_multialignment', _get_multialignment(label))

  shift_x_px = first_line_width_px / 2.0
  if which == 'last':
    shift_x_px = -shift_x_px

  offset = matplotlib.transforms.ScaledTranslation(
    shift_x_px / axes.figure.dpi,
    0,
    axes.figure.dpi_scale_trans,
  )
  label.set_transform(getattr(axes, f'_datetick_{which}_xlabel_transform') + offset)
  label.set_clip_on(False)


def _custom_label(axes, label, which, split=True):

  label_text = label.get_text()
  label_lines = label_text.split('\n')

  axes.figure.canvas.draw()
  renderer = axes.figure.canvas.get_renderer()

  first_line_text = label_lines[0]
  font_props = label.get_fontproperties().copy()
  first_line_width_px, _, _ = renderer.get_text_width_height_descent(
    first_line_text, font_props, ismath=False
  )

  inverted = axes.transAxes.inverted()
  xy = (first_line_width_px / 2.0, 0)
  shift_x = (inverted.transform(xy)[0] - inverted.transform((0, 0))[0])

  bbox = label.get_window_extent(renderer=renderer)
  if which == 'first':
    ha = 'left'
    xy = (bbox.x0, bbox.y1)
  else:
    ha = 'right'
    xy = (bbox.x1, bbox.y1)
    shift_x = -shift_x

  anchor_x, anchor_y = axes.transAxes.inverted().transform(xy)

  anchor_x = anchor_x - shift_x

  kwargs = {
    'transform': axes.transAxes,
    'ha': ha,
    'va': 'top',
    'multialignment': ha,
    'fontproperties': font_props,
    'color': label.get_color(),
    'clip_on': False,
    'zorder': label.get_zorder()
  }

  if not split:
    custom_label = axes.text(
      anchor_x,
      anchor_y,
      label_text,
      **kwargs,
    )
    setattr(axes, f'_datetick_custom_{which}_xlabel', custom_label)
    return

  line_spacing = getattr(label, '_linespacing', 1.2)
  line_height_px = font_props.get_size_in_points() * line_spacing * axes.figure.dpi / 72.0
  line_height_axes = (
    axes.transAxes.inverted().transform((0, line_height_px))[1]
    - axes.transAxes.inverted().transform((0, 0))[1]
  )

  custom_labels = []
  for idx, line in enumerate(label_lines):
    custom_label = axes.text(
      anchor_x,
      anchor_y - idx * line_height_axes,
      line,
      **kwargs,
    )
    custom_labels.append(custom_label)

  setattr(axes, f'_datetick_custom_{which}_xlabel', custom_labels)


def non_sub_label_font_size(axes, font_shrink_factor):
  xticklabels = axes.get_xticklabels()

  # Make all labels without newline slightly smaller than default fontsize 
  # so it is clearer that major_sub_format applies to larger number.
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Adjusting font size of x-labels without newline')

  orig = xticklabels[0].get_fontsize()
  new = orig*font_shrink_factor

  for label in xticklabels:
    if '\n' not in label.get_text():
      logger.debug(f"  Reducing font size of {label} from {orig} to {new}")
      label.set_fontsize(new)
