# MAIN FILE
# ///////////////////////////////////////////////////////////////
from guimain import *
import GERDPySim.boreholes as boreholes
import GERDPySim.heatpipes as heatpipes
import numpy as np
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class USEFunctions(MainWindow):

    def fcn_browse(self):
        f_name = QFileDialog.getOpenFileName(self, "Open file")
        return f_name


    def errorhandling(self):

      # error handling date
      day = self.ui.sb_day.value()
      month = int(self.ui.cb_month.currentData())

      if month == 2 and day > 28:
        check = False
        print('February only has 28 days maximum.')
        print('Please adjust!')
        self.ui.text_console.insertPlainText('February only has 28 days maximum.\n')
        self.ui.text_console.insertPlainText('Please adjust!\n')
      elif month in [4, 6, 9, 11] and day > 30:
        check = False
        print(self.ui.cb_month.currentText() + ' only has 30 days maximum!')
        print('Please adjust!')
        self.ui.text_console.insertPlainText(self.ui.cb_month.currentText() + ' only has 30 days maximum.\n')
        self.ui.text_console.insertPlainText('Please adjust!\n')
      elif not self.ui.line_weather_file.text():
        check = False
        self.ui.text_console.insertPlainText('Please choose a weather data file.')
      elif not self.ui.line_borefield_file.text():
        check = False
        self.ui.text_console.insertPlainText('Please choose a borefield geometry file.')
      else:
        check = True

      # ------------------------------
      # ERROR HANDLING BOREFIELD
      # ------------------------------

      borefield = boreholes.field_from_file(self, self.ui.line_borefield_file.text())
      # check for negative borehole length and radii
      for i in range(len(borefield)):
        if borefield[i].r_b <= 0:
          self.ui.text_console.insertPlainText("Borehole radius is zero or negative at borehole No. " + str(i + 1) + ".\n")
          check = False
          break
        elif borefield[i].H <= 0:
          self.ui.text_console.insertPlainText("Borehole depth is zero or negative at borehole No. " + str(i + 1) + ".\n")
          check = False
          break
        elif borefield[i].D <= 0:
          self.ui.text_console.insertPlainText("Borehole buried depth is zero or negative at borehole No. " + str(i + 1) + ".\n")
          check = False
          break

      # check for borehole duplicates
      duplicate_pairs = []
      for i in range(len(borefield)):
        borehole_1 = borefield[i]
        for j in range(i, len(borefield)):  # loop
          borehole_2 = borefield[j]
          if i == j:  # comparison of borehole with itself omitted
            continue
          else:
            dist = borehole_1.distance(borehole_2)
          if abs(dist - borehole_1.r_b) < borehole_1.r_b:
            duplicate_pairs.append((i + 1, j + 1))
      if duplicate_pairs:
        print(f'Geometric conflict between the following borehole pairs:')
        print(*duplicate_pairs, sep=", ")
        print('Please adjust!')
        print(duplicate_pairs)
        self.ui.text_console.insertPlainText(f'Geometric conflict between the following borehole pairs: \n')
        self.ui.text_console.insertPlainText(''.join(map(str, duplicate_pairs)))
        self.ui.text_console.insertPlainText('\nPlease adjust!\n')
        check = False

      # check for compatible heatpipe geometry

      # Load geometry
      N = self.ui.sb_number_heatpipes.value()  # no. of heatpipes per borehole [-] (default: 6)
      r_w = self.ui.sb_radius_w.value()  # radius of heatpipe-centres [m] (default: 0.12)
      r_iso_b = self.ui.sb_radius_iso.value()  # outer radius of heatpipe insulation [m] (default: 0.016)
      r_pa = self.ui.sb_radius_pa.value()  # outer radius of heatpipes [m] (default: 0.016)
      r_pi = self.ui.sb_radius_pi.value()  # inner radius of heatpipes [m] (default: 0.015)

      # Load thermal conductivities
      lambda_b = self.ui.sb_lambda_b.value()  # ~ of borehole backfill [W/mK] (default: 2.0)
      lambda_iso = self.ui.sb_lambda_iso.value()  # ~ of insulation layer [W/mK] (default: 0.03)
      lambda_p = self.ui.sb_lambda_p.value()  # ~ of heatpipe material [W/mK] (default: 14.0)

      for i in range(len(borefield)):
        hp = heatpipes.Heatpipes(N, borefield[i].r_b, r_w, r_iso_b, r_pa, r_pi, lambda_b,
                               lambda_iso, lambda_p)
        xy = hp.xy_mat()
        heatpipe_distance = np.sqrt((xy[1, 0] - xy[2, 0]) ** 2 + (xy[1, 1] - xy[2, 1]) ** 2)
        if ((hp.r_pa + hp.r_w) >= hp.r_b):
          print("Heat pipe circle too big!")
          self.ui.text_console.insertPlainText("Heat pipes overlap borehole wall at borehole No. " + str(i+1) + ".\n" 
                                               "Please adjust.\n")
          check = False
          break
        elif heatpipe_distance <= (2 * hp.r_pa):
          print("Too many heat pipes!")
          self.ui.text_console.insertPlainText("Too many heat pipes per borehole!\n"
                                               "Please adjust.\n")
          check = False

      return check

    def save_console(self):
      text = self.ui.text_console.toPlainText()
      path = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")
      with open(path[0], 'w') as f:
        f.write(text)
      self.ui.text_console.insertPlainText('Console output saved.\n')

    def save_results(self, results):
      if results.empty:
        self.ui.text_console.insertPlainText('No results to save. Please start simulation first.\n')
      else:
        path = QFileDialog.getSaveFileName(self, "Save file", "", "Csv files (*.csv)")
        results.to_csv(path[0], sep='\t')
        self.ui.text_console.insertPlainText('Results saved.\n')



