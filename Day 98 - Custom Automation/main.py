from PIL import Image, UnidentifiedImageError
import os

"""
Script for converting WEBP (e.g. memes downloaded from Reddit) images to JPG.
"""

folder = input("Type folder path (leave empty for current folder) > ")
if not folder:
    folder = "./"

for filename in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, filename)):
        try:
            with Image.open(os.path.join(folder, filename)) as im:
                if im.format == "WEBP":
                    if im.mode == "RGBA":
                        im = im.convert("RGB")
                    try:
                        print(f"Converting: {os.path.join(folder, filename)}")
                        im.save(f"./converted/{filename[:-3]}.jpg")
                    except FileNotFoundError:
                        print(f"Converting: {os.path.join(folder, filename)}")
                        os.makedirs(os.path.join(folder, "converted"))
                        im.save(f"./converted/{filename[:-3]}.jpg")

                    try:
                        os.rename(os.path.join(folder, filename), f"./original/{filename}")
                    except FileNotFoundError:
                        os.makedirs(os.path.join(folder, "original"))
                        os.rename(os.path.join(folder, filename), f"./original/{filename}")
        except (UnidentifiedImageError, PermissionError):
            pass

print("\n\n\t\t\tCompleted.\n\n")
