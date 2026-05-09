import matplotlib

from . import compute

def font_size(fig, axes, dir, min_gap, min_font_size, debug=False):
  # Print axes width in pixels and min_gap in pixels for debugging purposes.
  if debug:
    fig_width_inch = fig.get_size_inches()[0]
    dpi = fig.dpi
    fig_width_pix = fig_width_inch * dpi
    print(f'Figure width: {fig_width_inch:.2f} inch, {fig_width_pix:.1f} px')
    print(f'Minimum gap between labels: {min_gap:.1f} px')
    if debug:
      print(f'Minimum gap of {min_gap:.1f} px is less than min_font_size of {min_font_size} px. Shrinking font size to avoid overlap.')
    ticklabels = axes.get_xticklabels() if dir == 'x' else axes.get_yticklabels()
    font_size = ticklabels[0].get_fontsize() if len(ticklabels) > 0 else matplotlib.pyplot.rcParams['font.size']
    if isinstance(font_size, str):
      font_size = matplotlib.font_manager.FontProperties(size=font_size).get_size_in_points()

    new_font_size = _fit_font_size(axes, dir, min_font_size, min_font_size, font_size, debug=debug)
    matplotlib.pyplot.setp(axes.get_xticklabels() if dir == 'x' else axes.get_yticklabels(), fontsize=new_font_size)

    min_gap = compute.min_gap(axes, dir, debug=debug)
    if debug:
      print(f'After shrinking font size, minimum gap between labels is {min_gap:.1f} px.')

  return min_gap


def _fit_font_size(axes, dir, target_gap, min_font_size, font_size, debug=False):
  """Find a tick-label font size whose rendered minimum gap is near target_gap.

  This does a small binary search over font size in points. At each step it
  renders the current tick labels, measures the minimum separation between
  adjacent label bounding boxes with compute.min_gap(), and keeps the size that gets
  closest to target_gap in pixels.
  """

  ticklabels = axes.get_xticklabels() if dir == 'x' else axes.get_yticklabels()
  lo = min_font_size
  hi = float(font_size)
  best = hi
  best_err = abs(compute.min_gap(axes, dir) - target_gap)

  for _ in range(8):
    mid = 0.5 * (lo + hi)
    matplotlib.pyplot.setp(ticklabels, fontsize=mid)
    gap = compute.min_gap(axes, dir)
    err = abs(gap - target_gap)
    if err < best_err:
      best = mid
      best_err = err
    if gap < target_gap:
      hi = mid
    else:
      lo = mid

  if debug:
    print(f'Using font size {best:.2f} to target minimum gap of {target_gap:.1f} px.')
  return best


def time_range(dir, fig, axes, datamin, datamax, debug=False):

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
      print(f'_adjust_range(): Setting lower limit to {matplotlib.dates.num2date(first-pad)} and upper limit to {matplotlib.dates.num2date(last+pad)}')
    if dir == 'x':
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
      # If fmt1 iin last label longer than YYYY-MM, set justification to right.
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
