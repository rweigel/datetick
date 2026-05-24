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

  max_attempts = 1
  a = min_gap < font_size
  b = min_gap > 10*font_size
  if a or b:
    # Adjust rule if overlap in labels after shrinking font size.
    # Try to use next rule so fewer labels are used.
    if rule_idx_change is None:
      rule_idx_change = 0

    if a:
      rule_idx_change += 1
    else:
      rule_idx_change -= 1

    if abs(rule_idx_change) < max_attempts + 1:
      if logger.isEnabledFor(logging.DEBUG):
        msg = f"\nAttempting to use datetick with rule change {rule_idx_change}. "
        msg += f'Attempt {abs(rule_idx_change)} of {max_attempts}.\n'
        logger.debug(msg)
      return rule_idx_change, None
    else:
      if a:
        adjust_warning = f' Tried to use {max_attempts} rules but minimum gap is '
        adjust_warning += f'still less than font_size = {font_size} px.'
      else:
        adjust_warning = f' Tried to use {max_attempts} rules but minimum gap is '
        adjust_warning += f'still greater than 10*font_size = {10*font_size} px.'
      return 0, adjust_warning

  return 0, None


def font_size_for_overlap(axis, axes, min_gap_warn):
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
      adjust_warning = _font_size(axis, axes, min_gap, font_size)
      if adjust_warning is not None and min_gap_warn:
        util.warn(adjust_warning)
      font_size_change = util.get_font_size(axis, axes) - font_size

  return font_size_change, adjust_warning


def _font_size(axis, axes, min_gap, font_size_min):

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
    logger.debug('  After shrinking font size, minimum gap between labels is %.1f px.', min_gap)

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

  # Find max significant (non-trailing-zero) decimal places across all labels.
  n_sig = 0
  for label in labels:
    if "." in label:
      n_sig = max(n_sig, len(label.rstrip("0").split(".")[-1]))

  n_places = max(min_digits, n_sig) if min_digits is not None else n_sig

  for i in range(len(labels)):
    if "." in labels[i]:
      parts = labels[i].split(".")
      frac = parts[1].ljust(n_places, "0")[0:n_places]
      labels[i] = parts[0] + ("." + frac if n_places > 0 else "")

  return labels


def time_range(axis, axes, lim_data, tight):
  ticks = util.get_ticks(axis, axes)

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


def first_last_labels(axes, adjust_first_xlabel=False, adjust_last_xlabel=False):

  # Remove existing custom first/last labels if they exist.
  for which in ['first', 'last']:
    custom_label = getattr(axes, f'_datetick_custom_{which}_xlabel', None)
    if custom_label is not None:
      if logger.isEnabledFor(logging.DEBUG):
        logger.debug('Removing existing custom %s x-label', which)
      try:
        custom_label.remove()
      except ValueError:
        pass
      delattr(axes, f'_datetick_custom_{which}_xlabel')


  xticklabels = axes.get_xticklabels()

  original_first_alpha = getattr(axes, '_datetick_first_xlabel_alpha', xticklabels[0].get_alpha())
  original_last_alpha = getattr(axes, '_datetick_last_xlabel_alpha', xticklabels[-1].get_alpha())
  xticklabels[0].set_alpha(original_first_alpha)
  xticklabels[-1].set_alpha(original_last_alpha)

  adjusted = False

  if adjust_first_xlabel:
    firstlabel_text = xticklabels[0].get_text()
    if '\n' in firstlabel_text:
      if len(firstlabel_text.split('\n')[-1]) > 7:
        if logger.isEnabledFor(logging.DEBUG):
          _first = firstlabel_text.replace("\n", "\\n")
          logger.debug('Adjusting first x-label: "%s"', _first)

        adjusted = True
        xticklabels[0].set_ha('left')
        xticklabels[0].set_multialignment('left')

        axes._datetick_first_xlabel_alpha = xticklabels[0].get_alpha()
        xticklabels[0].set_alpha(0)

        _custom_label(axes, xticklabels[0], which='first')

      else:
        if logger.isEnabledFor(logging.DEBUG):
          logger.debug('First x-label does not have newline; no adjustment needed.')

  if adjust_last_xlabel:
    lastlabel_text = xticklabels[-1].get_text()
    if '\n' in lastlabel_text:
      if len(lastlabel_text.split('\n')[-1]) > 7:
        if logger.isEnabledFor(logging.DEBUG):
          _last = lastlabel_text.replace("\n", "\\n")
          logger.debug('Adjusting last x-label: "%s"', _last)

        adjusted = True
        xticklabels[-1].set_ha('right')
        xticklabels[-1].set_multialignment('right')

        axes._datetick_last_xlabel_alpha = xticklabels[-1].get_alpha()
        xticklabels[-1].set_alpha(0)

        _custom_label(axes, xticklabels[-1], which='last')

      else:
        if logger.isEnabledFor(logging.DEBUG):
          logger.debug('Last x-label does not have newline; no adjustment needed.')

  return adjusted


def _custom_label(axes, label, which):

  label_text = label.get_text()

  axes.figure.canvas.draw()
  renderer = axes.figure.canvas.get_renderer()

  first_line_text = label_text.split('\n')[0]
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
    multialignment = 'left'
    xy = (bbox.x0, bbox.y1)
  else:
    ha = 'right'
    multialignment = 'right'
    xy = (bbox.x1, bbox.y1)
    shift_x = -shift_x

  anchor_x, anchor_y = axes.transAxes.inverted().transform(xy)

  anchor_x = anchor_x - shift_x

  kwargs = {
    'transform': axes.transAxes,
    'ha': ha,
    'va': 'top',
    'multialignment': multialignment,
    'fontproperties': font_props,
    'color': label.get_color(),
    'linespacing': getattr(label, '_linespacing', 1.2),
    'clip_on': False,
    'zorder': label.get_zorder()
  }
  custom_label = axes.text(anchor_x, anchor_y, label_text, **kwargs)

  setattr(axes, f'_datetick_custom_{which}_xlabel', custom_label)


def non_sub_label_font_size(axes, font_shrink_factor=0.9):
  xticklabels = axes.get_xticklabels()

  # Make all labels without newline slightly smaller than default fontsize 
  # so it is clearer that major_sub_format applies to larger number.
  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('Adjusting font size of x-labels without newline')
  for label in xticklabels:
    if '\n' not in label.get_text():
      label.set_fontsize(label.get_fontsize()*font_shrink_factor)

