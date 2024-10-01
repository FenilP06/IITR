import streamlit as st
from PIL import Image
import pytesseract

def extract_text_from_image(image, lang='hin+eng'): 
    try:
        image_pil = Image.open(image)
        text = pytesseract.image_to_string(image_pil, lang=lang) 
        return text
    except pytesseract.pytesseract.TesseractNotFoundError:
        return "Tesseract not found. Please check the installation."
    except Exception as e:
        return f"An error occurred: {str(e)}"

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
    st.set_page_config(
        page_title="OCR Text Extraction Tool", 
        page_icon="./logo.png", 
        layout="wide"
    )
    logo = "./logo.png" 
    st.image(logo, use_column_width=True) 
    st.title("Welcome to Fenil's OCR Text Extraction Tool")
    st.write("Upload an image containing text, and I will extract the text for you. You can search for specific keywords within the extracted text.")
    
    uploaded_file = st.file_uploader("Choose an image to upload", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        extracted_text = extract_text_from_image(uploaded_file, lang='hin+eng')
        st.write("### Extracted Text:")
        st.write(extracted_text)

        keyword = st.text_input("🔍 Enter keyword(s) to search (use spaces for multiple words):")
        if keyword:
            search_result = search_keyword(extracted_text, keyword)
            st.write("### Search Result:")
            st.markdown(search_result, unsafe_allow_html=True)
            st.write("### Thank you !")

if __name__ == "__main__":
    main()
