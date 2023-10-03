from GenerateRandoms import GenerateRandomHalos
from GenerateRandoms import GenerateRandomVoids

#HALOS
#GenerateRandomHalos("Trial_PP_halo_catalog_2048Mpc_n512_1_25_10.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False)
#GenerateRandomHalos("Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False)
#GenerateRandomHalos("Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False)
GenerateRandomHalos("Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False)

#VOIDS
#GenerateRandomVoids("Trial_PP_void_catalog_2048Mpc_n512_1_25_10_centered.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False, autoCenter=False)
#GenerateRandomVoids("Trial_PP_void_catalog_2048Mpc_n1024_1_25_10_centered.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False, autoCenter=False)
#GenerateRandomVoids("Trial_PP_void_catalog_2048Mpc_n2048_1_25_10_centered.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False, autoCenter=False)
GenerateRandomVoids("Trial_PP_void_catalog_2048Mpc_n4096_1_25_10.npy", seed=0, export_rand_file=True, fileAppendix="random", include_rand_plot=False, autoCenter=False)