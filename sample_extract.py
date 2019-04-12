from scipy.io import wavfile
file_name = 'sawtooth'
fps, data = wavfile.read(file_name + '.wav')
out_file = open(file_name + '.txt', 'w')
for idx, sample in enumerate(data):
	out_file.write(str(sample[0]))
	out_file.write(', ')
	if idx % 50 == 0:
		out_file.write('\n')
out_file.close()
print('Frames per Second:', fps)
print('Number of samples:', data.shape[0])
