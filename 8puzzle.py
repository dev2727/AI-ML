# Hello World program in Python
    
#print "Hello World!\n"
goal =[1,2,3,4,5,6,7,8,0]
class graph :
    target=int()
    stop=0
    n = -1
    c = 1
    visited = {1 : [4,3,8,0,1,2,6,7,5]}
    node = int()
    parent = int()
    a = {}
    a[1] = int ()
    a[2] = int ()
    a[3] = int ()
    a[4] = int ()
    a[5] = int ()
    a[6] = int ()
    a[7] = int ()
    a[8] = int ()
    a[9] = int () 
    b = int()
def up(obb = graph(),p = int(),s =int()) :
    print("up")
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=temp1=obb.a[1]
    obj[graph.n].a[2]=temp2=obb.a[2]
    obj[graph.n].a[3]=temp3=obb.a[3]
    obj[graph.n].a[4]=temp4=obb.a[4]
    obj[graph.n].a[5]=temp5=obb.a[5]
    obj[graph.n].a[6]=temp6=obb.a[6]
    obj[graph.n].a[7]=temp7=obb.a[7]
    obj[graph.n].a[8]=temp8=obb.a[8]
    obj[graph.n].a[9]=temp9=obb.a[9]
    obj[graph.n].b=temp10=s
    print(obj[graph.n].b)
    obj[graph.n].parent = p
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[2]!=0 and obj[graph.n].a[3]!=0:
        print(obj[graph.n].b)
        #obj[graph.n].b=obj[graph.n]-3
        #print(obj[graph.n].a[7])
        temp=obj[graph.n].b
        temp=temp-3
        #print(obj[graph.n].a[obj[graph.n].b])
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        #print(obj[graph.n].a[obj[graph.n].b])
        #print(obj[graph.n].a[7])
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        print(obj[graph.n].b)
        ss=obj[graph.n].b
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if temp==goal:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.n
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                up(obj[graph.n],pp,ss)
            if graph.stop==0:
                left(obj[graph.n],pp,ss)
            if graph.stop==0:
                right(obj[graph.n],pp,ss)
    obb.a[1]=temp1
    obb.a[2]=temp2
    obb.a[3]=temp3
    obb.a[4]=temp4
    obb.a[5]=temp5
    obb.a[6]=temp6
    obb.a[7]=temp7
    obb.a[8]=temp8
    obb.a[9]=temp9
    obb.b=temp10
        
        
def down(obb = graph(),p = int(),s=int()) :
    print("down")
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=temp1=obb.a[1]
    obj[graph.n].a[2]=temp2=obb.a[2]
    obj[graph.n].a[3]=temp3=obb.a[3]
    obj[graph.n].a[4]=temp4=obb.a[4]
    obj[graph.n].a[5]=temp5=obb.a[5]
    obj[graph.n].a[6]=temp6=obb.a[6]
    obj[graph.n].a[7]=temp7=obb.a[7]
    obj[graph.n].a[8]=temp8=obb.a[8]
    obj[graph.n].a[9]=temp9=obb.a[9]
    obj[graph.n].b=temp10=s
    obj[graph.n].parent = p
    if obj[graph.n].a[7]!=0 and obj[graph.n].a[8]!=0 and obj[graph.n].a[9]!=0:
        #obj[graph.n].b=obj[graph.n]-3
        print(obj[graph.n].b)
        temp=obj[graph.n].b
        temp=temp+3
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        print(obj[graph.n].b)
        ss=obj[graph.n].b
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if temp==goal:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.n
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            #up(obj[graph.n],pp)
            if graph.stop==0:
                left(obj[graph.n],pp,ss)
            if graph.stop==0:
                down(obj[graph.n],pp,ss)
            if graph.stop==0:
                right(obj[graph.n],pp,ss)
    obb.a[1]=temp1
    obb.a[2]=temp2
    obb.a[3]=temp3
    obb.a[4]=temp4
    obb.a[5]=temp5
    obb.a[6]=temp6
    obb.a[7]=temp7
    obb.a[8]=temp8
    obb.a[9]=temp9
    obb.b=temp10

