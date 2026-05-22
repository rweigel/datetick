import datetime
import importlib
import warnings
from contextlib import contextmanager

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot

import datetick as datetick_pkg


datetick_module = importlib.import_module('datetick.datetick')
rules_module = importlib.import_module('datetick.rules')
util_module = importlib.import_module('datetick.util')


@contextmanager
def patched_attr(obj, name, value):
  original = getattr(obj, name)
  setattr(obj, name, value)
  try:
    yield
  finally:
    setattr(obj, name, original)


def capture_warnings(func, *args, **kwargs):
  with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always')
    result = func(*args, **kwargs)
  messages = [str(item.message) for item in caught]
  return result, messages


def make_datetime_plot(axis='x', start=None, stop=None):
  start = datetime.datetime(2001, 1, 1, 0, 0, 0) if start is None else start
  stop = datetime.datetime(2001, 1, 2, 0, 0, 0) if stop is None else stop
  fig, ax = matplotlib.pyplot.subplots()
  if axis == 'x':
    ax.plot([start, stop], [0, 1], '*')
  else:
    ax.plot([0, 1], [start, stop], '*')
  return fig, ax


def test_y_axis_nan_case_returns_none():
  fig, ax = matplotlib.pyplot.subplots()
  try:
    ax.plot([0, 1], [float('nan'), float('nan')], '*')
    result, messages = capture_warnings(datetick_pkg.datetick, 'y', axes=ax)
    assert result is None
    assert any('Cannot use datetick()' in message or 'Cannot use datetick.' in message for message in messages)
  finally:
    matplotlib.pyplot.close(fig)


def test_no_current_figure_raises_value_error():
  matplotlib.pyplot.close('all')
  try:
    datetick_pkg.datetick()
    assert False, 'Expected datetick() to raise with no current figure.'
  except ValueError as exc:
    assert 'No current figure' in str(exc)


def test_invalid_axis_selector_raises_value_error():
  fig, ax = make_datetime_plot(axis='x')
  try:
    datetick_pkg.datetick('z', axes=ax)
    assert False, 'Expected invalid axis selector to raise.'
  except ValueError as exc:
    assert "Expected 'x' or 'y'" in str(exc)
  finally:
    matplotlib.pyplot.close(fig)


def test_infinite_x_bounds_return_none_with_warning():
  fig, ax = matplotlib.pyplot.subplots()
  try:
    ax.plot([float('inf'), 1.0], [0, 1], '*')
    result, messages = capture_warnings(datetick_pkg.datetick, 'x', axes=ax)
    assert result is None
    assert messages == []
  finally:
    matplotlib.pyplot.close(fig)


def test_empty_axes_return_none_with_warning():
  fig, ax = matplotlib.pyplot.subplots()
  try:
    result, messages = capture_warnings(datetick_pkg.datetick, 'x', axes=ax)
    assert result is None
    assert any('NaN or +/-infinity' in message for message in messages)
  finally:
    matplotlib.pyplot.close(fig)


def test_equal_y_dates_return_none():
  fig, ax = matplotlib.pyplot.subplots()
  try:
    moment = datetime.datetime(2001, 1, 1, 0, 0, 0)
    ax.plot([0, 1], [moment, moment], '*')
    result = datetick_pkg.datetick('y', axes=ax)
    assert result is None
  finally:
    matplotlib.pyplot.close(fig)


def test_no_matching_rule_uses_manual_label_fallback():
  fig, ax = make_datetime_plot(axis='x')
  try:
    with patched_attr(rules_module, 'rule', lambda *args, **kwargs: None):
      result, messages = capture_warnings(datetick_pkg.datetick, 'x', axes=ax)
    assert isinstance(result, dict)
    assert result['rule'] is None
    assert len(result['labels']) > 0
    assert any('No config rule matched' in message for message in messages)
  finally:
    matplotlib.pyplot.close(fig)


