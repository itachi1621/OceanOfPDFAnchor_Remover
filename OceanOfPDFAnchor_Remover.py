import os
import zipfile # .epub is basically a wrapper and can unzipped
from bs4 import BeautifulSoup

def process_epub(input_file, output_file):
    try:
        with zipfile.ZipFile(input_file, 'r') as zin:
            with zipfile.ZipFile(output_file, 'w') as zout:
                for item in zin.infolist():
                    buffer = zin.read(item.filename)
                    if item.filename.endswith(('.html', '.xhtml', '.xml')):
                        # Use parser handling
                        if item.filename.endswith('.html'):
                            soup = BeautifulSoup(buffer, 'lxml')
                        else:
                            soup = BeautifulSoup(buffer, 'xml')

                        elements = soup.find_all("a", href="https://oceanofpdf.com") #what to search for and remove
                        for element in elements:
                            element.decompose()
                        buffer = str(soup).encode()
                    zout.writestr(item, buffer)
        return True
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        return False

# Directories for input and output files
input_folder = 'input'  # Replace with your input folder path
output_folder = 'output'  # Replace with your output folder path

# Ensure output folder exists
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Process each EPUB file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.epub'):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        if process_epub(input_path, output_path):
            os.remove(input_path)
            print(f"Processed and removed original {file_name}")
        else:
            print(f"Failed to process {file_name}")

print("All EPUB files have been processed.")
