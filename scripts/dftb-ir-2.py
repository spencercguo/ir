import numpy as np
import matplotlib.pyplot as plt
import time
import ir

TIMESTEPS = 100000
STEP_SIZE = 2e-15 # 2 femtosecond time step in simulations

def read_dipole_data(filename, dipoles, num_lines=-1):
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
    dipoles = []

    read_dipole_data('../dftb_files/dftb-dipole-data/traj_select_frames-dftb_dipole-d3-1.data', dipoles)
    read_dipole_data('../dftb_files/dftb-dipole-data/traj_select_frames-dftb_dipole-d3-2.data', dipoles)

    dipoles = np.array(dipoles)
    dipoles = dipoles.transpose()

    # dipole_autocorrelations = ir.autocorrelation(dipoles)
    # plt.plot(dipole_autocorrelations[49000:51000])
    # plt.show()

    # freq, fourier = ir.ir_spectrum(dipole_autocorrelations, STEP_SIZE)

    # fourier = np.abs(fourier)
    # total_integral = np.trapz(fourier, x=freq)
    # fourier /= total_integral
    # plt.plot(freq, fourier)
    # # plt.show()
    

if __name__ == '__main__':
    main()
