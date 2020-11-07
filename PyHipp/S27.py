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


# ignore spiketimes before the start of the Unity program
# and after the end of the Unity program
stimes2 = stimes[(stimes>udata2[0,0]) & (stimes<udata2[-1,0])]
# get the corresponding bin number (row_index) for each spiketime
bin_number = np.digitize(stimes2,udata2[:,0])     
# perform calculation after extracting values from udata2
indices = ( np.floor( (udata2[bin_number,1:3]+12.5) / 0.625 ) ).astype(int)
# convert 2D-indices to 1D-indices
index = indices[:,0] * 40 + indices[:,1]
# perform histogram
histcounts, bins = np.histogram(index,bins=np.arange(1601))
# reshape histogram count to 2D array
placebins = np.reshape(histcounts, (40,40))



# create a new figure
plt.figure()
# show the grid counts as a heat-map image
plt.imshow(placebins, origin='lower')

print(time.time()-t)