from classes import *

dog = Animal('Olapar', 2, False)
cat = Animal('Tom', 3, True)
mouse = Animal('Jerry', 2, True)
person = Person('Ahmad', 19)
print(dog.name, cat.name, mouse.name)
dog.is_alive = False
print(dog.is_alive, cat.is_alive, mouse.is_alive)
dog.eat()
dog.run()
cat.eat()
cat.run()
mouse.eat()
mouse.run()
person.sleep()