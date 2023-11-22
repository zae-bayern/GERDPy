from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(300, 300)
        SplashScreen.setMinimumSize(QSize(300, 300))
        SplashScreen.setMaximumSize(QSize(300, 300))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(40, 44, 52);\n"
"	color:  #ffffff;\n"
"	border-radius: 120px;\n"
"	font: \"Segoe UI\";\n"
"}")
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 180))
        self.texts.setStyleSheet(u"background: none;")
        self.texts.setFrameShape(QFrame.StyledPanel)
        self.texts.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.texts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title = QLabel(self.texts)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.empty = QFrame(self.texts)
        self.empty.setObjectName(u"empty")
        self.empty.setMinimumSize(QSize(0, 80))
        self.empty.setFrameShape(QFrame.NoFrame)
        self.empty.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.empty, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.texts)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.frame_3)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(80, 24))
        self.version.setMaximumSize(QSize(100, 24))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.version.setFont(font1)
        self.version.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(231, 81, 19, 50);\n"
"	color: rgb(231, 81, 19);\n"
"	border-radius: 12px;\n"
"}")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.version, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.running = QLabel(self.texts)
        self.running.setObjectName(u"running")
        self.running.setFont(font1)
        self.running.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.running, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.texts)


        self.verticalLayout_2.addWidget(self.circle_bg)


        self.verticalLayout.addWidget(self.container)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Running...", None))
        self.title.setText(QCoreApplication.translate("SplashScreen", u"GERDPy", None))
        self.version.setText(QCoreApplication.translate("SplashScreen", u"v2.0.0", None))
        self.running.setText(QCoreApplication.translate("SplashScreen", u"Initialization...", None))
    # retranslateUi

