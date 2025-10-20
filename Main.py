"""
File: main.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from Hacker import Hacker
from Rig import Rig
from Asset import Asset

print("STARTING SYSTEM")

# Create hacker and rig
hacker = Hacker("Batman")
rig = Rig("AlphaRig")
print(hacker)
print(rig)
print()

# Hacker acquires the rig
print("ACQUIRING RIG")
hacker.acquire_rig(rig)
print(hacker)
print()

# Generate and store some assets
print("GENERATING AND STORING ASSETS")
rig.generate_asset("Hardware Patch")
rig.generate_asset("Security Chip")
rig.generate_asset("Data Spike")
print(rig)
print()

# Move one asset to hacker inventory
print("MOVING ASSET TO HACKER INVENTORY")
asset_to_move = rig.release_asset("Security Chip")
if asset_to_move:
    hacker.inventory.append(asset_to_move)
print(hacker)
print(rig)
print()

# Encrypt and decrypt assets
print("ENCRYPTION TEST")
hacker.change_asset_encryption("Security Chip", "encrypt", "inventory")
hacker.change_asset_encryption("Security Chip", "decrypt", "inventory")
print()

# Upgrade rig
print("UPGRADING RIG")
hacker.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs."))
hacker.upgrade_rig()
print(rig)
print()

# Simulate a data spike attack
print("DATA SPIKE ATTACK")
target_rig = Rig("TargetRig")
hacker.launch_data_spike(target_rig)
print(target_rig)
print()

# Test damage and repair
print("DAMAGE AND REPAIR TEST")
target_rig.take_hit()
target_rig.take_hit()
print(target_rig)
target_rig.generate_asset("CryptoToken")
target_rig.repair()
print(target_rig)
print()

# Transfer assets between rig and hacker
print("ASSET TRANSFER TEST")
hacker.store_to_rig()  # move all to rig
print(hacker)
print(rig)
hacker.retrieve_from_rig()  # get all back
print(hacker)
print(rig)

print("DEMONSTRATION COMPLETE")

