"""Physical Constants

Units
-----
All units are SI unless other units are appended with an '_' to variable name.

Naming
------
Variable naming follows the PhysicalConstants package in Mathematica.
(Values are not identical to Mathematica though)

Source
------
2010 CODATA, accessed from http://physics.nist.gov/cuu/Constants/
(unless otherwise indicated)
"""

SpeedOfLight    = 299792458 # speed of light in vacuum [m/s]


# elementary charge
ElementaryCharge = 1.602176565e-19 # [C]
ProtonCharge = ElementaryCharge
ElectronCharge = - ElementaryCharge # Note: sign differs from Mathematica!

# proton mass
ProtonMass   = 1.672621777e-27 # [kg]
ProtonMass_amu = 1.007276466812 # [amu]

# proton rest energy (ProtonMass * SpeedOfLight**2)
ProtonRestEnergy = 1.503277484e-10 # [J]
ProtonRestEnergy_MeV = 938.272046 # [MeV]

# electron mass
ElectronMass = 9.10938291e-31 # [kg]
ElectronMass_amu = 5.4857990946e-4 # [amu]

# electron rest energy (ElectronMass * SpeedOfLight**2)
ElectronRestEnergy = 8.18710506e-14 # [J]
ElectronRestEnergy_MeV = 0.510998928 # [MeV]

# Boltzmann constant
BoltzmannConstant =  1.3806488e-23 # [J/K]
BoltzmannConstant_TorrLpK = 1.0355746e-22 # [Torr L/K] (*calculated)

# room temperature
Troom = 293.15 # [K]

# First ionization potentials
# source: http://www.nist.gov/data/nsrds/NSRDS-NBS34.pdf
IonizationPotentials = {'N': 14.534, # nitrogen
                        'O': 13.618 # oxygen
                        } # [V]

# Standard atomic mass
# source: Wikipedia
AtomicMass_amu = {'He': 4.002602} # [amu]

