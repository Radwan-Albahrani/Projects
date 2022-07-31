import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "small"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # Prepare a frontier and an explored
    frontier = []
    explored = []
    path = []
    nodes = []
    
    # Start with the neighbors of the source
    frontier = list(neighbors_for_person(source))

    # Add Initial State Node
    nodes.append([[None, source], None])

    # Keep track of parents and children
    parent = []
    parent.append(nodes[-1])
    newChildren = []
    newChildren.append(len(frontier))

    found = False
    while len(frontier) != 0:
        
        # check if target has been added to the frontier
        test = [item for item in frontier if target in item[1]]

        # If anything has been added to test
        if len(test) > 0:
            
            # Loop through the frontier as an index
            for i in range(len(frontier)):

                # Mark as found
                found = True

                # While the target is not the current index in the frontier
                if target not in frontier[i]:
                    # Get the current frontier
                    current = frontier[i]
                    
                    # Add the current as a new node along with its parent
                    nodes.append([list(current), parent[0]])

                    # Subtract Children
                    newChildren[0] -=1

                    # If children is zero, pop that and pop the parent
                    if newChildren[0] == 0:
                        newChildren.pop(0)
                        parent.pop(0)
                # If the target is the current index, Get it, add proper parent then exit loop
                else:
                    # first in last out
                    current = frontier[i]
                
                    # Add the current as a new node along with its parent
                    nodes.append([list(current), parent[0]])
                    newChildren[0] -=1
                    if newChildren[0] == 0:
                        newChildren.pop(0)
                        parent.pop(0)
                    break
            frontier = []
            
            # Make it the current node
            currentNode = nodes[-1]

            # While it has a parent
            while currentNode[1] != None:

                # Append the current node to the path
                path.append(tuple(currentNode[0]))

                # Move to the parent
                currentNode = currentNode[1]
            path.reverse()
            break
        
        # If frontier has been emptied, Break
        if len(frontier) == 0:
            break
        
        # first in last out
        current = frontier.pop(0)
        
        # Add the current as a new node along with its parent
        nodes.append([list(current), parent[0]])
        
        # Append it to explored
        explored.append(current)

        # Find any neighbors to this current node
        newNeighbors = list(neighbors_for_person(current[1]))

        # If any new neighbors are added to the frontier, increment this value
        added = 0
        for i in newNeighbors:
            if i not in frontier and i not in explored:
                frontier.append(i)
                added += 1
        
        # If any new neighbors are added
        if added > 0:
            # If this parent already exists, don't add it. But that should never be the case
            if nodes[-1] in parent:
                continue
            
            # If parent is new, add is
            else:
                parent.append(nodes[-1])
            # add the amount of new children to the newchildren list
            newChildren.append(added)

        
        # Subtract From new children
        newChildren[0] -= 1

        # If that makes the children Reach Zero, Pop the last parent and these children
        if newChildren[0] == 0:
                parent.pop(0)
                newChildren.pop(0)
    
    if found:
        return path
    else:
        return None


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
