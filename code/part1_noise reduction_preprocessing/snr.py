import numpy as np
import soundfile as sf

# Function to calculate signal-to-noise ratio (SNR)
def calculate_snr(clean_signal, noisy_signal):
    # Compute power of the signal
    signal_power = np.mean(clean_signal ** 2)
    # Compute power of the noise (difference between noisy and clean signal)
    noise_power = np.mean((clean_signal - noisy_signal) ** 2)
    # SNR in dB
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Function to load the audio file
def load_audio(file_path):
    audio, sr = sf.read(file_path)
    return audio, sr

# Example usage:
# Load the original audio and noisy audio
clean_audio_path = "path_to_clean_audio.wav"  # Replace with the actual path
noisy_audio_path = "path_to_noisy_audio.wav"  # Replace with the actual path

clean_audio, sr_clean = load_audio(clean_audio_path)
noisy_audio, sr_noisy = load_audio(noisy_audio_path)

# Ensure the sampling rates are the same
assert sr_clean == sr_noisy, "Sampling rates of clean and noisy signals must match."

# Calculate SNR before noise filtering
snr_before = calculate_snr(clean_audio, noisy_audio)
print(f"SNR before filtering: {snr_before} dB")

# Process the noisy audio (apply your noise filter or processing method)
filtered_audio = noise_filter(noisy_audio, sr_noisy)  # Replace this with your actual noise filtering function

# Calculate SNR after noise filtering
snr_after = calculate_snr(clean_audio, filtered_audio)
print(f"SNR after filtering: {snr_after} dB")