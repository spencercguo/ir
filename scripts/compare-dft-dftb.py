import numpy as np
import matplotlib.pyplot as plt

def read_dft_dipole_data(filename, dipoles, num_lines=-1):
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

def read_dftb_dipole_data(filename, dipoles, num_lines=-1):
	# Reads data from cp2k DFTB dipole calculation files. Each time step contains the box dipole moment
	# in atomic units, Debye, and then the derivative of the dipole moment. The 3rd, 4th, and 5th 
	# columns correspond to the x, y, and z axes, respectively.
	
	with open(filename, mode='r') as f1:
		for count, line in enumerate(f1, 1):
			if count == num_lines:
				break
			elif count % 3 == 1: # atomic units
				coord = []
				entries = line.split()
				
				coord.append(float(entries[3]))
				coord.append(float(entries[4]))
				coord.append(float(entries[5]))
				
				dipoles.append(coord)

def main():
	dft_dipoles = []
	filename = 'molecular_dipoles.dat'
	read_dft_dipole_data(filename, dft_dipoles)

	dft_dipoles = np.array(dft_dipoles)
	dft_dipoles = np.transpose(dft_dipoles)
        print(dft_dipoles[:10])
	dft_box_dipoles = np.linalg.norm(dft_dipoles, axis=0)
	plt.hist(dft_box_dipoles, bins=100)
	plt.xlabel('Dipole magnitude')
	plt.title('DFT dipole distribution')
	plt.show()

#	dftb_dipoles = []
#	read_dftb_dipole_data('../dftb_files/dftb-dipole-data/traj_select_frames-dftb_dipole-d3-diffparams.data', dftb_dipoles)
#	read_dftb_dipole_data('../dftb_files/dftb-dipole-data/traj_select_frames-dftb_dipole-d3-diffparams-2.data', dftb_dipoles)
#	dftb_dipoles = np.array(dftb_dipoles)
#	dftb_dipoles = dftb_dipoles.transpose()
#	dftb_box_dipoles = np.linalg.norm(dftb_dipoles, axis=0)
#	plt.hist(dftb_box_dipoles, bins=100)
#	plt.xlabel('Dipole magnitude')
#	plt.title('DFTB dipole distribution')
#	plt.show()
	# print(np.shape(dftb_box_dipoles[:-1]))

	# plt.scatter(dft_box_dipoles, dftb_box_dipoles[:-1])
	# plt.show()



if __name__ == '__main__':
	main()



