from PyPDF2 import PdfWriter, PdfReader
import PyPDF2
import os

def read_pdf(input_pdf):
    try:
        return PyPDF2.PdfReader(input_pdf)
    except FileNotFoundError:
        print(f"Error: The file '{input_pdf}' was not found.")
        return None
    except PyPDF2.errors.PdfReadError:
        print(f"Error: '{input_pdf}' is not a valid PDF file or is encrypted.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the PDF: {str(e)}")
        return None

def write_pdf(output_pdf, writer):
    try:
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)
        print(f"Successfully wrote PDF to {output_pdf}")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")

def process_pages(reader, writer, search_word, include=True):
    try:
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text().lower()

            if (search_word.lower() in text and include) or (search_word.lower() not in text and not include):
                writer.add_page(page)
                action = "Included" if include else "Deleted"
                print(f"{action} page {page_num + 1} containing '{search_word}'")
    except Exception as e:
        print(f"Error in process_pages: {str(e)}")
        raise

def search_and_delete_pages(input_pdf, output_pdf, search_word):
    reader = read_pdf(input_pdf)
    if reader:
        try:
            writer = PyPDF2.PdfWriter()
            process_pages(reader, writer, search_word, include=False)
            write_pdf(output_pdf, writer)
        except Exception as e:
            print(f"Error in search_and_delete_pages: {str(e)}")

def search_and_include_pages(input_pdf, output_pdf, search_word):
    reader = read_pdf(input_pdf)
    if reader:
        try:
            writer = PyPDF2.PdfWriter()
            process_pages(reader, writer, search_word, include=True)
            write_pdf(output_pdf, writer)
        except Exception as e:
            print(f"Error in search_and_include_pages: {str(e)}")

def main():
    input_pdf = "/Users/pc/Desktop/code/Meren pdf/Pages From giris.pdf"
    search_word = "unisex"
    output_pdf_deleted = os.path.join(os.path.dirname(input_pdf), "edited.pdf")
    output_pdf_included = os.path.join(os.path.dirname(input_pdf), "included.pdf")

    print(f"Processing input PDF: {input_pdf}")
    print(f"Searching for word: {search_word}")

    search_and_delete_pages(input_pdf, output_pdf_deleted, search_word)
    print(f"Process completed. Modified PDF saved as '{output_pdf_deleted}'")
    
    search_and_include_pages(input_pdf, output_pdf_included, search_word)
    print(f"Process completed. New PDF with included pages saved as '{output_pdf_included}'")

if __name__ == "__main__":
    main()
