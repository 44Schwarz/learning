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
        self.body_length, self.body_width, self.body_height = [float(part) for part in body_whl.split('x')] \
            if body_whl else (0.0, 0.0, 0.0)

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
            if row:
                try:
                    if row[0] == 'car':
                        car_list.append(Car(brand=row[1], photo_file_name=row[3], carrying=float(row[5]),
                                            passenger_seats_count=int(row[2])))
                    elif row[0] == 'truck':
                        car_list.append(Truck(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), 
                                              body_whl=row[4]))
                    elif row[0] == 'spec_machine':
                        car_list.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), 
                                                    extra=row[6]))
                except IndexError:
                    pass
    return car_list


print(get_car_list('cars.csv')[1].get_body_volume())
