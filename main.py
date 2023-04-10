#Exercise 3
#1

def count_vowels(text):
    if type(text) != str:
        return 42


    vowels = set("aeiouAEIOU")

    num_vowels = 0
    for char in text:
        if char in vowels:
            num_vowels += 1

    return num_vowels



result = count_vowels("Hello, Wooooooorld!")
result1 = count_vowels(12345)
result2 = count_vowels("AiErOpIiiEYUu")

print(result)
print(result1)
print(result2)


#2

def  hamming(text1, text2):
    if len(text1) != len(text2):
        return 0

    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1

    return distance


result = hamming("cat", "kats")
result1 = hamming("aspirin", "aspires")

print(result)
print(result1)

#3

class Vehicle():
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        Vehicle.__init__(self, color, fuel_type)
        self.doors = doors

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"

class Bus (Vehicle):
    def __init__(self, color, fuel_type, passengers):
        Vehicle.__init__(self, color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"


car = Car("white", "electric", 4)
bus = Bus("red", "diesel", 2)

print(car)
print(bus)


#4
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name}, {self.author}"

book = Book("Of Human Bondage", "William Somerset Maugham")
print(book)
