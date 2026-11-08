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
    print("=== Garden Plant Growh ===")
    catnip = Plant("Catnip", 15.434, 40, 0.8)
    catnip.show()
    init_height = catnip.height
    for days in range(1, 8):
        catnip.grow()
        catnip.age()
        print(f"=== Day {days} ===")
        catnip.show()
    print(f"Grow this week: {round(catnip.height - init_height, 1)}cm")
