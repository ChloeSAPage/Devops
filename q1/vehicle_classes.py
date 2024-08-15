class Vehicle:
    def __init__(self, make: str) -> None:
        self.make = make


class Wheeled(Vehicle):
    def __init__(self, make: str, wheels: int) -> None:
        super().__init__(make)
        self._wheels = wheels

    def get_wheels(self) -> int:
        return self._wheels


class Motorised(Wheeled):
    def __init__(self, make: str, wheels: int, typeOfEngine: str) -> None:
        super().__init__(make, wheels)
        self.typeOfEngine = typeOfEngine

    def switchOn(self) -> None:
        print("The Engine is switched on.")


class Aircraft(Motorised):
    def __init__(self, make: str, wheels: int, typeOfEngine: str) -> None:
        super().__init__(make, wheels, typeOfEngine)

    def takeOff(self) -> None:
        print(f"The {self.make} with {self.get_wheels()} wheels and a {self.typeOfEngine} engine is taking off.")