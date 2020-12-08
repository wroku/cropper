import os
import sys
import shutil
from PIL import Image

area1 = (130, 35, 1236, 656)
area2 = (198, 83, 874, 591)
default_dir_path = '/home/wroku/Just'
default_diff = 60
min_cropped_size = (400, 300)
default_transition_length = 6

def detect_borders(img):
    width, height = img.size
    rgb_img = img.convert('RGB')
    most_common_colours = {}
    for x in range(0, 31):
        rgb = rgb_img.getpixel((x, int(height/2)))
        if rgb not in most_common_colours:
            most_common_colours[rgb] = 1
        else:
            most_common_colours[rgb] += 1
    most_common_pixel = [k for k, v in sorted(most_common_colours.items(), key=lambda item: item[1], reverse=True)][0]

    while abs(sum(rgb_img.getpixel((x, int(height/2)))) - sum(most_common_pixel)) < default_diff:
        x += 1
    x += default_transition_length
    border_colour = rgb_img.getpixel((x, int(height/2)))
    x1 = x

    y = int(height/2)
    while abs(sum(rgb_img.getpixel((x1, y+1))) - sum(border_colour)) < default_diff:
        y += 1
    y2 = y

    y = int(height / 2)
    while abs(sum(rgb_img.getpixel((x1, y - 1))) - sum(border_colour)) < default_diff:
        y -= 1
    y1 = y

    x = x1 + min_cropped_size[0]
    while abs(sum(rgb_img.getpixel((x + 1, y2))) - sum(border_colour)) < default_diff:
        x += 1
    x2 = x

    return x1, y1, x2, y2


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '-a1':
            area = area1
        elif sys.argv[1] == '-a2':
            area = area2
    else:
        area = 'auto'

    for filename in os.listdir(default_dir_path):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img = Image.open(f'{default_dir_path}/{filename}')
            if area == 'auto':
                area = detect_borders(img)
            print(f'Cropping image {filename} to size {area}...')
            cropped_img = img.crop(area)

            if "CROPPED" not in os.listdir(default_dir_path):
                os.makedirs(f'{default_dir_path}/CROPPED')
            cropped_img.save(f'{default_dir_path}/CROPPED/cropped_{filename}')

            if "RAW" not in os.listdir(default_dir_path):
                os.makedirs(f'{default_dir_path}/RAW')
            shutil.move(f'{default_dir_path}/{filename}', f'{default_dir_path}/RAW/{filename}')
            area = 'auto'