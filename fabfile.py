from fabric.api import local
import os.path
import glob
import os

F_XCF = glob.glob('source/*.xcf')
os.system('mkdir -p thumbnails png pdf')

def _is_newer(f1, f2):
    # Returns True if f1 is newer than f2
    return os.stat(f1).st_mtime > os.stat(f2).st_mtime

def _get_name(f_in, dir_out, ext1, ext2):
    f_out = os.path.join(dir_out,os.path.basename(f_in))
    return f_out.replace('.'+ext1, '.'+ext2)

def thumbnails():

    for f_xcf in F_XCF:
        f_png = _get_name(f_xcf, 'thumbnails', 'xcf', 'png')
        if os.path.exists(f_png) and _is_newer(f_png, f_xcf):
            continue

        cmd1 = "xcf2png --full-image --full-image {} > {}"
        cmd2 = "mogrify -thumbnail x300 {}"
        local(cmd1.format(f_xcf, f_png))
        local(cmd2.format(f_png))

def fullsize():
    for f_xcf in F_XCF:
        f_png = _get_name(f_xcf, 'png', 'xcf', 'png')
        if os.path.exists(f_png) and _is_newer(f_png, f_xcf):
            continue

        cmd1 = "xcf2png --full-image --full-image {} > {}"
        local(cmd1.format(f_xcf, f_png))

def check():

    for f_xcf in F_XCF:
        f_pdf = _get_name(f_xcf, 'pdf', 'xcf', 'pdf')
        
        if os.path.exists(f_pdf) and _is_newer(f_pdf, f_xcf):
            continue

        local("gimp {} 2>/dev/null &".format(f_xcf))
        
        msg = "WARNING! {} is newer than {}!"
        raise ValueError(msg.format(f_pdf, f_xcf))
