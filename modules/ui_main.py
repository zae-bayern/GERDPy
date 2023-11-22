# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainukqzEJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1267, 670)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"	font: 11pt;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
""
                        "	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/ZAE-Logo_mini.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	backgroun"
                        "d-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	backgro"
                        "und-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraConte"
                        "nt{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, "
                        "57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
""
                        "	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	ba"
                        "ckground-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-b"
                        "ackground-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margi"
                        "n;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom"
                        ";\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72"
                        ");	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgba(249, 178, 0, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: p"
                        "adding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"SpinBox */\n"
"QSpinBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: cent"
                        "er right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: center right;\n"
"	margin-right: 28px;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(255, 211, 0);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////"
                        "////////////////////////////////////////////////////////////////////////////////////////\n"
"DoubleSpinBox */\n"
"QDoubleSpinBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: center right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QDoubleSpinBox::down-button {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: center right;\n"
"	margin-right: 28px;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, "
                        "150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QDoubleSpinBox QAbstractItemView {\n"
"	color: rgb(255, 211, 0);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizonta"
                        "l:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 2"
                        "55);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ToolTips */\n"
"Qt::WA_AlwaysShowToolTips\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setGeometry(QRect(0, 3, 60, 45))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 48, 215, 341))
        self.topMenu.setMinimumSize(QSize(0, 0))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.topMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_7.addWidget(self.btn_home)

        self.btn_weather = QPushButton(self.topMenu)
        self.btn_weather.setObjectName(u"btn_weather")
        sizePolicy.setHeightForWidth(self.btn_weather.sizePolicy().hasHeightForWidth())
        self.btn_weather.setSizePolicy(sizePolicy)
        self.btn_weather.setMinimumSize(QSize(0, 45))
        self.btn_weather.setFont(font)
        self.btn_weather.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_weather.setLayoutDirection(Qt.LeftToRight)
        self.btn_weather.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cloudy.png);")

        self.verticalLayout_7.addWidget(self.btn_weather)

        self.btn_heat = QPushButton(self.topMenu)
        self.btn_heat.setObjectName(u"btn_heat")
        sizePolicy.setHeightForWidth(self.btn_heat.sizePolicy().hasHeightForWidth())
        self.btn_heat.setSizePolicy(sizePolicy)
        self.btn_heat.setMinimumSize(QSize(0, 45))
        self.btn_heat.setFont(font)
        self.btn_heat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_heat.setLayoutDirection(Qt.LeftToRight)
        self.btn_heat.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-module.png);")

        self.verticalLayout_7.addWidget(self.btn_heat)

        self.btn_borefield = QPushButton(self.topMenu)
        self.btn_borefield.setObjectName(u"btn_borefield")
        sizePolicy.setHeightForWidth(self.btn_borefield.sizePolicy().hasHeightForWidth())
        self.btn_borefield.setSizePolicy(sizePolicy)
        self.btn_borefield.setMinimumSize(QSize(0, 45))
        self.btn_borefield.setFont(font)
        self.btn_borefield.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_borefield.setLayoutDirection(Qt.LeftToRight)
        self.btn_borefield.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-circle.png);")

        self.verticalLayout_7.addWidget(self.btn_borefield)

        self.btn_surface = QPushButton(self.topMenu)
        self.btn_surface.setObjectName(u"btn_surface")
        sizePolicy.setHeightForWidth(self.btn_surface.sizePolicy().hasHeightForWidth())
        self.btn_surface.setSizePolicy(sizePolicy)
        self.btn_surface.setMinimumSize(QSize(0, 45))
        self.btn_surface.setFont(font)
        self.btn_surface.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_surface.setLayoutDirection(Qt.LeftToRight)
        self.btn_surface.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_7.addWidget(self.btn_surface)

        self.btn_sim = QPushButton(self.topMenu)
        self.btn_sim.setObjectName(u"btn_sim")
        sizePolicy.setHeightForWidth(self.btn_sim.sizePolicy().hasHeightForWidth())
        self.btn_sim.setSizePolicy(sizePolicy)
        self.btn_sim.setMinimumSize(QSize(0, 45))
        self.btn_sim.setFont(font)
        self.btn_sim.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sim.setLayoutDirection(Qt.LeftToRight)
        self.btn_sim.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-media-play.png);")

        self.verticalLayout_7.addWidget(self.btn_sim)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setGeometry(QRect(0, 447, 60, 151))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background: transparent;")
        self.verticalLayout_10 = QVBoxLayout(self.home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 80))
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background: none;\n"
"color: rgb(231, 81, 19);")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.label_2)

        self.widget = QWidget(self.home)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"image: url(:/images/images/images/title.png);\n"
