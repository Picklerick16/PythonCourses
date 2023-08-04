
def main():
    file_name = list(input("File name: ").lower())
    print(to_media_type(file_name))

def to_media_type(file):
    # Check if it is an extension
    if "." in file:

        # Remove the filename and extension-dot
        index = file.index(".")
        file_extension = "".join(file[index+1:])
  
        # Compare the naked extensions
        match file_extension:
            case "gif":
                return "image/gif"
            case "doc":
                return "application/msword"
            case _:
                return "application/octet-stream"

main()