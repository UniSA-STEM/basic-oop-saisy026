"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self,name):
        self.name = name
        self.trace_level = 0
        self.inventory = []
        self.rig = None

    def acquire_rig(self,rig):
        for item in self.inventory:
            if item.name == "CryptoToken":
                self.inventory.remove(item)
                self.rig = rig
                print(f"{self.name} has acquired rig '{rig.name}'.")
                return
        print("No CryptoToken available to acquire rig.")

