import PyPDF2
import os

# Directory where the PDF files are located
pdf_directory = '/path/to/pdf/files'  # Replace with the actual directory path

# Output directory for text files
output_directory = '/path/to/output/directory'  # Replace with the desired output directory path

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for root, _, files in os.walk(pdf_directory):
    for pdf_file_name in files:
        if pdf_file_name.endswith('.pdf'):
            pdf_file_path = os.path.join(root, pdf_file_name)
            pdf_reader = PyPDF2.PdfReader(pdf_file_path)
    
            # Create the output text file path by changing the extension to .txt
            relative_path = os.path.relpath(pdf_file_path, pdf_directory)
            output_text_file_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + '.txt')
    
            with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
                for page_num, page in enumerate(pdf_reader.pages, start=1):
                    page_text = page.extract_text()
            
                    # Write extracted text to the output text file
                    text_file.write(page_text)
            
            print(f"Text extracted from {pdf_file_name} and saved to {output_text_file_path}")

print(f"Text extracted and saved to individual text files in {output_directory}")
