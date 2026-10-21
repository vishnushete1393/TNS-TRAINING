FRIENDS = {
    "Aisha": ["Ben", "Carla"],
    "Ben":   ["Aisha", "Dev"],
    "Carla": ["Aisha", "Dev"],
    "Dev":   ["Ben", "Carla", "Eli"],
    "Eli":   ["Dev"],
}


def add_person(graph, name):
    """Put `name` in the graph with no friends yet - unless already there."""
    # TODO: if name is not already a key in graph, give it an empty list.
    if name not in graph:
        graph[name] = []


def add_friendship(graph, a, b):
    """Link a and b BOTH ways. Friendship is mutual."""
    # TODO: make sure BOTH names exist, then append each to the other's
    #       list - but only if they are not already in there.
    add_person(graph, a)
    add_person(graph, b)
    if b  not in graph[a]:
        graph[a].append(b)
    if a  not in graph[b]:
         graph[b].append(a)
    return graph

friend=add_friendship(FRIENDS, "Alisha", "Ben")
print(friend)

def friend_count(graph, name):
    """How many friends does `name` have?"""
    # TODO: 0 if the name is not in the graph, otherwise len of their list.
    if name not in graph:
        return 0
    else :
        return len(graph[name])

name=input("ENter the name :")
print("number of friends:",friend_count(FRIENDS,name))



def are_friends(graph, a, b):
    """Is there a direct link between a and b?"""
    # TODO: careful - check that `a` is in the graph before looking a up,
    #       or you will get a KeyError.
    if a not in graph:
        print("not in graph")
    elif a  not in graph[b]:
        return False
    else :
        return True 
    
a=input("Enter the nmae :")    
b=input("Enter the nmae :")
print(f'{a} and {b} are friends',are_friends(FRIENDS,a,b)) 
   


  
    

         


    
