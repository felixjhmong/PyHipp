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
# loop over spiketimes in stimes
for i in stimes:
    # ignore spiketimes before the start of the Unity program
    # and after the end of the Unity program
    if (i>udata2[0,0]) and (i<udata2[-1,0]):
 	  # get the first row number in udata2 with timestamp greater
 	  # than spiketime
        row_index = (udata2[:,0]>i).nonzero()[0][0]
        # get the x- and y-positions in that row
        pos = udata2[row_index,1:3]
 	  # convert the x- and y-positions to rows and cols for the grid
 	  # we have to convert to integers to make sure we can use them
 	  # to index into the placebins array
        indices = (np.floor((pos+12.5)/0.625)).astype(int)
 	  # increment the spikecount at the appropriate grid position
        placebins[indices[0],indices[1]] += 1.0

# create a new figure
plt.figure()
# show the grid counts as a heat-map image
plt.imshow(placebins, origin='lower')

print(time.time()-t)