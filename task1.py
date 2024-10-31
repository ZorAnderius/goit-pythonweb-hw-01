from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, spec=None):
        self.make = make
        self.model = model
        self.spec = spec
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        if self.spec:
            print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено") 
        else:
            print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        if(self.spec):
            print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")
        else:
            print(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass
    
    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, 'US')
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, 'US')

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, 'EU')
    
    def create_motorcycle(self,make, model):
        return Motorcycle(make, model, 'EU')

vehicles_US = USVehicleFactory()
vehicles_EU = EUVehicleFactory()

vehicle1 = vehicles_US.create_car('Ford', 'Mustang')
vehicle1.start_engine()
vehicle2 = vehicles_US.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

vehicle3 = vehicles_EU.create_car("Toyota", "Corolla")
vehicle3.start_engine()
vehicle4 = vehicles_EU.create_motorcycle("Yava", "32")
vehicle4.start_engine()

vehicle5 = Car('Volvo', 'CX90')
vehicle5.start_engine()

vehicle6 = Motorcycle('Suzuki', '1')
vehicle6.start_engine()
