class Car:

    def __init__(self, model, name, year, colour, horsepower):
        self.model=model
        self.name=name
        self.year=year
        self.colour=colour
        self.horsepower=horsepower
        print('Car is created.\n')

    def description(self):
        print('Description:')
        print('Name -',self.name,'\nModel -',self.model,'\nYear -',self.year,'\nColour -',self.colour,'\nHorsepower -',self.horsepower,('\n'))

    def changename(self,name):
        self.name=name
        print('Name changed\n')

    def changecolour(self,colour):
        self.colour=colour
        print('Colour changed\n')

car1=Car('Alto','Maruti',2000,'Red',34628)
car1.description()
car1.changename('Suzuki')
car1.changecolour('Blue')
car1.description()
