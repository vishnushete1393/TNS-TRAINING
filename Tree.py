def make_node(value):
    return {"value": value, "left": None, "right": None}


def build():
    """Build and return this exact tree:

                 50
               /    \\
             30      70
            /  \\    /  \\
          20    40 60    80
    """
    # TODO: create the seven nodes and join them up.
    #       Start with root = make_node(50), then hang 30 and 70 on it,
    #       then hang 20 and 40 under 30, and 60 and 80 under 70.
    root = make_node(50)
    root["left"]=make_node(30)
    root["right"]=make_node(70)
    root["left"]["left"]=make_node(20)
    root["left"]["right"]=make_node(40)
    root["right"]["left"]=make_node(60)
    root["right"]["right"]=make_node(80)

    return root

tree=build()
print(tree)


def left_most(root):
    while root["left"] is not None:
        root=root["left"]
    return root["value"]

print("Left-most value:", left_most(tree))

def right_most(root):
    while root["right"] is not None:
        root=root["right"]
    return root["value"]

print("right-most value:", right_most(tree))
  
    