def right(obb = graph(),p = int(),s=int()) :
    print("right")
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=temp1=obb.a[1]
    obj[graph.n].a[2]=temp2=obb.a[2]
    obj[graph.n].a[3]=temp3=obb.a[3]
    obj[graph.n].a[4]=temp4=obb.a[4]
    obj[graph.n].a[5]=temp5=obb.a[5]
    obj[graph.n].a[6]=temp6=obb.a[6]
    obj[graph.n].a[7]=temp7=obb.a[7]
    obj[graph.n].a[8]=temp8=obb.a[8]
    obj[graph.n].a[9]=temp9=obb.a[9]
    obj[graph.n].b=temp10=s
    obj[graph.n].parent = p
    if obj[graph.n].a[3]!=0 and obj[graph.n].a[6]!=0 and obj[graph.n].a[9]!=0:
        #obj[graph.n].b=obj[graph.n]-3
        print(obj[graph.n].b)
        temp=obj[graph.n].b
        temp=temp+1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        ss=obj[graph.n].b
        print(obj[graph.n].b)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if temp==goal:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.n
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                up(obj[graph.n],pp,ss)
            if graph.stop==0:
                down(obj[graph.n],pp,ss)
            if graph.stop==0:
                right(obj[graph.n],pp,ss)
    obb.a[1]=temp1
    obb.a[2]=temp2
    obb.a[3]=temp3
    obb.a[4]=temp4
    obb.a[5]=temp5
    obb.a[6]=temp6
    obb.a[7]=temp7
    obb.a[8]=temp8
    obb.a[9]=temp9
    obb.b=temp10

def left(obb = graph(),p = int(),s=int()) :
    print("left")
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=temp1=obb.a[1]
    obj[graph.n].a[2]=temp2=obb.a[2]
    obj[graph.n].a[3]=temp3=obb.a[3]
    obj[graph.n].a[4]=temp4=obb.a[4]
    obj[graph.n].a[5]=temp5=obb.a[5]
    obj[graph.n].a[6]=temp6=obb.a[6]
    obj[graph.n].a[7]=temp7=obb.a[7]
    obj[graph.n].a[8]=temp8=obb.a[8]
    obj[graph.n].a[9]=temp9=obb.a[9]
    obj[graph.n].b=temp10=s
    print(obj[graph.n].b)
    obj[graph.n].parent = p
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[4]!=0 and obj[graph.n].a[7]!=0:
        #obj[graph.n].b=obj[graph.n]-3
        print(obj[graph.n].b)
        temp=obj[graph.n].b
        temp=temp-1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        print(obj[graph.n].b)
        ss=obj[graph.n].b
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if temp==goal:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.n
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                up(obj[graph.n],pp,ss)
            if graph.stop==0:
                down(obj[graph.n],pp,ss)
            if graph.stop==0:
                left(obj[graph.n],pp,ss)
    obb.a[1]=temp1
    obb.a[2]=temp2
    obb.a[3]=temp3
    obb.a[4]=temp4
    obb.a[5]=temp5
    obb.a[6]=temp6
    obb.a[7]=temp7
    obb.a[8]=temp8
    obb.a[9]=temp9
    obb.b=temp10


obj = {}
graph.n = graph.n+1
obj[graph.n] = graph()
obj[graph.n].node=graph.n
obj[graph.n].parent=-1
obj[graph.n].a[1]=4
obj[graph.n].a[2]=3
obj[graph.n].a[3]=8
obj[graph.n].a[4]=0
obj[graph.n].a[5]=1
obj[graph.n].a[6]=2
obj[graph.n].a[7]=6
obj[graph.n].a[8]=7
obj[graph.n].a[9]=5
obj[graph.n].b=4
up(obj[graph.n],0,4)
down(obj[graph.n],0,4)
right(obj[graph.n],0,4)
left(obj[graph.n],0,4)
print(graph.visited)
print(graph.target)
#graph.n=graph.target
#print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
final =int()
'''for i in range(graph.c):
    if graph.visited[i]==goal:
        final = i
        break
graph.n=final
print(final)
#graph.n=graph.target
print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
#print(obj[7].parent)
#print(obj[7].a1,obj[7].b1,obj[7].a2,obj[7].b2)
while obj[graph.n].parent != -1 :
    print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
    graph.n=obj[graph.n].parent
    print(graph.n)
print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])'''
