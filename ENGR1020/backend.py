import heapq


def dijkstra(graph, start):
    pq = [(0, start)]   # Priority queue to store (distance, vertex) tuples
    distances = {vertex: float('inf') for vertex in graph}  # Dictionary to store the shortest path to each vertex
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}  # Dictionary to store the previous vertex in the path
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)    # Pop the vertex with the smallest distance
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():  # Explore the neighbors of the current vertex
            distance = current_distance + weight
            if distance < distances[neighbor]:  # If the new distance is smaller, update the shortest path
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous_vertices

def shortest_path(graph, start, end):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path = path[::-1]  # Reverse the path to get the correct order
    return path


graph = {
    # Floor 1
    'Stair 1': {"Checkpoint 1": 1, "Checkpoint 8": 2},

    'Checkpoint 1': {"Stair 1": 1, "1073":2, 'Checkpoint 2':3},
    "1073": {'Checkpoint 1':1, 'Elevator 1':5, 'Checkpoint 2':1}, 
    'Elevator 1': {"1073":1, "2073":1},

    'Checkpoint 2': {'Checkpoint 1': 3, "1073": 2, 'H1074-East':1, 'Checkpoint 3':3},
    'H1074-East': {'H1074A':1, 'H1074B':2},
    'H1074A': {"1025":2, "1027":2},
        "1025": {}, "1027": {}, 
    'H1074B': {"1041":2, "1042":1},
        "1041": {}, "1042": {},
    
    'Checkpoint 3': {'Checkpoint 2': 3, 'H1074-West':1, 'H1200-South1':1,'Checkpoint 4':3},
    'H1074-West': {'H1074A':1, 'H1074B':1},
    'H1200-South1': {"1205":1, "1207":2},
        "1205": {}, "1207": {},

    'Checkpoint 4': {'Checkpoint 3': 3, 'H1200-North3':1, 'H1200-South2':1,'Checkpoint 5':3},
    'H1200-North3': {"1207":1, "1205":2},
    'H1200-South2': {"1213":1, "1215A":2, "1217":3, "1219":4},
        "1213": {"1111":1, "1113":1}, 
            "1111": {}, "1113": {},
        "1215A": {}, 
        "1217": {"1115A":1}, 
        "1219": {"1119":1, "1121":1},
            "1119": {}, "1121": {}, 
        "1115A":{"1215":1, "1115":1, "1117":1},
            "1115": {}, "1117": {}, "1215": {},

    'Checkpoint 5': {'Checkpoint 4': 3, 'H1200-North2':1, 'H1200-South3':1,'Checkpoint 6':3},
    'H1200-North2': {"1219":1, "1217":2, "1215A":3, "1213":4},
    'H1200-South3': {"1225":1, "1227":2, "1231":3},
        "1225": {"1123":1, "1125":1}, 
            "1123": {}, "1125": {},
        "1227": {"1127":1, "1129":1},
            "1127": {}, "1129": {}, 
        "1231": {"1131":1, "1133":1},
            "1131": {}, "1133": {},

    'Checkpoint 6': {'Checkpoint 5': 3, 'H1200-North1':1, 'H1200-Extra':1,'Checkpoint 7':1},
    'H1200-North1': {"1231":1, "1227":2, "1225":3},
    'H1200-Extra': {"1237":1},
        "1237": {},

    'Checkpoint 7': {'Checkpoint 6': 1, 'H1200-Extra':1, 'H1275':1},
    'H1275': {"Checkpoint 7":1 ,"1275":1, "1262":2, "1261":2},
        "1262": {}, "1261": {},
        "1275": {'H1275':1,'Elevator 2':3, 'Stair 2': 1},

    # Floor 2
    'Checkpoint 8': {'Stair 1': 2, "2073":2, 'Checkpoint 9':3},
        "2073": {'Checkpoint 8': 1,'H2072-North':1, "Elevator 1":2,"2010":1, 'Checkpoint 9':1},
    'H2072-North': {"2072":1},
        "2010": {"2010A":1, "2013":1, "2014":1, "2019":3},
            "2010A": {}, "2013": {}, "2014": {}, "2019": {},
        "2072": {"2001":1},
            "2001": {},

    'Checkpoint 9': {'Checkpoint 8':3, "2073":2, 'H2074-1East':1, 'Checkpoint 10':3},
    'H2074-1East': {"2019":1, 'H2074A':1, 'H2074B':2, 'H2074C':3, 'H2300-South':1},
        'H2074A': {"2025":2, "2027":2},
            "2025": {}, "2027": {},
        'H2074B': {"2041":2, "2042":1},
            "2041": {}, "2042": {},
        'H2074C': {"2051":2},
            "2051": {},
        'H2300-South': {"2302":1, "2304":2, "2208":3},
            "2302": {}, "2304": {}, "2208": {},

    'Checkpoint 10': {'Checkpoint 9':3, 'H2074-2East':1, 'H2074-West':1, 'H2200-South1':1, 'Checkpoint 11':4},
    'H2074-West': {"2019":2, 'H2074A':1, 'H2074B':0, 'H2074C':1},
    'H2200-South1': {"2201":1, "2203":2, "2205":3, "2207":4, "2204": 2, "2206": 3, "2208":4},
        "2201": {}, "2203": {}, "2205": {}, "2207": {}, "2204": {}, "2206": {}, 
    'H2074-2East': {'H2074B':0, 'H2074C':1},

    'Checkpoint 11': {'Checkpoint 10':4, 'H2074-2East':1, 'H2200-North3':1, 'H2200-South2':1,'Checkpoint 12':4},
    'H2200-North3': {"2208":1, "2206": 2, "2204":3, "2207":1, "2205":2, "2203":3, "2201":4},
    'H2200-South2': {"2213":1, "2215":2, "2219":3, "2214":1, "2216":2, "2220":3},
        "2213": {"2111":1, "2113":1}, 
            "2111": {}, "2113": {},
        "2215": {"2115":1, "2117":1},
            "2115": {}, "2117": {},
        "2219": {"2119":1, "2121":1},
            "2119": {}, "2121": {}, 
        "2214": {"2312":1, "2314":1},
            "2312": {}, "2314": {},
        "2216": {"2316":1, "2318":1},
            "2316": {}, "2318": {},
        "2220": {"2320":1, "2322":1},
            "2320": {}, "2322": {},
    
    'Checkpoint 12': {'Checkpoint 11':4, 'H2200-North2':1, 'H2200-South3':1,'Checkpoint 13':3},
    'H2200-North2': {"2219":1, "2215":2, "2213":3, "2220":1, "2216":2, "2214":3},
    'H2200-South3': {"2225":1, "2229A":2, "2231":3, "2226":1, "2228":2, "2232":3,},
        "2225": {"2123":1, "2125":1}, 
            "2123": {}, "2125": {},
        "2229A": {"2127":1, "2129":1, "2229":1},
            "2127": {}, "2129": {}, "2229": {},
        "2231": {"2131":1, "2133":1},
            "2131": {}, "2133": {}, 
        "2226": {"2324":1, "2326":1},
            "2324": {}, "2326": {},
        "2228": {"2328":1, "2330":1},
            "2328": {}, "2330": {},
        "2232": {"2332":1, "2334":1},
            "2332": {}, "2334": {},
    
    'Checkpoint 13': {'Checkpoint 12':3, 'H2200-North1':1, 'H2200-Extra':1,'Checkpoint 14':2},
    'H2200-North1': {"2231":1, "2229A":2, "2225":3, "2232":1, "2228":2, "2226":3},
    'H2200-Extra': {"2237":1, "2238":1},
        "2237": {}, "2238": {},
    
    'Checkpoint 14': {'Checkpoint 13':2, 'H2200-Extra':1, 'H2275':1},
    'H2275': {'Checkpoint 14':1 ,"2275":1, "2262":2, "2261":2},
        "2262": {}, "2261": {},
        "2275": {'H2275':1, 'Elevator 2':3, 'Stair 2': 1},
    'Stair 2': {'1275':1,'2275': 1},
    'Elevator 2': {'1275':1,'2275': 1},
}

