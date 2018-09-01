from corrLib import g2ToFile,g2ToFile_cpu
import numpy as np
import time
import scipy

mat_directory = "C:/Users/Ryd Berg/Google Drive/Rydberg Experiment/Matlab/CorrelationCalculations/For Sandy/"
data_directory = "C:/Users/Ryd Berg/Downloads/"

data_folder = data_directory+"g2_benchmark/"
mat_file = mat_directory+"g2_benchmark_cpu"
benchmark_mat = mat_directory+"g2_benchmark_cpu_full_multithread"

#max_time = 1e-6
#bin_width = 1e-9
#pulse_spacing = 100e-6
#max_pulse_distance = 4

#cpu_threads = np.array(range(32))+32

#time_taken = np.zeros(len(cpu_threads))
#for i in range(len(cpu_threads)):
#    start_time = time.time()
#    g2ToFile_cpu(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,cpu_threads[i])
#    time_taken[i] = time.time()-start_time

#scipy.io.savemat(benchmark_mat,{'num_threads':cpu_threads,'time':time_taken,'device':'Threadripper 1950x'})

bin_width = 82.3e-12*12
pulse_spacing = 100e-6
max_pulse_distance = 4
half_tau_bins = np.array([1,50,100,250,500,1000,2500,5000])
calc_bins = half_tau_bins * 2 + 1
time_taken = np.zeros(len(half_tau_bins))
for i in range(len(half_tau_bins)):
    max_time = half_tau_bins[i] * bin_width
    start_time = time.time()
    g2ToFile_cpu(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,32)
    time_taken[i] = time.time()-start_time

scipy.io.savemat(benchmark_mat,{'num_bins':calc_bins,'time':time_taken,'device':'Threadripper 1950x','thread_num':32})