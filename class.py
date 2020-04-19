class Planet:

    def __init__(self):
        self.name = 'Titan'
        self.radius = 50000
        self.gravity = 5.9
        self.system = 'Titan System'


    def orbit(self):
        return(f'{self.name} is orbiting in {self.system}')

titan = Planet()
print(f'Name is {titan.name}')
print(f'Radius is {titan.radius}')
print(f'Gravity is {titan.gravity}')
print(titan.orbit())
