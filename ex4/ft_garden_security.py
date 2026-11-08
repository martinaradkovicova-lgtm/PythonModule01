class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            grow_speed: float
            ) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._grow_speed = 0.0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative!")
            print("Height update rejected")
        else:
            self._height = round(height, 1)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be nagetive!")
            print("Age update rejected")
        else:
            self._age = age

    def set_grow_speed(self, grow_speed: float) -> None:
        if grow_speed > 0:
            self._grow_speed = round(grow_speed, 1)
        else:
            self._grow_speed = 0.1

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_grow_speed(self) -> float:
        return self._grow_speed

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, grow_speed: float) -> None:
        self._height += grow_speed

    def age(self):
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 17.3, 12, 0.25)
    print("Plant created: ", end="")
    plant.show()
    print()
    plant.set_height(32)
    print(f"Height updated: {plant.get_height()}cm")
    plant.set_age(25)
    print(f"Age updated: {plant.get_age()} days")
    print()

    plant.set_height(-9)
    plant.set_age(-23)
    print()
    print("Current state: ", end="")
    plant.show()
