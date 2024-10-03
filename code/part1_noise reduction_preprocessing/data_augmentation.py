import os
import numpy as np
import librosa
import soundfile as sf
from collections import Counter


# Path to your audio files [(pass test data dir location)]
path_audio = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\External\material_Bird Fly monitoring and analyse\material_Bird Fly monitoring and analyse\2n_data material\Audiodateien'

# Load species counts (dictionary with species codes as keys and their counts as values)
species_counts = {
    'st': 2003, 're': 1191, 'b': 322, 'to': 190, 'co': 67, 'h': 67, 's': 60, 'r': 47,
    'mh': 33, 'eo': 26, 'kr': 16, 'ch': 14, 'tp': 14, 'wg': 7, 'wa': 7, 't': 7,
    'wn': 6, 'gn': 5, 'gj': 5, 'l': 5, 'ma': 5, 'bf': 5, 'bh': 4, 'gr': 4, 'd': 4,
    'cs': 3, 'ms': 3, 'ff': 3, 'bo': 3, 'na': 2, 'gp': 1, 'bg': 1, 'zd': 1, 'cr': 1,
    'gl': 1, 'bl': 1, 'ge': 1, 'lg': 1, 'q': 1, 'hm': 1
}

# Target number of samples per species
target_samples = 200

# Function to augment data for underrepresented species
def augment_underrepresented_species():
    # Loop over each species and its count
    for species, count in species_counts.items():
        if count < target_samples:
            # Calculate how many new samples are needed
            samples_needed = target_samples - count

            # Select audio files for this species from the directory
            species_files = [f for f in os.listdir(path_audio) if f.endswith(f'{species}.wav')]

            # For each file, apply augmentations until the desired number of samples is reached
            for file in species_files:
                data, sr = librosa.load(os.path.join(path_audio, file), sr=16000)

                for i in range(samples_needed):
                    # Apply augmentations
                    noise_data = add_noise(data)
                    shifted_data = random_shift(data)
                    volume_scaled_data = volume_scaling(data)
                    time_stretched_data = time_stretching(data, rate=1.5)
                    
                    # List of augmentations
                    augmented_versions = [noise_data, shifted_data, volume_scaled_data, time_stretched_data]

                    # Save each augmented file
                    for aug in augmented_versions:
                        if samples_needed <= 0:
                            break
                        filename = f'{file.split(".")[0]}_aug_{i}_{species}.wav'
                        audio_augmentation(filename, aug)
                        samples_needed -= 1
                        


# Path to your audio files
path_audio = r'D:\Professional\Projects\Biodiversity\final\analysis_task\Data\External\material_Bird Fly monitoring and analyse\material_Bird Fly monitoring and analyse\2n_data material\Audiodateien'

# Function to add noise to the audio data
def add_noise(data):
    noise = np.random.normal(0, 0.1, len(data))  # Gaussian noise
    audio_noisy = data + noise
    return audio_noisy

# Function to shift the pitch of the audio
def pitch_shifting(data):
    sr = 16000
    bins_per_octave = 12
    pitch_pm = 2
    pitch_change = pitch_pm * 2 * (np.random.uniform())   
    data = librosa.effects.pitch_shift(data.astype('float64'), sr, n_steps=pitch_change, 
                                          bins_per_octave=bins_per_octave)
    return data  # Return the augmented data

# Function to randomly shift the audio
def random_shift(data):
    timeshift_fac = 0.2 * 2 * (np.random.uniform() - 0.5)  # Up to 20% of length
    start = int(data.shape[0] * timeshift_fac)
    if start > 0:
        data = np.pad(data, (start, 0), mode='constant')[0:data.shape[0]]
    else:
        data = np.pad(data, (0, -start), mode='constant')[0:data.shape[0]]
    return data

# Function to scale the volume of the audio
def volume_scaling(data):
    dyn_change = np.random.uniform(low=1.5, high=2.5)
    data = data * dyn_change
    return data

# Function to stretch the audio over time
def time_stretching(data, rate=1.5):
    # Use librosa's time_stretch function directly on data
    stretched = librosa.effects.time_stretch(data.astype('float32'), rate  = rate)
    
    # Ensure output length matches input length
    if len(stretched) > len(data):
        stretched = stretched[:len(data)]
    else:
        stretched = np.pad(stretched, (0, max(0, len(data) - len(stretched))), "constant")
    
    return stretched

# Function to save augmented audio
def audio_augmentation(file, aug):
    directory = 'ESC-50-augmented-data/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    sf.write(os.path.join(directory, file), aug, 16000, 'PCM_24')

# Function to perform data augmentation
def data_aug():
    path_files = np.random.choice(os.listdir(path_audio), size=(2000,), replace=False)
    
    for k, files in zip(range(len(path_files)), path_files):
        if files[0] != "5":  # Condition to filter certain files
            data_, fs = librosa.load(os.path.join(path_audio, files), sr=16000)
            noise_data = add_noise(data_)
            random_shift_data = random_shift(data_)
            volume_scale_data = volume_scaling(data_)
            time_stretching_data = time_stretching(data_, rate=1.5)

            # List of augmented data
            aug = [noise_data, time_stretching_data, random_shift_data, volume_scale_data]
            for j in range(len(aug)):
                filename = (files[0:2] + 'generated' + '-' + str(j) + '-' + str(k) + '-' + files[2:])
                audio_augmentation(filename, aug[j])

# Run the augmentation
data_aug()


# Run the augmentation for underrepresented species
augment_underrepresented_species()
