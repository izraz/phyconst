# Physical Constants

This is a simple python package with physical constants defined as variables.
I put this together for convenience for my own use.

## Units and naming

Variable naming follows the PhysicalConstants package in Mathematica - names are
descriptive in CamelCase. (Values are not identical to Mathematica though)

All units are SI unless other units are appended with an '_' to variable name.
E.g.
	
	ProtonRestEnergy
	
is the proton rest energy in joules, while

	ProtonRestEnergy_MeV
	
is the proton rest energy in MeV.
Units are explicitly stated in a comment in each variable definition.

## Usage

	from phyconst import BoltzmannConstant as k

## Source

2010 CODATA, accessed from http://physics.nist.gov/cuu/Constants/
