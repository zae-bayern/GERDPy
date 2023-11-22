# -*- coding: utf-8 -*-
""" GERDPySim - 'weather_data.py'
    
    Import of weather data from Excel-File

    Authors: Yannick Apfel, Meike Martin
"""
def get_weather_data(Nt, self):

    import sys
    import numpy as np
    import pandas as pd

    # path to excel-file
    path = self.ui.line_weather_file.text()  # './data/Wetterdaten_München-Riem_h.xlsx'

    # import data
    data = pd.read_excel(path, skiprows=3, header=1)

    # get startdate
    day = self.ui.sb_day.value()
    month = int(self.ui.cb_month.currentData())

    # create a list of row indices based on startdate
    start_index = data.index[(data.iloc[:, 0] == month) & (data.iloc[:, 1] == day)].tolist()[0]

    if start_index+Nt > len(data):
        if 0 != start_index:
            rows = list(range(start_index, len(data), 1)) + list(range(0, start_index, 1))
        else:
            rows = list(range(len(data)))
    else:
        rows = list(range(start_index, start_index+Nt, 1))

    # create looped list for multi-year simulation
    i = 1
    while i <= Nt/len(data)-1:
        if 0 != start_index:
            rows = rows + list(range(start_index, len(data), 1)) + list(range(0, start_index, 1))
        else:
            rows = rows + list(range(len(data)))
        i += 1

    # 1.) ambient wind speed [m/s]
    u_inf = np.array(data.iloc[rows, 6])

    # 2.) ambient temperature [°C]
    Theta_inf = np.array(data.iloc[rows, 4])

    # 3.) snowfall rate [mm/h]
    S_r = np.array(data.iloc[rows, 3])
    # sets entries to 0, in case Theta_inf >= 1 °C (precipitation comes down as rain)
    for i, j in enumerate(Theta_inf):
        if j >= 1:
            S_r[i] = 0

    # 4.) cloudiness [octal units/8]
    ''' between 0/8 - cloudless and 
                8/8 - fully overcast
    '''
    B = np.array(data.iloc[rows, 7]) / 8

    # 5.) relative humidity [-]
    Phi = np.array(data.iloc[rows, 5]) / 100

    # 6.) total precipitation [mm/h]
    RR = np.array(data.iloc[rows, 3])

    # 7.) dates array of strings
    dates = np.empty(len(rows), dtype=object)
    if len(rows) > 8760:  # if multi-year simulation, add the year to the date with format ['y-mm-dd-hh']
        for i in range(0, len(rows)):
            dates[i] = str(int(i/8760)+1) + '-' + str(data.iloc[rows[i], 0]) + '-' + str(data.iloc[rows[i], 1]) + '-' + str(data.iloc[rows[i], 2])
        fos = np.where(dates == '1-9-1-1')[0][0] # get index of first 1st of September
    else:  # else just use format ['mm-dd-hh']
        for i in range(0, len(rows)):
            dates[i] = str(data.iloc[rows[i], 0]) + '-' + str(data.iloc[rows[i], 1]) + '-' + str(data.iloc[rows[i], 2])
        fos = 0

    return u_inf, Theta_inf, S_r, B, Phi, RR, dates, fos
