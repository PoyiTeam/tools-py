import numpy as np
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QSplineSeries, QScatterSeries
from PySide6.QtCore import QPointF, Slot, Qt, Signal, QPoint
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget,
                               QGraphicsView, QGraphicsScene, QSizePolicy, QRubberBand,
                               QVBoxLayout, QFormLayout, QHBoxLayout, QSizePolicy, QPushButton)
from PySide6.QtGui import QPen, QColor, QPalette, QBrush, QWheelEvent, qRgb, QMouseEvent, QPainter


class ChartView(QChartView):
    # vertical_line_x = None
    # _vertical_line_pen = QPen(QColor('red'))
    # _vertical_line_pen.setWidth(2)
    vertical_line_x = None
    # @property
    # def vertical_line_x(self):
    #     return self._vertical_line_x

    # @vertical_line_x.setter
    # def vertical_line_x(self, vertical_line_x):
    #     self._vertical_line_x = vertical_line_x
    #     self.update()

    def drawForeground(self, painter, rect):
        if self.vertical_line_x is None:
            return
        # painter.save()
        # painter.setPen(self._vertical_line_pen)

        pos = self.chart().mapToPosition(QPointF(self.vertical_line_x, 0))
        plot_area = self.chart().plotArea()

        pos_1 = QPointF(pos.x(), plot_area.top())
        pos_2 = QPointF(pos.x(), plot_area.bottom())
        painter.drawLine(pos_1, pos_2)

        # painter.restore()


class LineChart(QWidget):
    mouse_moved = Signal(QPoint)

    def __init__(self):
        super().__init__()
        self.chart = QChart()
        self.series = QLineSeries()
        self.PushButton = QPushButton()

        self.chart.addSeries(self.series)
        self.axis_x = QValueAxis()
        self.axis_x.setRange(0, 100)
        self.axis_x.setGridLineVisible(False)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(-1, 1)
        self.axis_y.setGridLineVisible(True)

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)
        self.chart.legend().hide()

        self.chart.setBackgroundRoundness(0)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)
        self.chart_view = ChartView()
        self.chart_view.setChart(self.chart)
        self.line_x = np.linspace(0, 100, 512)
        self.line_y = np.zeros(512)
        self.buffer = [QPointF(x, y) for x, y in zip(self.line_x, self.line_y)]
        self.series.append(self.buffer)
        self.set_dark_theme()

    def mouseMoveEvent(self, event) -> None:
        self.mouse_moved.emit(event.pos())
        print(event.x(), event.y())
        # return QChartView.mouseMoveEvent(self, event)
        # return QChartView.mouseMoveEvent(self, event)

    def set_y(self, y_line):
        if len(self.buffer) != y_line.shape[0]:
            raise BaseException('Length of buffer and y-line is not match!')
        for i in range(y_line.shape[0]):
            self.buffer[i].setY(y_line[i])
        self.series.replace(self.buffer)

    def set_dark_theme(self):
        self.pen = QPen()
        self.pen.setWidth(1)
        self.pen.setColor(QColor(Qt.cyan))
        self.series.setPen(self.pen)

        self.chart.setBackgroundBrush(QBrush(QColor(qRgb(35, 35, 45))))
        self.axis_x.setTitleBrush(QBrush(QColor(Qt.white)))
        self.axis_y.setTitleBrush(QBrush(QColor(Qt.white)))
        self.axis_x.setLabelsBrush(QBrush(QColor(Qt.white)))
        self.axis_y.setLabelsBrush(QBrush(QColor(Qt.white)))


class WaveChart(LineChart):
    def __init__(self):
        super(WaveChart, self).__init__()

        self.axis_x.setRange(0, 100)
        self.axis_x.setLabelFormat('%d')
        self.axis_x.setLabelsEditable(True)
        self.axis_x.setTitleText("time (ms)")
        # self.axis_x.setTitleVisible(False)
        self.axis_x.setGridLineVisible(False)

        self.axis_y.setRange(-0.1, 0.1)
        self.axis_y.setLabelFormat('%.2f')
        self.axis_y.setLabelsEditable(True)
        self.axis_y.setTitleText("value")
        # self.axis_y.setTitleVisible(False)
        self.axis_y.setGridLineVisible(True)

        self.line_x = np.linspace(0, 100, 512)
        self.line_y = np.zeros(512)
        self.buffer = [QPointF(x, y) for x, y in zip(self.line_x, self.line_y)]
        self.series.append(self.buffer)

        # self.mouse_moved = Signal(QPoint)
        # self.mouse_moved.connect(self.mouseMoveEvent)

    def reset_axis(self, end_point, buffer_len):
        self.axis_x.setRange(0, end_point)
        self.line_x = np.linspace(0, end_point, buffer_len)
        self.line_y = np.zeros(buffer_len)
        self.buffer = [QPointF(x, y) for x, y in zip(self.line_x, self.line_y)]
        self.series.replace(self.buffer)

    def set_y_range(self, low_limit: float, high_limit: float):
        self.axis_y.setRange(low_limit, high_limit)

    def set_y_label(self, label: str):
        self.axis_y.setTitleText(label)


class SpectrumChart(LineChart):
    def __init__(self):
        super(SpectrumChart, self).__init__()

        self.axis_x.setRange(0, 1600)
        self.axis_x.setLabelFormat('%d')
        self.axis_x.setLabelsEditable(True)
        self.axis_x.setTitleText("Hz")
        self.axis_x.setGridLineVisible(False)
        self.axis_x.setTickCount(11)

        self.axis_y.setRange(0, 1)
        self.axis_y.setLabelFormat('%.2f')
        self.axis_y.setLabelsEditable(True)
        self.axis_y.setTitleText("power (norm 0~1)")

        self.line_x = np.linspace(0, 1600, 512)
        self.line_y = np.zeros(512)

        self.buffer = [QPointF(x, y) for x, y in zip(self.line_x, self.line_y)]
        self.series.append(self.buffer)

        # self.mouse_moved = Signal(QPoint)
        # self.mouse_moved.connect(self.mouseMoveEvent)

    def reset_axis(self, end_point, buffer_len):
        self.axis_x.setRange(0, end_point)
        self.axis_y.setRange(0, 1)
        self.line_x = np.linspace(0, end_point, buffer_len)
        self.line_y = np.zeros(buffer_len)
        self.buffer = [QPointF(x, y) for x, y in zip(self.line_x, self.line_y)]
        self.series.replace(self.buffer)

    def set_x_range(self, low_limit: float, high_limit: float):
        self.axis_x.setRange(low_limit, high_limit)

    def mark_max_x(self):
        ...


if __name__ == "__main__":
    app = QApplication()
    layout = QHBoxLayout()

    wave_chart_1 = WaveChart()
    wave_chart_2 = SpectrumChart()

    layout.addWidget(wave_chart_1.chart_view, 3)
    layout.addWidget(wave_chart_2.chart_view, 2)
    layout.setSpacing(0)
    window = QWidget()

    window.setLayout(layout)
    window.layout().setContentsMargins(0, 0, 0, 0)
    window.setFixedSize(640, 360)
    window.show()

    app.exec()
