from src.audio_processing import load_audio, save_audio
from src.model import BirdSoundModel
import numpy as np

def detect_bird_sounds_in_file(file_path, model_path, chunk_size=3, threshold=0.01):
    """Detect bird sounds in an audio file."""
    # Load and preprocess the audio
    audio, sample_rate = load_audio(file_path)

    # Save the processed (noise-reduced) audio for analysis
    processed_audio_path = "processed_audio.wav"  # Path for saving the processed audio
    save_audio(processed_audio_path, audio, sample_rate)
    print(f"Processed audio saved at: {processed_audio_path}")

    # Initialize the BirdNET model
    model = BirdSoundModel(model_path)

    # Split the audio into chunks
    total_duration = len(audio) / sample_rate
    # bird_sound_timestamps = []
    bird_sound_detections = []

    for start in np.arange(0, total_duration - chunk_size, chunk_size):
            end = start + chunk_size
            audio_chunk = audio[int(start * sample_rate):int(end * sample_rate)]
            
            # Run model prediction on the chunk
            bird_name, predictions = model.predict(audio_chunk)

            # Check if bird sound is detected above the threshold
            if predictions > threshold:
                bird_sound_detections.append((start, end, bird_name))

    return bird_sound_detections

def print_bird_sound_timestamps(detections):
    """Print detected bird sound time ranges in minutes:seconds format with bird species and serial numbers."""
    for idx, (start, end, bird_name) in enumerate(detections, 1):
        start_minutes, start_seconds = divmod(start, 60)
        end_minutes, end_seconds = divmod(end, 60)
        
        # Print with serial number, time range, and bird species name
        print(f"{idx}. Sound of ({bird_name}) bird detected from {int(start_minutes)}:{int(start_seconds):02d} to {int(end_minutes)}:{int(end_seconds):02d}")

