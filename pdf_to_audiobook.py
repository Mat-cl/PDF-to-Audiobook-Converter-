"""
PDF to Audiobook Converter
==========================

This script reads a PDF file, translates its content into a specified language, and converts it into an audiobook format with separate MP3 files for each chapter.

Usage:
- Ensure you have the required libraries installed: PyPDF2, deep-translator, pyttsx3, pywin32.
- Place your PDF file in the specified path.
- Run the script.

The generated MP3 files will be saved in the specified output directory.
"""

import PyPDF2
from deep_translator import GoogleTranslator
import pyttsx3
import os

# Change working directory for output files
output_directory = 'C:\\Users\\matmr\\Documents\\Audiobooks'
os.makedirs(output_directory, exist_ok=True)  # Create directory if it doesn't exist
os.chdir(output_directory)

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

def read_pdf(file_path, start_page=0, end_page=None):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""
        end_page = end_page or num_pages

        for page_num in range(start_page, end_page):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    return text

def split_into_chapters(text, keyword='Chapter'):
    chapters = text.split(keyword)
    chapters = [keyword + chapter for chapter in chapters if chapter.strip() != ""]
    return chapters

def translate_text(text, dest_lang='es'):
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translated
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def text_to_audio(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

def pdf_to_audiobook_by_chapters(pdf_file, dest_lang='es'):
    # Read the first page
    text = read_pdf(pdf_file, start_page=0, end_page=1)
    
    # Read from page 32 onwards
    text += read_pdf(pdf_file, start_page=31)
    
    # Read the index between pages 10 and 24
    index_text = read_pdf(pdf_file, start_page=10, end_page=24)
    
    # Split the text into chapters using the index as a guide
    chapters = split_into_chapters(text, keyword='Chapter')
    
    for i, chapter in enumerate(chapters):
        translated_text = translate_text(chapter, dest_lang)
        audio_file = f'audiobook_chapter_{i+1}.mp3'
        text_to_audio(translated_text, audio_file)
        print(f'Chapter {i+1} audiobook saved as {audio_file}')

# Example usage
pdf_file_path = 'C:\\Users\\matmr\\Downloads\\Technical Analysis.pdf'  # Ensure this path is correct
pdf_to_audiobook_by_chapters(pdf_file_path, dest_lang='es')

