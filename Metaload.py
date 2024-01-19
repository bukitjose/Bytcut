import array as arr
import random

# Set the number of iterations and the amount of metadata to generate per iteration
num_iterations = 100
metadata_size = 5 * (1024**3) // 8 // num_iterations

# Generate and load the metadata in a loop
for i in range(num_iterations):
    metadata = [random.random() for _ in range(metadata_size)] # Generate random metadata
    arr.array('d', metadata) # Force-load the metadata into memory
    print("Done!")  