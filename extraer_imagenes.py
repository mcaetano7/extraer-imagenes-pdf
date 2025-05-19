import os
import fitz  # PyMuPDF
from pathlib import Path

# Ruta a la carpeta de los PDFs 
desktop_path = Path(r"C:\Users\Estudiante UCU\OneDrive - Universidad Católica del Uruguay\Escritorio\lyss")
output_base = desktop_path / "ImagenesExtraidas"

# Crear carpeta de salida si no existe
output_base.mkdir(exist_ok=True)

# Recorrer todos los PDF de la carpeta
for pdf_file in desktop_path.glob("*.pdf"):
    pdf_name = pdf_file.stem
    output_dir = output_base / pdf_name
    output_dir.mkdir(exist_ok=True)

    doc = fitz.open(pdf_file)
    image_count = 0

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]  # png o jpeg
            image_filename = f"pagina{page_index+1}_img{img_index+1}.{image_ext}"

            with open(output_dir / image_filename, "wb") as f:
                f.write(image_bytes)

            image_count += 1

    print(f"{pdf_name}: {image_count} imagen(es) extraída(s)")

print("Extracción completada.")
