#Ahmadi_MohammadElyas 201792013 October2025 CA02.py
"""This program calculates the rover’s movement and battery usage on the Moon’s surface.
It determines if the rover reaches its target destination and whether it has enough battery to return or must recharge."""


import math

full_battery = 100
speed = 1.5
battery_usage_per_second = 2.7

angle_deg = float(input("Enter an angle in degrees from 0 to 90: "))
travel_time = float(input("Enter the time of travel in seconds: "))

#Converting angle from degrees to radians:
angle_radians = math.radians(angle_deg)

#To Calculate the total travelled distance:
total_distance = speed * travel_time

#To calculate the battery used during the travel:
battery_used = travel_time * battery_usage_per_second
battery_remaining = full_battery - battery_used

#To Calculate the horizontal and vertical distance:
horizontal_distance = total_distance * math.sin(angle_radians)
vertical_distance = total_distance * math.cos(angle_radians)


print(f"\n Input values received:")
print(f"Angle of travel: {angle_deg} degrees")
print(f"Travel time: {travel_time} seconds")
print("\n Calculations and reasoning:")

if battery_used <= full_battery:
    print("The rover has successfully reached the target position!")
    print(f"Overall distance travelled: {total_distance:.2f} meters")
    print(f"Horizontal movement: {horizontal_distance:.2f} meters")
    print(f"Vertical movement: {vertical_distance:.2f} meters")
    print(f"Battery used: {battery_used:.2f}%")
    print(f"Battery remaining: {battery_remaining:.2f}%")


    if battery_remaining >= battery_used:
        print("The rover has enough battery to return to the start point.")
    else:
        print(f"Now, the rover must wait at the destination to recharge. It needs an additional {battery_used - battery_remaining:.2f}% battery to return to the start point.")

else:
    actual_travel_time = full_battery / battery_usage_per_second
    actual_distance = speed * actual_travel_time
    actual_horizontal = actual_distance * math.sin(angle_radians)
    actual_vertical = actual_distance * math.cos(angle_radians)
    remaining_distance = (travel_time - actual_travel_time) * speed
    extra_battery_needed = (travel_time - actual_travel_time) * battery_usage_per_second

    print(f"Destination NOT achieved!")
    print(f"Intended total distance: {total_distance:.2f} m")
    print(f"Distance actually travelled: {actual_distance:.2f} m")
    print(f"Battery depleted after {actual_travel_time:.2f} seconds of travel.")
    print(f"Horizontal position reached: {actual_horizontal:.2f} m")
    print(f"Vertical position reached: {actual_vertical:.2f} m")
    print(f"Remaining distance to target: {remaining_distance:.2f} m")
    print(f"Additional battery power required: {extra_battery_needed:.2f}%")
    print("Status: Destination NOT achieved.")
    print("The rover is waiting at its current position to recharge before it can continue to the target destination.")


