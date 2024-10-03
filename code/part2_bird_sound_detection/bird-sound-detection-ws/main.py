from pathlib import Path
from src.birdnet_detection import detect_bird_sounds_in_file, print_bird_sound_timestamps

# Define file paths
SCRIPT_DIR = Path(__file__).resolve().parent
TEST_FILE_PATH = SCRIPT_DIR / "data" / "file.wav"
MODEL_FILE_PATH = SCRIPT_DIR / "models" / "BirdNET_GLOBAL_6K_V2.4_Model_FP32.tflite"

# "D:\Professional\Projects\Biodiversity\final\bird-sound-detection-ws\data\2459626.341944_Tautenburg___1074-5122kHz___10-19s___ch.wav"
def main():
    # Detect bird sounds in the audio file
    bird_sound_timestamps = detect_bird_sounds_in_file(TEST_FILE_PATH, MODEL_FILE_PATH, chunk_size=3, threshold=0.01)
    
    # Print the detected bird sound time ranges
    print_bird_sound_timestamps(bird_sound_timestamps)

if __name__ == "__main__":
    main()
