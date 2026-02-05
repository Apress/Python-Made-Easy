import h5py

with h5py.File('people.h5', 'r') as f:
    print(f['people']['person1']['age'][()])