"""Mit diesen Python Library kann man durch einpaar codes den Hintergrund eines Bildes ganzeinfach entfernen"""

import rembg
from PIL import Image

input_path = "images.png"
output_path = "images_2.png"
input_image = Image.open(input_path)
output_image = rembg.remove(input_image)
output_image.save(output_path)