"")

        self.verticalLayout_10.addWidget(self.widget)

        self.stackedWidget.addWidget(self.home)
        self.weather_local = QWidget()
        self.weather_local.setObjectName(u"weather_local")
        self.gridLayout_11 = QGridLayout(self.weather_local)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame = QFrame(self.weather_local)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: #e75113;")

        self.verticalLayout_11.addWidget(self.label_3)


        self.gridLayout_11.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.weather_local)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.line_weather_file = QLineEdit(self.frame_2)
        self.line_weather_file.setObjectName(u"line_weather_file")
        self.line_weather_file.setMinimumSize(QSize(0, 35))
        self.line_weather_file.setFont(font1)
        self.line_weather_file.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.line_weather_file, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color: #f9b200;")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.btn_browse_weather = QPushButton(self.frame_2)
        self.btn_browse_weather.setObjectName(u"btn_browse_weather")
        self.btn_browse_weather.setMinimumSize(QSize(150, 35))
        self.btn_browse_weather.setFont(font1)
        self.btn_browse_weather.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse_weather.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse_weather.setIcon(icon3)

        self.gridLayout_3.addWidget(self.btn_browse_weather, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(False)
        self.label_6.setFont(font7)
        self.label_6.setToolTipDuration(30000)

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.weather_local)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_3 = QFrame(self.frame_25)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, -1, -1, -1)
        self.frame_26 = QFrame(self.frame_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 50))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_26)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_26)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: #f9b200;")

        self.verticalLayout_5.addWidget(self.label_8)


        self.verticalLayout_29.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_28)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.label_9 = QLabel(self.frame_28)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)
        self.label_9.setToolTipDuration(30000)

        self.gridLayout_12.addWidget(self.label_9, 0, 0, 1, 1)

        self.sb_therm_diffu = QDoubleSpinBox(self.frame_28)
        self.sb_therm_diffu.setObjectName(u"sb_therm_diffu")
        self.sb_therm_diffu.setFont(font1)
        self.sb_therm_diffu.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_therm_diffu.setDecimals(1)
        self.sb_therm_diffu.setSingleStep(0.100000000000000)
        self.sb_therm_diffu.setValue(1.000000000000000)

        self.gridLayout_12.addWidget(self.sb_therm_diffu, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame_28)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)
        self.label_10.setToolTipDuration(30000)

        self.gridLayout_12.addWidget(self.label_10, 1, 0, 1, 1)

        self.sb_therm_cond = QDoubleSpinBox(self.frame_28)
        self.sb_therm_cond.setObjectName(u"sb_therm_cond")
        self.sb_therm_cond.setFont(font1)
        self.sb_therm_cond.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_therm_cond.setDecimals(1)
        self.sb_therm_cond.setValue(2.000000000000000)

        self.gridLayout_12.addWidget(self.sb_therm_cond, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_28)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)
        self.label_11.setToolTipDuration(30000)

        self.gridLayout_12.addWidget(self.label_11, 2, 0, 1, 1)

        self.sb_undis_soil_temp = QDoubleSpinBox(self.frame_28)
        self.sb_undis_soil_temp.setObjectName(u"sb_undis_soil_temp")
        self.sb_undis_soil_temp.setFont(font1)
        self.sb_undis_soil_temp.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_undis_soil_temp.setDecimals(1)
        self.sb_undis_soil_temp.setMinimum(-50.000000000000000)
        self.sb_undis_soil_temp.setMaximum(50.000000000000000)
        self.sb_undis_soil_temp.setSingleStep(1.000000000000000)
        self.sb_undis_soil_temp.setValue(10.000000000000000)

        self.gridLayout_12.addWidget(self.sb_undis_soil_temp, 2, 1, 1, 1)

        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font7)
        self.label_35.setToolTipDuration(30000)

        self.gridLayout_12.addWidget(self.label_35, 3, 0, 1, 1)

        self.sb_h_NHN = QSpinBox(self.frame_28)
        self.sb_h_NHN.setObjectName(u"sb_h_NHN")
        self.sb_h_NHN.setMinimumSize(QSize(0, 0))
        self.sb_h_NHN.setMaximumSize(QSize(16777215, 16777215))
        self.sb_h_NHN.setFont(font1)
        self.sb_h_NHN.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_h_NHN.setMinimum(0)
        self.sb_h_NHN.setMaximum(9000)
        self.sb_h_NHN.setSingleStep(10)
        self.sb_h_NHN.setValue(520)

        self.gridLayout_12.addWidget(self.sb_h_NHN, 3, 1, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_28)


        self.horizontalLayout_8.addWidget(self.frame_3)


        self.gridLayout_11.addWidget(self.frame_25, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.weather_local)
        self.heating_element = QWidget()
        self.heating_element.setObjectName(u"heating_element")
        self.verticalLayout_57 = QVBoxLayout(self.heating_element)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.frame_71 = QFrame(self.heating_element)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMaximumSize(QSize(16777215, 60))
        self.frame_71.setStyleSheet(u"background: transparent;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_71)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_83 = QLabel(self.frame_71)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font5)
        self.label_83.setStyleSheet(u"color: #e75113;background: transparent;")

        self.verticalLayout_56.addWidget(self.label_83)


        self.verticalLayout_57.addWidget(self.frame_71)

        self.frame_67 = QFrame(self.heating_element)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_67)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_68)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(15)
        self.gridLayout_28.setVerticalSpacing(0)
        self.gridLayout_28.setContentsMargins(9, 0, 9, 0)
        self.label_73 = QLabel(self.frame_68)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font7)
        self.label_73.setToolTipDuration(30000)

        self.gridLayout_28.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_77 = QLabel(self.frame_68)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(400, 0))
        self.label_77.setMaximumSize(QSize(16777215, 16777215))
        self.label_77.setFont(font7)
        self.label_77.setToolTipDuration(30000)

        self.gridLayout_28.addWidget(self.label_77, 6, 0, 1, 1)

        self.sb_l_An = QSpinBox(self.frame_68)
        self.sb_l_An.setObjectName(u"sb_l_An")
        self.sb_l_An.setMinimumSize(QSize(130, 0))
        self.sb_l_An.setMaximumSize(QSize(16777215, 16777215))
        self.sb_l_An.setFont(font1)
        self.sb_l_An.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_l_An.setMinimum(1)
        self.sb_l_An.setMaximum(1000)
        self.sb_l_An.setValue(5)

        self.gridLayout_28.addWidget(self.sb_l_An, 0, 1, 1, 1)

        self.sb_x_min = QDoubleSpinBox(self.frame_68)
        self.sb_x_min.setObjectName(u"sb_x_min")
        self.sb_x_min.setFont(font1)
        self.sb_x_min.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_x_min.setDecimals(3)
        self.sb_x_min.setMaximum(5.000000000000000)
        self.sb_x_min.setValue(0.025000000000000)

        self.gridLayout_28.addWidget(self.sb_x_min, 7, 1, 1, 1)

        self.label_78 = QLabel(self.frame_68)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font7)
        self.label_78.setToolTipDuration(30000)

        self.gridLayout_28.addWidget(self.label_78, 7, 0, 1, 1)

        self.sb_lambda_Bet = QDoubleSpinBox(self.frame_68)
        self.sb_lambda_Bet.setObjectName(u"sb_lambda_Bet")
        self.sb_lambda_Bet.setFont(font1)
        self.sb_lambda_Bet.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_lambda_Bet.setDecimals(2)
        self.sb_lambda_Bet.setMaximum(10.000000000000000)
        self.sb_lambda_Bet.setSingleStep(0.050000000000000)
        self.sb_lambda_Bet.setValue(2.100000000000000)

        self.gridLayout_28.addWidget(self.sb_lambda_Bet, 2, 1, 1, 1)

        self.label_75 = QLabel(self.frame_68)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font7)
        self.label_75.setToolTipDuration(30000)

        self.gridLayout_28.addWidget(self.label_75, 2, 0, 1, 1)

        self.label_76 = QLabel(self.frame_68)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font7)

        self.gridLayout_28.addWidget(self.label_76, 4, 0, 1, 1)

        self.label_74 = QLabel(self.frame_68)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font7)
        self.label_74.setToolTipDuration(30000)

        self.gridLayout_28.addWidget(self.label_74, 5, 0, 1, 1)

        self.sb_s_R = QDoubleSpinBox(self.frame_68)
        self.sb_s_R.setObjectName(u"sb_s_R")
        self.sb_s_R.setMinimumSize(QSize(130, 0))
        self.sb_s_R.setMaximumSize(QSize(16777215, 16777215))
        self.sb_s_R.setFont(font1)
        self.sb_s_R.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_s_R.setDecimals(3)
        self.sb_s_R.setMaximum(10.000000000000000)
        self.sb_s_R.setSingleStep(0.001000000000000)
        self.sb_s_R.setValue(0.050000000000000)

        self.gridLayout_28.addWidget(self.sb_s_R, 4, 1, 1, 1)

        self.sb_l_R = QSpinBox(self.frame_68)
        self.sb_l_R.setObjectName(u"sb_l_R")
        self.sb_l_R.setFont(font1)
        self.sb_l_R.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_l_R.setMaximum(5000)
        self.sb_l_R.setValue(1000)
        self.sb_l_R.setDisplayIntegerBase(10)

        self.gridLayout_28.addWidget(self.sb_l_R, 5, 1, 1, 1)

        self.sb_A_he = QSpinBox(self.frame_68)
        self.sb_A_he.setObjectName(u"sb_A_he")
        self.sb_A_he.setFont(font1)
        self.sb_A_he.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_A_he.setMaximum(10000)
        self.sb_A_he.setValue(35)

        self.gridLayout_28.addWidget(self.sb_A_he, 6, 1, 1, 1)


        self.gridLayout_27.addWidget(self.frame_68, 0, 0, 2, 1)

        self.frame_69 = QFrame(self.frame_67)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(2, 0))
        self.frame_69.setMaximumSize(QSize(2, 16777215))
        self.frame_69.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.gridLayout_27.addWidget(self.frame_69, 0, 1, 2, 1)

        self.frame_70 = QFrame(self.frame_67)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_70)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_81 = QLabel(self.frame_70)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font7)
        self.label_81.setToolTipDuration(30000)

        self.gridLayout_29.addWidget(self.label_81, 3, 0, 1, 1)

        self.sb_D_he = QDoubleSpinBox(self.frame_70)
        self.sb_D_he.setObjectName(u"sb_D_he")
        self.sb_D_he.setFont(font1)
        self.sb_D_he.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_D_he.setDecimals(2)
        self.sb_D_he.setMaximum(1.000000000000000)
        self.sb_D_he.setSingleStep(0.001000000000000)
        self.sb_D_he.setValue(0.250000000000000)

        self.gridLayout_29.addWidget(self.sb_D_he, 2, 1, 1, 1)

        self.label_79 = QLabel(self.frame_70)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font7)
        self.label_79.setToolTipDuration(30000)

        self.gridLayout_29.addWidget(self.label_79, 4, 0, 1, 1)

        self.sb_D_iso_he = QDoubleSpinBox(self.frame_70)
        self.sb_D_iso_he.setObjectName(u"sb_D_iso_he")
        self.sb_D_iso_he.setFont(font1)
        self.sb_D_iso_he.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_D_iso_he.setDecimals(2)
        self.sb_D_iso_he.setMaximum(1.000000000000000)
        self.sb_D_iso_he.setSingleStep(0.001000000000000)
        self.sb_D_iso_he.setValue(0.030000000000000)

        self.gridLayout_29.addWidget(self.sb_D_iso_he, 4, 1, 1, 1)

        self.label_82 = QLabel(self.frame_70)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(290, 0))
        self.label_82.setMaximumSize(QSize(16777215, 16777215))
        self.label_82.setFont(font7)
        self.label_82.setToolTipDuration(30000)

        self.gridLayout_29.addWidget(self.label_82, 2, 0, 1, 1)

        self.sb_D_iso_an = QDoubleSpinBox(self.frame_70)
        self.sb_D_iso_an.setObjectName(u"sb_D_iso_an")
        self.sb_D_iso_an.setFont(font1)
        self.sb_D_iso_an.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_D_iso_an.setDecimals(3)
        self.sb_D_iso_an.setMaximum(1.000000000000000)
        self.sb_D_iso_an.setSingleStep(0.001000000000000)
        self.sb_D_iso_an.setValue(0.005000000000000)

        self.gridLayout_29.addWidget(self.sb_D_iso_an, 3, 1, 1, 1)


        self.gridLayout_27.addWidget(self.frame_70, 1, 2, 1, 1)

        self.widget_borehole_3 = QWidget(self.frame_67)
        self.widget_borehole_3.setObjectName(u"widget_borehole_3")
        self.widget_borehole_3.setStyleSheet(u"image: url(:/images/images/images/heating_element.png); \n"
"background-color: rgb(255, 255, 255);\n"
"/*background-color: rgba(221, 221, 221, 200);*/\n"
"border-radius: 5px;")

        self.gridLayout_27.addWidget(self.widget_borehole_3, 0, 2, 1, 1)


        self.verticalLayout_57.addWidget(self.frame_67)

        self.stackedWidget.addWidget(self.heating_element)
        self.boreholes = QWidget()
        self.boreholes.setObjectName(u"boreholes")
        self.verticalLayout_22 = QVBoxLayout(self.boreholes)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_30 = QFrame(self.boreholes)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 60))
        self.frame_30.setStyleSheet(u"background: transparent;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_30)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_30)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"color: #e75113;background: transparent;")

        self.verticalLayout_12.addWidget(self.label_14)


        self.verticalLayout_22.addWidget(self.frame_30)

        self.frame_6 = QFrame(self.boreholes)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(15)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(9, 0, 9, 0)
        self.label_30 = QLabel(self.frame_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font7)
        self.label_30.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_30, 1, 0, 1, 1)

        self.sb_lambda_b = QDoubleSpinBox(self.frame_7)
        self.sb_lambda_b.setObjectName(u"sb_lambda_b")
        self.sb_lambda_b.setFont(font1)
        self.sb_lambda_b.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_lambda_b.setDecimals(1)
        self.sb_lambda_b.setSingleStep(0.100000000000000)
        self.sb_lambda_b.setValue(2.000000000000000)

        self.gridLayout_7.addWidget(self.sb_lambda_b, 6, 1, 1, 1)

        self.sb_r_borehole = QDoubleSpinBox(self.frame_7)
        self.sb_r_borehole.setObjectName(u"sb_r_borehole")
        self.sb_r_borehole.setFont(font1)
        self.sb_r_borehole.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_r_borehole.setDecimals(2)
        self.sb_r_borehole.setMaximum(2.000000000000000)
        self.sb_r_borehole.setSingleStep(0.050000000000000)
        self.sb_r_borehole.setValue(0.150000000000000)

        self.gridLayout_7.addWidget(self.sb_r_borehole, 3, 1, 1, 1)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)
        self.label_16.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_16, 6, 0, 1, 1)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)
        self.label_25.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)
        self.label_15.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(400, 0))
        self.label_17.setMaximumSize(QSize(16777215, 16777215))
        self.label_17.setFont(font7)
        self.label_17.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_17, 7, 0, 1, 1)

        self.sb_lambda_iso = QDoubleSpinBox(self.frame_7)
        self.sb_lambda_iso.setObjectName(u"sb_lambda_iso")
        self.sb_lambda_iso.setFont(font1)
        self.sb_lambda_iso.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_lambda_iso.setDecimals(1)
        self.sb_lambda_iso.setSingleStep(0.100000000000000)
        self.sb_lambda_iso.setValue(0.300000000000000)

        self.gridLayout_7.addWidget(self.sb_lambda_iso, 7, 1, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font7)
        self.label_18.setToolTipDuration(30000)

        self.gridLayout_7.addWidget(self.label_18, 8, 0, 1, 1)

        self.sb_lambda_p = QDoubleSpinBox(self.frame_7)
        self.sb_lambda_p.setObjectName(u"sb_lambda_p")
        self.sb_lambda_p.setFont(font1)
        self.sb_lambda_p.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_lambda_p.setDecimals(1)
        self.sb_lambda_p.setValue(14.000000000000000)

        self.gridLayout_7.addWidget(self.sb_lambda_p, 8, 1, 1, 1)

        self.sb_number_heatpipes = QSpinBox(self.frame_7)
        self.sb_number_heatpipes.setObjectName(u"sb_number_heatpipes")
        self.sb_number_heatpipes.setMinimumSize(QSize(130, 0))
        self.sb_number_heatpipes.setMaximumSize(QSize(16777215, 16777215))
        self.sb_number_heatpipes.setFont(font1)
        self.sb_number_heatpipes.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_number_heatpipes.setMinimum(1)
        self.sb_number_heatpipes.setMaximum(1000)
        self.sb_number_heatpipes.setValue(6)

        self.gridLayout_7.addWidget(self.sb_number_heatpipes, 5, 1, 1, 1)

        self.sb_depth_boreholes = QSpinBox(self.frame_7)
        self.sb_depth_boreholes.setObjectName(u"sb_depth_boreholes")
        self.sb_depth_boreholes.setMinimumSize(QSize(130, 0))
        self.sb_depth_boreholes.setMaximumSize(QSize(16777215, 16777215))
        self.sb_depth_boreholes.setFont(font1)
