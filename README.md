
# Fiscal Document Sorter

## Overview
The Fiscal Document Sorter is a Python-based tool for automatically classifying and organizing Brazilian fiscal documents from image files using Tesseract OCR. It is designed for triage and operational use, ideal for quickly sorting large numbers of files such as receipts, payment proofs, and invoices.

Documents are scanned for key fiscal terms and routed to appropriate folders, helping streamline manual organization tasks.

Note: Classification is keyword-based and may capture unrelated items (e.g., IDs). Manual verification is recommended.

## Features

- OCR text extraction using Tesseract (Portuguese language)
- Smart sorting:
  - Detects terms like "comprovante", "recibo", "pagamento", "transferência" and sends them to the `receipts/` folder
  - Other fiscal content is sent to the `others/` folder
- Recognizes common Brazilian date formats (e.g., dd/mm/yyyy, dd/mm)
- Batch processing with parallel execution via ThreadPoolExecutor
- Real-time progress using tqdm
- Simple folder selection using a graphical interface (tkinter)
- Files are moved, not copied

## Requirements

- Python: 3.10+
- Libraries:
  - opencv-python
  - pillow
  - pytesseract
  - tqdm

Install all dependencies with:

```bash
pip install opencv-python pillow pytesseract tqdm
```

Also ensure Tesseract OCR is installed and in your system PATH:
https://github.com/tesseract-ocr/tesseract

## Usage

1. Run the script:
   ```bash
   python fiscal_sorter.py
   ```
2. Select:
   - Source folder (containing image files)
   - Destination folder (where organized files will be saved)
3. Files will be scanned and sorted automatically.

## How It Works

The script uses Tesseract OCR to extract text from each image and searches for fiscal-related keywords in Brazilian Portuguese. Based on the content, it moves the file to either:

- `receipts/`: for payment-related documents
- `others/`: for general fiscal content

A progress bar displays the processing status. Files are handled in parallel for improved performance.

## Supported Formats

- .jpg
- .jpeg
- .png
- .bmp
- .tiff

## Example Folder Structure

```
destination_folder/
├── receipts/
│   ├── comprovante1.jpg
│   └── recibo_loja.png
└── others/
    ├── nota_fiscal_eletronica.jpg
    └── invoice_loja.png
```

## Limitations

- Currently optimized for Brazilian fiscal document types
- May classify unrelated documents due to keyword-only logic

## Future Improvements

- More robust classification logic
- PDF support and integration with pdf_anomaly_detector
- Unified interface for broader document triage

## License

MIT License – use freely with attribution.


MIT License – use freely with credit.
