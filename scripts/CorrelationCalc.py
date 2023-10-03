from nbodykit.lab import *
#import matplotlib.pyplot as plt

import datetime
start = datetime.datetime.now()
print("PROCESSING STARTED AT", start)

import numpy as np
from nbodykit.source import catalog
from nbodykit import CurrentMPIComm
from nbodykit.algorithms.paircount_tpcf.estimators import LandySzalayEstimator
#import logging
from nbodykit.binned_statistic import BinnedStatistic

#from nbodykit.source import estimators

from LoadCat import LoadHaloCatNbodykit
from LoadCat import LoadVoidCatNbodykit

histogram_bins_3d = np.logspace(-1,2.5)

print("With axions, 2048n512")
HalosTotal_2048n512 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n512_1_25_10.npy")
HalosTotal_2048n512_random = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n512_1_25_10_random.npy")

VoidsTotal_2048n512 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n512_1_25_10_centered.npy")
VoidsTotal_2048n512_random = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n512_1_25_10_centered_random.npy")

print("With axions, 2048n1024")
HalosTotal_2048n1024 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10.npy")
HalosTotal_2048n1024_random = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10_random.npy")

VoidsTotal_2048n1024 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n1024_1_25_10_centered.npy")
VoidsTotal_2048n1024_random = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n1024_1_25_10_centered_random.npy")

print("With axions, 2048n2048")
HalosTotal_2048n2048 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10.npy")
HalosTotal_2048n2048_random = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10_random.npy")

VoidsTotal_2048n2048 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n2048_1_25_10_centered.npy")
VoidsTotal_2048n2048_random = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n2048_1_25_10_centered_random.npy")

print("With axions, 2048n4096")
HalosTotal_2048n4096 = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10.npy")
HalosTotal_2048n4096_random = LoadHaloCatNbodykit("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_random.npy")

VoidsTotal_2048n4096 = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_1_25_10.npy")
VoidsTotal_2048n4096_random = LoadVoidCatNbodykit("Trial_PP_void_catalog_2048Mpc_n4096_1_25_10_random.npy")

#With axions, 2048n512
#corr_voidhalo_total_2048n512 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n512, VoidsTotal_2048n512, HalosTotal_2048n512_random, VoidsTotal_2048n512_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)
#corr_halohalo_total_2048n512 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n512, HalosTotal_2048n512, HalosTotal_2048n512_random, HalosTotal_2048n512_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)

#With axions, 2048n1024"
#corr_voidhalo_total_2048n1024 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n1024, VoidsTotal_2048n1024, HalosTotal_2048n1024_random, VoidsTotal_2048n1024_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)
#corr_halohalo_total_2048n1024 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n1024, HalosTotal_2048n1024, HalosTotal_2048n1024_random, HalosTotal_2048n1024_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)

#With axions, 2048n2048
#corr_voidhalo_total_2048n2048 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n2048, VoidsTotal_2048n2048, HalosTotal_2048n2048_random, VoidsTotal_2048n2048_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)
#corr_halohalo_total_2048n2048 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n2048, HalosTotal_2048n2048, HalosTotal_2048n2048_random, HalosTotal_2048n2048_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)

#With axions, 2048n4096
corr_voidhalo_total_2048n4096 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n4096, VoidsTotal_2048n4096, HalosTotal_2048n4096_random, VoidsTotal_2048n4096_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)
corr_halohalo_total_2048n4096 = LandySzalayEstimator(SimulationBoxPairCount, HalosTotal_2048n4096, HalosTotal_2048n4096, HalosTotal_2048n4096_random, HalosTotal_2048n4096_random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)


#np.save("corr_voidhalo_total_2048n512", corr_voidhalo_total_2048n512[4]['corr'])
#np.save("corr_halohalo_total_2048n512", corr_halohalo_total_2048n512[4]['corr'])
#np.save("corr_voidhalo_total_2048n1024", corr_voidhalo_total_2048n1024[4]['corr'])
#np.save("corr_halohalo_total_2048n1024", corr_halohalo_total_2048n1024[4]['corr'])
#np.save("corr_voidhalo_total_2048n2048", corr_voidhalo_total_2048n2048[4]['corr'])
#np.save("corr_halohalo_total_2048n2048", corr_halohalo_total_2048n2048[4]['corr'])
np.save("corr_voidhalo_total_2048n4096", corr_voidhalo_total_2048n4096[4]['corr'])
np.save("corr_halohalo_total_2048n4096", corr_halohalo_total_2048n4096[4]['corr'])

finish = datetime.datetime.now()

print("Processing DONE at", finish)

delta = finish - start

print("Total Processing time:", delta)