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

def saveDTL(tree, filename):
    f= open(filename,"w+")
    f.write("(,")
    writeDTL(tree, f)
    f.close()  

def readDTL(string, root):
    start_idx = 0
    if(len(string) <= 1):
        return root
    for i in range(len(string)-1):
        if(string[i]=="(" or string[i]==")"):
            data = string[start_idx:i].split(",")
            target = id3.Vertex(data[1])
            edge = id3.Edge(data[0],target)
            root.add_edge(edge)
            if(string[i]=="("):
                target = readDTL(string[i+1:],target)
            elif(string[i]==")"):
                if(string[i+1]=="("):
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


def loadDTL(filename):
    f=open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        tree = readRootDTL(contents)
    return tree

def saveMLP(model, filename):
    f= open(filename,"w+")
    # save input layer (number of input perceptron)
    f.write("I\n")
    f.write(str(len(model.layer_list[0].perceptron_list))+"\n")
    # save hidden layer
    for i in range (1,model.num_layer-1):
        f.write("H"+str(i)+"\n")
        for perceptron in model.layer_list[i].perceptron_list:
            for weight in perceptron.weight:
                f.write(str(weight)+",")
            f.write("\n")
    # save output layer
    for outpercep in model.layer_list[model.num_layer-1].perceptron_list:
        f.write("O\n")
        f.write(outpercep.label+"\n")
        for weight in outpercep.weight:
            f.write(str(weight)+",")
    f.close()  

def loadMLP(filename):
    model = mlp.Model()
    f=open(filename, "r")
    content = f.readlines()
    i=0
    # initialize input layer
    if(content[i][0]=="I"):
        layer = mlp.Layer()
        i += 1
        for j in range (int(content[i])):
            input = mlp.InputPerceptron()
            layer.add_perceptron(input)
        model.add_layer(layer)
    i+=1
    # read weights to hidden layer
    while i< len(content):
        if content[i][0]=="O":
            break
        else:
            if content[i][0]=="H":
                layer = mlp.Layer()
                i +=1
                while(content[i][0]!="H" and content[i][0]!="O"):
                    weights = content[i].split(",")
                    h = mlp.HiddenPerceptron(len(weights)-2)
                    for j in range (len(weights)-1):
                        h.set_weight(j,weights[j])
                    layer.add_perceptron(h)
                    i += 1
                model.add_layer(layer)
                i-=1
            i+=1
    # read weight and label to output layer
    if content[i][0]=="O":
        i+=1
        layer = mlp.Layer()
        while (i<len(content)):
            weights = content[i+1].split(",")
            o = mlp.OutputPerceptron(content[i].rstrip(),len(weights)-2)
            for j in range (len(weights)-1):
                o.set_weight(j,weights[j])
            layer.add_perceptron(o)
            i += 2
        model.add_layer(layer)
    return model

