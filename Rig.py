"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset, CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage = [DataSpike(), DataSpike(), RemovableDrive()]

    def take_hit(self):
        for item in self.storage:
            if item == "CryptoToken":
                self.damage += 1
                print(f"{self.name} hit taken. Currently the damage is {self.damage}")
                if self.damage >= 2 and self.upgrade_level == 0:
                    self.broken = True
                    print(f"{self.name} is broken")
            return
        print("No DataSpike found for hit.")

    def repair(self):
        for item in self.storage:
            if item == "CryptoToken":
                if self.broken:
                    self.damage = 0
                    self.broken = False
                    print(f"{self.name} has been repaired using a CryptoToken.")
                else:
                    print(f"{self.name} does not need repairs.")
                return
        print("No CryptoToken found for repair.")

    def upgrade(self):
        for item in self.storage:
            if item == "Hardware Patch":
                self.storage.remove(item)
                self.upgrade_level += 1
                print(f"{self.name} upgraded to Level {self.upgrade_level}.")
                return
        print("No Hardware Patch available to upgrade rig.")


# generate assets method. Rig has no control over what type of Asset is generated but generate 1 asset each time.

    def generate_asset(self, asset_name):
        asset_list = {
        "CryptoToken": "Used to acquire or repair rigs.",
        "Data Spike": "Used in battles.",
        "Removable Drive": "Found in rigs and used for extraction.",
        "Security Chip": "Used to encrypt or decrypt assets.",
        "Hardware Patch": "Used to upgrade rigs.",
    }
        if asset_name not in asset_list:
            print(f"Unknown asset type: {asset_name}")
            return None

        new_asset = Asset(asset_name, asset_list[asset_name])
        self.storage.append(new_asset)
        return new_asset


# store and release methods

    def release_asset(self, asset_name):
        for asset in self.storage:
            if asset.name == asset_name:
                if asset.encrypt():
                    print(f"Asset {asset.name} cannot transfer and release because it is encrypted.")
                    return None
                self.storage.remove(asset)
                return asset

        print(f"Asset {asset_name} not found in storage.")
        return None

    def store_asset(self, asset):
        if asset.encrypt():
            print(f"Asset {asset.name} cannot transfer and release because it is encrypted.")
            return False
        self.storage.append(asset)
        return True

# condition method which return the rig’s conditon based on damage and upgrade level.

    def get_condition(self):
        if self.broken:
            status = "Broken"
        elif self.damage >= 0:
            status = "Damaged"
        else:
            status = "Pristine"
        return f"{status} (Level {self.upgrade_level})"

# The string conversion method which print the rig’s name, conditon, upgrade level, and stored assets.
