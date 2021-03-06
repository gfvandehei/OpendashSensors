from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from numpy import interp
import numpy as np

class _Tach(QtWidgets.QWidget):
    
    def __init__(self, title: str, start_angle=0, end_angle=270, max_val=256,
                 color: QtGui.QColor=Qt.green, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_angle = start_angle
        self.potential_span = end_angle
        self.max_value = max_val
        self.color = Qt.green
        self.title = title
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

        self.value = 0

    def sizeHint(self):
        return QtCore.QSize(600, 600)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self.color, 10, Qt.SolidLine))
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawArc(0, 0, self.geometry().width()-40, self.geometry().height()-40, self.start_angle,  self.value*-16)
        painter.drawText(e.rect(), Qt.AlignCenter, self.title+"\n"+str(self.value))
        painter.end()

    def _trigger_refresh(self, value: int):
        self.value = value % 256
        self.value = np.floor(np.interp(value, [0, self.max_value], [self.start_angle, self.potential_span]))
        print(value, self.max_value, self.start_angle)
        self.update()


class Tacheometer(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, title: str, start_angle=0, end_angle=270, max_val=256,
                 color: QtGui.QColor=Qt.green, *args, **kwargs):
        super(Tacheometer, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout()
        self._tach = _Tach(title, start_angle, end_angle, max_val, color)
        layout.addWidget(self._tach)

        self.setLayout(layout)