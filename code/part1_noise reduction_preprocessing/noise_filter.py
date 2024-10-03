import os
import numpy as np
import scipy.signal
import scipy.io.wavfile

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = scipy.signal.butter(order, [low, high], analog=False, btype='band', output='sos')
    filtered_data = scipy.signal.sosfiltfilt(sos, data)
    return filtered_data

# Specify the folder containing the audio files
input_folder_path = "D:/Professional/Projects/Biodiversity/final/analysis_task/Data/Raw"  # Replace with your input folder path

# Specify the output folder for filtered audio files
output_folder_path = r"D:\Professional\Projects\Biodiversity\final\analysis_task\Data\Processed"

# Specify the filter parameters
lowcut = 10  # Adjust as needed
highcut = 50  # Adjust as needed
order = 4  # Adjust as needed

# Create output directory if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Iterate through files in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".wav"):
        file_path = os.path.join(input_folder_path, filename)
        
        # Load the audio file
        sample_rate, data = scipy.io.wavfile.read(file_path)
        
        # Apply the bandpass filter
        filtered_audio = bandpass_filter(data, lowcut, highcut, sample_rate, order)
        
        # Construct the output file path for filtered audio
        output_path = os.path.join(output_folder_path, f"filtered_{filename}")
        
        # Save the filtered audio
        scipy.io.wavfile.write(output_path, sample_rate, filtered_audio.astype(np.int16))
        
        print(f"Filtered audio saved as: {output_path}")
