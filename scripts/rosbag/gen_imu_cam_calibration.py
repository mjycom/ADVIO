import sys, os
import yaml
import numpy as np

yaml_fn = sys.argv[1]
print(yaml_fn)

with open(yaml_fn) as fptr:
    yaml_dict = yaml.safe_load(fptr)

print(yaml_dict)

T_cam_imu = np.array(yaml_dict['cameras'][0]['camera']['T_cam_imu']['data'])
T_imu_cam = np.linalg.inv(T_cam_imu)

print('------- T_cam_imu')
print(T_cam_imu)
print('------- T_imu_cam')
print(T_imu_cam)
print('------- R')
print(T_imu_cam[:3, :3].tolist())
print('------- T')
print(list(T_imu_cam[:3, 3]))
