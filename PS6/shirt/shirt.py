import sys
import os
from PIL import Image, ImageOps

def main():

    check_args()

    extensions = [".jpg", ".jpeg", ".png"]

    argv1_ext = get_extensions(sys.argv[1])
    argv2_ext = get_extensions(sys.argv[2])


    try:
        if argv1_ext != argv2_ext:
            sys.exit("Input and output have different extensions")
        if (argv1_ext.lower() not in extensions) or (argv2_ext.lower() not in extensions):
            sys.exit("Invalid input")

        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])
        muppet = ImageOps.fit(muppet, size=shirt.size)
        muppet.paste(shirt, shirt)
        muppet = Image.Image.save(muppet, sys.argv[2].lower())

    except FileNotFoundError:
        sys.exit("File does not exist")

def get_extensions(file):
    argv = os.path.splitext(file)
    return argv[1]

def check_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()