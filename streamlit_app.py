import streamlit as st
import base64
import replicate
import os

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
                    "prompt": prompt,
                    "prompt_upsampling": False,
                    "safety_tolerance": 2,
                    "seed": 32
                }
                )
                # 
                image_url = "https://example.com/path/to/image.jpg"  # replace with your actual URL

            with st.expander("Input Image"):
                st.image(uploaded_file, caption="Input Image", use_column_width=True)                
            
            # Create an expander
            with st.expander("Image Result"):
                # Display the image from the URL
                st.image(image_url, caption="Generated Image", use_column_width=True)
        else:
            st.info("No image attached.")
            
with st.expander('Playground Outputs'):
    st.write('yet to work')