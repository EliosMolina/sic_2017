# coding: utf-8

from gaia2 import *
import os

# Read sig files
fnames = os.listdir('.')
sigs = []
for fname in fnames:
    if fname[-4:] == '.sig':
        sigs.append(fname)
        
# Create gaia2 DataSet
ds = DataSet()
for sig in sigs:
    print sig
    p = Point()
    p.load(sig)
    p.setName(sig)
    ds.addPoint(p)


# Select some descriptors and apply some processings
selected_ds = transform(ds,
                        'select',
                        {'descriptorNames': ['lowlevel.pitch_salience.mean',
                                             'lowlevel.spectral_centroid.mean',
                                             'lowlevel.spectral_entropy.mean',
                                             'lowlevel.spectral_flux.mean',
                                             'lowlevel.mfcc.mean',
                                             'sfx.logattacktime']})
selected_ds = transform(selected_ds, 'FixLength')
norm_ds = transform(selected_ds, 'normalize')

# Create view for nnSearch
v = View(norm_ds)
euclideanMetric = DistanceFunctionFactory.create('euclidean',
                                                 norm_ds.layout())
# query by id
# http://essentia.upf.edu/documentation/gaia/tutorial.html

results = v.nnSearch(sigs[0], euclideanMetric).get(5)

for r in results:
    cmd = "mplayer '%s'" % r[0].replace('.sig', '')
    os.system(cmd) 
