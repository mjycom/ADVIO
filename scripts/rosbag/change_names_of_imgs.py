import sys, os
from shutil import copyfile

folder = sys.argv[1]
out_folder = sys.argv[2]

times = []
with open(os.path.join(folder, 'times.txt')) as fptr:
    for line in fptr:
        times.append(line.strip())

for i in range(len(times)):
    t_str = times[i]
    print(os.path.join(folder, t_str + '.png'), os.path.join(out_folder, str(i).zfill(6) + '.png'))
    copyfile(os.path.join(folder, t_str + '.png'), os.path.join(out_folder, str(i).zfill(6) + '.png'))


