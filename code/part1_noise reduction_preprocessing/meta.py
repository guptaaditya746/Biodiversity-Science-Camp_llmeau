


import os
import re

# Function to parse the filename
def parse_filename(filename):
    # Use regex to extract components
    match = re.match(r'(\d+\.\d+)_(\w+)___(\d+-\d+kHz)___(\d+-\d+\.\d+s)___.*\.wav', filename)
    if match:
        timestamp = match.group(1)
        bird_name = match.group(2)
        frequency_range = match.group(3)
        duration = match.group(4)
        return {
            "timestamp": timestamp,
            "bird_name": bird_name,
            "frequency_range": frequency_range,
            "duration": duration
        }
    return None

# Directory containing .wav files
directory = "D:/Professional/Projects/Biodiversity/final/analysis_task/Data/Raw"

# List to hold parsed information
parsed_results = []

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        parsed_info = parse_filename(filename)
        if parsed_info:
            parsed_results.append(parsed_info)

# Display the results
for result in parsed_results:
    print(result)



