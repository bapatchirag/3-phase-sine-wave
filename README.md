# 3-phase-sine-wave
Generates a 3 phase sine wave for a balanced load and balanced source

This script takes inputs as frequency of the source (f), the RMS value of the voltage supplied (Vrms) and the initial phase difference (phase) through a GUI window.
This would plot 3 sine waves on the same graph, each at a phase difference of 120 degrees from each other.
These sine waves depict the alternating voltages in a 3 phase, balanced load and balanced source system.

Equations:
V1 = Vrms * sqrt(2) * sin((2 * pi * f) + phase)
V2 = Vrms * sqrt(2) * sin((2 * pi * f) + phase - 120 degrees)
V2 = Vrms * sqrt(2) * sin((2 * pi * f) + phase + 120 degrees)
