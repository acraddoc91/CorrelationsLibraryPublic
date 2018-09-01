mat_directory = "C:/Users/Ryd Berg/Google Drive/Rydberg Experiment/Matlab/CorrelationCalculations/For Sandy/"
data_directory = "C:/Users/Ryd Berg/PycharmProjects/simulated_g2_DATA/"

from corrLib import g2ToFile,g3ToFile,g2ToFile_channelPair

data_folder = data_directory+"data/"
#data_folder = data_directory+"test_files/"
mat_file = mat_directory+"g2_simulated_loss"
max_time = 1e-6*(82.3e-12*2/5e-9)
bin_width = 82.3e-12*2
pulse_spacing = 100e-6*(82.3e-12*2/5e-9)
max_pulse_distance = 4
#g2ToFile_channelPair(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,1,2)
g2ToFile(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance)