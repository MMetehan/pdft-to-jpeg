# PDF to JPEG Converter

Kendi ihtiyaçlarımdan dolayı geliştirdiğim bir PDF'ten JPEG'e dönüştürme aracıdır. PDF dosyalarındaki her sayfayı ayrı bir JPEG görüntüsüne dönüştürür; görüntüler en-boy oranı korunarak ve kırpılmadan yeniden boyutlandırılır.

A PDF to JPEG conversion tool developed for my own needs. Converts each page of PDF files into separate JPEG images, resized while preserving the aspect ratio without cropping.

---

## Kullanım / Usage

### Gereksinimler / Requirements

```
pip install pdf2image pillow
```

> macOS için `poppler` gereklidir: `brew install poppler`
> For macOS, `poppler` is required: `brew install poppler`
>
> Windows için poppler binary'lerini indirip PATH'e eklemeniz gerekir.
> For Windows, download poppler binaries and add them to PATH.

### Çalıştırma / Running

1. PDF dosyalarını `pdfs/` klasörüne koy. / Place PDF files into the `pdfs/` folder.
2. Scripti çalıştır. / Run the script.

```bash
python3 pdf_to_jpeg.py
```

3. Dönüştürülen görüntüler `output/` klasöründe oluşturulur. / Converted images will be saved in the `output/` folder.

---

## Yapılandırma / Configuration

`pdf_to_jpeg.py` içindeki `MAX_SIZE` değişkeni ile maksimum çıktı boyutunu ayarlayabilirsiniz.

You can adjust the maximum output size by changing the `MAX_SIZE` variable in `pdf_to_jpeg.py`.

```python
MAX_SIZE = (1024, 1024)  # varsayılan / default
```
