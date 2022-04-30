from glob import iglob
from fnmatch import fnmatch
from PIL import ImageFont
for fn in iglob("c:/Windows/Fonts/*.tt*"):
    if not fnmatch(fn, "*.tt[cf]"):
        continue
    try:
        for i in range(5):
            ttf = ImageFont.truetype(font=fn, index=i)
        print("{} (face={}): {}".format(fn, i, ttf.getname()))
    except IOError as e:
        pass