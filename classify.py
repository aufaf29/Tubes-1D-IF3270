import id3

def create_new_instance():
    attr = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
    new_instance = {}

    for i in range(len(attr)):
        x = input(attr[i] + " : ")
        new_instance[attr[i]]=x
    return new_instance

#classify
def classify_new_instance(tree,instance):
    if(len(tree.edges) == 0 ):
        print("Result : " + tree.name)
    else:
        if(len(tree.edges) > 1):
            for i in range(len(tree.edges)):
                evaluate = instance[tree.name] + tree.edges[i].name
                if(eval(evaluate)):
                    classify_new_instance(tree.edges[i].target_vertex, instance)
                    break
        else:
            evaluate = instance[tree.name] + tree.edges[0].name
            if(eval(evaluate)):
                classify_new_instance(tree.edges[0].target_vertex, instance)
            else:
                print("Result : NONE")

#test
# root = id3.Vertex("petal.length")
# node1 = id3.Vertex("Versicolor")
# node2 = id3.Vertex("Virginica")
# node3 = id3.Vertex("sepal.width")
# edge1 = id3.Edge(" < 2.2", node1)
# edge2 = id3.Edge(" >= 2.2", node2)
# node3.add_edge(edge1)
# node3.add_edge(edge2)
# edge3 = id3.Edge(" >= 1", node3)
# node4 = id3.Vertex("petal.width")
# node4.add_edge(edge3)
# edge4 = id3.Edge(">= 4.9", node4)
# node5 = id3.Vertex("sepal.length")
# node5.add_edge(edge4)
# node6 = id3.Vertex("Sentosa")
# edge5 = id3.Edge(" > 3", node5)
# edge6 = id3.Edge("< 3 ", node6)
# root.add_edge(edge5)
# root.add_edge(edge6)

# id3.print_tree(root,0)
# new_instance = create_new_instance()
# classify_new_instance(root, new_instance)
