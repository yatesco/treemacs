from os import listdir
from os.path import abspath, join, isdir, isfile
import sys

def dir_content(path):
    return [join(path, item) for item in listdir(path)]

out  = sys.stdout
root = sys.argv[1]
dirs = [d for d in dir_content(root) if isdir(d)]

for d in dirs:
    content = dir_content(d)
    collapsed = None
    steps = []
    if len(content) > 0:
        first = content[0]
        if len(content) == 1 and isdir(first):
            collapsed = join(d, first)
            steps.append(first)
            while True:
                content = dir_content(collapsed)
                first = content[0]
                if len(content) == 1 and isdir(first):
                    collapsed = join(collapsed, first)
                    steps.append(first)
                else:
                    break
        if collapsed:
            final_dir = steps[len(steps) - 1]
            display_dir = final_dir[len(d):]
            out.write("\n"  + d + "//" + display_dir + "//" + "//".join(steps))
