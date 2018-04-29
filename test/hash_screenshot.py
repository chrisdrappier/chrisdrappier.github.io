import hashlib
from subprocess import call

def hash_file(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

screenshot = hash_file('screenshot.png')
screenshot_baseline = hash_file('baseline-screenshot.png')

equal = screenshot == screenshot_baseline

print("screenshot          : {}".format(screenshot))
print("screenshot_baseline : {}".format(screenshot_baseline))
print("equal?              : {}".format(equal))

if (not equal):
    print("generating diff.png")
    call(["compare","baseline-screenshot.png","screenshot.png","-compose","src","diff.png"])
    print("view diff.png to see differences")
