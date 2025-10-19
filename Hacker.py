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
        for item in self.inventory:
            if item == "CryptoToken":
                self.inventory.remove(item)
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

    def

