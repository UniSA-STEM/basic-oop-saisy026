"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self,name):
        self.name = name
        self.trace_level = 0
        self.inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.rig = None
        self.threshold = 5

    def acquire_rig(self,rig):
        for i in self.inventory:
            if i == 'CryptoToken':
                self.inventory.remove(i)
                self.rig = rig
                print(f"{self.name} has acquired rig '{rig.name}'.")
                return
        print("No CryptoToken available to acquire rig.")

    def is_exposed(self):
        return self.trace_level > self.threshold

    def launch_data_spike(self, target_rig):
        if not self.rig:
            print('Rig not found for attack.')
            return
        if self.is_exposed():
            print('Some Actions are blocked as the hacker is exposed.')
            return
        if not self.rig.release_asset("Data Spike"):
            print('Attack is fails as rig have no Data Spike.')
            return

        target_rig.take_hit()
        self.trace_level += 2
        print(f"Attack launched. Trace increased to {self.trace_level}.")

# method to encrypt or decrypt an asset in inventory or rig storage.
# Requires a Security Chip somewhere (inventory or rig storage).
# action: 'encrypt' or 'decrypt'
# location: 'inventory' or 'rig'

    def change_asset_encryption(self, asset_name, action, location):
        if action not in ('encrypt', 'decrypt'):
            print("Invalid action. Use 'encrypt' or 'decrypt'.")
            return False

        # determine storage based on location
        if location == 'inventory':
            storage = self.inventory
        elif location == 'rig' and self.rig:
            storage = self.rig.storage
        else:
            print("Failed due to invalid location or no rig.")
            return False

        # check for security chip
        chip_found = False
        for i in self.inventory:
            if i.name == 'Security Chip':
                chip_found = True
                break
        if not chip_found and self.rig:
            for j in self.rig.storage:
                if j.name == 'Security Chip':
                    chip_found = True
                    break
        if not chip_found:
            print("Failed due to no Security Chip found.")
            return False

        # Find the asset
        asset = None
        for i in storage:
            if i.name == asset_name:
                asset = i
                break
        if not asset:
            print(f"Failed: asset not found in {location}.")
            return False

        # Perform action
        if action == 'encrypt':
            asset.encrypt()
            print(f"{asset.name} encrypted in {location}.")
        else:  # decrypt
            if not asset.encrypted:
                print("Asset already decrypted.")
            else:
                asset.decrypt()
                print(f"{asset.name} decrypted in {location}.")

        return True

    def upgrade_rig(self):
        if not self.rig:
            print("Unable to upgrade as no rig available.")
            return False
        # Search for a Hardware Patch in inventory
        for asset in self.inventory:
            if asset.name == 'Hardware Patch':
                self.inventory.remove(asset)  # remove the patch
                message = self.rig.upgrade()  # upgrade the rig
                print(message)
                return True

        print("Unable to upgrade as no Hardware Patch found in inventory.")
        return False


# method to move one or all assets from inventory to rig storage.

    def store_to_rig(self, asset_name=None):
        if not self.rig:
            print("Failed to store: no rig available.")
            return False

        # Move all assets
        if asset_name is None:
            moved = len(self.inventory)
            # Move each asset individually
            for asset in list(self.inventory):
                self.rig.storage.append(asset)
                self.inventory.remove(asset)
            print(f"Moved {moved} assets to rig storage.")
            return True

        # Move one asset
        for asset in self.inventory:
            if asset.name == asset_name:
                self.rig.storage.append(asset)
                self.inventory.remove(asset)
                print(f"Moved {asset_name} to rig storage.")
                return True

        print("Failed to store: asset not found in inventory.")
        return False

