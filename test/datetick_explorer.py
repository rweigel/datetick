import datetime
from dataclasses import dataclass, field
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.offsetbox import AnchoredText
from matplotlib.widgets import Button, Slider
from datetick import datetick


INITIAL_START = '1999-01-01T00:00:00'
INITIAL_END = '1999-01-01T05:00:00'
FIGURE_SIZE = (16, 9)
PLOT_HSPACE = 0.35
PLOT_TITLE_Y = 1
PLOT_TITLE_PAD = -14
PLOT_LABEL_PAD = 0.25
PLOT_LABEL_BORDER_PAD = 0.6
PLOT_LABEL_BOX_STYLE = 'round,pad=0.25'
PLOT_LABEL_FACE_COLOR = 'white'
PLOT_LABEL_EDGE_COLOR = '0.5'

SLIDER_LEFT = 0.15
SLIDER_GAP = 0.4
SLIDER_WIDTH = 0.3
SLIDER_HEIGHT = 0.02
SLIDER_ROW_COUNT = 6
SLIDER_ROW_FILL = 0.85
SLIDER_BOTTOM = 0.1
SLIDER_EDGE_PAD = 0.5
SLIDER_HANDLE_SIZE = 14

RESET_LEFT = 0.47
RESET_WIDTH = 0.05
RESET_HEIGHT = 0.02
RESET_GAP_ABOVE_SLIDERS = 0.03

SUBPLOTS_BOTTOM = 0.25

SLIDER_DEFS_I = [
    ('Year',   1900, 2100, 1999),
    ('Month',  1,    12,   1),
    ('Day',    1,    31,   1),
    ('Hour',   0,    23,   0),
    ('Minute', 0,    59,   0),
    ('Second', 0,    59,   0),
]
SLIDER_DEFS_F = [
    ('Year',   1900, 2100, 1999),
    ('Month',  1,    12,   1),
    ('Day',    1,    31,   1),
    ('Hour',   0,    23,   2),
    ('Minute', 0,    59,   0),
    ('Second', 0,    59,   0),
]


@dataclass
class ExplorerState:
    fig: object
    ax1: object
    ax2: object
    plt1: object
    plt2: object
    label1: object
    label2: object
    sliders_i: list = field(default_factory=list)
    sliders_f: list = field(default_factory=list)
    last_valid_i: list = field(default_factory=list)
    last_valid_f: list = field(default_factory=list)
    suppress_update: bool = False


def get_datetime(sliders):
    return datetime.datetime(*[int(s.val) for s in sliders])


def slider_values(sliders):
    return [int(s.val) for s in sliders]


def create_plot(subplots_bottom):
    ds1 = INITIAL_START
    ds2 = INITIAL_END
    dt1 = datetime.datetime.fromisoformat(ds1)
    dt2 = datetime.datetime.fromisoformat(ds2)
    x = np.array([dt1, dt2], dtype=object)
    y = [0.0, 0.0]

    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=FIGURE_SIZE)
    plt.subplots_adjust(bottom=subplots_bottom, hspace=PLOT_HSPACE)

    plt1, = ax1.plot(x, y, '*')
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax1.xaxis.set_major_locator(locator)
    ax1.xaxis.set_major_formatter(formatter)
    label1 = AnchoredText(
        'matplotlib+AutoDateLocator/ConciseDateFormatter',
        loc='upper left',
        pad=PLOT_LABEL_PAD,
        borderpad=PLOT_LABEL_BORDER_PAD,
        frameon=True,
    )
    label1.patch.set_boxstyle(PLOT_LABEL_BOX_STYLE)
    label1.patch.set_facecolor(PLOT_LABEL_FACE_COLOR)
    label1.patch.set_edgecolor(PLOT_LABEL_EDGE_COLOR)
    ax1.add_artist(label1)

    ax1.set_title(ds1 + ' - ' + ds2, loc='center')#, y=1, pad=-14)
    ax1.grid()

    plt2, = ax2.plot(x, y, '*')
    label2 = AnchoredText(
        'datetick',
        loc='upper left',
        pad=PLOT_LABEL_PAD,
        borderpad=PLOT_LABEL_BORDER_PAD,
        frameon=True,
    )
    label2.patch.set_boxstyle(PLOT_LABEL_BOX_STYLE)
    label2.patch.set_facecolor(PLOT_LABEL_FACE_COLOR)
    label2.patch.set_edgecolor(PLOT_LABEL_EDGE_COLOR)
    ax2.add_artist(label2)
    datetick('x', axes=ax2, debug=True)
    ax2.grid()

    ax3.axis('off')
    return ExplorerState(
        fig=fig,
        ax1=ax1,
        ax2=ax2,
        plt1=plt1,
        plt2=plt2,
        label1=label1,
        label2=label2,
    )


