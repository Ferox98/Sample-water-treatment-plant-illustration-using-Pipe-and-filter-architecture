"""
Author: Kaleab Belete (ATR/3763/09) Section-02
Description: This program uses the Pipe-and-Filter architecture to illustrate how water treatment facilities purify water from impurities
"""

class Water:
    def __init__(self, sand_levels, salt_levels, impurities_levels):
        self.sand_levels = sand_levels
        self.salt_levels = salt_levels
        self.impurities_levels = impurities_levels

def SandFilter(water):
    # remove sand impurities from the water
    for i in range(0, water.sand_levels):
        water.sand_levels -= 1

def SaltFilter(water):
    # remove salt impurities from the water
    for i in range(0, water.salt_levels):
        water.salt_levels -= 1

def ImpuritiesFilter(water):
    # remove impurities from the water
    for i in range(0, water.impurities_levels):
        water.impurities_levels -= 1

water = Water(12, 18, 3)

print("Water impurities initially are: " + str(water.sand_levels) + "% sand , " + str(water.salt_levels) + "% salt , " + str(water.impurities_levels) + "% other impurities")

SandFilter(water) 
SaltFilter(water)
ImpuritiesFilter(water)

print("Water impurities after filters have been performed are: " + str(water.sand_levels) + "% sand , " + str(water.salt_levels) + "% salt , " + str(water.impurities_levels) + "% other impurities")

