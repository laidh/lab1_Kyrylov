class Oscillograph:
    counter = 0

    @classmethod
    def getCount(cls):
        print(f"\nКількість об'єктів {cls.counter}\n")

    def __init__(self, frequency=0, volume=0, mark=""):
        self.frequency = frequency
        self.volume = volume
        self.mark = mark
        Oscillograph.counter += 1

    def __str__(self):
        return f"\nfrequency(MGh): {self.frequency} \nvolume(Kb): {self.volume} \nmark: {self.mark}"

    def __del__(self):
        del self

def main():
    obj1 = Oscillograph(5, 10, "Hantek")
    print(obj1)

    obj2 = Oscillograph(8, 16, "FSD")
    print(obj2)

    obj3 = Oscillograph(7, 14, "Siglent")
    print(obj3)

    Oscillograph.getCount()

if __name__ == "__main__":
    main()