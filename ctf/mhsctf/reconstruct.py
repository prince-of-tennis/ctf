from PIL import Image

pixel_list = []
actual_pixel_list = []
with open("reconstruct.txt") as p:
        pixel_list = (p.read().split(";")[0]) .split(",")

for value in pixel_list:
        if value != "":
                actual_pixel_list.append(int(value))

img_bytes = bytes(actual_pixel_list)

img = Image.frombytes("RGB", (360, 360), img_bytes)
img.show()
