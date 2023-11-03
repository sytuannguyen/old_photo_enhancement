import os
import streamlit as st
import subprocess

# Streamlit UI
st.title("GFPGAN Environment Setup")

# Clone GFPGAN and enter the GFPGAN folder
if st.button("Clone GFPGAN Repository"):
    st.text("Cloning GFPGAN repository...")
    subprocess.run(["git", "clone", "https://github.com/TencentARC/GFPGAN.git"])
    os.chdir("GFPGAN")
    st.success("GFPGAN repository cloned successfully!")
    st.write("Please proceed with the environment setup.")

# Set up the environment
if st.button("Set Up Environment"):
    st.text("Setting up the environment...")
    subprocess.run(["pip", "install", "basicsr"])
    subprocess.run(["pip", "install", "facexlib"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["python", "setup.py", "develop"])
    subprocess.run(["pip", "install", "realesrgan"])
    st.success("Environment set up successfully!")

# Download pre-trained model
if st.button("Download Pre-trained Model"):
    st.text("Downloading pre-trained model...")
    model_url = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
    subprocess.run(["wget", model_url, "-P", "experiments/pretrained_models"])
    st.success("Pre-trained model downloaded successfully!")

# Display success message
if os.path.exists("experiments/pretrained_models/GFPGANv1.3.pth"):
    st.write("Pre-trained model is available and ready to use.")
