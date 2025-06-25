## OOP Exercises

# Part 1

# 1. Create a `Vehicle` class without any attribute and methods.

# class vehicle:
# def __init__(self):

# 2. Extend the `Vehicle` class to contain attributes for max speed and colour. Instantiate the class and print out the attributes.


class Vehicle:
    def __init__(self, maxspeed, colour):
        self.maxspeed = maxspeed
        self.colour = colour
        print(
            f"for this vehicle the max speed is {maxspeed} and the colour is {colour}"
        )


Vehicle(100, "Red")

# 3. Extend the `Vehicle` class to contain methods for the below. Instantiate the class and call the two methods to update the attributes. Print the changes out.
#    - Change the value of max speed
#    - Change the car colour


class Vehicle:
    def __init__(self, maxspeed, colour):
        self.maxspeed = maxspeed
        self.colour = colour
        print(
            f"for this vehicle the max speed is {maxspeed} and the colour is {colour}"
        )

    def colour_change(self, new_colour):
        self.colour = new_colour
        print(
            f"for this vehicle the max speed is {self.maxspeed} and the colour is {self.colour}"
        )

    def speed_change(self, new_speed):
        self.maxspeed = new_speed
        print(
            f"for this vehicle the max speed is {self.maxspeed} and the colour is {self.colour}"
        )


car = Vehicle(100, "red")
car.speed_change(250)
car.colour_change("Blue")


# Part 2

# 1. Create a child class `Bus` that will inherit all of the variables and methods of the Vehicle class and nothing else. Instantiate a `Bus` instance and print out the attributes.


class Bus(Vehicle):
    def __init__(self, maxspeed, colour):
        super().__init__(maxspeed, colour)


Bus(300, "yellow")

# 2. Use one of the built-in Python functions to print out the underlying object type of the `Bus` object.

print(type(Bus))

# 3. Use one of the built-in Python functions to print out if the `Bus` object is an instance of `Vehicle`.

print(isinstance(Bus, Vehicle))

# 4. Extend the `Bus` class to also contain an attribute of `seating_capacity`. Add a method to calculate the price of a ticket. This is calculated as `seating_capacity * 0.05`, with an extra 10% of the total of `seating_capacity * 0.05` on top. Instantiate a `Bus` instance and print the ticket price.


class Bus(Vehicle):
    def __init__(self, maxspeed, colour, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(maxspeed, colour)

    def ticket_calc(self):
        return (self.seating_capacity * 0.05) + (0.10 * (self.seating_capacity * 0.05))


new_bus = Bus(300, "yellow", 300)
print(new_bus.ticket_calc())

# 5. Research how to print a `Bus` object in a printable representation. Hint: Look up overriding the `__str__` function. It should print something like `Bus: Max speed: 120, Colour: white, Seating capacity: 40`.
