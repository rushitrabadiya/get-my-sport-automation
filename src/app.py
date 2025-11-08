import os
import streamlit as st
from backend import generate_caption_and_prompt, generate_image, save_to_excel

# Streamlit Config
st.set_page_config(page_title="AI Caption & Image Generator",
                   page_icon="✨", layout="centered")

OUTPUT_DIR = "output/images"
EXCEL_FILE = "captions.xlsx"
os.makedirs(OUTPUT_DIR, exist_ok=True)


st.title("🧠 AI Caption & Image Generator")
st.markdown(
    "<center>Generate <b>Instagram-ready captions, hashtags, and AI images</b> instantly.</center><br>", unsafe_allow_html=True)

content = st.text_area("✍️ Enter your post idea or topic:", height=150)

if st.button("🚀 Generate", width='stretch'):
    if not content.strip():
        st.warning("Please enter some content first.")
        st.stop()

    with st.spinner("Generating caption and image prompt..."):
        try:
            caption, image_prompt, hashtags = generate_caption_and_prompt(
                content)
        except Exception as e:
            st.error(str(e))
            st.stop()

    st.success("✅ Content generated successfully!")

    # Display Caption
    st.subheader("✨ Generated Caption")
    st.write(caption)
    # st.code(caption, language=None)
    # st.download_button("📋 Copy Caption", caption,
    #                    file_name="caption.txt", width="stretch")

    # Display Hashtags
    st.subheader("🏷️ Hashtags")
    hashtags_text = " ".join(hashtags)
    st.write(hashtags_text)
    # st.download_button("📋 Copy Hashtags", hashtags_text,
    #                    file_name="hashtags.txt", width="stretch")

    # # Display Image Prompt
    # st.subheader("🎨 Image Prompt")
    # st.text(image_prompt)
    # st.download_button("📋 Copy Image Prompt", image_prompt,
    #                    file_name="image_prompt.txt")

    # Generate Image
    st.subheader("🖼️ Generated Image")
    image_index = len(os.listdir(OUTPUT_DIR)) + 1

    with st.spinner("Creating AI image..."):
        try:
            image_path = generate_image(image_prompt, image_index)
        except Exception as e:
            st.error(str(e))
            st.stop()

    st.image(image_path, width='stretch')
    # st.image(image_path, caption=image_prompt, width='stretch')

    # Download Image
    with open(image_path, "rb") as f:
        img_bytes = f.read()

    # Combined Download
    combined_text = f"Caption:\n{caption}\n\nHashtags:\n{hashtags_text}\n\nImage Prompt:\n{image_prompt}"
    st.download_button(
        "📦 Download All (Text Only)",
        combined_text,
        file_name="post_content.txt",
        width="stretch"
    )

    st.download_button(
        label="📥 Download Image",
        data=img_bytes,
        file_name=os.path.basename(image_path),
        mime="image/png",
        width="stretch"
    )

    # Save Data
    save_to_excel(caption, hashtags, image_path)
    # st.info(f"✅ Data saved to `{EXCEL_FILE}`")


else:
    st.info("👆 Enter your post idea and click **Generate** to begin!")
