import sys, os
from shutil import copyfile

folder = sys.argv[1]
print(folder)

times = []
with open(os.path.join(folder + '/frames', 'times.txt')) as fptr:
    for line in fptr:
        times.append(line.strip())

with open(os.path.join(folder, 'rgb_depth.txt'), 'w') as out_fptr:
    for i in range(len(times)):
        out_fptr.write(times[i] + ' ' + os.path.join(folder + '/frames/', times[i] + '.png') +
            ' ' + times[i] + ' ' + os.path.join(folder + '/frames-depth/', times[i] + '.png'))
        if i < len(times) - 1:
            out_fptr.write('\n')