#if QT_CONFIG(tooltip)
        self.sb_depth_boreholes.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.sb_depth_boreholes.setToolTipDuration(-1)
        self.sb_depth_boreholes.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_depth_boreholes.setMinimum(1)
        self.sb_depth_boreholes.setMaximum(1000)
        self.sb_depth_boreholes.setValue(50)

        self.gridLayout_7.addWidget(self.sb_depth_boreholes, 1, 1, 1, 1)

        self.rb_depth = QRadioButton(self.frame_7)
        self.rb_depth.setObjectName(u"rb_depth")
        self.rb_depth.setFont(font7)
        self.rb_depth.setToolTipDuration(30000)
        self.rb_depth.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.rb_depth, 0, 0, 1, 2)


        self.gridLayout_8.addWidget(self.frame_7, 0, 0, 2, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(2, 0))
        self.frame_9.setMaximumSize(QSize(2, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_9, 0, 1, 2, 1)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)
        self.label_22.setToolTipDuration(30000)

        self.gridLayout_6.addWidget(self.label_22, 5, 0, 1, 1)

        self.sb_radius_w = QDoubleSpinBox(self.frame_8)
        self.sb_radius_w.setObjectName(u"sb_radius_w")
        self.sb_radius_w.setMinimumSize(QSize(150, 0))
        self.sb_radius_w.setFont(font1)
        self.sb_radius_w.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_radius_w.setDecimals(2)
        self.sb_radius_w.setMaximum(10.000000000000000)
        self.sb_radius_w.setSingleStep(0.010000000000000)
        self.sb_radius_w.setValue(0.120000000000000)

        self.gridLayout_6.addWidget(self.sb_radius_w, 1, 1, 1, 1)

        self.sb_radius_pi = QDoubleSpinBox(self.frame_8)
        self.sb_radius_pi.setObjectName(u"sb_radius_pi")
        self.sb_radius_pi.setFont(font1)
        self.sb_radius_pi.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_radius_pi.setDecimals(3)
        self.sb_radius_pi.setMaximum(1.000000000000000)
        self.sb_radius_pi.setSingleStep(0.001000000000000)
        self.sb_radius_pi.setValue(0.015000000000000)

        self.gridLayout_6.addWidget(self.sb_radius_pi, 5, 1, 1, 1)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font7)
        self.label_20.setToolTipDuration(30000)

        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font7)
        self.label_21.setToolTipDuration(30000)

        self.gridLayout_6.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(290, 0))
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setFont(font7)
        self.label_19.setToolTipDuration(30000)

        self.gridLayout_6.addWidget(self.label_19, 3, 0, 1, 1)

        self.sb_radius_pa = QDoubleSpinBox(self.frame_8)
        self.sb_radius_pa.setObjectName(u"sb_radius_pa")
        self.sb_radius_pa.setFont(font1)
        self.sb_radius_pa.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_radius_pa.setDecimals(3)
        self.sb_radius_pa.setMaximum(1.000000000000000)
        self.sb_radius_pa.setSingleStep(0.001000000000000)
        self.sb_radius_pa.setValue(0.016000000000000)

        self.gridLayout_6.addWidget(self.sb_radius_pa, 4, 1, 1, 1)

        self.sb_radius_iso = QDoubleSpinBox(self.frame_8)
        self.sb_radius_iso.setObjectName(u"sb_radius_iso")
        self.sb_radius_iso.setFont(font1)
        self.sb_radius_iso.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_radius_iso.setDecimals(3)
        self.sb_radius_iso.setMaximum(1.000000000000000)
        self.sb_radius_iso.setSingleStep(0.001000000000000)
        self.sb_radius_iso.setValue(0.016000000000000)

        self.gridLayout_6.addWidget(self.sb_radius_iso, 3, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_8, 1, 2, 1, 1)

        self.widget_borehole = QWidget(self.frame_6)
        self.widget_borehole.setObjectName(u"widget_borehole")
        self.widget_borehole.setStyleSheet(u"image: url(:/images/images/images/borehole.png);\n"
"background-color: rgb(255, 255, 255);\n"
"/*background-color: rgba(221, 221, 221, 200);*/\n"
"border-radius: 5px;")

        self.gridLayout_8.addWidget(self.widget_borehole, 0, 2, 1, 1)


        self.verticalLayout_22.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.boreholes)
        self.borefield_sim = QWidget()
        self.borefield_sim.setObjectName(u"borefield_sim")
        self.gridLayout_16 = QGridLayout(self.borefield_sim)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_4 = QFrame(self.borefield_sim)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setItalic(False)
        self.frame_4.setFont(font8)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: #e75113;")

        self.verticalLayout_13.addWidget(self.label)


        self.gridLayout_16.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.borefield_sim)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 160))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font6)
        self.label_12.setStyleSheet(u"color: #f9b200;")

        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)
        self.label_13.setToolTipDuration(30000)

        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)

        self.line_borefield_file = QLineEdit(self.frame_5)
        self.line_borefield_file.setObjectName(u"line_borefield_file")
        self.line_borefield_file.setMinimumSize(QSize(0, 35))
        self.line_borefield_file.setFont(font1)
        self.line_borefield_file.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.line_borefield_file, 2, 0, 1, 1)

        self.btn_browse_borefield = QPushButton(self.frame_5)
        self.btn_browse_borefield.setObjectName(u"btn_browse_borefield")
        self.btn_browse_borefield.setMinimumSize(QSize(150, 35))
        self.btn_browse_borefield.setFont(font1)
        self.btn_browse_borefield.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse_borefield.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_browse_borefield.setIcon(icon3)

        self.gridLayout_5.addWidget(self.btn_browse_borefield, 2, 1, 1, 1)


        self.gridLayout_16.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.borefield_sim)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 50))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"color: #f9b200;")

        self.gridLayout_14.addWidget(self.label_26, 0, 0, 1, 3)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(2, 0))
        self.frame_15.setMaximumSize(QSize(2, 16777215))
        self.frame_15.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.frame_15, 2, 1, 1, 1)

        self.frame_29 = QFrame(self.frame_11)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_29)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.rb_multiyearsim = QRadioButton(self.frame_29)
        self.rb_multiyearsim.setObjectName(u"rb_multiyearsim")
        self.rb_multiyearsim.setFont(font7)
        self.rb_multiyearsim.setToolTipDuration(30000)

        self.verticalLayout_28.addWidget(self.rb_multiyearsim)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_32)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_32)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font7)
        self.label_29.setToolTipDuration(30000)

        self.gridLayout_4.addWidget(self.label_29, 1, 0, 1, 1)

        self.sb_simtime = QSpinBox(self.frame_32)
        self.sb_simtime.setObjectName(u"sb_simtime")
        self.sb_simtime.setFont(font1)
        self.sb_simtime.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_simtime.setMinimum(24)
        self.sb_simtime.setMaximum(8760)
        self.sb_simtime.setValue(730)
        self.sb_simtime.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.sb_simtime, 1, 1, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_32)

        self.frame_35 = QFrame(self.frame_29)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_35)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font7)
        self.label_32.setToolTipDuration(30000)

        self.horizontalLayout_10.addWidget(self.label_32)

        self.sb_rf = QDoubleSpinBox(self.frame_35)
        self.sb_rf.setObjectName(u"sb_rf")
        self.sb_rf.setFont(font1)
        self.sb_rf.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_rf.setDecimals(1)
        self.sb_rf.setMaximum(1.000000000000000)
        self.sb_rf.setSingleStep(0.100000000000000)
        self.sb_rf.setValue(0.200000000000000)

        self.horizontalLayout_10.addWidget(self.sb_rf)


        self.verticalLayout_28.addWidget(self.frame_35)


        self.gridLayout_14.addWidget(self.frame_29, 2, 2, 1, 1)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_16)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(16777215, 60))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_33)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_33)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 50))
        self.label_31.setFont(font6)
        self.label_31.setToolTipDuration(30000)
        self.label_31.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.label_31)


        self.verticalLayout_32.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_16)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_34)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_34)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)

        self.gridLayout_9.addWidget(self.label_27, 0, 0, 1, 1)

        self.cb_month = QComboBox(self.frame_34)
        self.cb_month.setObjectName(u"cb_month")
        self.cb_month.setFont(font1)
        self.cb_month.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_month.setMaxVisibleItems(12)

        self.gridLayout_9.addWidget(self.cb_month, 0, 1, 1, 1)

        self.label_28 = QLabel(self.frame_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)

        self.gridLayout_9.addWidget(self.label_28, 1, 0, 1, 1)

        self.sb_day = QSpinBox(self.frame_34)
        self.sb_day.setObjectName(u"sb_day")
        self.sb_day.setFont(font1)
        self.sb_day.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.sb_day.setMinimum(1)
        self.sb_day.setMaximum(31)

        self.gridLayout_9.addWidget(self.sb_day, 1, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.frame_34)


        self.gridLayout_14.addWidget(self.frame_16, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_11, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.borefield_sim)
        self.simulation = QWidget()
        self.simulation.setObjectName(u"simulation")
        self.verticalLayout_14 = QVBoxLayout(self.simulation)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_17 = QFrame(self.simulation)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(16777215, 60))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_17)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 50))
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"color: #e75113;")

        self.verticalLayout_24.addWidget(self.label_33)


        self.verticalLayout_14.addWidget(self.frame_17)

        self.frame_12 = QFrame(self.simulation)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_12)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_23)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 9, -1, -1)
        self.label_34 = QLabel(self.frame_23)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 0))
        self.label_34.setMaximumSize(QSize(16777215, 16777215))
        self.label_34.setFont(font7)
        self.label_34.setTextFormat(Qt.AutoText)
        self.label_34.setScaledContents(False)
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_26.addWidget(self.label_34)

        self.frame_18 = QFrame(self.frame_23)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(650, 150))
        self.frame_18.setMaximumSize(QSize(16777215, 200))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(100, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_20)

        self.btn_startsim = QPushButton(self.frame_18)
        self.btn_startsim.setObjectName(u"btn_startsim")
        self.btn_startsim.setMinimumSize(QSize(300, 100))
        self.btn_startsim.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setPointSize(16)
        font9.setBold(False)
        font9.setItalic(False)
        self.btn_startsim.setFont(font9)
        self.btn_startsim.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_startsim.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(242, 146, 0, 130);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(228, 38, 24, 130);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_startsim.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.btn_startsim)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(100, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_21)


        self.verticalLayout_26.addWidget(self.frame_18)

        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(650, 150))
        self.frame_27.setMaximumSize(QSize(16777215, 200))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(100, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_31)

        self.btn_save_results = QPushButton(self.frame_27)
        self.btn_save_results.setObjectName(u"btn_save_results")
        self.btn_save_results.setMinimumSize(QSize(300, 100))
        self.btn_save_results.setFont(font9)
        self.btn_save_results.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_results.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(242, 146, 0, 130);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(228, 38, 24, 130);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_results.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.btn_save_results)

        self.frame_36 = QFrame(self.frame_27)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(100, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_36)


        self.verticalLayout_26.addWidget(self.frame_27)


        self.horizontalLayout_6.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.frame_12)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_22)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_10 = QFrame(self.frame_22)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 50))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"color: #f9b200;")

        self.horizontalLayout_14.addWidget(self.label_36)

        self.btn_save_console = QPushButton(self.frame_10)
        self.btn_save_console.setObjectName(u"btn_save_console")
        self.btn_save_console.setMinimumSize(QSize(200, 35))
        self.btn_save_console.setMaximumSize(QSize(200, 16777215))
        self.btn_save_console.setFont(font9)
        self.btn_save_console.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_console.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(242, 146, 0, 130);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(228, 38, 24, 130);\n"
