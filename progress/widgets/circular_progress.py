from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Custom properties
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0xf29200
        self.max_value = 100
        # Text
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 15
        self.suffix = "%"
        self.text_color = 0xe75113
        # BG
        self.enable_bg = True
        self.bg_color = 0x44475a

        # Set default size without layout
        self.resize(self.width, self.height)

    # Add dropshadow
    def add_shadow(self, enable):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

    # Set value
    def set_value(self, value):
        self.value = value
        self.repaint()  # Render progress bar after change value

    # Paint event
    def paintEvent(self, event):
        # Set progress parameters
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value

        # Painter
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))

        # Create Rectangel
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        # Pen
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        # Set round cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        # Enable BG
        if self.enable_bg:
            pen.setColor(QColor(self.bg_color))
            paint.setPen(pen)
            paint.drawArc(margin, margin, width, height, 0, 360 * 16)

        # Create arc / circular progress
        pen.setColor(QColor(self.progress_color))
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 * 16, -value * 16)

        # Create text
        if self.enable_text:
            pen.setColor(QColor(self.text_color))
            paint.setPen(pen)
            paint.drawText(rect, Qt.AlignCenter, f"{self.value}{self.suffix}")

        # End
        paint.end()

