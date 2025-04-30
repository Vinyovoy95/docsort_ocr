import os
import pytesseract
import cv2
from PIL import Image
from tkinter import filedialog, Tk, messagebox
import shutil
import concurrent.futures
from tqdm import tqdm
import re

# Initial setup
pytesseract.pytesseract.tesseract_cmd = 'tesseract'  # Use the full path if needed

# Simplified list of fiscal keywords (in Portuguese - BR)
fiscal_keywords = [
    "R$", "$", "NF", "Data:", "Hora:", "CPF:", "CNPJ:", "Nº", "Valor:", "Total:",
    "Desconto:", "Forma de Pagamento:", "PIX", "Cartão", "Dinheiro",
    "Nota Fiscal", "Recibo", "Comprovante", "Transação:", "Autenticação:",
    "Código:", "Chave de Acesso:"
]

# Keywords for category-specific grouping
receipt_keywords = ["comprovante", "recibo", "pagamento", "transferência"]

def choose_directory(title):
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title=title)

def perform_ocr(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return ""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='por')
    return text.lower()  # Normalize to lowercase

def contains_fiscal_elements(text):
    # Check for fiscal keywords or typical date formats
    date_pattern = r"\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b"
    return any(word.lower() in text for word in fiscal_keywords) or re.search(date_pattern, text)

def get_category(text):
    if any(word in text for word in receipt_keywords):
        return "receipts"
    return "others"

def process_file(file_path, destination):
    text = perform_ocr(file_path)
    if contains_fiscal_elements(text):
        category = get_category(text)
        category_path = os.path.join(destination, category)
        os.makedirs(category_path, exist_ok=True)
        shutil.move(file_path, os.path.join(category_path, os.path.basename(file_path)))
        return category
    return None

def main():
    source = choose_directory("Select the directory with images to analyze")
    if not source:
        messagebox.showinfo("Canceled", "Source directory not selected.")
        return

    destination = choose_directory("Select the destination directory")
    if not destination:
        messagebox.showinfo("Canceled", "Destination directory not selected.")
        return

    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f)) and
             f.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp"))]

    results = {"receipts": 0, "others": 0}

    def process_wrapper(file_name):
        path = os.path.join(source, file_name)
        category = process_file(path, destination)
        return category

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for result in tqdm(executor.map(process_wrapper, files), total=len(files), desc="Processing"):
            if result:
                results[result] += 1

    messagebox.showinfo(
        "Completed",
        f"Processing complete.\nReceipts/Payments: {results['receipts']}\nOthers: {results['others']}"
    )

if __name__ == "__main__":
    main()
