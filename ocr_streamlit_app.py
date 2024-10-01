import streamlit as st
from PIL import Image
import pytesseract

def extract_text_from_image(image):
    image_pil = Image.open(image)
    text = pytesseract.image_to_string(image_pil)
    return text

def search_keyword(extracted_text, keyword):
    lower_text = extracted_text.lower()
    lower_keyword = keyword.lower()
    
    keywords = lower_keyword.split()
    highlighted_text = extracted_text
    all_found = all(kw in lower_text for kw in keywords)

    if all_found:
        for kw in keywords:
            highlighted_text = highlighted_text.replace(kw, f"<span style='background-color: #ffeb3b; color: black; font-weight: bold;'>{kw}</span>")
        return f"**Keywords Found:** <br> {highlighted_text}"
    else:
        return "❌ **Keywords not found in the extracted text.**"

def main():
    st.set_page_config(page_title="OCR Text Extraction Tool", page_icon="🖼️", layout="wide")
    st.title("Welcome to Fenil OCR Text Extraction Tool")
    st.write("Upload an image containing text, and we will extract the text for you. You can then search for specific keywords within the extracted text.")
    
    uploaded_file = st.file_uploader("Choose an image to upload", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        extracted_text = extract_text_from_image(uploaded_file)
        st.write("### Extracted Text:")
        st.write(extracted_text)

        keyword = st.text_input("🔍 Enter keyword(s) to search (use spaces for multiple words):")
        if keyword:
            search_result = search_keyword(extracted_text, keyword)
            st.write("### Search Result:")
            st.markdown(search_result, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
