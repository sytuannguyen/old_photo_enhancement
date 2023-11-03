import streamlit as st
import os
from PIL import Image

# Streamlit app
st.title("GFPGAN Image Restoration App")

# Process images with GFPGAN
os.system("git clone https://github.com/TencentARC/GFPGAN.git")
os.chdir("GFPGAN")
os.system("pip install -r requirements.txt")
os.system("python setup.py develop")
os.system("pip install realesrgan")
os.system("python inference_gfpgan.py -i ../inputs/upload -o ../results -v 1.3 -s 2 --bg_upsampler realesrgan")
os.chdir("..")

st.write("Upload your images and click 'Process Images' to restore them using GFPGAN.")

if st.button("Process Images"):
    os.chdir("GFPGAN")
    
    # Upload images
    uploaded_files = st.file_uploader("Upload your images", type=["jpg", "png"], accept_multiple_files=True)
    upload_folder = "inputs/upload"

    if uploaded_files:
        os.makedirs(upload_folder, exist_ok=True)

        # Save uploaded images to upload_folder
        for uploaded_file in uploaded_files:
            with open(os.path.join(upload_folder, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.read())

        
        
        # Display processed images
        result_folder = "../results/restored_imgs"
        output_files = os.listdir(result_folder)

        for output_file in output_files:
            img_path = os.path.join(result_folder, output_file)
            img = Image.open(img_path)
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
