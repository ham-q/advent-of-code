class Planet:
    def __init__(self, planet_name):
        self.name = planet_name
        self.orbit = None
        self.neighbour = []

    def __repr__(self):
        return self.name 

    def AddOrbiting(self, orbit):
        self.orbit = orbit

    def AddNeighbour(self, neighbour):
        self.neighbour.append(neighbour)

    def AddParent(self,parent):
        self.parent = parent

    def GetNeighbours(self):
        return self.neighbour

    def GetOrbiting(self):
        return self.orbit
    
    def GetName(self):
        return self.name
    
    def GetParent(self):
        return self.parent

def ReadFile(filename):
    planet_data = []
    with open(filename, "r") as input_data:
        for line in input_data:
            line2 = line.rstrip("\n")
            planet_data.append(line2.split(")"))
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

def BreadthFirstSearch(planet_list):
    for planet in planet_list:
        if planet.GetName() == "YOU":
            planet_main = planet
    found = False
    stack = [planet_main]
    visited = []
    while not found:
        current_planet  = stack.pop()
        nearby_planets = current_planet.GetNeighbours()
        nearby_planets.append(current_planet.GetOrbiting())
        if current_planet.GetName() == "SAN":
            found = True
        for neighbour in nearby_planets:
            if not ((neighbour in visited) or (neighbour == None)):
                neighbour.AddParent(current_planet)
                stack.append(neighbour)
        visited.append(current_planet)
    for planet in planet_list:
        if planet.GetName() == "SAN":
            planet_main = planet
    path = -2
    while planet_main.GetName() != "YOU":
        planet_main = planet_main.GetParent()
        path += 1
    return path

def CheckOrbiting(planet_list):
    for planet in planet_list:
        print([str(planet), planet.GetOrbiting(), planet.GetNeighbours()])

def Main():
    count = 0
    planet_list, count = InitialisePlanets(ReadFile("Day6/main_input.txt"), count)
    print(BreadthFirstSearch(planet_list))

if __name__ == "__main__":
    Main()