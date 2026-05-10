import matplotlib

def min_gap(axis, axes, debug=False):

  from . import util
  axes.figure.canvas.draw()

  renderer = axes.figure.canvas.get_renderer()
  ticklabels = util.get_ticklabels(axis, axes, strings=False)

  bboxes = [label.get_window_extent(renderer) for label in ticklabels]

  def _min_gap(axis, bboxes, ticklabels, sub_labels=False, debug=False):

    min_ = float('inf')

    if sub_labels:
      # Keep only labels and bboxes with \n
      pairs = [(b, t) for b, t in zip(bboxes, ticklabels) if "\n" in t.get_text()]
    else:
      # Keep only labels and bboxes without \n
      pairs = [(b, t) for b, t in zip(bboxes, ticklabels) if "\n" not in t.get_text()]
    bboxes = [b for b, _ in pairs]
    ticklabels = [t for _, t in pairs]

    for i in range(len(bboxes)-1):
      prev = ticklabels[i].get_text().replace('\n', '\\n')
      next_ = ticklabels[i+1].get_text().replace('\n', '\\n')

      if axis == 'x':
        separation = bboxes[i+1].x0 - bboxes[i].x1
      else:
        separation = bboxes[i+1].y0 - bboxes[i].y1

      min_ = min(min_, separation) if i > 0 else separation
      if separation <= 0:
        if debug:
          prev = ticklabels[i].get_text().replace('\n', '\\n')
          next_ = ticklabels[i+1].get_text().replace('\n', '\\n')
          print(f"Tick labels '{next_}' and '{prev}' may overlap (separation={separation:.1f}px).")

    return min_

  min_gap_primary = _min_gap(axis, bboxes, ticklabels, sub_labels=False, debug=debug)
  min_gap_sub = _min_gap(axis, bboxes, ticklabels, sub_labels=True, debug=debug)

  return min(min_gap_sub, min_gap_primary)


def numsize(ax, num, sign, debug=False):
  '''Returns (width, height) of str(num) in pixels.

  If ax is given, measures against that axes' renderer and DPI (correct).
  Otherwise creates a temporary figure using rcParams figure.dpi.
  '''
  import re

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
