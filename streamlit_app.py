import streamlit as st
import base64
import replicate
import os
from PIL import Image


# Access the API token from Streamlit Cloud secrets
api_token = st.secrets["REPLICATE_API_TOKEN"]
api = replicate.Client(api_token=api_token)


# Helper function to convert an image to a data URL
def image_to_data_url(image):
    img_str = base64.b64encode(image.read()).decode()  # directly encode the file's bytes
    return f"data:image/png;base64,{img_str}"

st.title('Vizlit x Black Forest Labs -> Image Background Generator using GenAI techniques (FLUX)')

st.info('This is a POC to test how flux 1.1-pro model works good with background variotions with respective to prompt settings')

with st.expander("**POC - Customized Background Generation**"):
    # Predefined prompts
    predefined_prompts = [
        "Dimly lit, moody environment with deep shadows and a hint of fog. Rich colors create an atmosphere of mystery and intrigue, perfect for dramatic product photography.",
        "Elegant studio backdrop for product photography. Soft gradient lighting, minimalist design, neutral tones with subtle texture."
    ]

    # Radio buttons for predefined prompts
    selected_predefined_prompt = st.radio(
        "Choose a predefined prompt (or type your own below):",
        options=["Use my own prompt"] + predefined_prompts
    )

    # Text input for custom prompt
    custom_prompt = st.text_input("Or type your own prompt:", placeholder="Describe the background you want to generate...")

    # File uploader for attaching images
    uploaded_file = st.file_uploader("Attach an image (optional):", type=["jpg", "jpeg", "png"])

    # Action button
    if st.button("Generate Background"):
        # Determine the prompt to use
        if selected_predefined_prompt != "Use my own prompt":
            prompt = selected_predefined_prompt
        elif custom_prompt:
            prompt = custom_prompt
        else:
            st.error("Please select or type a prompt before generating.")
            st.stop()

        # Display selected options
        st.success(f"Background generation initiated with the prompt: {prompt}")
        if uploaded_file is not None:
            # st.image(uploaded_file, caption="Attached Image", use_column_width=True)
            image_data_url = image_to_data_url(uploaded_file)
            if image_to_data_url:
                output = api.run(
                "black-forest-labs/flux-1.1-pro",
                input={
                    "aspect_ratio": "1:1",
                    "image_prompt": image_data_url,
                    "output_quality": 100,
                    "output_format": "png",
                    "prompt": prompt,
                    "prompt_upsampling": False,
                    "safety_tolerance": 2,
                    "seed": 32
                }
                )
                
                st.info("**Input Image**")
                st.image(uploaded_file, caption="Input Image", use_column_width=True)
                
                # Section for Generated Image
                st.info("**Generated Image**")
                st.image(output.url, caption="Generated Image", use_column_width=True)
        else:
            st.info("No image attached.")

st.info('To explore some prediction results from the flux-1.1-pro model, check out the expanders below.')            

with st.expander('Playground Outputs - Iphone'):
    image_path = 'images/iphone.jpg'

    # Using a with block to open and display the image
    st.subheader("Feeded Image")  # Subheading above the image
    with Image.open(image_path) as image:
        st.image(image, use_column_width=True)
    
    st.subheader("Generated Image")  # Subheading above the generated image
    st.image("https://replicate.delivery/czjl/oZlSUHd9RxovC53u4xXIVtNlzbpCHDWzf4rX3J5f3HsqRewnA/tmpwumvktqu.jpg", use_column_width=True)
    
with st.expander('Playground Outputs - Drone'):
    image_path = 'images/drone.jpg'

    # Using a with block to open and display the image
    st.subheader("Feeded Image")  # Subheading above the image
    with Image.open(image_path) as image:
        st.image(image, use_column_width=True)
    
    st.subheader("Generated Image")  # Subheading above the generated image
    st.image("https://replicate.delivery/czjl/xgvAN3RWv6LiGpMakkYvsUYzC0e2iXj2ff0W8rv1epdUm4hPB/tmpjt531xlc.jpg", use_column_width=True)
    
with st.expander('Playground Outputs - AMEX Credit Card'):
    image_path = 'images/amex.jpg'

    # Using a with block to open and display the image
    st.subheader("Feeded Image")  # Subheading above the image
    with Image.open(image_path) as image:
        st.image(image, use_column_width=True)
    
    st.subheader("Generated Image")  # Subheading above the generated image
    st.image("https://replicate.delivery/czjl/mpyQdjIQTdq5FB2Qhev5ak0yr2yK74xnE56IZTXC59YgEP8JA/tmpjzzm6u0k.jpg", use_column_width=True)
    
with st.expander('Playground Outputs - Logitech Mouse'):
    image_path = 'images/mouse.jpg'

    # Using a with block to open and display the image
    st.subheader("Feeded Image")  # Subheading above the image
    with Image.open(image_path) as image:
        st.image(image, use_column_width=True)
    
    st.subheader("Generated Image")  # Subheading above the generated image
    st.image("https://replicate.com/p/c2wkpeev1xrge0ckm3cs2y47xm", use_column_width=True)
    
with st.expander('Playground Outputs - Apple MacBook'):
    image_path = 'images/macbook.jpg'

    # Using a with block to open and display the image
    st.subheader("Feeded Image")  # Subheading above the image
    with Image.open(image_path) as image:
        st.image(image, use_column_width=True)
    
    st.subheader("Generated Image")  # Subheading above the generated image
    st.image("https://replicate.delivery/czjl/bEalnf2QHiSjUase1fzgmOd0LwNRrOZTeAyu69kYefPfBGP8JA/tmp3s30ep5u.jpg", use_column_width=True)