class graph :
    n = -1
    c = 1
    visited = {1 : [0,0]}
    node = int()
    parent = int()
    a = int ()
    b = int ()

def fillA(obb,p) :
    print("fillA")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    temp = []
    temp = [3 , obb.b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        #visited = {}
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(3)
        graph.visited[graph.c].append(obb.b)
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].a=3
        obj[graph.n].b=obb.b
        obj[graph.n].parent = p
        print(obj[graph.n].a,obj[graph.n].b)
    obb.a=tempa
    obb.b=tempb
        
    
def fillB(obb,p) :
    print("fillB")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    temp = []
    temp = [obb.a , 4]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        #visited[c] = {}
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(obb.a)
        graph.visited[graph.c].append(4)
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].a=obb.a
        obj[graph.n].b=4
        print(obj[graph.n].a,obj[graph.n].b)
        obj[graph.n].parent = p
        #print("updated ")
        #print(graph.visited)
    obb.a=tempa
    obb.b=tempb

def emptyA(obb,p) :
    print("emptyA")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    temp = []
    temp = [0, obb.b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        #visited[c] = {}
        graph.c = graph.c +1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(0)
        graph.visited[graph.c].append(obb.b)
        #print("updated ")
        #print(graph.visited)
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].parent = p
        obj[graph.n].a=0
        obj[graph.n].b=obb.b
        print(obj[graph.n].a,obj[graph.n].b)
        #print("test!!")
        #print(obb.a)
        #print(obb.b)
    obb.a=tempa
    obb.b=tempb
def emptyB(obb,p) :
    print("emptyB")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    temp = []
    temp = [obb.a , 0]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        #visited[c] = {}
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(obb.a)
        graph.visited[graph.c].append(0)
        #print("updated ")
        #print(graph.visited)
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].a=obb.a
        obj[graph.n].b=0
        obj[graph.n].parent = p
        print(obj[graph.n].a,obj[graph.n].b)
    obb.a=tempa
    obb.b=tempb

def AtoB(obb,p) :
    print("AtoB")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    empty=4-obb.b
    if obb.a<=empty:
        obb.b=obb.b+obb.a
        obb.a=0
    else:
        obb.a=obb.a-empty
        obb.b=4
    temp = []
    temp = [obb.a , obb.b]
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    
    if check == 0:
        #visited[c] = {}
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(obb.a)
        graph.visited[graph.c].append(obb.b)
        #print("updated ")
        #print(graph.visited)
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].a=obb.a
        obj[graph.n].b=obb.b
        obj[graph.n].parent = p
        print(obj[graph.n].a,obj[graph.n].b)
    obb.a=tempa
    obb.b=tempb

def BtoA(obb,p) :
    print("BtoA")
    #graph.n = obb.node
    tempa=obb.a
    tempb=obb.b
    empty=3-obb.a
    print(empty)
    if obb.b<=empty:
        obb.a=obb.a+obb.b
        obb.b=0
    else:
        obb.b=obb.b-empty
        obb.a=3
    temp = []
    temp = [obb.a , obb.b]
    #print(temp)
    check = 0
    for i in graph.visited:
        if graph.visited[i] == temp:
            check = 1
    if check == 0:
        #visited[c] = {}
        graph.c = graph.c+1
        graph.visited[graph.c] = []
        graph.visited[graph.c].append(obb.a)
        graph.visited[graph.c].append(obb.b)
        #print("updated ")
        #print(graph.visited)
        #emptyA(obj[graph.n])
        graph.n = graph.n+1
        print(p)
        print(graph.n)
        obj[graph.n] = graph()
        obj[graph.n].parent = p
        obj[graph.n].a=obb.a
        obj[graph.n].b=obb.b
        print(obj[graph.n].a,obj[graph.n].b)
    obb.a=tempa
    obb.b=tempb
obj = {}
graph.n = graph.n+1
obj[graph.n] = graph()
obj[graph.n].parent=-1
obj[graph.n].a=0
obj[graph.n].b=0
a=0
while a<=graph.n:
    fillA(obj[a],a)
    fillB(obj[a],a)
    emptyA(obj[a],a)
    emptyB(obj[a],a)
    AtoB(obj[a],a)
    BtoA(obj[a],a)
    a=a+1
print(graph.visited)
final =int()
for i in range(0, graph.n):
    if obj[i].a==0 and obj[i].b==2:
        final = i
        #break
graph.n=final
while obj[graph.n].parent > -1 :
    print(obj[graph.n].a,obj[graph.n].b)
    graph.n=obj[graph.n].parent
print(obj[graph.n].a,obj[graph.n].b)
