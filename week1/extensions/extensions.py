def main():
    file = input("File name: ").lower().strip()
    ext_check(file)

def ext_check(f):
    if f.endswith(".gif"):
        print("image/gif")

    elif f.endswith(".jpeg") or f.endswith(".jpg"):
        print("image/jpeg")

    elif f.endswith(".png"):
        print("image/png")

    elif f.endswith(".pdf"):
        print("application/pdf")

    elif f.endswith(".txt"):
        print("text/plain")

    elif f.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")


main()