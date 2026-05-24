import logging
import matplotlib


logger = logging.getLogger(__name__)

def min_gap(axis, axes):

  from . import util
  axes.figure.canvas.draw()

  renderer = axes.figure.canvas.get_renderer()
  ticklabels = util.get_ticklabels(axis, axes, strings=False)

  bboxes = [label.get_window_extent(renderer) for label in ticklabels]

  def _min_gap(axis, bboxes, ticklabels, sub_labels=False):

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
        if logger.isEnabledFor(logging.DEBUG):
          prev = ticklabels[i].get_text().replace('\n', '\\n')
          next_ = ticklabels[i+1].get_text().replace('\n', '\\n')
          logger.debug("  Tick labels '%s' and '%s' may overlap (separation=%.1fpx).", next_, prev, separation)

    return min_

  min_gap_primary = _min_gap(axis, bboxes, ticklabels, sub_labels=False)
  min_gap_sub = _min_gap(axis, bboxes, ticklabels, sub_labels=True)

  return min(min_gap_sub, min_gap_primary)


def numsize(ax, num, sign):
  '''Returns the x-offset of str(num) in display dots.'''
  num = str(num)

  ax.figure.canvas.draw()
  renderer = ax.figure.canvas.get_renderer()

  ticklabels = ax.get_xticklabels()
  if ticklabels:
    font_props = ticklabels[0].get_fontproperties()
  else:
    fontsize = matplotlib.rcParams['xtick.labelsize']
    font_props = matplotlib.font_manager.FontProperties(size=fontsize)

  # first_last_labels() shifts by half the width of the first line.
  width_px, height_px, descent_px = renderer.get_text_width_height_descent(
    num, font_props, ismath=False
  )
  dx = sign * 0.5 * width_px

  if logger.isEnabledFor(logging.DEBUG):
    logger.debug('  compute.numsize():')
    logger.debug('    num      = "%s"', num)
    logger.debug('    fontsize = %s', font_props.get_size_in_points())
    logger.debug('    width_px = %s', width_px)
    logger.debug('    height_px = %s', height_px)
    logger.debug('    descent_px = %s', descent_px)
    logger.debug('    delta_px = %s', dx)
    logger.debug('    dx       = %s', dx)

  return dx