def test_none_major_locator_uses_manual_label_fallback():
  fig, ax = make_datetime_plot(axis='x')
  fallback_rule = {
    'major': {
      'locator': None,
      'formatter': None,
      'sub_format': '',
      'sub_transition': None,
    },
    'minor': {
      'locator': None,
      'formatter': None,
    },
  }
  try:
    with patched_attr(rules_module, 'rule', lambda *args, **kwargs: fallback_rule):
      result = datetick_pkg.datetick('x', axes=ax)
    assert isinstance(result, dict)
    assert result['rule'] == fallback_rule
    assert len(result['labels']) > 0
  finally:
    matplotlib.pyplot.close(fig)


def test_repeated_second_row_is_removed_from_two_line_labels():
  ticks = matplotlib.dates.date2num([
    datetime.datetime(2001, 1, 1, 0, 0, 0),
    datetime.datetime(2001, 1, 1, 1, 0, 0),
    datetime.datetime(2001, 1, 1, 2, 0, 0),
  ])
  labels = ['00\nJan', '01\nJan', '02\nJan']
  result = datetick_module._add_major_sub_string('x', [ticks[0], ticks[-1]], ticks, labels, '%Y', 'day')
  assert result[1] == '01\nJan'
  assert result[2] == '02'


def test_repeated_third_row_is_removed_from_three_line_labels():
  ticks = matplotlib.dates.date2num([
    datetime.datetime(2001, 1, 1, 0, 0, 0),
    datetime.datetime(2001, 1, 2, 0, 0, 0),
    datetime.datetime(2001, 1, 3, 0, 0, 0),
  ])
  labels = ['00\nJan', '00\nJan', '00\nJan']
  result = datetick_module._add_major_sub_string('x', [ticks[0], ticks[-1]], ticks, labels, '%Y', 'day')
  assert result[1] == '00\nJan'
  assert result[2] == '00\nJan'


def test_manual_labels_handle_mixed_fractional_and_integer_strings():
  with patched_attr(util_module, 'get_ticks', lambda axis, axes: [0, 1]):
    with patched_attr(util_module, 'get_ticklabels', lambda axis, axes: ['00', '00.50']):
      ticks, labels = datetick_module._manual_labels('x', object())
  assert ticks == [0, 1]
  assert labels == ['00', '00.5']


def test_mixed_naive_and_aware_datetimes_do_not_crash():
  fig, ax = matplotlib.pyplot.subplots()
  try:
    naive = datetime.datetime(2001, 1, 1, 0, 0, 0)
    aware = datetime.datetime(2001, 1, 2, 0, 0, 0, tzinfo=datetime.timezone.utc)
    ax.plot([naive, aware], [0, 1], '*')
    result = datetick_pkg.datetick('x', axes=ax)
    assert isinstance(result, dict)
  finally:
    matplotlib.pyplot.close(fig)


def test_microsecond_span_returns_rule_result():
  start = datetime.datetime(2001, 1, 1, 0, 0, 0, 0)
  stop = datetime.datetime(2001, 1, 1, 0, 0, 0, 200)
  fig, ax = make_datetime_plot(axis='x', start=start, stop=stop)
  try:
    result = datetick_pkg.datetick('x', axes=ax)
    assert isinstance(result, dict)
    assert result['delta_t'].total_seconds() > 0
  finally:
    matplotlib.pyplot.close(fig)


def test_multi_year_span_returns_rule_result():
  start = datetime.datetime(2001, 1, 1, 0, 0, 0)
  stop = datetime.datetime(2010, 1, 1, 0, 0, 0)
  fig, ax = make_datetime_plot(axis='x', start=start, stop=stop)
  try:
    result = datetick_pkg.datetick('x', axes=ax)
    assert isinstance(result, dict)
    assert result['delta_t'].days >= 365
  finally:
    matplotlib.pyplot.close(fig)


if __name__ == '__main__':
  for name in sorted(globals()):
    if name.startswith('test_'):
      globals()[name]()
      print(f'PASS {name}')
