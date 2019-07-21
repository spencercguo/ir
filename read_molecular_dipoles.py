import numpy as np
import matplotlib.pyplot as plt
import time
import ir
import pickle

def read_dipole_data(filename, dipoles, num_lines=-1):
	"""
	Reads dipole data from the molecular dipoles data. Each time step lists the dipoles for all 128
	water molecules in the system. All dipoles are reported in Debye.
	"""
	with open(filename, mode='r') as f:
		while(True):
			if (not f.readline()): # line with column titles
				break

			box_x_sum, box_y_sum, box_z_sum = 0, 0, 0

			for i in range(128):
				line = f.readline()
				entries = line.split()
				box_x_sum += float(entries[2])
				box_y_sum += float(entries[3])
				box_z_sum += float(entries[4])

			box_dipole_vector = [box_x_sum, box_y_sum, box_z_sum]
			dipoles.append(box_dipole_vector)

def main():
	dipoles = []
	filename = 'molecular_dipoles.dat'
	read_dipole_data(filename, dipoles)

	dipoles = np.array(dipoles)
	dipoles = np.transpose(dipoles)
	box_dipoles = np.linalg.norm(dipoles, axis=0)
	plt.hist(box_dipoles, bins=100)
	plt.show()

	dipole_autocorrelation = ir.autocorrelation(dipoles)
	autocorrelation_file = open('molecule_dipole_autocorrelation.dat', 'wb')
	pickle.dump(dipole_autocorrelation, autocorrelation_file)
	autocorrelation_file.close()
	

if __name__ == '__main__':
	main()