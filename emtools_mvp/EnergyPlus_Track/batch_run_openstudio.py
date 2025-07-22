# emtools_mvp/EnergyPlus_Track/batch_run_openstudio.py

import argparse
import os
import subprocess


def is_valid_model_file(filename):
    return filename.endswith(".osm") or filename.endswith(".json")

def run_openstudio_simulation(input_path, output_dir):
    job_name = os.path.splitext(os.path.basename(input_path))[0]
    job_output = os.path.join(output_dir, job_name)
    os.makedirs(job_output, exist_ok=True)

    # Dummy simulation placeholder (replace with actual OpenStudio CLI call)
    result_file = os.path.join(job_output, "eplusout.sql")
    with open(result_file, "w") as f:
        f.write(f"-- Simulated result for {job_name}\n")

    print(f"[SIMULATED] {input_path} -> {result_file}")


def main():
    parser = argparse.ArgumentParser(description="Batch run OpenStudio models")
    parser.add_argument("--input-folder", required=True, help="Folder with .osm or .json models")
    parser.add_argument("--output-folder", required=True, help="Folder to store results")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    if not os.path.isdir(input_folder):
        raise NotADirectoryError(f"Input folder not found: {input_folder}")
    os.makedirs(output_folder, exist_ok=True)

    model_files = [f for f in os.listdir(input_folder) if is_valid_model_file(f)]

    if not model_files:
        print("[INFO] No valid model files found.")
        return

    print(f"[INFO] Found {len(model_files)} model(s) to process.")
    for model_file in model_files:
        model_path = os.path.join(input_folder, model_file)
        run_openstudio_simulation(model_path, output_folder)

    print("[DONE] Batch simulation complete.")


if __name__ == "__main__":
    main()