"}")
        self.btn_save_console.setIcon(icon5)

        self.horizontalLayout_14.addWidget(self.btn_save_console)


        self.verticalLayout_8.addWidget(self.frame_10)

        self.text_console = QPlainTextEdit(self.frame_22)
        self.text_console.setObjectName(u"text_console")
        self.text_console.setMinimumSize(QSize(200, 200))
        self.text_console.setFont(font1)
        self.text_console.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.text_console.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.text_console)


        self.horizontalLayout_6.addWidget(self.frame_22)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.simulation)
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.verticalLayout_27 = QVBoxLayout(self.results)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_24 = QFrame(self.results)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 60))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_24)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_24)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: #e75113;")

        self.verticalLayout_15.addWidget(self.label_5)


        self.verticalLayout_27.addWidget(self.frame_24)

        self.frame_19 = QFrame(self.results)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.results)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon6)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font10 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font10);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_23.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font11 = QFont()
        font11.setBold(False)
        font11.setItalic(False)
        self.creditsLabel.setFont(font11)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.cb_month.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"GerdPy", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Simulation Tool", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_weather.setText(QCoreApplication.translate("MainWindow", u"Weather parameters\n"
"Local parameters", None))
        self.btn_heat.setText(QCoreApplication.translate("MainWindow", u"Heating elements", None))
        self.btn_borefield.setText(QCoreApplication.translate("MainWindow", u"Borehole parameters", None))
        self.btn_surface.setText(QCoreApplication.translate("MainWindow", u"Borehole geometry\n"
"Simulation parameters", None))
        self.btn_sim.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to GERDPy", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Weather & local parameters", None))
        self.line_weather_file.setText("")
        self.line_weather_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.btn_browse_weather.setText(QCoreApplication.translate("MainWindow", u" Browse", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Excel-file must be formatted as described in GERDPy documentation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter weather data file path:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Local ground parameters", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal diffusivity of the ground.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Thermal diffusivity [1e-6 m2/s]:", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal conductivity of the ground.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Thermal conductivity [W/mK]:", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Undisturbed soil temperature will be set as starting-point for all entities in the simulation.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Undisturbed soil temperature [\u00b0C]:", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Altitude of chosen location above sea level.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Altitude above sea level [m]:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Heating elements", None))
#if QT_CONFIG(tooltip)
        self.label_73.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total length of all borehole-to-heating element connections (one connection per borehole).</span></p><p><span style=\" font-size:11pt;\">These connections contain the heatpipes from the boreholes as a bundle.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Overall connecting pipes length [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_77.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total area of thermal activated surface.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Surface area heating element [m2]:", None))
