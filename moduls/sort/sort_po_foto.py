import hashlib

from PIL import Image

from config import bases, fimage
from moduls.read_write.get_image import image_get


def sort_po_foto(msg, base):
    histo = ''
    if msg['attachments'][0]['type'] == 'photo' and\
            image_get(msg['attachments'][0]['photo']['sizes'][0]['url']):
        image = Image.open(bases + fimage)
        histo = image.histogram()
        hash_object = hashlib.md5(str(histo).encode())
        histo = hash_object.hexdigest()
        if histo in base['hash']:
            msg = []
            histo = ''

    return msg, histo


if __name__ == '__main__':
    pass
