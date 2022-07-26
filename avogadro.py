from math import pi
import sys


def main():
    disFile = sys.stdin.read().split() if not (
        sys.stdin.isatty()) else open('displacements.txt').read().split()
    fi2 = 0
    DelT = 0.5
    for i in disFile:
        fi2 += ((float(i)*0.175*(10**(-6)))**2)/(2*len(disFile))
    D = fi2/(2*DelT)
    k = (D*6*pi*9.135*(10**(-4))*0.5*(10**(-6)))/297
    avogadro = 8.31446/k
    print(f'boltzmann : {k}\navogadro : {avogadro}')


main()
