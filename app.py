import streamlit as st
import os
import cv2
import shutil
import requests
from tqdm import tqdm

# Function to download files using requests
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=8192)):
                if chunk:
                    f.write(chunk)

# Streamlit app
st.title("GFPGAN Image Restoration App")
st.write("Upload your images and click 'Process Images' to restore them using GFPGAN.")

if st.button("Process Images"):
    # Clone GFPGAN and enter the GFPGAN folder
    os.system("git clone https://github.com/TencentARC/GFPGAN.git")
    os.chdir("GFPGAN")
    st.write(os.listdir('.'))
             
    # Set up the environment (install dependencies)
    os.system("pip install -r requirements.txt")
    os.system("python setup.py develop")
    os.system("pip install realesrgan")

    # Download the pre-trained model
    model_url = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth"
    model_path = "experiments/pretrained_models/GFPGANv1.3.pth"
    download_file(model_url, model_path)

    # Upload images
    uploaded_files = st.file_uploader("Upload your images", type=["jpg", "png"], accept_multiple_files=True)
    upload_folder = "inputs/upload"

    if uploaded_files:
        if os.path.exists(upload_folder):
            shutil.rmtree(upload_folder)
        os.mkdir(upload_folder)

        for uploaded_file in uploaded_files:
            file_path = os.path.join(upload_folder, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

        # Process images with GFPGAN
        os.system("python inference_gfpgan.py -i inputs/upload -o results -v 1.3 -s 2 --bg_upsampler realesrgan")

        # Display processed images
        result_folder = "results/restored_imgs"
        output_files = os.listdir(result_folder)

        for output_file in output_files:
            img_path = os.path.join(result_folder, output_file)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            st.image(img, caption=output_file, use_column_width=True)

        # Download processed images
        st.markdown("---")
        st.write("Download processed images")
        st.download_button(
            label="Download Results",
            data="results",
            file_name="GFPGAN_Results.zip",
        )
    os.chdir("..")
