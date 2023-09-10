import sys
from PIL import Image, ImageOps

def main():
    check_command_line_args()

    try:
        # Open the person image (JPEG)
        person_image = Image.open(sys.argv[1])

        # Open the shirt image (PNG with transparency)
        shirt_image = Image.open("shirt.png")

        # Resize the shirt image to fit the person's dimensions
        shirt_image = shirt_image.resize(person_image.size)

        # Overlay the shirt image on the person image
        result_image = Image.alpha_composite(person_image.convert("RGBA"), shirt_image.convert("RGBA"))

        # Save the resulting image as a JPEG
        result_image.convert("RGB").save(sys.argv[2], "JPEG")
    except FileNotFoundError:
        sys.exit("File not found")



def check_command_line_args():
    # Check amount of arguments
    if len(sys.argv) > 3:
        sys.exit("too many arguments")
    
    if len(sys.argv) < 3:
        sys.exit("too few arguments")

    # Check if file extensions are valid
    extensions = ["jpeg", ".jpg", ".png"]

    if not (sys.argv[1][-4:] in extensions or sys.argv[2][-4:] in extensions ) :
        sys.exit("Not right file-types")
    
    if not sys.argv[1][-4:] == sys.argv[2][-4:]:
        sys.exit("Files need to be of the same type")
    
if __name__ == "__main__":
    main()