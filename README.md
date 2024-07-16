# PDF to Audiobook Converter

This script reads a PDF file, translates its content into a specified language (Spanish), and converts it into an audiobook format with separate MP3 files for each chapter. The script recognizes chapter headings, skips some pages, and handles translation errors gracefully by not translating the text if the translation fails.

## Features

- Recognizes chapter headings based on the keyword "Chapter".
- Skips specific pages (e.g., reads the first page, then skips to page 32 onwards).
- If translation to Spanish fails, the text remains in its original language.
- Creates separate MP3 files for each chapter.

## Requirements

- Python 3.6+
- PyPDF2
- deep-translator
- pyttsx3
- pywin32 (Windows only)

## Installation

Install the required libraries using pip:

```sh
pip install PyPDF2 deep-translator pyttsx3 pywin32
