import os
from docx import Document

def combine_docx_files(input_directory, output_file):
    # Buat dokumen baru untuk hasil gabungan
    combined_document = Document()
    
    # Iterasi melalui semua file di direktori input
    for filename in os.listdir(input_directory):
        if filename.endswith('.docx'):
            file_path = os.path.join(input_directory, filename)
            
            # Baca dokumen yang ada
            doc = Document(file_path)
            
            # Tambahkan konten dari dokumen yang ada ke dokumen gabungan
            for element in doc.element.body:
                combined_document.element.body.append(element)
    
    # Simpan dokumen gabungan ke file output
    combined_document.save(output_file)
    print(f"File gabungan disimpan sebagai {output_file}")

# Tentukan direktori input dan nama file output
input_directory = 'path/to/your/directory'
output_file = 'path/to/your/combined_document.docx'

# Panggil fungsi untuk menggabungkan file
combine_docx_files(input_directory, output_file)
