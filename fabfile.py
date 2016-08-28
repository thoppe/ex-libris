from fabric.api import local
import os.path
import glob
import os

def is_newer(f1, f2):
    # Returns True if f1 is newer than f2
    return os.stat(f1).st_mtime > os.stat(f2).st_mtime

def get_thumbnail_name(f_xcf):
    f_png = os.path.join('thumbnails',os.path.basename(f_xcf))
    return f_png.replace('.xcf','.png')

def thumbnails():
    F_XCF = glob.glob('*.xcf')

    for f_xcf in F_XCF:
        f_png = get_thumbnail_name(f_xcf)
        if os.path.exists(f_png) and is_newer(f_png, f_xcf):
            continue

        cmd1 = "xcf2png --full-image --full-image {} > {}"
        cmd2 = "mogrify -thumbnail x300 {}"
        local(cmd1.format(f_xcf, f_png))
        local(cmd2.format(f_png))
