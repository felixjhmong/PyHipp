import numpy as np
import matplotlib.pyplot as plt
import PyHipp as pyh
import time

t = time.time()

st1 = pyh.Spiketrain()
sptimes = st1.spiketimes[0]
stimes = np.array(sptimes, dtype='float')/1000

# load the Umaze object
um = pyh.Umaze()
# get the time bins for the digitize function
umst = um.sessionTime
stedges = umst[:,0]
# ignore spiketimes before the start of the Unity program
# and after the end of the Unity program
stimes2 = stimes[(stimes>stedges[1]) & (stimes<stedges[-1])]
# get the bin number corresponding to each spike time
# subtract by 1 in order to use bin_number to index umst
bin_number = np.digitize(stimes2, stedges) - 1
# extract the grid position
gp = umst[bin_number,1]
# subtract grid position by 1 to change from 1-indexed to 0-indexed integers
gp2 = gp[gp>0] - 1
# perform histogram
histcounts, bins = np.histogram(gp2,bins=np.arange(1601))
# reshape histogram count to 2D array
placebins = np.reshape(histcounts, (40,40))

plt.figure()
plt.imshow(placebins, origin='lower')

print(time.time()-t)