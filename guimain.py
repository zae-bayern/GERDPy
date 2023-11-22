# ///////////////////////////////////////////////////////////////
#
# BY: YANNICK APFEL AND MEIKE MARTIN
# V: 2.0.0
#
# GUI BASED ON Modern_GUI_PyDracula BY WANDERSON M.PIMENTA:
# https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6
# PROJECT MADE WITH: Qt Designer and PySide6
#
# SIMULATION BASED ON PYGFUNCTION BY MASSIMO CIMMINO:
# https://github.com/MassimoCimmino/pygfunction
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits in the Python scripts.
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import pandas as pd

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from GERDPySim._main import main as simulation
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "GERDPy"
        description = "GERDPy - Simulation Tool for Geothermal Heat Pipe Surface Heating Systems"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # RADIOBUTTONS
        widgets.rb_depth.toggled.connect(lambda: UIFunctions.rbstate(self, self.ui.rb_depth))
        widgets.rb_multiyearsim.toggled.connect(lambda: UIFunctions.rbsimtime(self, self.ui.rb_multiyearsim))

        # DROPDOWN MONTHS
        widgets.cb_month.addItem("January", 1)
        widgets.cb_month.addItem("February", 2)
        widgets.cb_month.addItem("March", 3)
        widgets.cb_month.addItem("April", 4)
        widgets.cb_month.addItem("May", 5)
        widgets.cb_month.addItem("June", 6)
        widgets.cb_month.addItem("July", 7)
        widgets.cb_month.addItem("August", 8)
        widgets.cb_month.addItem("September", 9)
        widgets.cb_month.addItem("October", 10)
        widgets.cb_month.addItem("November", 11)
        widgets.cb_month.addItem("December", 12)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_weather.clicked.connect(self.buttonClick)
        widgets.btn_heat.clicked.connect(self.buttonClick)
        widgets.btn_borefield.clicked.connect(self.buttonClick)
        widgets.btn_surface.clicked.connect(self.buttonClick)
        widgets.btn_sim.clicked.connect(self.buttonClick)

        # WEATHER SHEET
        widgets.btn_browse_weather.clicked.connect(self.buttonClick)

        # BOREFIELD SHEET
        widgets.btn_browse_borefield.clicked.connect(self.buttonClick)

        # SIMULATION SHEET
        widgets.btn_startsim.clicked.connect(self.buttonClick)
        widgets.btn_save_console.clicked.connect(self.buttonClick)
        widgets.btn_save_results.clicked.connect(self.buttonClick)

        # INITIALIZE RESULTS DATAFRAME
        results = pd.DataFrame()

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes/py_dark.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET START/STOP ICONS
        start_icon = QIcon()
        stop_icon = QIcon()
        start_icon.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        stop_icon.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)

        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WEATHER PAGE
        if btnName == "btn_weather":
            widgets.stackedWidget.setCurrentWidget(widgets.weather_local)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW GROUND PAGE
        if btnName == "btn_heat":
            widgets.stackedWidget.setCurrentWidget(widgets.heating_element)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW GROUND PAGE
        if btnName == "btn_borefield":
           widgets.stackedWidget.setCurrentWidget(widgets.boreholes)
           UIFunctions.resetStyle(self, btnName)
           btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW SURFACE PAGE
        if btnName == "btn_surface":
           widgets.stackedWidget.setCurrentWidget(widgets.borefield_sim)
           UIFunctions.resetStyle(self, btnName)
           btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW SIMULATION PAGE
        if btnName == "btn_sim":
           widgets.stackedWidget.setCurrentWidget(widgets.simulation)
           UIFunctions.resetStyle(self, btnName)
           btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # BROWSE WEATHER DATA
        if btnName == "btn_browse_weather":
            w_file = USEFunctions.fcn_browse(self)
            widgets.line_weather_file.setText(w_file[0])

        # BROWSE BOREFIELD DATA
        if btnName == "btn_browse_borefield":
            b_file = USEFunctions.fcn_browse(self)
            widgets.line_borefield_file.setText(b_file[0])

        # START SIMULATION
        if btnName == "btn_startsim":

            self.ui.text_console.clear()
            correct = USEFunctions.errorhandling(self)

            if correct:
                if self.ui.btn_startsim.text() == " START SIMULATION":
                    self.ui.btn_startsim.setText(" ABORT SIMULATION")
                    self.ui.btn_startsim.setIcon(stop_icon)
                    self.ui.text_console.insertPlainText('------SIMULATION STARTED------\n')
                    self.ui.text_console.insertPlainText('Date-Check: OK!\n')
                    self.ui.text_console.insertPlainText('Parameter-Check: OK!\n')
                    self.ui.text_console.insertPlainText('Geometry-Check: OK!\n')
                    # with concurrent.futures.ThreadPoolExecutor() as executor:
                    #     future = executor.submit(simulation, self)  # how to pass self as arg??
                    #     self.results = future.result()
                    self.results = simulation(self)
                    self.ui.btn_startsim.setText(" START SIMULATION")
                    self.ui.btn_startsim.setIcon(start_icon)
                else:
                    quit()
                    self.ui.btn_startsim.setText(" START SIMULATION")
                    self.ui.btn_startsim.setIcon(start_icon)
                    self.ui.text_console.insertPlainText('------SIMULATION ABORTED------\n')

        # SAVE DATA
        if btnName == "btn_save_console":
            USEFunctions.save_console(self)

        if btnName == "btn_save_results":
            USEFunctions.save_results(self, self.results)

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ZAE.ico"))
    window = MainWindow()
    sys.exit(app.exec())
