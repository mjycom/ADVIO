# Create ROSBAG with the IMU and uncompressed video data 
#
# Description:
#   Create data structure containing IMU and ARKit data.
#
# Arguments:
#   - Data folder.
#   - sequences to bag
#
# Copyright (C) 2018 Santiago Cortes
#
# This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.

# Import system libraries 
import sys, os
import csv
import numpy as np
# Import opencv
import cv2

# Read arguments
# Folder
folder = sys.argv[1]
try:
    sys.argv[2]
except:
    tst = range(1,24)
else:
    tst = [int(sys.argv[2])]

print('Creating rosbags for sequences in '+ str(tst))

# Delete first frames
start=0.5

# Loop trough all sequences.
for i in iter(tst):
    # Find folder
    dir =folder+'/advio-'+str(i).zfill(2)+'/iphone'
    print(dir)

    # Initialize data and video reader.
    index=0
    csvfile=open(dir+'/'+'imu-gyro.csv')
    datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Read video and check for number of frames.
    vidcap = cv2.VideoCapture(dir+'/'+'frames.mov')
    vlength = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # For each row in the data matrix
    for row in datareader:
        # Read data row
        sp=row[0].split(",")

        # If the row correspond to a frame
        if int(float(sp[1]))==7:
            # Read next frame and check.
            success,image = vidcap.read()
            if success and float(sp[0])>start:


                stamp=float(sp[0])

                # Put image in corect orientation and convert into grayscale.
                #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray_image = cv2.transpose(image)
                gray_image = cv2.flip(gray_image,+1)

                # Print progress.
                if index%500==0:
                    print(str(int(np.round(100*float(index)/float(vlength))))+'%')

                # Create ros image and put frame in it.
                #Img = Image()
                #Img=bridge.cv2_to_imgmsg(gray_image,encoding='mono8')
                #Img.header.stamp = stamp

                # Put image in rosbag.
                #bag.write('/cam0/image_raw', Img, stamp)

                cv2.imwrite(dir+'/frames/'+str(stamp)+'.png', gray_image)

                index=index+1

print('Process complete')
