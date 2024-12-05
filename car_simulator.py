import time

#Start
print("Welcome to the Car Simulator!")
input("Press enter to start the simulation.")

#inisial
speed = 0 # speed = int
warning_index = 0 # warning_index = int
program = True

#Engine starting and idling
time.sleep(1)
print("Engine is idling.")

#accelerating function
def accelerating(acceleration):
    global speed
    speed += acceleration
    time.sleep(1)
    print("speed =", speed)
    print()

#warning function
def warning_acceleration(speed, acceleration):
    time.sleep(1)
    print("speed =", speed)
    print("Your vehicle is accelerating dangerously, slow down immediately.")
    print()

    global warning_index
    warning_index += 1

#slowing down function
def slowdown(speed):
    global program
    while program == True:
        speed -= 3
        if speed <= 0:
            speed = 0
            program = False
        time.sleep(1)
        print("speed =", speed)
        print()
   
#to keep the program running
while program == True:
    acceleration = int(input("Input your vehicle's acceleration (in km /(h·s)): "))
    duration = int(input("Input the duration for the occuring acceleration (in seconds): "))

    start_time = time.time()
    while (time.time()-start_time) < duration:
        if warning_index >= 3:
            start_time = time.time()
            slowdown(speed)
            break

        elif warning_index < 3:
            if acceleration < 8 and speed < 120:
                accelerating(acceleration)

            elif acceleration >= 8 and speed < 120:
                print("You can\'t accelerate your car because it\'s too fast")
                break

            elif speed >= 120:
                speed += acceleration
                warning_acceleration(speed, acceleration)
                
    
print("Your vehicle has been stopped.")
