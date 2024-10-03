import os
import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_spectrum(file_path):
    # Read the audio file
    sample_rate, data = wavfile.read(file_path)
    
    # If stereo, convert to mono by averaging channels
    if len(data.shape) > 1:
        data = data.mean(axis=1)
    
    # Create a new figure for the spectrogram
    plt.figure(figsize=(10, 6))
    
    # Plot the spectrogram
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='viridis')
    
    # Set the title and labels
    plt.title(f'Spectrum of {os.path.basename(file_path)}')
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    
    # Show color bar for reference
    plt.colorbar(label='Intensity [dB]')
    
    # Show the plot
    plt.show()

# Paths to your audio folders (replace with actual paths)
folder1_path = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\Raw'
folder2_path = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\Processed'

# Function to plot spectrograms for all .wav files in a given folder
def plot_spectrograms_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.wav'):
            file_path = os.path.join(folder_path, filename)
            plot_spectrum(file_path)

# Plot spectrograms for both folders
plot_spectrograms_in_folder(folder1_path)
plot_spectrograms_in_folder(folder2_path)
