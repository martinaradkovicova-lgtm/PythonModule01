class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    catnip = Plant("Catnip", 15.4, 40)
    catnip.show()
    cyperus = Plant("Cyperus", 20.5, 30)
    cyperus.show()
    nepeta_cataria = Plant("Nepeta cataria", 23.2, 32)
    nepeta_cataria.show()
