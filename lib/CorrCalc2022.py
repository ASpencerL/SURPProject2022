from nbodykit.lab import *
#import matplotlib.pyplot as plt

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

halodir2022 = "/home/alexander/surp2022/SURPProject2022/cat/halo/2022Test/"
voiddir2022 = "/home/alexander/surp2022/SURPProject2022/cat/void/default/2022Test/"
resultsDir = "/home/alexander/surp2022/SURPProject2022/results/corrfunc/2022Test/"

print("No axions, 2048n4096")

HaloMassBin1 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_massmin_680000000000.0_massmax_3927384460000.0.npy")
HaloMassBin2 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_massmin_3927384460000.0_massmax_22682865800000.0.npy")
HaloMassBin3 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_massmin_22682865800000.0_massmax_131006374000000.0.npy")
HaloMassBin4 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_massmin_131006374000000.0_massmax_756635880000000.0.npy")
HaloMassBin5 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_massmin_756635880000000.0_massmax_4370000000000000.0.npy")

HaloMassBin1_Random = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin1.npy")
HaloMassBin2_Random = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin2.npy")
HaloMassBin3_Random = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin3.npy")
HaloMassBin4_Random = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin4.npy")
HaloMassBin5_Random = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin5.npy")

VoidMassBin1 = LoadVoidCatNbodykit(voiddir2022 + "2048Mpc_n4096zobov-Voids_cat_massmin_1e+44_massmax_1.67952207e+46.npy", autoCenter=False)
VoidMassBin2 = LoadVoidCatNbodykit(voiddir2022 + "2048Mpc_n4096zobov-Voids_cat_massmin_1.67952207e+46_massmax_3.95657784e+47.npy", autoCenter=False)

VoidMassBin1_Random = LoadVoidCatNbodykit(voiddir2022 + "RandomVoids_2048n4096_bin1.npy", autoCenter=False)
VoidMassBin2_Random = LoadVoidCatNbodykit(voiddir2022 + "RandomVoids_2048n4096_bin2.npy", autoCenter=False)

print("\n")

print("1 25 10, 2048n4096")

HaloMassBin1_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_680000000000.0_massmax_3927384460000.0.npy")
HaloMassBin2_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_3927384460000.0_massmax_22682865800000.0.npy")
HaloMassBin3_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_22682865800000.0_massmax_131006374000000.0.npy")
HaloMassBin4_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_131006374000000.0_massmax_756635880000000.0.npy")
HaloMassBin5_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10_massmin_756635880000000.0_massmax_4370000000000000.0.npy")

HaloMassBin1_Random_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin1_1_25_10.npy")
HaloMassBin2_Random_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin2_1_25_10.npy")
HaloMassBin3_Random_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin3_1_25_10.npy")
HaloMassBin4_Random_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin4_1_25_10.npy")
HaloMassBin5_Random_1_25_10 = LoadHaloCatNbodykit(halodir2022 + "RandomHalos_2048n4096_bin5_1_25_10.npy")

VoidMassBin1_1_25_10 = LoadVoidCatNbodykit(voiddir2022 + "2048Mpc_n4096_1_25_10zobov-Voids_cat_massmin_1e+44_massmax_1.67952207e+46.npy", autoCenter=False)
VoidMassBin2_1_25_10 = LoadVoidCatNbodykit(voiddir2022 + "2048Mpc_n4096_1_25_10zobov-Voids_cat_massmin_1.67952207e+46_massmax_3.95657784e+47.npy", autoCenter=False)

VoidMassBin1_Random_1_25_10 = LoadVoidCatNbodykit(voiddir2022 + "RandomVoids_2048n4096_bin1_1_25_10.npy", autoCenter=False)
VoidMassBin2_Random_1_25_10 = LoadVoidCatNbodykit(voiddir2022 + "RandomVoids_2048n4096_bin2_1_25_10.npy", autoCenter=False)

#2048n4096, HALO-HALO, NO AXIONS
corr_halohalo_Mass5 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin5, HaloMassBin5, HaloMassBin5_Random, HaloMassBin5_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
print("done 5")
np.save(resultsDir + "corr_halohalo_Mass5", corr_halohalo_Mass5[4]['corr'])

corr_halohalo_Mass4 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin4, HaloMassBin4, HaloMassBin4_Random, HaloMassBin4_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
print("done 4")
np.save(resultsDir + "corr_halohalo_Mass4", corr_halohalo_Mass4[4]['corr'])

corr_halohalo_Mass3 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin3, HaloMassBin3, HaloMassBin3_Random, HaloMassBin3_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
print("done 3")
np.save(resultsDir + "corr_halohalo_Mass3", corr_halohalo_Mass3[4]['corr'])

corr_halohalo_Mass2 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin2, HaloMassBin2, HaloMassBin2_Random, HaloMassBin2_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
print("done 2")
np.save(resultsDir + "corr_halohalo_Mass2", corr_halohalo_Mass2[4]['corr'])

corr_halohalo_Mass1 = LandySzalayEstimator(SimulationBoxPairCount, HaloMassBin1, HaloMassBin1, HaloMassBin1_Random, HaloMassBin1_Random, R1R2=None, logger=None, mode='1d', edges=histogram_bins_3d, BoxSize=1392.7, periodic=True, show_progress=True)
print("done 1")
np.save(resultsDir + "corr_halohalo_Mass1", corr_halohalo_Mass1[4]['corr'])