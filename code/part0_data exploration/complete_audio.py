from pydub import AudioSegment
import os

def combine_audio_files_from_directory(directory_path, output_path):
    combined = AudioSegment.empty()  # Start with an empty audio segment
    
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".wav"):  # Check for .wav files
            file_path = os.path.join(directory_path, filename)
            print(f"Combining {file_path}")  # Optional: Print the file being combined
            sound = AudioSegment.from_file(file_path)
            combined += sound  # Concatenate the audio segments
    
    # Export the combined audio file
    combined.export(output_path, format="wav")
    print(f"Combined audio exported to {output_path}")  # Confirm export

# Example usage:
if __name__ == "__main__":
    input_directory = r"D:\Professional\Projects\Biodiversity\final\analysis_task\Data\External\material_Bird Fly monitoring and analyse\material_Bird Fly monitoring and analyse\2n_data material\Audiodateien"  
    output_file = r"D:\output\path\combined_audio.wav"  # Make sure this directory exists
    
    combine_audio_files_from_directory(input_directory, output_file)
