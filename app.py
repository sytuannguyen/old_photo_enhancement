import os
import streamlit as st
import subprocess

# Streamlit UI
st.title("GFPGAN Environment Setup")

# Clone GFPGAN and enter the GFPGAN folder
if st.button("Clone GFPGAN Repository"):
    st.text("Cloning GFPGAN repository...")
    subprocess.run(["git", "clone", "https://github.com/TencentARC/GFPGAN.git"])
    st.success("GFPGAN repository cloned successfully!")
    st.write("Please proceed with the environment setup.")

# Set up the environment
if st.button("Set Up Environment"):
    st.text("Setting up the environment...")
    subprocess.run(["pip", "install", "GFPGAN/basicsr"])
    subprocess.run(["pip", "install", "GFPGAN/facexlib"])
    subprocess.run(["pip", "install", "-r", "GFPGAN/requirements.txt"])
    subprocess.run(["python", "GFPGAN/setup.py", "GFPGAN/develop"])
    subprocess.run(["pip", "install", "GFPGAN/realesrgan"])
    st.success("Environment set up successfully!")

# Function to download pre-trained model
def download_pretrained_model():
    st.text("Downloading pre-trained model...")
    model_url = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
    save_path = os.path.join("GFPGAN/experiments", "pretrained_models", "GFPGANv1.3.pth")
    try:
        response = requests.get(model_url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        st.success("Pre-trained model downloaded successfully!")
    except Exception as e:
        st.error(f"Error: {e}")
        raise

# Streamlit UI
st.title("Download Pre-trained Model")
if st.button("Download Pre-trained Model"):
    download_pretrained_model()

# Display success message
if os.path.exists("experiments/pretrained_models/GFPGANv1.3.pth"):
    st.write("Pre-trained model is available and ready to use.")

