import math


class Calculator:

    def __init__(self):
        self.state = 0
        self.first_run = True
        self.trig_mode = 'degrees'

    def get_state(self):
        return self.state

    def set_state(self, x):
        self.state = x

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if x == 0 or y == 0:
            return "cannot divide by 0"
        return x / y

    def square(self, x):
        return x ** 2

    def square_root(self, x,):
        return math.sqrt (x)

    def exponentiate(self, x, y):
        return x ** y

    def inverse(self, x):
        if x == 0:
            return 'cannot divide by 0'
        return 1/x

    def invert_sign(self, x):
        return -x

    def clear(self):
        self.display = 0

    def display_error(self):
        self.diplay = "Err"

    def set_display(self,x):
        self.display = x

    def get_display(self):
        return self.display

    def sine(self, x):
        if self.trig_mode == "degrees":
            return math.sin(math.radians(x))
        else:
            return math.sin(x)

    def cosine(self, x):
        if self.trig_mode == "degrees":
            return math.cos(math.radians(x))
        else:
            return math.cos(x)

    def tangent(self, x):
        if self.trig_mode == "degrees":
            return math.tan(math.radians(x))
        else:
            return math.tan(x)

    def inverse_sine(self, x):
        if self.trig_mode == "degrees":
            return math.asin(math.radians(x))
        else:
            return math.asin(x)

    def inverse_cosine(self, x):
        if self.trig_mode == "degrees":
            return math.acos(math.radians(x))
        else:
            return math.acos(x)

    def inverse_tangent(self, x):
        if self.trig_mode == "degrees":
            return math.atan(math.radians(x))
        else:
            return math.atan(x)
    
    def get_current_trig_unit(self):
        return self.trig_mode

    def toggle_trig_unit(self):
        if self.trig_mode == 'radians':
            self.trig_mode = 'degrees' 
        else:
            self.trig_mode = 'radians'

    def factorial(self, x):
        return math.factorial(x)

    def natural_log(self, x):
        return math.log(x)

    def log(self, x, y):
        return math.log(x,y)



# add lots more methods to this calculator class.
