class Plant:
    def __init__(self, name: str, height: float, days: int, grow_speed: float):
        self.name = name
        self.height = round(height, 1)
        self.days = days
        self.grow_speed = grow_speed

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm {self.days} days old")

    def grow(self) -> None:
        self.height += self.grow_speed
        self.height = round(self.height, 1)

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    new_plants = [
        Plant("Rose", 25.098, 30, 0.2),
        Plant("Cactus", 5.345, 90, 0.1),
        Plant("Catnip", 10.45, 42, 0.5),
        Plant("Cyperus", 15.67, 33, 0.3),
        Plant("Nepeta cataria", 12.32, 11, 0.4)
        ]
    for plant in new_plants:
        print("Created: ", end="")
        plant.show()
