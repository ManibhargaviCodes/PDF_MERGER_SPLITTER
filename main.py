from pypdf import PdfReader, PdfWriter
import os

# Merge PDFs
def merge_pdfs():
    writer = PdfWriter()
    folder = "input_pdfs"

    files = [file for file in os.listdir(folder) if file.endswith(".pdf")]

    if len(files) < 2:
        print("At least 2 PDF files are required.")
        return

    for file in files:
        reader = PdfReader(os.path.join(folder, file))

        for page in reader.pages:
            writer.add_page(page)

    output_path = "output/merged.pdf"

    with open(output_path, "wb") as f:
        writer.write(f)

    print("PDFs merged successfully!")
    print("Saved as:", output_path)


# Split PDF
def split_pdf():
    file_name = input("Enter PDF filename (example: sample.pdf): ")

    path = os.path.join("input_pdfs", file_name)

    if not os.path.exists(path):
        print("File not found.")
        return

    reader = PdfReader(path)

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_file = f"output/page_{i+1}.pdf"

        with open(output_file, "wb") as f:
            writer.write(f)

    print("PDF Split Successfully!")


# Main Menu
while True:
    print("\n===== PDF MERGER & SPLITTER =====")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        merge_pdfs()

    elif choice == "2":
        split_pdf()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")