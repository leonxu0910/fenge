import numpy as np
import pydicom as pd
import h5py
import matplotlib.pyplot as plt
import os

print("Start...")
# path = '../data/result/ouput.npy'
# sample = np.load(path)
# print(sample.shape)
# for i in range(sample.shape[0]):
# 	img = np.squeeze(sample[0], axis=2)
# 	plt.imsave(os.path.join('../data/result/', str(i+1)+'.png'), img)
path = '../data/test/'
ck = '../data/ck/'
if not os.path.isdir(ck):
	os.mkdir(ck)

for maindir, subdirlist, filelist in os.walk(path, topdown=False):
    for filename in filelist:
        if ".npy" in filename.lower():
            filepath = os.path.join(maindir, filename)
            data = np.load(filepath).item()
            plt.imsave(os.path.join(ck, filename.split('.')[0]+'_img.png'), np.squeeze(data['input'], axis=2))
            plt.imsave(os.path.join(ck, filename.split('.')[0]+'_mask.png'), np.squeeze(data['output'], axis=2))

print("Done")