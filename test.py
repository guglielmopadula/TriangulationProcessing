import meshio
import numpy as np
from dijkstra import dijkstra
from tqdm import trange

def find_common_points(mesh1,mesh2):
    l=[]
    for i in trange(len(mesh2.points)):
        l.append(np.argmin(np.linalg.norm(mesh1.points-mesh2.points[i],axis=1)))

    return l


def create_linear_graph(triangulation):
    len_points=np.max(triangulation)+1
    edges=set([])
    for t in triangulation:
        edges.add(tuple([t[0],t[1]]))
        edges.add(tuple([t[1],t[0]]))
        edges.add(tuple([t[1],t[2]]))
        edges.add(tuple([t[2],t[1]]))
        edges.add(tuple([t[0],t[2]]))
        edges.add(tuple([t[2],t[0]]))
        edges.add(tuple([t[0],t[0]]))
        edges.add(tuple([t[1],t[1]]))
        edges.add(tuple([t[2],t[2]]))

    return edges


def create_adjacency_list(triangulation):
    len_points=np.max(triangulation)+1
    adjacency_list=[set([]) for i in range(len_points)]
    for t in triangulation:
        adjacency_list[t[0]].add(t[1])
        adjacency_list[t[0]].add(t[2])
        adjacency_list[t[1]].add(t[0])
        adjacency_list[t[1]].add(t[2])
        adjacency_list[t[2]].add(t[0])
        adjacency_list[t[2]].add(t[1])

    return adjacency_list


def create_pooling_graph(adjlist,common_points,len_points):
    arr=[]
    for i in trange(len_points):
        test=np.array(dijkstra(i,adjlist,len_points))
        test=test[common_points]
        index=np.argmin(test)
        arr.append([i,index])
    return arr


for i in range(5):
    fmesh=meshio.read("Bunny_red_"+str(i)+".stl")
    triangles=fmesh.cells_dict["triangle"]
    lin=create_linear_graph(triangles)
    adj_list=create_adjacency_list(triangles)
    np.save("from_"+str(i)+"_to_"+str(i)+".npy",lin)
    smesh=meshio.read("Bunny_red_"+str(i+1)+".stl")
    l=find_common_points(fmesh,smesh)
    pool=create_pooling_graph(adj_list,l,len(fmesh.points))
    np.save("from_"+str(i)+"_to_"+str(i+1)+".npy",pool)



fmesh=meshio.read("Bunny_red_5.stl")
triangles=fmesh.cells_dict["triangle"]
lin=create_linear_graph(triangles)
np.save("from_5_to_5.npy",lin)







