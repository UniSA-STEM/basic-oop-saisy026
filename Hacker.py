"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset, CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch
from Rig import Rig
class Hacker:
    def __init__(self,name):
        self.name = name
        self.trace_level = 0
        self.inventory = ['CryptoToken']
        self.rig = None
        self.threshold = 5

    def acquire_rig(self,rig):
        for item in self.inventory:
            if item == "CryptoToken":
                self.inventory.remove(item)
                self.rig = rig
                print(f"{self.name} has acquired rig '{rig.name}'.")
                return
        print("No CryptoToken available to acquire rig.")

    def is_exposed(self):
        return self.trace_level > self.threshold



