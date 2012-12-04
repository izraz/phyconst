"""Some physical constants

For non-SI units, units are appended to the variable name
"""


BoltzmannConstant = 1.3806503e-23 # Boltzmann constant [J/K]
BoltzmannConstant_TorrLpK = 1.0355758239450354e-22 # Boltzmann constant [Torr L/K]

ProtonCharge = 1.60217646e-19 # proton charge [C]
ElectronCharge = - ProtonCharge


Troom = 293.15 # room temperature [K]

# First ionization potentials [V]
IonizationPotentials = {'N': 14.53, # nitrogen
                        'O': 13.61 # oxygen
                        }


# Backward compatibility ---

BoltzmannConstant_JpK = BoltzmannConstant
IonizationPotentials_V = IonizationPotentials
Troom_K = Troom
ProtonCharge_C = ProtonCharge
ElectronCharge_C = ElectronCharge