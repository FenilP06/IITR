# OCR Streamlit App

## Overview
This is a simple web application built with Streamlit that allows users to upload an image file for Optical Character Recognition (OCR) processing. The extracted text can then be searched using keywords, with highlighted results displayed on the same page.

## Features
- Upload an image file for OCR processing.
- Display the extracted text from the image.
- Enter keywords to search within the extracted text.
- Highlight the matching sections in the extracted text.

## Technologies Used
- **Python**: The programming language used to build the application.
- **Streamlit**: A framework for creating web applications in Python.
- **Tesseract OCR**: A library for Optical Character Recognition.
- **OpenCV**: A library for computer vision tasks.

# Live Demo

You can view and interact with the deployed version of this project on Streamlit at the following link:

[View Project on Streamlit](https://fenilocr.streamlit.app/)

## Installation

1. **Clone the Repository**:
   - Run the following command in your terminal:
     ```bash
     git clone https://github.com/FenilP06/IITR
     cd IITR
     ```

2. **Create a Virtual Environment (optional but recommended)**:
   - Run the following commands:
     ```bash
     python3 -m venv ocr_env
     On Windows use `ocr_env\Scripts\activate`
     On Linux use 'source ocr_env/bin/activate'
     ```

3. **Install Dependencies**:
   - Execute the command:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Run the Streamlit Application**:
   - Use the command:
     ```bash
     streamlit run ocr_streamlit_app.py
     ```

2. **Open the Application**:
   - After running the above command, a new tab will open in your default web browser displaying the OCR application.

3. **Upload an Image**:
   - Click on the "Browse files" button to upload an image containing text.

4. **Extract and Search**:
   - The extracted text will be displayed on the page.
   - Enter a keyword in the search box to find it in the extracted text.
   - If found, the matching sections will be highlighted.

## Screenshot of webapp :

![Screenshot from 2024-10-01 02-27-48](https://github.com/user-attachments/assets/945c61f6-d011-43d0-b206-3030cc0f0c3c)
#
![Screenshot from 2024-10-01 03-05-54](https://github.com/user-attachments/assets/1aa7e51c-3470-4c1b-a855-7f16ed1879a4)
# 
![Screenshot from 2024-10-01 03-06-19](https://github.com/user-attachments/assets/29c9c642-12a3-43d6-8560-89aef4813cce)
#
![Screenshot from 2024-10-01 03-07-19](https://github.com/user-attachments/assets/2f524ffe-ae65-4e18-8b2f-95869792bfaa)
#
