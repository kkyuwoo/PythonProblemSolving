import math
import sys
a, b = map(int, sys.stdin.readline().split())
c, d = map(int ,sys.stdin.readline().split())
denominator = math.lcm(b, d)
molecule = denominator // b * a + denominator // d * c
if math.gcd(molecule, denominator) != 1:
    r_molecule = molecule // math.gcd(molecule, denominator)
    r_denominator = denominator // math.gcd(molecule, denominator)
    molecule = r_molecule
    denominator = r_denominator
print(molecule, denominator)