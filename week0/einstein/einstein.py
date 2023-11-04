def main():
    mass = int(input("Enter the mass in kg: "))
    result = energyformula(mass)
    print(result)

def energyformula(mass_in_kg):
    lightspeed = 300000000
    energy = mass_in_kg * pow(lightspeed, 2)
    return energy

main()
