import time

#Start
print("Welcome to the Car Simulator!")
input("Press enter to start the simulation.")

#inisial
speed = 0
warning_index = 0
program = True

#Info printing function
def print_info(speed):
    print("Speed =", speed)
    print()

#Engine starting and idling
time.sleep(1)
print("Engine is idling.")

#accelerating function
def accelerating(acceleration):
    global speed
    speed += acceleration
    time.sleep(1)
    print(speed)

#warning function
def warning_acceleration(speed,acceleration):
    speed += acceleration
    time.sleep(1)
    print_info(speed)
    print("Your vehicle is accelerating dangerously, slow down immediately.")
    
    global warning_index
    warning_index += 1

    return speed

#slowing down function
def slowdown(speed):
    while True:
        speed -= 3
        if speed <= 0:
            speed = 0
            return False
        time.sleep(1)
        print_info(speed)

#to keep the program running
while program == True:
    acceleration = int(input("Input your vehicle's acceleration (in km /(h·s)): "))
    duration = int(input("Input the duration for the occuring acceleration (in seconds): "))

    start_time = time.time()
    while (time.time()-start_time) < duration:
        if warning_index >= 3:
            start_time = time.time()
            slowdown(speed)

        elif warning_index < 3:
            if acceleration < 8:
                print_info(accelerating(acceleration))

            elif acceleration >= 8:
                print_info(warning_acceleration(acceleration,warning_index))

            elif speed >= 120:
                print_info(warning_acceleration(acceleration,warning_index))

print("Your vehicle has been stopped.")