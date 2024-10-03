import os
import librosa
import pandas as pd
import re

def get_duration_librosa(file_path):
    audio_data, sample_rate = librosa.load(file_path)
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)
    return duration

def parse_filename(filename):
    # Extract relevant parts from the filename using regex
    match = re.search(r'(\d+\.\d+)_(\w+)___(\d+-\d+kHz)___(\d+-\d+\.\d+s)', filename)
    if match:
        timestamp = match.group(1)  # Example: 2459626.192622
        bird_name = match.group(2)   # Example: Tautenburg
        frequency_range = match.group(3)  # Example: 6589-9171kHz
        time_segment = match.group(4)  # Example: 10-10.9s
        return timestamp, bird_name, frequency_range, time_segment
    return None, None, None, None

# Specify the folder containing your audio files
folder_path = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\External\material_Bird Fly monitoring and analyse\material_Bird Fly monitoring and analyse\2n_data material\Audiodateien'
# Specify the output Excel file path
output_file_path = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\durations.xlsx'

# Create a list to hold file names, durations, and parsed data
data = []

# Iterate through all .wav files in the specified folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)
        duration = get_duration_librosa(file_path)
        
        # Parse the filename to extract details
        timestamp, bird_name, frequency_range, time_segment = parse_filename(filename)
        
        # Append a tuple of (filename, duration, parsed details) to the list
        data.append((filename, duration, timestamp, bird_name, frequency_range, time_segment))

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=['Filename', 'Duration (seconds)', 'Timestamp', 'Bird Name', 'Frequency Range', 'Time Segment'])

# Save the DataFrame to an Excel file
df.to_excel(output_file_path, index=False)

print(f"Durations and parsed data saved to {output_file_path}")
