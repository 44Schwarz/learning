import os
import csv


class Vehicle:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = self.__class__.__name__.lower()
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(Vehicle):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.passenger_seats_count = passenger_seats_count

class Truck(Vehicle):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.body_length, self.body_width, self.body_height = [float(part) for part in  body_whl.split('x')] if body_whl else (0.0, 0.0, 0.0)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height    


class SpecMachine(Vehicle):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            print(row)

    return car_list


c1 = Car('brand', 'photo', 43, 4)
c2 = Truck('br', 'ph', 443, '2x4x0.5')
c3 = SpecMachine('ef', 'gw', 245, 546)
# print(c1.car_type, c1.brand, c1.photo_file_name, c1.carrying)
# print(c2.car_type, c2.body_length, c2.body_width, c2.body_height, c2.get_body_volume())
# print(c3.car_type)
get_car_list('cars.csv')

