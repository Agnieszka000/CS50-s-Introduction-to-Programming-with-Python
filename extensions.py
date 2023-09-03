# Implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, 
# case-insensitively, in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip.
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

def main():
    filename = input("File: ")
    ext = sep_endings(filename)
    check_ext(ext)

def sep_endings(filename):
    file_end = filename.split(sep=".")
    return file_end[-1]

def check_ext(ext):
    match ext:
        case "gif" | "jpg" | "jpeg" | "png":
            print (f"image/{ext}")
        case "pdf" | "zip":
            print(f"application/{ext}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")

main()