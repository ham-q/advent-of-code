class Planet:
    """Used to hold data for individual planets, alongside their relation to others"""
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
    """Reads in text file and splits it into a list
    Input: filename(STR) - name of file in directory
    Output: planet_data(LIST - all STR elements) - list containing program data"""
    planet_data = []
    with open(filename, "r") as input_data:
        for line in input_data:
            line2 = line.rstrip("\n")
            planet_data.append(line2.split(")"))
    return planet_data

def InitialisePlanets(planet_data):
    """Used to create all the planet instances from input data and add their orbiters and neighbours
    Inputs: planet_data(LIST w/ STR elements) - list of elements to use for creating each planet instance, alongside what they orbit
    Outputs: planet_list(LIST w/ OBJ elements) - a list of all planet objects in system"""
    planet_list = []
    planet_names = []
    for planet in planet_data:
        if not planet[0] in planet_names:
            planet_list.append(Planet(planet[0]))
            planet_names.append(planet[0])
        if not planet[1] in planet_names:
            planet_list.append(Planet(planet[1]))
            planet_names.append(planet[1])
        planet_list[planet_names.index(planet[0])].AddNeighbour(planet_list[planet_names.index(planet[1])])
        planet_list[planet_names.index(planet[1])].AddOrbiting(planet_list[planet_names.index(planet[0])])
    return planet_list

def CheckIndirect(planet_list):
    """Used to check how many indirect orbits exist within the system
    Inputs: planet_list(LIST w/ OBJ elements) - list of all planets in system
    Outputs: count(INT) the number of indirects in the system"""
    count = 0
    for planet in planet_list:
        has_orbit = True
        current_planet = planet
        while has_orbit is True:
            if current_planet.GetOrbiting() is None:
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
    """Searches entire graph until SAN is found, building a tree graph which is then traversed up in reverse to find shortest path
    Inputs: planet_list(LIST w/ OBJ elements) - list of all planets in system
    Outputs: path(INT) - the shortest path between YOU and SAN"""
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
            if not ((neighbour in visited) or (neighbour is None)):
                neighbour.AddParent(current_planet)
                stack.append(neighbour)
        visited.append(current_planet)
    for planet in planet_list:
        if planet.GetName() == "SAN":
            planet_main = planet
    path = -2 #used to account for the additions made by YOU and SAN
    while planet_main.GetName() != "YOU":
        planet_main = planet_main.GetParent()
        path += 1
    return path 

def CheckOrbiting(planet_list):
    """Debug command, used to check the surrounding planets to all planets in system
    Inputs: planet_list(LIST w/ OBJ elements) - list of all planets in system"""
    for planet in planet_list:
        print([str(planet), planet.GetOrbiting(), planet.GetNeighbours()])

def Main():
    planet_list = InitialisePlanets(ReadFile("Day6/main_input.txt"))
    print(BreadthFirstSearch(planet_list))

if __name__ == "__main__":
    Main()