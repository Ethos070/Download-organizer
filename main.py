import os

p = os.path.expanduser('~') + '/Downloads'
dirs = ['Images', 'Documents', 'Videos', 'Books', 'Music', 'Compressed', 'Executables']
extensions = [
    ["jpg", "jpeg", "jpe", "jif", "jfif", "jfi", "png", "gif", "webp", "tiff", "tif", "psd", "raw", "arw", "cr2", "nrw",
     "k25", "bmp", "dib", "heif", "heic", "ind", "indd", "indt", "jp2", "j2k", "jpf", "jpf", "jpx", "jpm", "mj2", "svg", "svgz", "ai", "eps", "ico"],
    ["doc", "docx", "odt", "pdf", "xls", "xlsx", "ppt", "pptx", "csv", "json"],
    ["webm", "mpg", "mp2", "mpeg", "mpe", "mpv", "ogg","mp4", "mp4v", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf", "avchd"],
    ['epub'],
    ['mp3', 'wav', 'flac', 'm4a', 'aac', 'ogg'],
    ['zip', 'rar', '7z', 'tar.gz', 'gz', 'tgz', 'tar.xz', 'xz', 'tar.bz2', 'bz2', 'tbz2', 'tar.lzma', 'tlz', 'lzma', 'txz', 'zipx', 'tar', 'iso'],
    ['exe', 'msi', 'AppImage', 'tar', 'deb', 'rpm', 'apk', 'dmg', 'pkg', 'jar'],
]


for file in os.listdir(p):
    for file_type in extensions:
        for ext in file_type:
            if f'.{ext}' in file:
                ind = extensions.index(file_type)
                folder = dirs[ind]
                if folder not in os.listdir(p):
                    os.mkdir(f'{p}/{folder}')
                os.rename(f'{p}/{file}', f'{p}/{folder}/{file}')
