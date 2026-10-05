from PIL import Image, ImageOps
import os


def build_comic_page(panel_paths, output_path, columns=2):
    """
    Arrange comic panels into a single comic page.
    """

    if not panel_paths:
        raise ValueError("No panel images were provided.")

    # Open all panels
    panels = [Image.open(path).convert("RGB") for path in panel_paths]

    # Make all panels the same size
    panel_width = 500
    panel_height = 500

    resized_panels = []

    for panel in panels:
        panel = ImageOps.fit(
            panel,
            (panel_width, panel_height)
        )
        resized_panels.append(panel)

    # Calculate rows
    rows = (len(resized_panels) + columns - 1) // columns

    # Space between panels
    spacing = 20

    page_width = columns * panel_width + (columns + 1) * spacing
    page_height = rows * panel_height + (rows + 1) * spacing

    # Create white comic page
    comic_page = Image.new(
        "RGB",
        (page_width, page_height),
        "white"
    )

    # Place panels
    for index, panel in enumerate(resized_panels):

        row = index // columns
        column = index % columns

        x = spacing + column * (panel_width + spacing)
        y = spacing + row * (panel_height + spacing)

        comic_page.paste(panel, (x, y))

    # Create output folder if necessary
    output_directory = os.path.dirname(output_path)

    if output_directory:
        os.makedirs(output_directory, exist_ok=True)

    # Save comic page
    comic_page.save(output_path)

    return output_path


if __name__ == "__main__":

    print("Layout Builder is ready.")
    print("It will combine comic panels into a single page.")