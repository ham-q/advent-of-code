class Planet:
    def __init__(self, planet_name):
        self.name = planet_name
        self.orbit = None
        self.neighbour = []

    def __str__(self):
        return self.name 

    def AddOrbiting(self, orbit):
        self.orbit = orbit

    def AddNeighbour(self, neighbour):
        self.neighbour.append(neighbour)

    def GetNeighbours(self):
        return self.neighbour

    def GetOrbiting(self):
        return self.orbit
    
    def GetName(self):
        return self.name

def ReadFile(filename):
    planet_data = []
    with open(filename, "r") as input_data:
        for line in input_data:
            line2 = line.rstrip("\n")
            planet_data.append(line2.split(")"))
    print(planet_data)
    return planet_data

def InitialisePlanets(planet_data,count):
    planet_list = []
    planet_names = []
    for planet in planet_data:
        if not planet[0] in planet_names:
            exec("a"+planet[0]+" = Planet('"+ planet[0] + "')")
            exec("planet_list.append(a" + planet[0] + ")")
            exec("planet_names.append(a" + planet[0] + ".GetName())")
        if not planet[1] in planet_names:
            exec("a"+planet[1]+" = Planet('"+ planet[1] + "')")
            exec("planet_list.append(a" + planet[1] + ")")
            exec("planet_names.append(a" + planet[1] + ".GetName())")
        exec("planet_list[planet_list.index(a" + planet[0] + ")]" + ".AddNeighbour(" + "planet_list[planet_list.index(a" + planet[1] + ")])")
        exec("planet_list[planet_list.index(a" + planet[1] + ")]" + ".AddOrbiting(" + "planet_list[planet_list.index(a" + planet[0] + ")])")
    return planet_list, count

def CheckIndirect(planet_list, count):
    for planet in planet_list:
        has_orbit = True
        current_planet = planet
        while has_orbit == True:
            if current_planet.GetOrbiting() == None:
                has_orbit = False
                print(current_planet)
                print(current_planet.GetOrbiting())
            else:
                print(current_planet)
                print(current_planet.GetOrbiting())
                current_planet = current_planet.GetOrbiting()
                count += 1
    return count

def CheckOrbiting(planet_list):
    for planet in planet_list:
        print([str(planet), planet.GetOrbiting(), planet.GetNeighbours()])

def Main():
    count = 0
    planet_list, count = InitialisePlanets(ReadFile("Day6/main_input.txt"), count)
    print(CheckIndirect(planet_list, count))

if __name__ == "__main__":
    Main()