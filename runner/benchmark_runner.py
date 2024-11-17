import os
import subprocess
import time

def run_minisat_on_files(input_folder_path, output_folder_path):
    # Path to minisat executable
    minisat_path = r"C:\Users\Marius\Desktop\minisat\build\Debug\minisat.exe"
    
    # Ensure the output directory exists
    os.makedirs(output_folder_path, exist_ok=True)

    # Get a list of all files in the directory
    benchmark_files = [f for f in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, f))]

    # Iterate over each file and run minisat
    for filename in benchmark_files:
        file_path = os.path.join(input_folder_path, filename)
        output_file = os.path.join(output_folder_path, f"{os.path.splitext(filename)[0]}.txt")

        print(f"Running minisat on {filename}...")

        # Start the timer
        start_time = time.time()

        # Run minisat command with absolute path and 3-hour timeout
        try:
            with open(output_file, 'w') as f:
                result = subprocess.run(
                    [minisat_path, file_path], 
                    stdout=f, 
                    stderr=subprocess.STDOUT, 
                    text=True, 
                    timeout= 3 * 3600
                )
            end_time = time.time()
            time_taken = end_time - start_time

            print(f"Completed {filename} in {time_taken:.2f} seconds, output saved to {output_file}")

        except subprocess.TimeoutExpired:
            # If a timeout occurs, log a message in the output file
            with open(output_file, 'a') as f:
                f.write("\nExecution timed out after 3 hours.\n")
            print(f"Timeout expired for {filename}, partial output saved to {output_file}")

# Folder containing the benchmark files
input_folder_path = r"C:\Users\Marius\Desktop\tseitin-formulas"  # Replace with the actual path to your benchmark folder

# Output folder for results on Desktop
output_folder_path = r"C:\Users\Marius\Desktop\minisat_output"  # You can rename this folder as desired

# Run the benchmark
run_minisat_on_files(input_folder_path, output_folder_path)