def set_controls(subplots_bottom, update_callback, reset_callback):
    slider_row_gap = (subplots_bottom * SLIDER_ROW_FILL) / SLIDER_ROW_COUNT
    slider_top = SLIDER_BOTTOM + (SLIDER_ROW_COUNT - 1) * slider_row_gap + SLIDER_HEIGHT
    reset_bottom = slider_top + RESET_GAP_ABOVE_SLIDERS

    slider_list = [(SLIDER_DEFS_I, []), (SLIDER_DEFS_F, [])]


    for col, (defs, sliders) in enumerate(slider_list):
        x0 = SLIDER_LEFT + col * SLIDER_GAP
        for row, (label, vmin, vmax, vinit) in enumerate(reversed(defs)):
            ax_s = plt.axes([x0, SLIDER_BOTTOM + row * slider_row_gap, SLIDER_WIDTH, SLIDER_HEIGHT])
            allowed_values = np.arange(vmin, vmax + 1)
            s = Slider(
                ax_s,
                label,
                vmin - SLIDER_EDGE_PAD,
                vmax + SLIDER_EDGE_PAD,
                valinit=vinit,
                valfmt='%0.0f',
                valstep=allowed_values,
                handle_style={'size': SLIDER_HANDLE_SIZE},
            )
            s.on_changed(lambda val, slider=s: update_callback(val, slider))
            sliders.insert(0, s)

    sliders_i, sliders_f = slider_list[0][1], slider_list[1][1]

    axreset = plt.axes([RESET_LEFT, reset_bottom, RESET_WIDTH, RESET_HEIGHT])
    breset = Button(axreset, 'Reset')
    breset.on_clicked(reset_callback)

    return sliders_i, sliders_f


def main():
    subplots_bottom = SUBPLOTS_BOTTOM
    state = create_plot(subplots_bottom)

    def update_plot(xlow, xhigh):
        if xlow >= xhigh:
            return

        x = np.array([xlow, xhigh], dtype=object)
        title = xlow.isoformat() + ' to ' + xhigh.isoformat()

        print("---Updating matplotlib plot")
        state.plt1.set_xdata(x)
        state.ax1.set_xlim(xlow, xhigh)
        state.ax1.set_title(title, loc='center', y=PLOT_TITLE_Y, pad=PLOT_TITLE_PAD)

        print("---Updating datetick plot")
        state.plt2.set_xdata(x)
        state.ax2.set_xlim(xlow, xhigh)

    def restore_slider(slider):
        state.suppress_update = True
        try:
            if slider in state.sliders_i:
                idx = state.sliders_i.index(slider)
                slider.set_val(state.last_valid_i[idx])
            elif slider in state.sliders_f:
                idx = state.sliders_f.index(slider)
                slider.set_val(state.last_valid_f[idx])
        finally:
            state.suppress_update = False

    def update(val, changed_slider=None):
        if state.suppress_update:
            return

        try:
            xlow = get_datetime(state.sliders_i)
            xhigh = get_datetime(state.sliders_f)
        except ValueError:
            if changed_slider is not None:
                restore_slider(changed_slider)
            return

        if xlow >= xhigh:
            if changed_slider is not None:
                restore_slider(changed_slider)
            return

        state.last_valid_i = slider_values(state.sliders_i)
        state.last_valid_f = slider_values(state.sliders_f)
        print(f"---Update to {xlow.isoformat()} to {xhigh.isoformat()}---")
        update_plot(xlow, xhigh)

    def reset(event):
        for slider in state.sliders_i + state.sliders_f:
            slider.reset()
        update(None)

    sliders_i, sliders_f = set_controls(subplots_bottom, update, reset)
    state.sliders_i = sliders_i
    state.sliders_f = sliders_f
    state.last_valid_i = slider_values(sliders_i)
    state.last_valid_f = slider_values(sliders_f)
    plt.show()


if __name__ == '__main__':
    main()
