import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
import ir
import pickle
from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter

C = 3e8 # speed of light

def main():
	autocorrelation_file = open('molecule_dipole_autocorrelation.dat', 'rb')
	dipole_autocorrelation = pickle.load(autocorrelation_file)
	autocorrelation_file.close()
	
	freq, fourier = ir.ir_spectrum(dipole_autocorrelation, 2e-15)
	fourier = np.abs(fourier)

	# normalize
	total_integral = np.trapz(fourier, x=freq)
	fourier /= total_integral

	smoothed = savgol_filter(fourier, 751, 3)
	# spline = UnivariateSpline(freq, fourier, k=5)
	# smoothed = spline(freq)
	# print(smoothed[:100])
	#plt.plot(freq, fourier)
	plt.plot(freq, smoothed)
	plt.show()


if __name__ == '__main__':
	main()
