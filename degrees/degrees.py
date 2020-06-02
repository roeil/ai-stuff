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
    with open("{}/people.csv".format(directory), encoding="utf-8") as f:
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
    with open("{}/movies.csv".format(directory), encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open("{}/stars.csv".format(directory), encoding="utf-8") as f:
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
        print("{} degrees of separation.".format(degrees))
        path = [(None, source)] + path
        print("\n\n**************",path,'**************\n\n\n')
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]

            print("{}: {} and {} starred in {}".format(i+1,person1,person2,movie))


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO
    #raise NotImplementedError

    node=Node(source,None,None)
    print(node.state)
    qf=QueueFrontier()
    #qf.frontier.append((None,source))
    qf.add(node)
    NotFound=True

    parents=[node.state]

    parents2=list()
    path=list()
    path2=list()
    f=True
    while f:

        print('p:',parents)
        for p in parents:
            #print(type(p))
            nfpS=neighbors_for_person(p)
       
            

            #print(nfpS)
            for m,a in nfpS:
                parents2.append(a)
                qf.add(Node(a,p,m))
                
                #path2.append(qf.remove)
                
                if a==target:
                    
                        #print("<<<<<<<<<<<<<<<-------------",qf.frontier)
                        for node in qf.frontier:
                            #print("************",node.state)
                            path.append((node.state,node.parent,node.action))
                        path.reverse()
                        #print(path)
                        parent=p
                        movie=m
                        for st,pa,mo in path:
                            if st==parent and pa!=None and st!=pa:
                                path2.append((st,pa,mo))
                                parent=pa
                                break;
                        f=False

                        path2.reverse()
                        path2=path2+[(a,p,m)]                        
                        print(path)
                        path=list()
                        for sta,par,mov in path2:
                            path.append((mov,sta))
                        
                        print()
                        return(path)
                        
                        break;

        parents=parents2
        parents2=list()
                
            
def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print("Which '{}'?".format(name))
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print("ID: {}, Name: {}, Birth: {}".format(person_id,name,birth))
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
    print('person_id=',person_id)
    movie_ids = people[person_id]["movies"]
    
   
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
