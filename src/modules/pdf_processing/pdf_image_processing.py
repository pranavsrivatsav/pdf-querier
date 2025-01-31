import pytesseract
from pdf2image import convert_from_path
from pdf_chunk import chunk_pdf
from io import BytesIO

def pdf_to_images(pdf_path, poppler_path=None, dpi=300):
    """
    Converts a PDF file to a list of images.

    Args:
        pdf_path (str): Path to the PDF file.
        poppler_path (str): Path to the Poppler binaries (optional).
        dpi (int): Resolution of the output images (default: 300).

    Returns:
        list: List of PIL.Image objects.
    """
    images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)
    return images

def image_to_bytes(image):
    """
    Converts a PIL.Image object to bytes.

    Args:
        image (PIL.Image): The image to convert.

    Returns:
        bytes: The image in bytes.
    """
    byte_stream = BytesIO()
    image.save(byte_stream, format="PNG")  # Save image as PNG format
    byte_stream.seek(0)  # Reset the stream position to the beginning
    return byte_stream.read()

def parse_pdf_image_and_chunk(pdf_path, dpi=300):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\PranavSrivatsavC\Documents\software\tesseract\tesseract.exe"
    poppler_path = r"C:\Users\PranavSrivatsavC\Documents\software\poppler-24.08.0\Library\bin"
    images = pdf_to_images(pdf_path, poppler_path, dpi=dpi)
    extracted_text = ""

    for i, image in enumerate(images):
        # Convert the image to bytes
        image_bytes = image_to_bytes(image)

        # Use pytesseract to extract text
        text = pytesseract.image_to_string(image)
        extracted_text += f"Page {i + 1}:\n{text}\n"

    chunks = chunk_pdf(extracted_text, inputType="text")
    return chunks
    