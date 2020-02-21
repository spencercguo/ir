"""
ir.py
--------------------------
Author: Spencer Guo

This files defines functions for calculating IR spectra from dipole moment data. The dipole moment data
can come from DFT, DFTB, or other simulations.
"""

from scipy.signal import correlate
from numpy import fft

C = 3e8 # speed of light

def autocorrelation(dipoles):
	# Calculate the autocorrelation for a sequence of 3-D dipole vectors over time.
	# Uses scipy.signal.correlate to calculate the autocorrelation function for 
	# each axis, and then sum each time step (equivalent to taking the dot product)
	# 
	# dipoles: an i x 3 array containing the dipole moments at each time step i
	#
	# Returns an array containing the autocorrelations for each lag.

	correlation_x = correlate(dipoles[:,0], dipoles[:,0])
	correlation_y = correlate(dipoles[:,1], dipoles[:,1])
	correlation_z = correlate(dipoles[:,2], dipoles[:,2])

	return correlation_x + correlation_y + correlation_z

def ir_spectrum(autocorrelation, time_interval):
    # Returns the IR spectrum of from the autocorrelation function
    # Calculates the fast Fourier transform of the autocorrelation and the
    # associated frequencies/wavenumbers
    #
    # autocorrelation: autocorrelation function of dipole moments
    # time_interval: length of time step (in seconds)
    #
    # Returns the frequencies (wavenumbers) and the intensities (both as numpy arrays)

    fourier = fft.rfft(autocorrelation)

    # d is sample frequency, inverse of sample time interval
    freq = fft.rfftfreq(len(autocorrelation), d=time_interval) 

    # convert to wavenumbers (cm^-1) 
    # wavenumbers = freq / speed of light
    freq = (freq / (C * 100)) 

    # IR spectrum scaling
    fourier *= freq**2

    return freq, fourier
