class Cars(object):
    def __init__(self, name, colour, model, speedlimit):
        self.name = name
        self.colour = colour
        self.model = model
        self.speedlimit = speedlimit

    def start(self):
        print("Started")
    
    def stop(self):
        print("Stop")
    
    def abtCar(self):
        print(self.name)
        print(self.colour)
        print(self.model)
        print(self.speedlimit)

    def acpAr(self, owner, rating):
        print(owner, "is the name of the owner")
        print(rating, "is the rating given by the owner")


audi = Cars("Q5", "red", "Audi", 200)
ford = Cars("Mustang GT", "blue", "Ford", 220)

audi.acpAr("Aadithya", "Good")