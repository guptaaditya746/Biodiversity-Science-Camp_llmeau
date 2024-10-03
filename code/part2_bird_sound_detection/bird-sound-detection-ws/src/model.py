import tensorflow as tf
import numpy as np
from pathlib import Path

class BirdSoundModel:
    def __init__(self, model_path):
        # Load the TensorFlow Lite model
        self.interpreter = tf.lite.Interpreter(model_path=str(model_path))
        self.interpreter.allocate_tensors()

        # Get input and output tensor details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        # Load bird species names (a list of species)
        self.bird_species = self.load_bird_species()

    def load_bird_species(self):
        # Path to the labels file (inside the models folder)
        labels_file_path = Path(__file__).resolve().parent.parent / "models" / "BirdNET_GLOBAL_6K_V2.4_Labels.txt"

        # Load bird species names from the file
        with open(labels_file_path, "r") as f:
            return [line.strip() for line in f]

    def predict(self, audio_chunk):
        """Run prediction on a single audio chunk."""
        # Prepare the input tensor
        input_data = audio_chunk.astype('float32')
        input_data = input_data.reshape(1, len(audio_chunk))

        # Set input tensor
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)

        # Invoke the interpreter
        self.interpreter.invoke()

        # Get output tensor (prediction)
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])

        # Find the bird species with the highest probability
        bird_idx = np.argmax(output_data)
        bird_name = self.bird_species[bird_idx]
        prediction_score = output_data[0][bird_idx]

        return bird_name, prediction_score

    def detect_bird_sound(self, predictions, threshold=0.01):
        """Check if bird sound is detected based on predictions."""
        # Check if any prediction score exceeds the threshold
        if np.any(predictions > threshold):
            return 1  # Bird sound detected
        return 0  # No bird sound detected

