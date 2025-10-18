"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    def encrypt(self):
        self.encrypted = True
        print(f'Asset {self.name} is now encrypted.')

    def decrypt(self):
        self.encrypted = False
        print(f'Asset {self.name} is now decrypted.')

    def __str__(self):
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"

# The core assets include - CryptoToken, Data Spike, Removable Drive, Security Chip, Hardware Patch.

class CryptoToken(Asset):
    def _init_(self):
        super()._init_("CryptoToken", "Used to acquire or repair rigs.")

class DataSpike(Asset):
    def _init_(self):
        super()._init_("Data Spike", "Used in battles.")

class RemovableDrive(Asset):
    def _init_(self):
        super()._init_("Removable Drive", "Found in rigs and used for extraction.")

class SecurityChip(Asset):
    def _init_(self):
        super()._init_("Security Chip", "Used to encrypt or decrypt assets.")

class HardwarePatch(Asset):
    def _init_(self):
        super()._init_("Hardware Patch", "Used to upgrade rigs.")

