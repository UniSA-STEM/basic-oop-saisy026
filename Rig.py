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
