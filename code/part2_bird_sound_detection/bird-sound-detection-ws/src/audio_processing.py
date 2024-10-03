import librosa
import numpy as np
from scipy import signal
import noisereduce as nr  # library for noise reduction
from scipy import signal
from scipy.io import wavfile

def load_audio(file_path, sample_rate=48000):
    """Load and preprocess the audio file."""
    # Load the audio file
    audio, sr = librosa.load(file_path, sr=sample_rate)
    return audio, sr

def apply_noise_reduction(audio, sr):
    # High-pass filter to remove noise
    sos = signal.butter(10, 300, 'hp', fs=sr, output='sos')
    filtered_audio = signal.sosfilt(sos, audio)

    # Apply a bandpass filter to isolate bird sound frequencies (300 Hz to 8 kHz)
    sos_bandpass = signal.butter(10, [300, 8000], 'bandpass', fs=sr, output='sos')
    filtered_audio = signal.sosfilt(sos_bandpass, filtered_audio)

    # Apply noise reduction
    reduced_noise_audio = nr.reduce_noise(y=filtered_audio, sr=sr)

    # Return the preprocessed audio and sampling rate
    return reduced_noise_audio, sr

def save_audio(file_path, audio, sr):
    """Save the processed audio to a file for analysis."""
    wavfile.write(file_path, sr, (audio * 32767).astype(np.int16))  # Convert to int16 for WAV format
