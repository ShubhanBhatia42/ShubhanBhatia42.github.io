import os
import subprocess

def convert_mp4_to_mov(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp4"):
                mp4_path = os.path.join(root, file)
                mov_path = os.path.splitext(mp4_path)[0] + ".mov"
                
                # Run ffmpeg command to convert mp4 to mov
                command = [
                    "ffmpeg",
                    "-i", mp4_path,
                    "-vf", "scale=800:450",  # Set resolution to 800x450
                    "-c:v", "prores_ks",    # Use ProRes codec for MOV files
                    "-profile:v", "3",      # Set ProRes profile (default for most cases)
                    "-c:a", "aac",          # Use AAC audio codec
                    "-movflags", "+faststart",  # Optimize for web streaming
                    mov_path
                ]
                
                try:
                    print(f"Converting: {mp4_path} -> {mov_path}")
                    subprocess.run(command, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {mp4_path}: {e}")

if __name__ == "__main__":
    main_directory = input("Enter the path to the main directory: ")
    if os.path.isdir(main_directory):
        convert_mp4_to_mov(main_directory)
    else:
        print("Invalid directory path. Please provide a valid main directory.")

