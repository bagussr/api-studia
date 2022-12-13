from api_studia.modules import os, PUBLIC_DIR


def detete_local_file(filename: str):
    os.remove(os.path.join(PUBLIC_DIR, f"{filename}.png"))
