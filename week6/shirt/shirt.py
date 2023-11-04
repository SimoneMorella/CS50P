import sys, os
from PIL import Image, ImageOps

def main():
    allowed_ext = [".jpg", ".png", ".jpeg"]

    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")

    else:
        in_file, in_ext = os.path.splitext(sys.argv[1])
        out_file, out_ext = os.path.splitext(sys.argv[2])

        if  in_ext.lower() not in allowed_ext or out_ext.lower() not in allowed_ext:
            sys.exit("Invalid input")

        else:
            if not in_ext.lower() == out_ext.lower():
                sys.exit("Input and Output have different extensions")
            else:
                put_shirt(sys.argv[1], sys.argv[2])

def put_shirt(input, output):
    try:
        background = Image.open(input)
        shirt = Image.open("shirt.png")
        s_size = shirt.size
        background = ImageOps.fit(background, size=s_size , method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        background.paste(shirt, shirt)
        background.save(output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()