import sys
from PIL import Image, ImageOps
def main():
    check_command_line_args()

    try:
        # open shirt image
        blank_shirt = Image.open("shirt.png")
        size = blank_shirt.size
        # Open to format image
        # Resize image
        #crop image
        resized_image = ImageOps.fit(Image.open(sys.argv[1]), size)
        # merge the to / overlay and make new file out of it
        resized_image.paste(blank_shirt, blank_shirt)
    
        resized_image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("file not found")





def check_command_line_args():
    # Check amount of arguments
    if len(sys.argv) > 2:
        sys.exit("too many arguments")
    
    if len(sys.argv) < 2:
        sys.exit("too few arguments")

    # Check if file extensions are valid
    extensions = ["jpeg", ".jpg", ".png"]

    if not (sys.argv[1][-4:] in extensions or sys.argv[2][-4:] in extensions ) :
        sys.exit("Not right file-types")
    
    if not sys.argv[1][-4:] == sys.argv[2][-4:]:
        sys.exit("Files need to be of the same type")
    
