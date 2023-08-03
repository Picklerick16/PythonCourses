
def main():
    mass = int(input("How much mass in kilograms do you wish to convert to energy? "))
    print((f"{mass_to_energy_conversion(mass):,} joules").replace(",", "."))
    
def mass_to_energy_conversion(mass):
    # E = mc^2
    energy = mass * 299792458**2
    return energy

main()