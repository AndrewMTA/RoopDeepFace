import os
import subprocess
import shutil

# Clone the repository and change the working directory
subprocess.run(["git", "clone", "https://github.com/s0md3v/roop"])
os.chdir("roop")

# Checkout the specific commit (Optional)
# subprocess.run(["git", "checkout", "b41149e4a22a55198447a7accb671021b47d8bad"])

# Install required packages
subprocess.run(["pip", "install", "onnxruntime-gpu"])
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Download the ONNX model
os.makedirs("models", exist_ok=True)
os.chdir("models")
subprocess.run(["wget", "https://huggingface.co/MonsterMMORPG/SECourses/resolve/main/inswapper_128.onnx"])

# Move back to the root directory
os.chdir("../")

# Run the face swapping and face enhancing
# Run the face swapping and face enhancing
subprocess.run([
    "python", "run.py",
    "-s", "face2.jpeg",
    "-t", "brad.mp4",
    "-o", "face_changed_video.mp4",
    "--keep-frames",
    "--keep-fps",
    "--video-quality", "7",
    "--execution-provider", "cuda",
])

# The generated video "face_changed_video.mp4" will remain in the same directory where the script is executed.
