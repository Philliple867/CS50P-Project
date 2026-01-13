import sys
import os
from PIL import Image, ImageOps

def main():
    # Check command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # Check file extensions
    ext1 = os.path.splitext(file1)[1].lower()
    ext2 = os.path.splitext(file2)[1].lower()
    valid_ext = [".jpg", ".jpeg", ".png"]

    if ext2 not in valid_ext:
        sys.exit("Invalid output")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(file1):
        sys.exit("Input does not exist")

    # Process the image
    try:
        shirt = Image.open("shirt.png")
        with Image.open(file1) as input_img:
            # Resize and crop input image to match shirt size
            input_cropped = ImageOps.fit(input_img, shirt.size)
            # Overlay shirt onto the image
            input_cropped.paste(shirt, shirt)
            # Save the result
            input_cropped.save(file2)
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
