import sys
import os
import platform
from pathlib import Path
from pdf2image import convert_from_path

MAX_SIZE = (1024, 1024)

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
    # Windows exe içine gömülü poppler
    if platform.system() == "Windows":
        POPPLER_PATH = os.path.join(sys._MEIPASS, "poppler_bin")
    else:
        POPPLER_PATH = "/opt/homebrew/bin"
else:
    BASE_DIR = Path(__file__).parent
    POPPLER_PATH = "/opt/homebrew/bin" if platform.system() == "Darwin" else None

pdfs_dir = BASE_DIR / "pdfs"
output_dir = BASE_DIR / "output"
output_dir.mkdir(exist_ok=True)

pdf_files = list(pdfs_dir.glob("*.pdf"))
if not pdf_files:
    print("pdfs/ klasöründe PDF bulunamadı.")
else:
    for pdf_path in pdf_files:
        print(f"İşleniyor: {pdf_path.name}")
        pages = convert_from_path(pdf_path, dpi=150, poppler_path=POPPLER_PATH)
        for i, page in enumerate(pages, start=1):
            page.thumbnail(MAX_SIZE)
            output_path = output_dir / f"{pdf_path.stem}_sayfa_{i}.jpg"
            page.save(output_path, "JPEG", quality=85)
            print(f"  Kaydedildi: {output_path} ({page.width}x{page.height})")

    print("Tamamlandı.")
