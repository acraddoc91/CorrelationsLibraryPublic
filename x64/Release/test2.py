#mat_directory = "C:/Users/Ryd Berg/Google Drive/Rydberg Experiment/Matlab/CorrelationCalculations/For Sandy/"
mat_directory = "Z:/Data/Processed Correlations/"
data_directory = "Z:/Data/Correlation Data/2018/June/"

from corrLib import g2ToFile,g3ToFile,g2ToFile_channelPair,count_tags

data_folder = data_directory+"7/cw_139/"
#data_folder = data_directory+"test_files/"
max_time = 100e-6
bin_width = 5e-9
pulse_spacing = 100e-6
max_pulse_distance = 5
mat_file = mat_directory+"cw_139"
#g2ToFile_channelPair(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,0,1)
#mat_file = mat_directory+"g2_March_38_5ns"
#g2ToFile_channelPair(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,0,2)
#mat_file = mat_directory+"g2_March_58_5ns"
#g2ToFile_channelPair(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance,1,2)
g2ToFile(data_folder,mat_file,max_time,bin_width,pulse_spacing,max_pulse_distance)
#count_tags(data_folder,max_time,bin_width,pulse_spacing,max_pulse_distance)