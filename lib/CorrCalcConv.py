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

haloConvDir = "/home/alexander/surp2022/SURPProject2022/cat/halo/converged/binned/"
haloConvRandDir = "/home/alexander/surp2022/SURPProject2022/cat/halo/converged/binned/rand/"

voidConvCentDir = "/home/alexander/surp2022/SURPProject2022/cat/void/converged/centered/"
voidConvCentRandDir = "/home/alexander/surp2022/SURPProject2022/cat/void/converged/centered/rand/"

resultsDir = "/home/alexander/surp2022/SURPProject2022/results/corrfunc/2048RestTestConv/"

#Halos
HalosBin1_2048n512 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n512_1_25_10_converged_bin1.npy")
HalosBin2_2048n512 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n512_1_25_10_converged_bin2.npy")

HalosBin1_2048n1024 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10_converged_bin1.npy")
HalosBin2_2048n1024 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10_converged_bin2.npy")

HalosBin1_2048n2048 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10_converged_bin1.npy")
HalosBin2_2048n2048 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10_converged_bin2.npy")

HalosBin1_2048n4096 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_converged_bin1.npy")
HalosBin2_2048n4096 = LoadHaloCatNbodykit(haloConvDir + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_converged_bin2.npy")

#Halos - Random
HalosBin1_2048n512_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n512_bin1.npy")
HalosBin2_2048n512_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n512_bin2.npy")

HalosBin1_2048n1024_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n1024_bin1.npy")
HalosBin2_2048n1024_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n1024_bin2.npy")

HalosBin1_2048n2048_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n2048_bin1.npy")
HalosBin2_2048n2048_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n2048_bin2.npy")

HalosBin1_2048n4096_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n4096_bin1.npy")
HalosBin2_2048n4096_rand = LoadHaloCatNbodykit(haloConvRandDir + "RandomHalos_2048n4096_bin2.npy")

#Voids
Voids_2048n512 = LoadVoidCatNbodykit(voidConvCentDir + "2048Mpc_n512_convzobov-Voids_cat_centered.npy")
Voids_2048n1024 = LoadVoidCatNbodykit(voidConvCentDir + "2048Mpc_n1024_convzobov-Voids_cat_centered.npy")
Voids_2048n2048 = LoadVoidCatNbodykit(voidConvCentDir + "2048Mpc_n2048_convzobov-Voids_cat_centered.npy")
Voids_2048n4096 = LoadVoidCatNbodykit(voidConvCentDir + "2048Mpc_n4096_convzobov-Voids_cat_centered.npy")

#Voids - Random
Voids_2048n512_rand = LoadVoidCatNbodykit(voidConvCentRandDir + "RandomVoids_2048n512.npy")
Voids_2048n1024_rand = LoadVoidCatNbodykit(voidConvCentRandDir + "RandomVoids_2048n1024.npy")
Voids_2048n2048_rand = LoadVoidCatNbodykit(voidConvCentRandDir + "RandomVoids_2048n2048.npy")
Voids_2048n4096_rand = LoadVoidCatNbodykit(voidConvCentRandDir + "RandomVoids_2048n4096.npy")

corr_halohalo_bin1_2048n1024 = LandySzalayEstimator(SimulationBoxPairCount, HalosBin1_2048n1024, HalosBin1_2048n1024, HalosBin1_2048n1024_rand, HalosBin1_2048n1024_rand, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.64, periodic=True, show_progress=True)

np.save(resultsDir + "corr_halohalo_bin1_2048n1024", corr_halohalo_bin1_2048n1024[4]['corr'])

finish = datetime.datetime.now()

print("Processing DONE at", finish)

delta = finish - start

print("Total Processing time:", delta)