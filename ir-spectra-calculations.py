import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.signal import correlate
import ir

TIMESTEPS = 100000


def read_dipole_data(filename, dipoles, num_lines=-1):
	"""
	Reads data from cp2k DFTB dipole calculation files. Each time step contains the dipole moment
	in atomic units, Debye, and then the derivative of the dipole moment. The 3rd, 4th, and 5th 
	columns correspond to the x, y, and z axes, respectively.
	"""
	with open(filename, mode='r') as f1:
	    for count, line in enumerate(f1, 1):
	        if count == num_lines:
	            break
	        elif count % 3 == 1:
	            coord = []
	            entries = line.split()
	            
	            coord.append(float(entries[3]))
	            coord.append(float(entries[4]))
	            coord.append(float(entries[5]))
	            
	            dipoles.append(coord)

def main():
	dipoles = []
	file1 = '../sherlock/dftb-dipole-data/traj_select_frames-dftb_dipole-1.data'
	file2 = '../sherlock/dftb-dipole-data/traj_select_frames-dftb_dipole-2.data'
	file3 = '../sherlock/dftb-dipole-data/traj_select_frames-dftb_dipole-3.data'

	read_dipole_data(file1, dipoles, 63000)
	read_dipole_data(file2, dipoles)
	read_dipole_data(file3, dipoles)

	dipoles = np.array(dipoles)

	dipoles = dipoles.transpose()

	dipole_autocorrelations = ir.autocorrelation(dipoles)

	plt.plot(dipole_autocorrelations[49000:50000])
	plt.show()

if __name__ == '__main__':
	main()