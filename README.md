# Fiscal Document Sorter (OCR-based)

This is a simple Python-based tool that uses Tesseract OCR to **analyze images of documents**, attempting to identify **Brazilian fiscal elements** (e.g., receipts, payment proofs, or invoices), and automatically move them into categorized folders.

> ⚠️ **Important**: This tool is configured to detect Brazilian Portuguese text and is not fully accurate — some unrelated documents (e.g., personal IDs) may still be classified. It is **recommended as a triage step**, with final validation by a human.

---

## ✅ Features

- ⚙️ **OCR via Tesseract** (language: `por`)
- 📁 Automatically moves images containing:
  - `"comprovante"`, `"recibo"`, `"pagamento"`, `"transferência"` → to the `receipts/` folder
  - Other fiscal content → to the `others/` folder
- 🔍 Recognizes typical fiscal keywords and dates in formats like `dd/mm/yyyy` or `dd/mm`
- 🔄 **Batch processing** with **parallelism** (`ThreadPoolExecutor`)
- 📊 Progress bar using `tqdm`
- 🧠 GUI-based folder selection with `tkinter`
- 📂 Moves files (does not copy) to destination folders

---

## 🧰 Dependencies

Install these with pip:

```bash
pip install opencv-python pillow pytesseract tqdm
```

Also, make sure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed and available in your system path.

---

## 📁 Example Folder Structure After Running

```
destination_folder/
├── receipts/
│   ├── receipt1.jpg
│   └── comprovante_mercado.png
└── others/
    ├── nota_fiscal_loja.jpg
    └── invoice123.png
```

---

## ⚠️ Limitations

- Currently tuned for **Brazilian fiscal documents**, but may capture **unrelated documents** (e.g., ID cards or certificates).
- The tool uses a simple keyword-based matching strategy, which might need refinement based on your use case.

---

## 🧠 Recommended Workflow

I recommend using this tool **in combination with**:

- 🔍 [`pdf_anomaly_detector`](https://github.com/Vinyovoy95/pdf_anomaly_detector): a tool for deeper PDF inspection after the initial image-level triage.

> 💡 In the future, both tools will be **merged into a single unified application** to improve efficiency and usability.

---

## 🖼️ Supported Input Formats

- `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`

---

## 🚀 Usage

1. Run the script:
   ```bash
   python fiscal_sorter.py
   ```

2. Select:
   - The **source folder** with your images
   - The **destination folder** where results will be organized

3. Wait for completion and check the sorted files in the output folders.

---

## 🔒 License

MIT License – use freely with credit.
