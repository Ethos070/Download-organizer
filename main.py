import os

p = '/home/alessandro/Downloads'
dirs = ['Images', 'Documents', 'Videos', 'Books', 'Music', 'Compressed']
extensions = [
    ['png', 'jpeg', 'jpg'],
    ['pdf', 'xlsx', 'csv'],
    ['mp4'],
    ['epub'],
    ['mp3'],
    ['zip']
]

for d in dirs:
    if d not in os.listdir(p):
        os.mkdir(f'{p}/{d}')

while True:
    for file in os.listdir(p):
        for file_type in extensions:
            for ext in file_type:
                if f'.{ext}' in file:
                    ind = extensions.index(file_type)
                    folder = dirs[ind]
                    os.rename(f'{p}/{file}', f'{p}/{folder}/{file}')
