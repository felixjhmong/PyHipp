import numpy as np
import matplotlib.pyplot as plt
import PyHipp as pyh
import time

t = time.time()

st1 = pyh.Spiketrain()
sptimes = st1.spiketimes[0]
nspikes = np.size(sptimes)
stimes = np.array(sptimes, dtype='float')/1000
uy = pyh.Unity()
utime = uy.unityTime[0]
udata = uy.unityData[0]
utime2 = (utime[1:]).reshape((-1,1))
udata2 = np.concatenate((utime2, udata[:,2:4]), axis=1)

# create array to store information about grid positions
placebins = np.zeros((40,40))
# create vector that will store the row indices, which should be integers
pos = np.zeros(nspikes, dtype='int')
# initialize index into the pos vector
pind = 0
# loop over spiketimes in stimes
for i in stimes:
    # ignore spiketimes before the start of the Unity program
    # and after the end of the Unity program
    if (i>udata2[0,0]) and (i<udata2[-1,0]):
        # store the row_index in pos[pind]
        pos[pind] = (udata2[:,0]>i).nonzero()[0][0]
        # increment index into the pos vector
        pind += 1
        
# perform calculation after extracting values from udata2
indices = (np.floor((udata2[pos[0:pind],1:3]+12.5)/0.625)).astype(int)
# performs cumulative increment of the indices in placebins
np.add.at(placebins, (indices[:,0], indices[:,1]), 1)

# create a new figure
plt.figure()
# show the grid counts as a heat-map image
plt.imshow(placebins, origin='lower')

print(time.time()-t)