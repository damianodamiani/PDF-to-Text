import PyPDF2
import os

# Directory where the PDF files are located
pdf_directory = '/path/to/pdf/files'  # Replace with the actual directory path

# Output directory for the combined text file
output_directory = '/path/to/output/directory'  # Replace with the desired output directory path

# Name of the combined text file
combined_text_file_name = 'combined_text.txt'  # Replace with the desired name of the combined text file

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize a variable to store the combined text
combined_text = ""

for root, _, files in os.walk(pdf_directory):
    for pdf_file_name in files:
        if pdf_file_name.endswith('.pdf'):
            pdf_file_path = os.path.join(root, pdf_file_name)
            pdf_reader = PyPDF2.PdfReader(pdf_file_path)

            for page_num, page in enumerate(pdf_reader.pages, start=1):
                page_text = page.extract_text()

                # Append extracted text to the combined text
                combined_text += page_text

# Create the output text file path in the specified output directory
output_text_file_path = os.path.join(output_directory, combined_text_file_name)

# Write the combined text to the output text file
with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(combined_text)

print(f"Text extracted from PDFs and saved to {output_text_file_path}")
