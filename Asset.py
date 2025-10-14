"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Suruchi Saini
ID: 110434667
Username: saisy026
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    def __str__(self):
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"
