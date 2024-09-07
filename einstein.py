def main():
    mass = float(input("Enter mass in kg:  "))
    energy = compute_einsten_of(mass)
    print(f"Energy: {energy} joules")

    

def compute_einsten_of(mass):
    speed_of_light = 3e8
    energy = mass * speed_of_light**2
    return energy

if __name__ == "__main__":
    main()
    
