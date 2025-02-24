import numpy as np
import itertools

# order wavecars to be in order specified by EIGENVAL file

data = np.fromfile("WAVECAR", dtype = np.float64)
print("wavecar shape: " + str(data.shape[0]))
print("Reading header: nspin = " + str(int(data[1])))
nSpin = int(data[1])
for line in open("OUTCAR","r"):
        if "plane waves" in line:
                nPW = int(line.split()[8])
print("Number of plane waves: " + str(nPW))

# slice along plane wave blocks. First four indices are header-like
slicedData = np.reshape(data, (-1,nPW))
nBlocks = slicedData.shape[0]
nSpin = int(data[1]);  nBands = int( (nBlocks - 3)/nSpin )
nBandsPres = int(slicedData[1,1])

print('nBands: ', nBands)
print("nBandsPres: ", nBandsPres)
print(slicedData.shape)

data_eval = np.loadtxt("EIGENVAL", skiprows=8) #, max_rows = nBands)

ind_band1 = np.argsort(data_eval[:,1])
ind_band2 = np.argsort(data_eval[:,2]) # spin down (minority)
# print(ind_band2)
# get the sort spin_dwon

sort_data_eval1 = data_eval[:,3][ind_band1]
sort_data_eval2 = data_eval[:,4][ind_band2]
# print FERWE and FERDO
ferwe = []
ferdo = []

for m, g in itertools.groupby(sort_data_eval2, lambda x: float(x)):
    ferdo.append(f"{len(tuple(g))}*{int(m)}")

for m, g in itertools.groupby(sort_data_eval1, lambda x: float(x)):
    ferwe.append(f"{len(tuple(g))}*{int(m)}")

print(f'FERDO = {" ".join(ferdo)}')
print(f'FERWE = {" ".join(ferwe)}')


coppiedData = np.copy(slicedData)

# sort the wavefunctions

band1_data = slicedData[3:nBandsPres+3,:]
band1_data[:nBandsPres] = band1_data[ind_band1]
coppiedData[3:nBandsPres+3] = band1_data

band2_data = slicedData[nBandsPres+4:,:]
band2_data[:nBandsPres] = band2_data[ind_band2]
coppiedData[(nBandsPres+4):] = band2_data

coppiedData.flatten().tofile("WAVECAR")
print(coppiedData.flatten().shape)

print("done.")
