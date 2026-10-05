import os
from PIL import Image
from fpdf import FPDF


def export_as_png(image_path: str, output_path: str) -> str:
    """
    Export the comic page as a PNG image.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Comic image not found: {image_path}"
        )

    os.makedirs(
        os.path.dirname(output_path) or ".",
        exist_ok=True
    )

    image = Image.open(image_path).convert("RGB")
    image.save(output_path, "PNG")

    return output_path


def export_as_pdf(image_path: str, output_path: str) -> str:
    """
    Export the comic page as a PDF file.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Comic image not found: {image_path}"
        )

    os.makedirs(
        os.path.dirname(output_path) or ".",
        exist_ok=True
    )

    image = Image.open(image_path).convert("RGB")

    # Convert pixels to PDF points
    width, height = image.size
    width_pt = width * 72 / 96
    height_pt = height * 72 / 96

    pdf = FPDF(
        orientation="P",
        unit="pt",
        format=(width_pt, height_pt)
    )

    pdf.add_page()

    # Save a temporary JPEG because FPDF handles JPEG reliably
    temp_jpeg = "static/exports/temp_comic.jpg"
    os.makedirs("static/exports", exist_ok=True)

    image.save(temp_jpeg, "JPEG", quality=95)

    pdf.image(
        temp_jpeg,
        x=0,
        y=0,
        w=width_pt,
        h=height_pt
    )

    pdf.output(output_path)

    # Remove temporary file
    if os.path.exists(temp_jpeg):
        os.remove(temp_jpeg)

    return output_path


if __name__ == "__main__":

    print("--- Comic Exporter is ready ---")
    print("PNG and PDF export functions are available.")