from abc import ABC, abstractmethod
import logging
from typing import Optional

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("task1.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("Task1")


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: Optional[str] = None) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        if self.spec:
            logger.info(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")
        else:
            logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        if self.spec:
            logger.info(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")
        else:
            logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU")


vehicles_US: VehicleFactory = USVehicleFactory()
vehicles_EU: EUVehicleFactory = EUVehicleFactory()

vehicle1 = vehicles_US.create_car("Ford", "Mustang")
vehicle1.start_engine()
vehicle2 = vehicles_US.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

vehicle3 = vehicles_EU.create_car("Toyota", "Corolla")
vehicle3.start_engine()
vehicle4 = vehicles_EU.create_motorcycle("Yava", "32")
vehicle4.start_engine()

vehicle5 = Car("Volvo", "CX90")
vehicle5.start_engine()

vehicle6 = Motorcycle("Suzuki", "1")
vehicle6.start_engine()
