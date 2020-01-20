#1111111111
class Dog():
    age=0
    name=""
    weight=0
 
    def bark(self):
        print( "Woof" ) 
myDog = Dog() 
myDog.name="Spot"
myDog.weight=20
myDog.age=3
myDog.bark()
def bark(self):
    print( "Woof says",self.name )
#2222222222
class Person():
    name=""
    cellPhone=""
    email =""

#3333333333
class Bird():
    color = ""
    name = ""
    breed = ""
myBird = Bird()
myBird.color="green"
myBird.name="Sunny"
myBird.breed="Sun Conure"
print('\n'
      'Информация:'
      '\n'
      '\n'
      f'Цвет: {myBird.color} \n'
      f'Имя: {myBird.name} \n'
      f'Порода: {myBird.breed} \n')
#4444444444
class Character():
    coord = ""
    name = ""
    force = ""
character = Character()
character.coord = '\nX: 25 \nY: 30'
character.name = 'Ben'
character.force = '15'
print('\n'
      'Информация:'
      '\n'
      '\n'
      f'Координаты: {chatacter.coord} \n'
      f'Имя: {character.name} \n'
      f'Сила: {character.force} \n')
#5555555555
class Person:
    name=""
    money=0
 
nancy=Person()
name="Nancy"
money=100
print(f'{name},{money}')
#6666666666
class Person:
    name=""
    money=0
 
bob = Person()
print (bob.name,"has",money,"dollars.")
#666666666
class Person:
    name=""
    money=0
 
bob = Person()
bob.name="Bob"
bob.money=100
nancy = bob
nancy.name="Nancy"
 
print(bob.name,"has",bob.money,"dollars.")
print(nancy.name,"has",nancy.money,"dollars.")

#Cat
class Cat():
    name = ""
    color = ""
    weight = ""
cat = Cat()
cat.name = "Cassi"
cat.color = "red"
cat.weight = "3 kg"

class Meow:
    meow = ""
meow = Meow()
meow.meow = "Meow Meow Meow"
print('\n'
      f'Имя: {cat.name} \n'
      f'Цвет: {cat.color} \n'
      f'Вес: {cat.weight} \n'
      f'{meow.meow}')







