import os
import librosa
import soundfile as sf

def segment_audio_files(input_folder, output_folder):
    """
    Function to segment audio files based on time segments specified in the file names.

    Parameters:
    - input_folder: Folder containing the original audio files.
    - output_folder: Folder to save the segmented audio files.
    
    File name format: "...___start-end(s)___...", e.g., "2459626.192622_Tautenburg___10-10.9s___b..wav"
    """
    
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):
            # Construct the full file path
            file_path = os.path.join(input_folder, file_name)
            
            # Parse the time segment from the file name (assuming format: '...___10-10.9s___...')
            try:
                # Extract time segment part from file name (e.g., "10-10.9s")
                time_segment = file_name.split("___")[2]  # This is the part with 'start-end(s)'
                
                # Remove the 's' at the end and split by '-'
                start_time, end_time = map(float, time_segment[:-1].split('-'))  # Remove 's' and split
                
                # Load the audio file
                audio, sr = librosa.load(file_path, sr=None)  # Load with original sampling rate
                
                # Calculate sample indices for the start and end times
                start_sample = int(start_time * sr)
                end_sample = int(end_time * sr)
                
                # Slice the audio data to get the segment
                audio_segment = audio[start_sample:end_sample]
                
                # Construct the output file name and path
                output_file_name = f"segment_{start_time}-{end_time}s_{file_name}"
                output_file_path = os.path.join(output_folder, output_file_name)
                
                # Save the segmented audio file
                sf.write(output_file_path, audio_segment, sr)
                
                print(f"Segmented audio saved as: {output_file_path}")

            except Exception as e:
                print(f"Failed to process {file_name}: {e}")

# Example usage:
input_folder = "Data/Raw"
output_folder = "Data/Segmented"
segment_audio_files(input_folder, output_folder)
