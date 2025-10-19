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

