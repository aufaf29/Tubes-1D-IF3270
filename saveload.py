import id3
import mlp

def writeDTL(tree, f):
    f.write(tree.name)
    if tree.count_edge() != 0 :
        for x in tree.edges:
            f.write("("+x.name+",")
            writeDTL(x.target_vertex, f)
        f.write(")")
    else:
        f.write(")")

def saveDTL(tree):
    f= open("DTL.txt","w+")
    f.write("(,")
    writeDTL(tree, f)
    f.close()  

def readDTL(string, root):
    print(root.name)
    start_idx = 0
    if(len(string) <= 1):
        return root
    for i in range(len(string)-1):
        if(string[i]=="(" or string[i]==")"):
            data = string[start_idx:i].split(",")
            print(data)
            target = id3.Vertex(data[1])
            edge = id3.Edge(data[0],target)
            root.add_edge(edge)
            if(string[i]=="("):
                target = readDTL(string[i+1:],target)
            elif(string[i]==")"):
                if(string[i+1]=="("):
                    #print(string[i+2:])
                    root = readDTL(string[i+2:],root)
            return root  


def readRootDTL(string):
    for i in range(2, len(string)-1):
        if(string[i]=="("):
            root = id3.Vertex(string[2:i])
            root = readDTL(string[i+1:], root)
            break
        elif (string[i]==")"):
            root = id3.Vertex(string[2:i])
            break
    return root


def loadDTL():
    f=open("DTL.txt", "r")
    if f.mode == "r":
        contents = f.read()
        tree = readRootDTL(contents)
    return tree

# TEST

# tree = id3.Vertex('a')
# edge1 = id3.Edge("<1", id3.Vertex("b"))
# edge2 = id3.Edge(">=1", id3.Vertex("c"))
# tree.add_edge(edge1)
# tree.add_edge(edge2)
# saveDTL(tree)

# id3.print_tree(loadDTL(),0)