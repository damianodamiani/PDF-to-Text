import PyPDF2
import os

# Directory where the PDF files are located
pdf_directory = '/path/to/pdf/files'  # Replace with the actual directory path

# Output directory for the combined text file
output_directory = '/path/to/output/directory'  # Replace with the desired output directory path

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# List PDF files in the specified directory
pdf_files = [pdf_file_name for pdf_file_name in os.listdir(pdf_directory) if pdf_file_name.endswith('.pdf')]

# Initialize an empty string to store the combined text
combined_text = ""

for pdf_file_name in pdf_files:
    pdf_file_path = os.path.join(pdf_directory, pdf_file_name)
    pdf_reader = PyPDF2.PdfReader(pdf_file_path)

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        combined_text += page_text

# Create the output text file path
output_text_file_path = os.path.join(output_directory, 'combined_text.txt') # Rename the output text file as desired

# Write the combined text to the output text file
with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(combined_text)

print(f"Text extracted from PDF files in {pdf_directory} and saved to {output_text_file_path}")
