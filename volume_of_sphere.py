import math

def calculate_volume_of_sphere(radius):
    pi = math.pi
    volume = (4/3) * pi * radius ** 3
    return volume

def main():
    radius1 = 30
    volume1 = calculate_volume_of_sphere(radius1)
    print(f"The volume of sphere with radius {radius1} is: {volume1}")

    radius2 = 40
    volume2 = calculate_volume_of_sphere(radius2)
    print(f"The volume of sphere with radius {radius2} is: {volume2}")

main()
