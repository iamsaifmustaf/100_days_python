def add(*args):
    print(args)

def calculate(**kwargs):
    print(kwargs)

add(1,2,3,4)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make="nissan", model="GTR")

print(my_car.model)