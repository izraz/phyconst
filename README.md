# Physical Constants

This is a simple python package with physical constants defined as variables.
I put this together for convenience for my own use.

## Units

All units are SI unless other units are appended with an '_' to variable name.
Units are explicitly stated in a comment in each variable definition.

## Naming

Variable naming follows the PhysicalConstants package in Mathematica - 
are descriptive in CamelCase, e.g.

	BoltzmannConstant

for the Botzmann constant in units J/K.
(Values are not identical to Mathematica though)

## Usage

	from phyconst import BoltzmannConstant as k

## Source

2010 CODATA, accessed from http://physics.nist.gov/cuu/Constants/
