print("=============HALOS================")
from ObjectInfo import VoidInfo
from ObjectInfo import HaloInfo

print("2048 Mpc, 4096 Resolution")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 2048 Resolution")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 1024 Resolution")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 1024 Resolution - Random")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n1024_1_25_10_random.npy', autoCenter=False, boxLength=2048)

print("\n")

print("2048 Mpc, 512 Resolution")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n512_1_25_10.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 512 Resolution - Random")
HaloInfo('Trial_PP_halo_catalog_2048Mpc_n512_1_25_10_random.npy', autoCenter=False, boxLength=2048)
print("\n")

print("=============VOIDS===============")

#print("2048 Mpc, 4096 Resolution")
#VoidInfo('Trial_PP_halo_catalog_2048Mpc_n4096_1_25_10.npy', autoCenter=False, boxLength=2048)
#print("\n")

#print("2048 Mpc, 2048 Resolution")
#VoidInfo('Trial_PP_halo_catalog_2048Mpc_n2048_1_25_10.npy', autoCenter=False, boxLength=2048)
#print("\n")

print("2048 Mpc, 1024 Resolution")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n1024_1_25_10_centered.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 1024 Resolution - Random")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n1024_1_25_10_centered_random.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 512 Resolution")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n512_1_25_10_centered.npy', autoCenter=False, boxLength=2048)
print("\n")

print("2048 Mpc, 512 Resolution")
VoidInfo('Trial_PP_void_catalog_2048Mpc_n512_1_25_10_centered_random.npy', autoCenter=False, boxLength=2048)
print("\n")