'''
Test Table:

| Test | Angle | Time | Expected Result                                          | Actual Result                           | Comment |
|------|-------|------|----------------------------------------------------------|-----------------------------------------|---------|
| 1    | 67    | 10   | Overall distance = 15.0 m                                | Overall distance = 15.00 m              | okay    |
|      |       |      | Horizontal movement = 13.807572801786606 m               | Horizontal movement = 13.81 m           | okay    |
|      |       |      | Vertical movement = 5.860966927339105 m                  | Vertical movement = 5.86 m              | okay    |
|      |       |      | Battery used = 27.0%                                     | Battery used = 27.00%                   | okay    |
|      |       |      | Battery remaining = 73.0%                                | Battery remaining = 73.00%              | okay    |
|      |       |      | Destination achieved;                                    | Destination achieved;                   | okay    |
|      |       |      | rover has enough battery to return.                      | rover has enough battery to return.     | okay    |
--------------------------------------------------------------------------------------------------------------------------------------
| 2    | 17.95 |36.579| Overall distance = 54.8685 m                             | Overall distance = 54.87 m              | okay    |
|      |       |      | Horizontal movement = 16.90975420856197 m                | Horizontal movement = 16.91 m           | okay    |
|      |       |      | Vertical movement = 52.19782088225543 m                  | Vertical movement = 52.20 m             | okay    |
|      |       |      | Battery used = 98.76330000000002%                        | Battery used = 98.76%                   | okay    |
|      |       |      | Battery remaining = 1.2366999999999848%                  | Battery remaining = 1.24%               | okay    |
|      |       |      | Destination achieved;                                    | Destination achieved;                   | okay    |
|      |       |      | not enough battery to return.                            | not enough battery to return.           | okay    |
Now, the rover must wait at the destination to recharge. It needs an additional 97.53% battery to return to the start point.
--------------------------------------------------------------------------------------------------------------------------------------
| 3    | 0     | 5.6  | Overall distance = 8.399999999999999 m                   | Overall distance = 8.40 m               | okay    |
|      |       |      | Horizontal movement = 0.0 m                              | Horizontal movement = 0.00 m            | okay    |
|      |       |      | Vertical movement = 8.399999999999999 m                  | Vertical movement = 8.40 m              | okay    |
|      |       |      | Battery used = 15.12%                                    | Battery used = 15.12%                   | okay    |
|      |       |      | Battery remaining = 84.88%                               | Battery remaining = 84.88%              | okay    |
|      |       |      | Destination achieved;                                    | Destination achieved;                   | okay    |
|      |       |      | rover has enough battery to return.                      | rover has enough battery to return.     | okay    |
--------------------------------------------------------------------------------------------------------------------------------------
| 4    | 90    | 21   | Overall distance = 31.5 m                                | Overall distance = 31.50 m              | okay    |
|      |       |      | Horizontal movement = 31.5 m                             | Horizontal movement = 31.50 m           | okay    |
|      |       |      | Vertical movement = 0.0 m                                | Vertical movement = 0.00 m              | okay    |
|      |       |      | Battery used = 56.7%                                     | Battery used = 56.70%                   | okay    |
|      |       |      | Battery remaining = 43.3%                                | Battery remaining = 43.30%              | okay    |
|      |       |      | Destination achieved;                                    | Destination achieved;                   | okay    |
|      |       |      | not enough battery to return.                            | not enough battery to return.           | okay    |
Now, the rover must wait at the destination to recharge. It needs an additional 13.40% battery to return to the start point.
--------------------------------------------------------------------------------------------------------------------------------------
| 5    | 45    | 37.1 | Intended total distance = 55.650 m                       | Intended total distance = 55.65 m       | okay    |
|      |       |      | Overall distance travelled = 55.55555555555555 m         | Overall distance travelled = 55.56 m    | okay    |
|      |       |      | Battery ran out after 37.03703703703704 seconds          | Battery ran out after = 37.04 seconds   | okay    |
|      |       |      | Horizontal position reached = 39.28371006591931 m        | Horizontal position reached = 39.28 m   | okay    |
|      |       |      | Vertical position reached = 39.28371006591931 m          | Vertical position reached = 39.28 m     | okay    |
|      |       |      | Remaining distance to target = 0.094444444444444 m       | Remaining distance to target = 0.09 m   | okay    |
|      |       |      | Extra battery needed = 0.17%                             | Extra battery needed = 0.17%            | okay    |
|      |       |      | Destination not achieved.                                | Destination not achieved.               | okay    |
The rover is waiting at its current position to recharge before it can continue to the target destination.
--------------------------------------------------------------------------------------------------------------------------------------
| 6    | 72.9  | 100  | Intended total distance = 150.0 m                        | Intended total distance = 150.00 m      | okay    |
|      |       |      | Overall distance travelled = 55.55555555555555 m         | Overall distance travelled = 55.56 m    | okay    |
|      |       |      | Battery ran out after 37.03703703703704 seconds          | Battery ran out after = 37.04 seconds   | okay    |
|      |       |      | Horizontal position reached = 53.09961193324057 m        | Horizontal position reached = 53.10 m   | okay    |
|      |       |      | Vertical position reached = 16.335573624016885 m         | Vertical position reached = 16.34 m     | okay    |
|      |       |      | Remaining distance to target = 94.44444444444444 m       | Remaining distance to target = 94.44 m  | okay    |
|      |       |      | Extra battery needed = 170.0%                            | Extra battery needed = 170.00%          | okay    |
|      |       |      | Destination not achieved.                                | Destination not achieved.               | okay    |
The rover is waiting at its current position to recharge before it can continue to the target destination.
--------------------------------------------------------------------------------------------------------------------------------------
| 7    | 90    | 52.9 | Intended total distance = 79.35 m                        | Intended total distance = 79.35 m       | okay    |
|      |       |      | Overall distance travelled = 55.55555555555555 m         | Overall distance travelled = 55.56 m    | okay    |
|      |       |      | Battery ran out after 37.03703703703704 seconds          | Battery ran out after = 37.04 seconds   | okay    |
|      |       |      | Horizontal position reached = 55.55555555555555 m        | Horizontal position reached = 55.56 m   | okay    |
|      |       |      | Vertical position reached = 0.0 m                        | Vertical position reached = 0.00 m      | okay    |
|      |       |      | Remaining distance to target = 23.79444444444444 m       | Remaining distance to target = 23.79 m  | okay    |
|      |       |      | Extra battery needed = 42.83%                            | Extra battery needed = 42.83%           | okay    |
|      |       |      | Destination not achieved.                                | Destination not achieved.               | okay    |
The rover is waiting at its current position to recharge before it can continue to the target destination.
--------------------------------------------------------------------------------------------------------------------------------------
| 8    | 0     |10000 | Intended total distance = 15000.0 m                      | Intended total distance = 15000.00 m    | okay    |
|      |       |      | Overall distance travelled = 55.55555555555555 m         | Overall distance travelled = 55.56 m    | okay    |
|      |       |      | Battery ran out after 37.03703703703704 seconds          | Battery ran out after = 37.04 seconds   | okay    |
|      |       |      | Horizontal position reached = 0.0 m                      | Horizontal position reached = 0.00 m    | okay    |
|      |       |      | Vertical position reached = 55.55555555555555 m          | Vertical position reached = 55.56 m     | okay    |
|      |       |      | Remaining distance to target = 14944.444444444444 m      | Remaining distance to target =14944.44 m| okay    |
|      |       |      | Extra battery needed = 26900%                            | Extra battery needed = 26900.00%        | okay    |
|      |       |      | Destination not achieved.                                | Destination not achieved.               | okay    |
The rover is waiting at its current position to recharge before it can continue to the target destination.
--------------------------------------------------------------------------------------------------------------------------------------
'''