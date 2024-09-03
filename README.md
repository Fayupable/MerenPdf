# MerenPdf
PDF Processing Script using PyPDF2

## Description
MerenPdf is a Python-based tool for processing PDF files using the PyPDF2 library. It provides functionality for manipulating PDF documents, including merging multiple PDFs, splitting PDFs into separate pages, and extracting text content from PDF files.

## Setup

### Create a virtual environment

bash
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


### Install dependencies
bash
pip install PyPDF2



## Usage
To use MerenPdf, run the script with the appropriate command-line arguments:




Examples:
- Merge PDFs: `python meren_pdf.py merge input1.pdf input2.pdf output.pdf`
- Split PDF: `python meren_pdf.py split input.pdf output_prefix`
- Extract text: `python meren_pdf.py extract input.pdf output.txt`

## Features
- Merge multiple PDF files into a single document
- Split a PDF into individual pages
- Extract text content from PDF files
- [Add any additional features your script provides]

## Contributing
Contributions to MerenPdf are welcome! Please feel free to submit a Pull Request.

