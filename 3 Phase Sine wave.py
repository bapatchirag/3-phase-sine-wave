"""

EEE ASSIGNMENT:
To show the waveforms of a balanced 3 phase system, given the values of the RMS value of voltage, the frequency of the AC voltage and the initial phase angle
(GUI enabled)

Authors: Chirag Bapat, Dinesh Babu S, Ambu Karthik, Furqan Abdul Khadar Ramadurg

Date and time of creation: 21 February, 2019 @ 11:09
Last save for a major change: 27 February, 2019 @ 23:45
Last major change: GUI added to the program; once 3 Phase Sine wave.exe is run, application will start

"""

from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np

# Main GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle('3 Phase Sine Wave')
window.setStyleSheet('QWidget {background-color: black; color: white;}')
grid_layout = QGridLayout()

# Text and value box for frequency
freq_text = QLabel('Enter frequency: ')
freq_val = QDoubleSpinBox()
freq_val.setMinimum(0.00)

# Text and value box for RMS voltage
rms_text = QLabel('Enter RMS value of voltage: ')
rms_val = QDoubleSpinBox()
rms_val.setMinimum(0.00)

# Text and value box for phase
phase_text = QLabel('Enter initial phase angle in degrees: ')
phase_val = QDoubleSpinBox()
phase_val.setMinimum(0.00)
phase_val.setMaximum(179.99)

# Button for entry
accept_button = QPushButton('Enter values')
accept_button.setStyleSheet('QPushButton {border: 1px solid red;}')

# Button to exit
exit_button = QPushButton('Quit')
exit_button.setStyleSheet('QPushButton {border: 1px solid red;}')

# Plotting function
def plot_waveforms():
    freq = freq_val.value() # Frequency
    V_rms = rms_val.value() # RMS value of voltage
    phase = phase_val.value() # Initial phase

    V_m = V_rms * np.sqrt(2) # Peak Voltage
    phase = phase * np.pi / 180 # Conversion to radians
    omega = 2 * np.pi * freq # Angular Frequency
    
    t = np.arange(-2 * np.pi, 2 * np.pi, 0.0001)
    e1 = V_m * np.sin(omega * t + phase)
    e2 = V_m * np.sin((omega * t) + ((2 * np.pi) / 3) + phase)
    e3 = V_m * np.sin((omega * t) - ((2 * np.pi) / 3) + phase)

    plt.axhline(y = 0, linestyle = 'solid', color = 'black', linewidth = 3) # X Axis
    plt.axvline(x = 0, linestyle = 'solid', color = 'black', linewidth = 3) # Y Axis
    plt.axhline(y = V_m, linestyle = 'dashed', color = 'black', label = 'V_m = '+str(V_m)+'V') # Denoting peak voltage
    plt.axhline(y = V_rms, linestyle = 'dashdot', color = 'black', label = 'V_rms = '+str(V_rms)+'V') # Denoting RMS voltage
    plt.grid()
    plt.plot(t, e1, label = 'e1 = '+str(V_m)+' * sin('+str(omega)+'t + ('+str(phase)+')) V')
    plt.plot(t, e2, label = 'e2 = '+str(V_m)+' * sin('+str(omega)+'t + (2 * pi/3) + ('+str(phase)+')) V')
    plt.plot(t, e3, label = 'e3 = '+str(V_m)+' * sin('+str(omega)+'t - (2 * pi/3) + ('+str(phase)+')) V')
    plt.legend(loc = 'upper center', bbox_to_anchor = (0.5, 1.15), shadow = True, ncol = 2)
    plt.show()

# Signal to button, slotting plot_waveforms
accept_button.clicked.connect(plot_waveforms)
exit_button.clicked.connect(window.close)

# Add widgets to layout
grid_layout.addWidget(freq_text, 0, 0)
grid_layout.addWidget(freq_val, 0, 1)
grid_layout.addWidget(rms_text, 1, 0)
grid_layout.addWidget(rms_val, 1, 1)
grid_layout.addWidget(phase_text, 2, 0)
grid_layout.addWidget(phase_val, 2, 1)
grid_layout.addWidget(accept_button, 4, 0)
grid_layout.addWidget(exit_button, 4, 1)

# Set and show layouts
window.setLayout(grid_layout)
window.show()

# Execute application
app.exec_()