#Returns
def numExtract(text):
    if len(text) == 4:
        return int(text)
    elif "H" in text:
        return int(text[1:5])


def directions(path):
    i = 0
    toString = []
    door = False
    direction = ""
    while i < (len(path)):
        if "Checkpoint" in path[i] and "Checkpoint" in path[i+1]:
            if (" 1" in path[i] and " 2" in path[i+1]) or ("8" in path[i] and "9" in path[i+1]):
                toString += ["Walk across the lobby toward the hallway"]
            # elif (("2" in path[i] and "3" in path[i + 1]) or ("9" in path[i] and "10" in path[i + 1])) and ("Checkpoint" in path[i+2] or "South" in path[i+2]):
            #     toString += ["Walk into the hallway and make a right into the connecting hallway "]
            elif (" 2" in path[i] and " 3" in path[i + 1]) or ("9" in path[i] and "10" in path[i + 1]):
                toString += ["Walk into the hallway" ]
            elif (" 3" in path[i] and " 4" in path[i+1]) or ("10" in path[i] and "11" in path[i+1]):
                toString += ["Make a right into the hallway "]

            elif (" 2" in path[i] and " 1" in path[i + 1]) or ("9" in path[i] and "8" in path[i+1]):
                toString += ["Walk across the lobby and into the stairs "]
            elif (" 3" in path[i] and " 2" in path[i + 1]) or ("10" in path[i] and "9" in path[i+1]):
                toString += ["Walk out of the hallway and into the lobby "]
            elif ((" 4" in path[i] and " 3" in path[i+1]) or ("11" in path[i] and "10" in path[i+1])) and ("West" in path[i+2] or "Checkpoint" in path[i+2]):
                toString += ["Walk straight towards the exit of the hallway and turn left"]
            elif (" 4" in path[i] and " 3" in path[i+1]) or ("11" in path[i] and "10" in path[i+1]):
                toString += ["Walk straight towards the exit of the hallway "]

        elif "Checkpoint" in path[i]:
            if path[i+1][0] == "H":
                if "East" in path[i+1]:
                    toString += ["Keep heading straight into hallway"]
                    direction = "East"
                elif "West" in path[i+1] and not path[i] == "Checkpoint 10":
                    toString += ["Make a left into the hallway"]
                    direction = "West"
                elif "South" in path[i+1]:
                    toString += ["Head straight"]
                    direction = "South"
                elif "North" in path[i+1]:
                    toString += ["Head straight"]
                    direction = "North"
        
        elif "Elevator" in path[i]:
            if path[i-1] == "1073":
                toString += ["Take the elevator to the second floor"]
            elif path[i-1] == "2073":
                toString += ["Take the elevator to the first floor"]
            elif path[i-1] == "1275":
                toString += ["Take the elevator to the first floor"]
            elif path[i-1] == "2275":
                toString += ["Take the elevator to the first floor"]      

        elif "Stair" in path[i]:
            if path[i-1] == "Checkpoint 1":
                toString += ["Take the stairs to the second floor"]
            elif path[i-1] == "Checkpoint 8":
                toString += ["Take the stairs to the first floor"]
            elif path[i-1] == "2275":
                toString += ["Take the stairs to the first floor"]
            elif path[i-1] == "1275":
                toString += ["Take the stairs to the first floor"]    

        elif (path[i][1] == "3" or path[i][1] == "1") and not "H" in path[i]:
            if path[i-1] == "2216" or path[i-1] == "2215":
                if path[i][-2:] == path[i-1][-2:]:
                    toString += ["Office has a door"]
                    door = True
                else:
                    toString += ["Office has no door"]
            elif "2229" in path[i] and "2229" in path[i-1]:
                if path[i-1][-2:] == path[i][-3:-1]:
                    toString += ["Office has a door"]
                    door = True
                else:
                    toString += ["Office has no door"]
            elif path[i][-2:] == path[i-1][-2:]:
                toString += ["Office has no door"]
            else:
                toString += ["Office has a door"]
                door = True
        
        elif ((path[i] == "2261" or path[i] == "2262") or (path[i] == "1261" or path[i] == "1262")) and len(path) == 3:
            if path[i] == "2261" or path[i] == "1261":
                toString += ["Go to the right and the restroom is all the way down"]
            elif path[i] == "2262" or path[i] == "1262":
                toString += ["Go to the right and the restroom is one door before the end"]

        elif ((path[i] == "2261" or path[i] == "2262") and path[i-3] == "Checkpoint 13") or ((path[i] == "1261" or path[i] == "1262") and path[i-3] == "Checkpoint 6"):
            toString += ["Head all the way down the hallway"]
            if path[i] == "2261" or path[i] == "1261":
                toString += ["Take a left and the restroom is all the way down"]
            elif path[i] == "2262" or path[i] == "1262":
                toString += ["Take a left and the restroom is one door before the end"]

        elif (path[i] == "1275" or path[i] == "2275") and "Stair" not in path[i-1] :
            toString += ["Go to the end of the hallway until you see stairs on your left"]
        elif (path[i] == "1275" or path[i] == "2275") and "Stair" in path[i-1]:
            toString += ["Take a right into the hallway"]
        
        elif (path[i] == "2262" or path[i] == "1262") and path[i-2] == "2275":
            toString += ["The restroom is on the right"]

        elif numExtract(path[i]) % 2 == 0 and path[i][0] != "H" and path[i][1] != "0":
            if direction == "South":
                toString += ["Keep looking to the right until you find room "+ path[i]+" and enter"]
                direction = ""
            elif direction == "North":
                toString += ["Keep looking to the left until you find room "+ path[i]+" and enter"]
                direction = ""
            else:
                toString += ["Walk straight ahead until you see room "+ path[i]]
        elif numExtract(path[i]) % 2 != 0 and path[i][0] != "H" and path[i][1] != "0":
            if direction == "South":
                toString += ["Keep looking to the left until you find room "+ path[i]+" and enter"]
                direction = ""
            elif direction == "North":
                toString += ["Keep looking to the right until you find room "+ path[i]+" and enter"]
                direction = ""
            else:
                toString += ["Walk straight ahead until you see room "+ path[i]]
       
        elif path[i] == "H2072-North":
            toString += ["Take the hallway to the right of the stairs"]
        elif "H2074" in path[i] and len(path[i]) == 6:
            if path[i] == "H2074A" and "East" in path[i-1]:
                toString += ["Enter the first hallway on the left"]
            elif path[i] == "H2074A" and "West" in path[i-1]:
                toString += ["Enter the first hallway on the right"]
            elif path[i] == "H2074B" and "2East" in path[i-1]:
                toString += ["Enter the hallway straight ahead"]
            elif path[i] == "H2074B" and "1East" in path[i-1]:
                toString += ["Enter the second hallway on the left"]
            elif path[i] == "H2074B" and path[i-2] == "Checkpoint 10":
                toString += ["Turn around and enter the hallway"]
            elif path[i] == "H2074C" and path[i-2] == "Checkpoint 10":
                toString += ["Continue down the hallway and enter the final hallway on the left"]
            elif path[i] == "H2074C" and "1East" in path[i-1]:
                toString += ["Continue down the hallway and enter the final hallway on the left"]
            else:
                toString += ["hallway directions, error if printed"]


        elif path[i][1] == "0":
            if path[i] == "1073" or path[i] == "2073":
                toString += ["Head straight into the lobby"]
            elif path[i] == "2072": 
                toString += ["Take the first left after the hallway"]
            elif path[i] == "2001":
                toString += ["Go straight through two double doors"]
            elif path[i] == "2010":
                toString += ["Enter the main office, room 2010"]
            elif path[i] == "2013":
                toString += ["The office is first from the left"]
            elif path[i] == "2014":
                toString += ["The office is second from the left"]
            elif path[i] == "2019" and path[i-1] == "H2074-1East":
                toString += ["Room 2019 is the second door on the left"]
            elif path[i] == "2019" and path[i-1] == "H2074-West":
                toString += ["Room 2019 is the first door after the hallway"]
            elif path[i] == "2041" or path[i] == "2051":
                toString += ["Head straight down that hallway"]
            elif path[i] == "2042":
                toString += ["Enter the door on the right"]
            elif path[i] == "2025":
                toString += ["The restroom is down that hallway and on the left"]
            elif path[i] == "2027":
                toString += ["The restroom is down that hallway and on the right"]
            elif path[i] == "1025":
                toString += ["The restroom is on the left"]
            elif path[i] == "1027":
                toString += ["The restroom is on the right"]
            elif path[i] == "1041":
                toString += ["Take a left at the second hallway and head straight"]
            elif path[i] == "1042":
                toString += ["Take a left at the second hallway and then the room is on the right"]
            else:
                toString += ["0 directions, error if printed"]
        i +=1
    return toString

# code should record the previous direction, counter or something
# using previous direction, code should differentiate between odd and even numbers (sides of the room)
# Ex: Visitor comes down in the south direction, has to enter room 1214
# - Room is on the left side on floor plan BUT on the right for user
start = 'Checkpoint 1'
end = '2051'
accessibility = True

def navigateMR5(start, end, accessibility):
    if len(start) == 12:
        checkpoint_number = int(start[-1])
    elif len(start) == 13:
        checkpoint_number = int(start[-2:])
    
    returned = []
    if accessibility and ((checkpoint_number > 7 and end[0] == "1") or (checkpoint_number < 8 and end[0] == "2")):
        if 0 < checkpoint_number%7 < 4:
            returned += directions(shortest_path(graph, start, "Elevator 1"))
            returned += directions(shortest_path(graph, "Elevator 1", end)[1:])
        else:
            returned += directions(shortest_path(graph, start, "Elevator 2"))
            returned += directions(shortest_path(graph, "Elevator 2", end)[1:])
    else:
        returned += directions(shortest_path(graph, start, end))
    returned += [f"You have arrived at room {end}!"]
    return returned
