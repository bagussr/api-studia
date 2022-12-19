from api_studia.modules import os, PUBLIC_DIR, Image, io


def delete_local_file(filename: str):
    os.remove(os.path.join(os.getcwd(), f"{filename}.png"))


def resize_image(file):
    size = len(file.read())
    image = Image.open(file)
    if size > 10 * 1000000:
        ratio = 0.25
    elif size > 5 * 1000000:
        ratio = 0.4
    elif size > 1 * 1000000:
        ratio = 0.55
    else:
        ratio = 1
    image = image.resize([int(ratio * s) for s in image.size])
    new_image = io.BytesIO()
    image.save(new_image, "JPEG")
    return new_image
