# cython: language_level=3
""" GERDPySim - 'weather_data.py'
    
    Import of weather data from Excel-File

    Authors: Yannick Apfel, Meike Martin
"""

import numpy as np
cimport numpy as np
import pandas as pd
cimport cython

cpdef tuple get_weather_data(int Nt, self):
    """
    Import weather data from an Excel file.

    Parameters
    ----------
    Nt : int
        Number of time steps.
    self : object
        Reference to the main class instance containing UI elements.

    Returns
    -------
    tuple
        Contains arrays of wind speed, ambient temperature, snowfall rate,
        cloudiness, relative humidity, total precipitation, dates, and index
        of the first of September.
    """
    # Path to excel-file
    path = self.ui.line_weather_file.text()

    # Import data
    data = pd.read_excel(path, skiprows=3, header=1)

    # Get startdate
    day = self.ui.sb_day.value()
    month = int(self.ui.cb_month.currentData())

    # Create a list of row indices based on startdate
    start_index = data.index[(data.iloc[:, 0] == month) & (data.iloc[:, 1] == day)].tolist()[0]

    # Handling data for multi-year simulation
    rows = []
    if start_index + Nt > len(data):
        if start_index != 0:
            rows = list(range(start_index, len(data))) + list(range(start_index))
        else:
            rows = list(range(len(data)))
    else:
        rows = list(range(start_index, start_index + Nt))

    # Looping list for multi-year simulation
    i = 1
    while i <= Nt / len(data) - 1:
        if start_index != 0:
            rows += list(range(start_index, len(data))) + list(range(start_index))
        else:
            rows += list(range(len(data)))
        i += 1

    # Extracting weather data
    u_inf = np.array(data.iloc[rows, 6])  # Wind speed [m/s]
    Theta_inf = np.array(data.iloc[rows, 4])  # Ambient temperature [°C]
    S_r = np.array(data.iloc[rows, 3])  # Snowfall rate [mm/h]
    B = np.array(data.iloc[rows, 7]) / 8  # Cloudiness [octal units/8]
    Phi = np.array(data.iloc[rows, 5]) / 100  # Relative humidity [-]
    RR = np.array(data.iloc[rows, 3])  # Total precipitation [mm/h]
    dates = np.empty(len(rows), dtype=object)  # Dates array

    # Formatting dates
    for i in range(len(rows)):
        dates[i] = str(data.iloc[rows[i], 0]) + '-' + str(data.iloc[rows[i], 1]) + '-' + str(data.iloc[rows[i], 2])

    # Find index of first of September
    fos = np.where(dates == '9-1-1')[0][0] if len(rows) > 8760 else 0

    return u_inf, Theta_inf, S_r, B, Phi, RR, dates, fos