#if QT_CONFIG(tooltip)
        self.label_78.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Minimum vertical piping-to-surface distance inside heating element.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: x_min</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Minimal surface distance [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_75.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal conductivity of surface material of heating element. Usually concrete.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: lambda_C</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Thermal conductivity surface material [W/mK]:", None))
#if QT_CONFIG(tooltip)
        self.label_76.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Centerline distance of the equidistant heatpipes inside the heating element.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: s_R</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Centerline distance condenser pipes [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_74.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Total length of all condensor pipes inside heating element.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Overall length condenser pipes [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_81.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thickness of insulation of borehole-to-heating element connections.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Thickness insulation connecting pipes [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_79.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thickness of insulation layer on the bottom side of heating element.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: D_iso,he</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Thickness insulation bottom side [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_82.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Heating element vertical thickness.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: D_he</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Thickness heating element [m]:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Borehole parameters", None))
#if QT_CONFIG(tooltip)
        self.label_30.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Borehole depth will be assumed for every borehole when radiobutton above is not checked.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Borehole depth [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal conductivity of the borehole backfill material.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: lambda_b</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Thermal conductivity backfill [W/mK]:", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Borehole radius will be assumed for every borehole.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: r_b</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Borehole radius [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">This number of heat pipes are uniformly spaced on a circle with radius heat pipe epicenters.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Number of heat pipes per borehole:", None))
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal conductivity of borehole insulating layer.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: lambda_iso</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Thermal conductivity insulating layer [W/mK]:", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Thermal conductivity of a single heat pipe. Value will be assumed for every heat pipe in the system.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: lambda_p</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Thermal conductivity heat pipe [W/mK]:", None))
#if QT_CONFIG(tooltip)
        self.rb_depth.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">If checked, borehole depths and radii will be taken from borefield geometry file.</span></p><p><span style=\" font-size:11pt;\">Otherwise borehole depths and radii will be taken from parameter input below and will be equal for all boreholes.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.rb_depth.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.rb_depth.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.rb_depth.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.rb_depth.setText(QCoreApplication.translate("MainWindow", u"Activate varying borehole depths", None))
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Inner radius of single heat pipe. Value will be assumed for every heat pipe in the system.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: r_pi</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Inner radius heat pipes [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">The heat pipes per borehole are uniformly spaced on a circle with this radius.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: r_w</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Radius heat pipe epicenters [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Outer radius of single heat pipe. Value will be assumed for every heat pipe in the system.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: r_pa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Outer radius heat pipes [m]:", None))
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Outer radius of borehole insulating layer.</span></p><p><span style=\" font-size:11pt;\">Schematics symbol: r_iso</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Outer radius insulating layer [m]:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Borefield geometry & Simulation parameters", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Borefield geometry import", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Select the path to the txt.-file containing the borefield geometry. The file must be formatted like described in the GERDPy-documentation.</span></p><p><span style=\" font-size:11pt;\">If varying borehole depth and radii is checked, the file must contain both parameters for every borehole.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Enter borefield geometry file path:", None))
        self.line_borefield_file.setText("")
        self.line_borefield_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.btn_browse_borefield.setText(QCoreApplication.translate("MainWindow", u" Browse", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Simulation parameters", None))
#if QT_CONFIG(tooltip)
        self.rb_multiyearsim.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">If checked, only full years are possible. The weather data file will be looped for every year, beginning from Startdate.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rb_multiyearsim.setText(QCoreApplication.translate("MainWindow", u"Activate multi-year simulation", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">If muli-year simulation is checked, only full years will be simulated. For single year simulation, simulationtime is choosed in hours.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Simulation time [h]:", None))
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Snow free area ratio is the part of surface, which is always free of snow, if snow cumulates at the surface.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Snow free area ratio:", None))
#if QT_CONFIG(tooltip)
        self.label_31.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">The simulation will be started with the weather conditions at chosen date from weather data file and ends with the date one day before startdate.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Month:", None))
        self.cb_month.setCurrentText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Day:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>When pressing 'START SIMULATION', the simulation will be initialized. <br>This can take a few minutes.</p><p>After initialization, the simulation progress will be shown in a <br>seperate window.</p></body></html>", None))
        self.btn_startsim.setText(QCoreApplication.translate("MainWindow", u" START SIMULATION", None))
        self.btn_save_results.setText(QCoreApplication.translate("MainWindow", u" SAVE RESULTS", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.btn_save_console.setText(QCoreApplication.translate("MainWindow", u" Save Console", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"based on \"Modern GUI PyDracula\" by Wanderson M. Pimenta", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

