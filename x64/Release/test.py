mat_directory = "C:/Users/Ryd Berg/Google Drive/Rydberg Experiment/Matlab/CorrelationCalculations/For Sandy/"
data_directory = "C:/Users/Ryd Berg/Downloads/"

from corrLib import g2ToFile,g2ToFile_nominibatching, g2ToFile_nostreams

data_folder = data_directory+"g2_benchmark/"
#data_folder = data_directory+"test_files/"
mat_file = mat_directory+"g2_benchmark_gpu"
max_time = 1e-6
bin_width = 1e-9
pulse_spacing = 100e-6
max_pulse_distance = 4
#g3ToFile(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance)
g2ToFile(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance)
#g2ToFile_cpu(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance)