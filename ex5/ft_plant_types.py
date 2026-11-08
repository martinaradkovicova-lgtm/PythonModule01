class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 grow_speed: float):
        self._name = name
        self._height = round(height, 1)
        self._age_days = age_days
        self._grow_speed = grow_speed

    def set_name(self, name):
        self._name = name

    def set_height(self, height):
        self._height = round(height)

    def set_age(self, age_days):
        self._age_days = age_days

    def set_grow_speed(self, grow_speed):
        self._grow_speed = round(grow_speed)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def get_grow_speed(self) -> float:
        return self._grow_speed

    def age(self):
        self._age_days += 1

    def grow(self):
        self._height += self._grow_speed

    def show(self):
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 grow_speed: float, color: str):
        super().__init__(name, height, age_days, grow_speed)
        self._color = color
        self._bloomed = False

    def set_color(self, color):
        self._color = color

    def get_color(self) -> str:
        return self._color

    def bloom(self):
        self._bloomed = True

    def show(self):
        Plant.show(self)
        print(f" Color: {self._color}")
        if self._bloomed is True:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
            print(f"[Asking the {self._name.lower()} to bloom]")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 grow_speed: float, trunk_diameter: float):
        super().__init__(name, height, age_days, grow_speed)
        self._trunk_diameter = round(trunk_diameter, 1)
        self._produce_shade = False

    def set_trunk_diameter(self, trunk_diameter):
        self._trunk_diameter = round(trunk_diameter, 1)

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self):
        self._produce_shade = True

    def show(self):
        if self._produce_shade is True:
            print(f"Tree {self._name} now produces a shade of "
                  f"{self._height:.1f}cm long and "
                  f"{self._trunk_diameter:.1f}cm wide.")
        else:
            Plant.show(self)
            print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")
            print(f"[asking the {self._name.lower()} to produce shade]")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 grow_speed: float, harvest_season: str,
                 nutritional_value: int):
        super().__init__(name, height, age_days, grow_speed)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def set_harvest_season(self, harvest_season):
        self._harvest_season = harvest_season

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def set_nutritional_value(self, nutritional_value):
        self._nutritional_value = nutritional_value

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def show(self):
        Plant.show(self)
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")
        if self._nutritional_value == 0:
            print(f"[make {self._name.lower()} grow and age for 20 days]")

    def grow(self):
        Plant.grow(self)
        self._nutritional_value += 5

    def age(self):
        Plant.age(self)
        self._age_days += 20
        self._nutritional_value += 37


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15, 10, 0.3, "red")
    flower.show()
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 5, 0.5, 50.5)
    tree.show()
    tree.produce_shade()
    tree.show()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, 16.8, "April", 0)
    vegetable.show()
    vegetable.grow()
    vegetable.age()
    vegetable.show()
