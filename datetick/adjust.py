import matplotlib

from . import util
from . import compute

def font_size(axis, axes, min_gap, font_size_min, debug=False):

  ticklabels = util.get_ticklabels(axis, axes, strings=False)

  font_size_orig = util.get_font_size(axis, axes)

  if debug:
    msg = f'Minimum gap of {min_gap:.1f} px bewteen labels is less than font size of '
    msg += f'{font_size_orig} pt. Shrinking font size to avoid overlap.'
    print(msg)

  if debug:
    # Print size info in pixels for debugging purposes.
    inch = axes.figure.get_size_inches()[0]
    px = inch * axes.figure.dpi
    print(f'  Figure width: {inch:.2f} inch, {px:.1f} px')
    print(f'  axes.figure.dpi: {axes.figure.dpi} dpi')

  font_size = ticklabels[0].get_fontsize() if len(ticklabels) > 0 else matplotlib.rcParams['xtick.labelsize']

  if isinstance(font_size, str):
    font_size = matplotlib.font_manager.FontProperties(size=font_size).get_size_in_points()

  new_font_size = _fit_font_size(axis, axes, font_size, font_size_min, font_size, debug=debug)
  if debug:
    print(f'  Trying font size {new_font_size:.2f} pt.')
  matplotlib.pyplot.setp(ticklabels, fontsize=new_font_size)

  min_gap = compute.min_gap(axis, axes, debug=debug)

  if debug:
    print(f'  After shrinking font size, minimum gap between labels is {min_gap:.1f} px.')

  min_gap_warning = None
  if min_gap < font_size_min:
    lim_axis = axes.get_xlim() if axis == 'x' else axes.get_ylim()
    lim_axis_str = f"{matplotlib.dates.num2date(lim_axis[0])}/"
    lim_axis_str += f"{matplotlib.dates.num2date(lim_axis[1])}"

    min_gap_warning = f'for axis limits {lim_axis_str}, minimum gap between labels is '
    min_gap_warning += f'{min_gap:.1f} px after reducing font size from {font_size_orig} pt to '
    min_gap_warning += f'min_font_size = {font_size_min} pt.'

  return min_gap_warning


def _fit_font_size(axis, axes, target_gap, font_size_min, font_size, debug=False):
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

  if debug:
    print(f'  Using font size {best:.2f} to target minimum gap of {target_gap:.1f} px.')

  return best


def time_range(axis, axes, data_lim, debug=False):

  ticks = util.get_ticks(axis, axes)

  if len(ticks) >= 2:
    fig = axes.figure
    fig.canvas.draw()
    dt = ticks[1] - ticks[0]
    pad = 0.05 * dt
    first_candidates = ticks[ticks <= data_lim[0]]
    last_candidates = ticks[ticks >= data_lim[1]]
    first  = first_candidates[-1]  if len(first_candidates) > 0 else ticks[0] - dt
    last = last_candidates[0]  if len(last_candidates) > 0 else ticks[-1] + dt
    if debug:
      lower = matplotlib.dates.num2date(first-pad)
      upper = matplotlib.dates.num2date(last+pad)
      print(f'_adjust_range(): Setting lower limit to {lower} and upper limit to {upper}')
    if axis == 'x':
      axes.set_xlim(first - pad, last + pad)
    else:
      axes.set_ylim(first - pad, last + pad)


def xlabels(axes, adjust_first_xlabel=False, adjust_last_xlabel=False, major_font_shrink_factor=0.9, major_font_shrink_always=False, debug=False):

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
      offset = compute.numsize(axes, first_fmt1, +1, debug=debug)
      xticklabels[0].set_transform(xticklabels[0].get_transform() - offset)

  if adjust_last_xlabel and '\n' in lastlabel_text:
    if len(lastlabel_text.split('\n')[-1]) > 7:
      if debug:
        _last = lastlabel_text.replace("\n", "\\n")
        print(f'Adjusting last x-label: "{_last}"')
      adjusted = True
      # If fmt1 in last label longer than YYYY-MM, set justification to right.
      xticklabels[-1].set_ha('right')
      # Shift to left by 1/2 width of fmt1 in last label.
      last_fmt1 = lastlabel_text.split('\n')[0]
      offset = compute.numsize(axes, last_fmt1, -1, debug=debug)
      xticklabels[-1].set_transform(xticklabels[-1].get_transform() - offset)

  if adjusted or major_font_shrink_always:
    # Make all labels without newline slightly smaller than default fontsize 
    # so it is clearer that major_sub_format applies to larger number.
    if debug:
      print('Adjusting font size of x-labels without newline')
    for label in xticklabels:
      if '\n' not in label.get_text():
        label.set_fontsize(label.get_fontsize()*major_font_shrink_factor)
