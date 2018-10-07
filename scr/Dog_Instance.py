from Dog_Class import Dog


class RusselTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


jim = Bulldog("Jim", 12)
print(jim.description())
print(jim.run("slowly"))

print(isinstance(jim, Dog))

julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

johnnywalker = RusselTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# print(isinstance(julie, jim))