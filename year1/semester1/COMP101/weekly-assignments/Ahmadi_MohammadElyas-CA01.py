#Ahmadi_MohammadElyas  201792013  Ahmadi_MohammadElyas-CA01.py  October 2025
#Computing barge draft from length, breadth, height inputs and Output calculations


# Input three dimensions of the barge in meters
length = float(input("Enter the length of the barge in meters: "))
breadth = float(input("Enter the breadth of the barge in meters: "))
height = float(input("Enter the height of the barge in meters: "))


# Calculating base area and total surface area (4 walls + floor)
base_area = float(breadth * length)
area_of_the_4_walls = float(2 * height * (breadth + length))
total_surface_area = float(base_area + area_of_the_4_walls)

# Calculating the mass of iron (1.06 kg per m^2)
iron_weight = 1.06
mass = float(iron_weight * total_surface_area)

# Draft calculation:
draft = float(mass/base_area)


print("You entered the following values:")
print(f"Length: {length:.2f} meters")
print(f"Breadth: {breadth:.2f} meters")
print(f"Height: {height:.2f} meters")
print(f"Surface area: {total_surface_area:.2f} square meters")
print(f"Mass: {mass:.2f} kg")
print(f"Draft: {draft:.2f} meters")



"""
Test Results:

| Test | length, breadth, height |  expected draft    | actual draft | comment |
|------|-------------------------|--------------------|--------------|---------|
| 1    | 10, 7, 3                | 2.604571428571429  |  2.60(2dp)   |  Okay   |
| 2    | 3, 10, 7                | 7.490666666666667  |  7.49(2dp)   |  Okay   |
| 3    | 7, 3, 10                | 11.15523809523809  |  11.16(2dp)  |  Okay   |
| 4    | 2, 5, 9                 | 14.416             |  14.42(2dp)  |  Okay   |
| 5    | 5, 9, 2                 | 2.379111111111111  |  2.38(2dp)   |  Okay   |
| 6    | 9, 2, 5                 | 7.537777777777778  |  7.54(2dp)   |  Okay   |
| 7    | 9, 9, 9                 | 5.3                |  5.30(2dp)   |  Okay   |

"""