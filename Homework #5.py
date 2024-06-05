# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.

class Transport:
    tires=4
    fuel_type='Gasoline'
    max_speed=250
    engine='Internal combustion engine'
    lights=4

    @staticmethod
    def transport_types():
        print('\nCommon Transport Types: Car, Bus, Motorcycle, Scooter, Truck, Bicycle, Minibus...')

    @classmethod
    def common_transport_maxspeed(cls):
        print(f"\nCommon max speed in vehicles is {cls.max_speed} km/h")

    @classmethod
    def common_transport_engine(cls):
        print(f"\nCommon engine type in vehicles is {cls.engine}")

    def __init__(self, type, brand, capacity, engine):
        self.type = type
        self.brand=brand
        self.capacity = capacity
        self.engine = engine

    def say_vehicle(self):
        print(f"\nHi, I have a {self.type} and it's a {self.brand}.")

    def say_capacity(self):
        print(f"My {self.type} can fit {self.capacity} people.")

    def __repr__(self):
        return f'\nTransport(Type: {self.type}, Brand: {self.brand}, Capacity: {self.capacity}, Engine: {self.engine})'


car=Transport('Car', 'Ford', 5, 'Gasoline')
bus=Transport('Bus', 'Toyota', 25, 'Diesel')
motorcycle=Transport('Motorcycle', 'Yamaha', 2, 'Gasoline')
truck=Transport('Truck', 'MAN', '2', "Diesel")
minibus=Transport('Minibus', 'Renault', 17, "Gasoline")

Transport.transport_types()
Transport.common_transport_maxspeed()
Transport.common_transport_engine()

print(car)
print(bus)
print(motorcycle)
print(truck)
print(minibus)


minibus.say_vehicle()
minibus.say_capacity()

car.say_vehicle()
car.say_capacity()










