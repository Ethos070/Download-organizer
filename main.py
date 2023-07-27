import os

p = '/home/alessandro/Downloads'

if 'Images' not in os.listdir(p):
    os.mkdir(p + '/Images')

for file in os.listdir(p):
    if '.png' in file:
        os.rename(f'{p}/{file}', f'{p}/Images/{file}')