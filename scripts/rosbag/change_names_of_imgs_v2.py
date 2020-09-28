import sys, os
from shutil import copyfile

folder = sys.argv[1]
out_folder = sys.argv[2]

times = []
with open(os.path.join(folder, 'times.txt')) as fptr:
    for line in fptr:
        times.append(line.strip())

with open(os.path.join(out_folder, 'data.csv'), 'w') as fptr:
    fptr.write('#timestamp [ns],filename')
    for i in range(len(times)):
        t_str = times[i]
        t_ns = int(1000000000 * float(t_str))
        print(os.path.join(folder, t_str + '.png'), os.path.join(out_folder, str(t_ns) + '.png'))
        copyfile(os.path.join(folder, t_str + '.png'), os.path.join(out_folder, str(t_ns) + '.png'))
        fptr.write('\n' + str(t_ns) + ',' + str(t_ns) + '.png')



