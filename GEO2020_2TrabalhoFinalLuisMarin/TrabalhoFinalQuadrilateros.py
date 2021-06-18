import math
import glob
import numpy as np
import pandas as pd
from time import time
import matplotlib.pyplot as plt
from sympy import Point, Polygon

path = 'Files/'
path2 = 'Results/'

# draw points on the plane
def plotPoints(name,puntos):
    lista = puntos[:,-1]
    plt.title(name[:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/original_' + name[0:-4] +'.png')
    plt.show()
    
# draw points and outline on the plane 
def plotPointsOutline(name,puntos,outline):
    outline = np.append(outline,outline[0])
    x = []
    y = []
    for i in range(0, len(outline)):
        x.append(puntos[:,0][outline[i]])
        y.append(puntos[:,1][outline[i]])
    plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title(name[0:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/outline_' + name[0:-4] +'.png')
    plt.show()



# draw points and triangles on the plane 
def plotPointsTriangles(name,puntos,triangles):
    maximo = triangles['t'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['t']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Triangles_' + name[:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/Triangles_' + name + '.png')
    plt.show()
    
# draw points and triangles and dual Graph on the plane 
def plotPointsTrianglesPlusGraph(name,puntos,triangles,dualGraph):
    maximo = triangles['t'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['t']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Triangles_' + name[:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    x = dualGraph.iloc[:,1].values
    y = dualGraph.iloc[:,2].values
    plt.plot(x, y,'bo-')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/Triangles_' + name + '.png')
    plt.show()
    
# draw points and quadrilaterals on the plane for indirectMethod1 with vertex Name
def plotPointsIndiretQuadrilate(name,puntos,triangles,outline):
    #print(outline)
    outline = np.append(outline,outline[0])
    #print(outline)
    x = []
    y = []
    for i in range(0, len(outline)):
        x.append(puntos[:,0][outline[i]])
        y.append(puntos[:,1][outline[i]])
    plt.plot(x, y,'bo-')
    maximo = triangles['Q'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Quadrilate_' + name[:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/QuadrilateVertex_' + name + '.png')
    plt.show()
    
# draw points and quadrilaterals on the plane for indirectMethod1 without vertex Name
def plotPointsIndiretQuadrilateWithout(name,puntos,triangles,outline):
    #print(outline)
    outline = np.append(outline,outline[0])
    #print(outline)
    x = []
    y = []
    for i in range(0, len(outline)):
        x.append(puntos[:,0][outline[i]])
        y.append(puntos[:,1][outline[i]])
    plt.plot(x, y,'bo-')
    maximo = triangles['Q'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Quadrilate_' + name[:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
# =============================================================================
#     i = 0
#     for x,y,z in puntos:
#         text = "v{v:d}"
#         label = text.format(v = int(lista[i]))
#         i += 1
#         plt.annotate(label, # this is the text
#                      (x,y), # this is the point to label
#                      textcoords="offset points", # how to position the text
#                      xytext=(0,5), # distance from text to points (x,y)
#                      ha='center') # horizontal alignment can be left, right or center
# =============================================================================
    plt.savefig('Figures/Quadrilate_' + name + '.png')
    plt.show()
    
# draw points and quadrilaterals on the plane with vertex name
def plotPointsQuadrilate(name,puntos,quadrilate,triangles):
    maximo = triangles['t'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['t']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    maximo = int(quadrilate['Q'].max())
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = quadrilate[quadrilate['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Quadrilate_' + name[0:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/QuadrilateVertex_' + name + '.png')
    plt.show()
    
# draw points and quadrilaterals on the plane without vertex name
def plotPointsQuadrilateWithout(name,puntos,quadrilate,triangles):
    maximo = triangles['t'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['t']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    maximo = int(quadrilate['Q'].max())
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = quadrilate[quadrilate['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('Quadrilate_' + name[0:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
# =============================================================================
#     i = 0
#     for x,y,z in puntos:
#         text = "v{v:d}"
#         label = text.format(v = int(lista[i]))
#         i += 1
#         plt.annotate(label, # this is the text
#                      (x,y), # this is the point to label
#                      textcoords="offset points", # how to position the text
#                      xytext=(0,5), # distance from text to points (x,y)
#                      ha='center') # horizontal alignment can be left, right or center
# =============================================================================
    plt.savefig('Figures/Quadrilate_' + name + '.png')
    plt.show()
    
# draw points and quadrilaterals on the plane for indirect2 function with vertex Name
def plotPointsQuadrilate2(name,puntos,quadrilate,triangles):
    maximo = triangles['Q'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    maximo = int(quadrilate['Q'].max())
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = quadrilate[quadrilate['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('QuadrilateInd2_' + name[0:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
    i = 0
    for x,y,z in puntos:
        text = "v{v:d}"
        label = text.format(v = int(lista[i]))
        i += 1
        plt.annotate(label, # this is the text
                     (x,y), # this is the point to label
                     textcoords="offset points", # how to position the text
                     xytext=(0,5), # distance from text to points (x,y)
                     ha='center') # horizontal alignment can be left, right or center
    plt.savefig('Figures/QuadrilateInd2Vertex_' + name + '.png')
    plt.show()    

# draw points and quadrilaterals on the plane for indirect2 function without vertex Name
def plotPointsQuadrilate2without(name,puntos,quadrilate,triangles):
    maximo = triangles['Q'].max()
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = triangles[triangles['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    maximo = int(quadrilate['Q'].max())
    for j in range(0,maximo + 1):
        x = []
        y = []
        data = quadrilate[quadrilate['Q']==j].values
        for k in range(0,len(data)):
            x.append(data[k,1])
        x.append(data[0,1])
        for k in range(0,len(data)):
            y.append(data[k,2])
        y.append(data[0,2])
        plt.plot(x, y,'bo-')
    lista = puntos[:,-1]
    plt.title('QuadrilateInd2_' + name[0:-4])
    plt.plot(puntos[:,[0]], puntos[:,[1]],'bo')
# =============================================================================
#     i = 0
#     for x,y,z in puntos:
#         text = "v{v:d}"
#         label = text.format(v = int(lista[i]))
#         i += 1
#         plt.annotate(label, # this is the text
#                      (x,y), # this is the point to label
#                      textcoords="offset points", # how to position the text
#                      xytext=(0,5), # distance from text to points (x,y)
#                      ha='center') # horizontal alignment can be left, right or center
# =============================================================================
    plt.savefig('Figures/QuadrilateInd2_' + name + '.png')
    plt.show()    
    

# find the point with the smallest angle between vertex
def angleVertex(x1,y1,x2,y2,x3,y3):
    vector_1 = [x2 - x1, y2 - y1]
    vector_2 = [x3 - x1, y3 - y1]
    cosTh = np.dot(vector_1,vector_2)
    sinTh = np.cross(vector_1,vector_2)
    angle = np.rad2deg(np.arctan2(sinTh,cosTh))
    if ( angle < 0):
        return 360 + angle
    else:
        return angle
    

# Determine the angle between a reference point and two points in radians
def findAngle(x1,y1,x3,y3,x4,y4):
    x2 = x1+ 10
    y2 = y1
    vector_1 = [x2 - x1, y2 - y1]
    vector_2 = [x3 - x1, y3 - y1]
    cosTh = np.dot(vector_1,vector_2)
    sinTh = np.cross(vector_1,vector_2)
    angle1 = np.rad2deg(np.arctan2(sinTh,cosTh))
    vector_2 = [x4 - x1, y4 - y1]
    cosTh = np.dot(vector_1,vector_2)
    sinTh = np.cross(vector_1,vector_2)
    angle2 = np.rad2deg(np.arctan2(sinTh,cosTh))
    return angle1, angle2 


# Find the positive order in which the vertices should be stored
def dataforAngles(ang1,ang2,v1,ax,ay,v2,bx,by,trian,tableVertex,x):
    if(np.sign(ang1) == np.sign(ang2)):
        if(np.sign(ang1) < 0):
            if(abs(ang1) > abs(ang2)):
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
            else:
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
        else:
            if(ang1 < ang2):
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
            else:
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
    else:
        if(x < ax):
            if(ang1 < ang2):
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
            else:
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
        else:
            if(ang1 < ang2):
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
            else:
                new_vertex = {'V':v1, 'x':ax, 'y':ay, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                new_vertex = {'V':v2, 'x':bx, 'y':by, 't':trian}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
    return tableVertex

# Determine if a point is to the right of a line defined by two points.
def pointRight(ax, ay, bx, by, cx, cy):
    return (((bx - ax)*(cy - ay) - (by - ay)*(cx - ax)) < 0)
#Donde a \= punto de línea 1; b \= punto de línea 2; c \= punto a comprobar.


# Define if the angles of the 3 points are convex
def isConvex2(x1,y1,x2,y2,x3,y3):
    vector_1 = [x2 - x1, y2 - y1]
    vector_2 = [x3 - x1, y3 - y1]
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    degrees = math.degrees(angle)
    return degrees

# Inter triangle angles
def needinvertEdge(t1,t2,equal,differ,sort,tableTriangle):
    tv1 = tableTriangle[tableTriangle['t']==t1].values.flatten()
    tv2 = tableTriangle[tableTriangle['t']==t2].values.flatten()
    t1ver = [tv1[1],tv1[2],tv1[3]]
    t2ver = [tv2[1],tv2[2],tv2[3]]
    t3ver = [differ[0],differ[1],equal[0]]
    t4ver = [differ[0],equal[1],differ[1]]
    angles = []
    
    x1 = sort[t1ver[0],0]
    y1 = sort[t1ver[0],1]
    x2 = sort[t1ver[1],0]
    y2 = sort[t1ver[1],1]
    x3 = sort[t1ver[2],0]
    y3 = sort[t1ver[2],1]
    p1, p2, p3 = map(Point, [(x1,y1),(x2,y2),(x3,y3)])
    poly = Polygon(p1, p2, p3 )
    point = [p1, p2, p3]
    for i in range(0,3):
        temp = math.degrees(poly.angles[point[i]].evalf())
        angles.append(temp)
    
    x1 = sort[t2ver[0],0]
    y1 = sort[t2ver[0],1]
    x2 = sort[t2ver[1],0]
    y2 = sort[t2ver[1],1]
    x3 = sort[t2ver[2],0]
    y3 = sort[t2ver[2],1]
    p1, p2, p3 = map(Point, [(x1,y1),(x2,y2),(x3,y3)])
    poly = Polygon(p1, p2, p3 )
    point = [p1, p2, p3]
    for i in range(0,3):
        temp = math.degrees(poly.angles[point[i]].evalf())
        angles.append(temp)
    
    
    list1 = sorted(angles, key=float)
    angles = []
    
    x1 = sort[t3ver[0],0]
    y1 = sort[t3ver[0],1]
    x2 = sort[t3ver[1],0]
    y2 = sort[t3ver[1],1]
    x3 = sort[t3ver[2],0]
    y3 = sort[t3ver[2],1]
    p1, p2, p3 = map(Point, [(x1,y1),(x2,y2),(x3,y3)])
    poly = Polygon(p1, p2, p3 )
    point = [p1, p2, p3]
    for i in range(0,3):
        temp = math.degrees(poly.angles[point[i]].evalf())
        angles.append(temp)
       
    x1 = sort[t4ver[0],0]
    y1 = sort[t4ver[0],1]
    x2 = sort[t4ver[1],0]
    y2 = sort[t4ver[1],1]
    x3 = sort[t4ver[2],0]
    y3 = sort[t4ver[2],1]
    p1, p2, p3 = map(Point, [(x1,y1),(x2,y2),(x3,y3)])
    poly = Polygon(p1, p2, p3 )
    point = [p1, p2, p3]
    for i in range(0,3):
        temp = math.degrees(poly.angles[point[i]].evalf())
        angles.append(temp)

    
    list2 = sorted(angles, key=float)

    i = 0
    while (i < len(list1)):
        if(list1[i] != list2[i]):
            if(list1[i] < list2[i]):
                return True
            else:
                return False
        i += 1
    return False
    
    

# Define if the angles of the 4 points are convex
def convex(t1,t2,sort,tableTriangle):
    tv1 = tableTriangle[tableTriangle['t']==t1].values.flatten()
    tv2 = tableTriangle[tableTriangle['t']==t2].values.flatten()
    #print(tv1,tv2)
    equal = []
    differ = []
    for l in range(1,4):
        if(tv1[l] in tv2[1:4]):
            equal.append(tv1[l])
        else:
            differ.append(tv1[l])
    for l in range(1,4):
        if(tv2[l] not in equal):
            differ.append(tv2[l])
    #print(f'equals: {equal}, different: {differ}')
    p1, p2, p3, p4 = map(Point, [(sort[differ[0],0], sort[differ[0],1]), (sort[equal[0],0], sort[equal[0],1]), (sort[differ[1],0], 
                                 sort[differ[1],1]), (sort[equal[1],0], sort[equal[1],1])])
    poly = Polygon(p1, p2, p3, p4 )
    point = [p1, p2, p3, p4]
    for i in range(0,4):
        angle = math.degrees(poly.angles[point[i]].evalf())
        if (angle > 180):
            return False, equal,differ
    return True, equal,differ

    
# Triangle table construction
def triangleTableB(tableVertex,tableTriangle):
    maximo = len(tableVertex)
    for k in range(0, maximo,3):
        new_triangle = {'t':tableVertex.iloc[k,3], 'V0':tableVertex.iloc[k,0], 'V1':tableVertex.iloc[k+1,0],'V2':tableVertex.iloc[k+2,0],'t0':-1,'t1':-1,'t2':-1}
        tableTriangle = tableTriangle.append(new_triangle,ignore_index=True)

    ind = np.full(len(tableTriangle),4)
    for l in range(0,len(tableTriangle) - 1):
        end = False
        i = l + 1
        anchor = tableTriangle[tableTriangle['t']==l].values.flatten()
        while not end and ind[i] != 7:
            slide = tableTriangle[tableTriangle['t']==i].values.flatten()
            if(((anchor[1]==slide[1] or anchor[1]==slide[2] or anchor[1]==slide[3]) and 
               (anchor[2]==slide[1] or anchor[2]==slide[2] or anchor[2]==slide[3])) or
               ((anchor[3]==slide[1] or anchor[3]==slide[2] or anchor[3]==slide[3]) and 
               (anchor[2]==slide[1] or anchor[2]==slide[2] or anchor[2]==slide[3])) or
               ((anchor[1]==slide[1] or anchor[1]==slide[2] or anchor[1]==slide[3]) and 
               (anchor[3]==slide[1] or anchor[3]==slide[2] or anchor[3]==slide[3]))):
                if(ind[l] == 4):
                    tableTriangle.loc[tableTriangle['t']==l, 't0'] = slide[0]
                    ind[l] += 1
                    if(ind[i] == 4):
                        tableTriangle.loc[tableTriangle['t']==i, 't0'] = anchor[0]
                        ind[i] += 1
                    elif(ind[i] == 5):
                        tableTriangle.loc[tableTriangle['t']==i, 't1'] = anchor[0]
                        ind[i] += 1
                    else:
                        tableTriangle.loc[tableTriangle['t']==i, 't2'] = anchor[0]
                        ind[i] += 1
                elif(ind[l] == 5):
                    tableTriangle.loc[tableTriangle['t']==l, 't1'] = slide[0]
                    ind[l] += 1
                    if(ind[i] == 4):
                        tableTriangle.loc[tableTriangle['t']==i, 't0'] = anchor[0]
                        ind[i] += 1
                    elif(ind[i] == 5):
                        tableTriangle.loc[tableTriangle['t']==i, 't1'] = anchor[0]
                        ind[i] += 1
                    else:
                        tableTriangle.loc[tableTriangle['t']==i, 't2'] = anchor[0]
                        ind[i] += 1
                else:
                    tableTriangle.loc[tableTriangle['t']==l, 't2'] = slide[0]
                    ind[l] += 1
                    if(ind[i] == 4):
                        tableTriangle.loc[tableTriangle['t']==i, 't0'] = anchor[0]
                        ind[i] += 1
                    elif(ind[i] == 5):
                        tableTriangle.loc[tableTriangle['t']==i, 't1'] = anchor[0]
                        ind[i] += 1
                    else:
                        tableTriangle.loc[tableTriangle['t']==i, 't2'] = anchor[0]
                        ind[i] += 1
                if(ind[l] == 7):
                    end = True
            i += 1
            if(i == len(tableTriangle)):
                end = True
    return tableTriangle

# Triangle table construction
def triangleTable(tableVertex2,tableTriangle):
    tableVertex = tableVertex2.copy()
    maximo = len(tableVertex)
    for k in range(0, maximo,3):
        new_triangle = {'t':tableVertex.iloc[k,3], 'V0':tableVertex.iloc[k,0], 'V1':tableVertex.iloc[k+1,0],'V2':tableVertex.iloc[k+2,0],'t0':-1,'t1':-1,'t2':-1}
        tableTriangle = tableTriangle.append(new_triangle,ignore_index=True)
    
    for i in range(0,len(tableTriangle)):
        tv1 = tableVertex[tableVertex.V == tableTriangle.iloc[i,1]]
        tv2 = tv1.iloc[:,3].values
        for j in tv2:
            if( j != tableTriangle.iloc[i,0]):
                tv3 = tableVertex[tableVertex.t == j]
                tv4 = tv3.iloc[:,0].values

                if(tableTriangle.iloc[i,2] in tv4):
                    if(tableTriangle.iloc[i,4] == -1):
                        tableTriangle.iloc[i,4] = j
                    elif(tableTriangle.iloc[i,5] == -1):
                        tableTriangle.iloc[i,5] = j
                    elif(tableTriangle.iloc[i,6] == -1):
                        tableTriangle.iloc[i,6] = j
                    else:
                        print("error")
                
                if(tableTriangle.iloc[i,3] in tv4):
                    if(tableTriangle.iloc[i,4] == -1):
                        tableTriangle.iloc[i,4] = j
                    elif(tableTriangle.iloc[i,5] == -1):
                        tableTriangle.iloc[i,5] = j
                    elif(tableTriangle.iloc[i,6] == -1):
                        tableTriangle.iloc[i,6] = j
                    else:
                        print("error")
        tv5 = tableVertex[tableVertex.V == tableTriangle.iloc[i,2]]
        tv6 = tv5.iloc[:,3].values
        for j in tv6:
            if( j != tableTriangle.iloc[i,0]):
                tv7 = tableVertex[tableVertex.t == j]
                tv8 = tv7.iloc[:,0].values
                if(tableTriangle.iloc[i,3] in tv8):
                    if(tableTriangle.iloc[i,4] == -1):
                        tableTriangle.iloc[i,4] = j
                    elif(tableTriangle.iloc[i,5] == -1):
                        tableTriangle.iloc[i,5] = j
                    elif(tableTriangle.iloc[i,6] == -1):
                        tableTriangle.iloc[i,6] = j
                    else:
                        print("error")
    return tableTriangle

# find the center point between two points
def midpoint(x0,y0,x1,y1):
    return ((x0 + x1)/2),((y0 + y1)/2)

# Funtion for application of the Catmull-Clark Quadrilateral Method
def catnullQuad(tableVertex,sort,fileName,convexClosure):
    limit = tableVertex['t'].max()
    numVertex = tableVertex['V'].max()
    indexQuad = int(0)
    tableQuad = pd.DataFrame(columns = ['V', 'x', 'y','Q']) 

    for i in range(0,limit + 1):
        tv1 = tableVertex[tableVertex['t']==i]
        tv1 = tv1.reset_index(drop = True)
        new_vertex = {'V':tv1.iloc[0,0], 'x':tv1.iloc[0,1], 'y':tv1.iloc[0,2], 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        x1,y1 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[1,1],tv1.iloc[1,2])
        exist = tableQuad.index[tableQuad['x'] == x1].tolist()
        
        if len(exist) != 0:
            vertex1 = -1
            for ind in exist:
                if(tableQuad.iloc[ind,2] == y1):
                    vertex1 = tableQuad.iloc[ind,0]
            if(vertex1 == -1):
                numVertex += 1
                vertex1 = numVertex
        else:
            numVertex += 1
            vertex1 = numVertex
            
        new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        sort = np.append(sort,[[x1,y1,vertex1]], axis = 0)
        centerX = (tv1.iloc[0,1] + tv1.iloc[1,1] + tv1.iloc[2,1])/3
        centerY = (tv1.iloc[0,2] + tv1.iloc[1,2] + tv1.iloc[2,2])/3
        numVertex += 1
        centerNum = numVertex
        new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        sort = np.append(sort,[[centerX,centerY,centerNum]], axis = 0)
        x3,y3 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[2,1],tv1.iloc[2,2])
        
        exist = tableQuad.index[tableQuad['x'] == x3].tolist()
        if len(exist) != 0:
            vertex3 = -1
            for ind in exist:
                if(tableQuad.iloc[ind,2] == y3):
                    vertex3 = tableQuad.iloc[ind,0]
            if(vertex3 == -1):
                numVertex += 1
                vertex3 = numVertex
        else:
            numVertex += 1
            vertex3 = numVertex
        
        new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        sort = np.append(sort,[[x3,y3,vertex3]], axis = 0)
        
        indexQuad += 1
        new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        new_vertex = {'V':tv1.iloc[1,0], 'x':tv1.iloc[1,1], 'y':tv1.iloc[1,2], 'Q':indexQuad}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        x2,y2 = midpoint(tv1.iloc[1,1],tv1.iloc[1,2],tv1.iloc[2,1],tv1.iloc[2,2])
        
        exist = tableQuad.index[tableQuad['x'] == x2].tolist()
        if len(exist) != 0:
            vertex2 = -1
            for ind in exist:
                if(tableQuad.iloc[ind,2] == y2):
                    vertex2 = tableQuad.iloc[ind,0]
            if(vertex2 == -1):
                numVertex += 1
                vertex2 = numVertex
        else:
            numVertex += 1
            vertex2 = numVertex
        
        new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        sort = np.append(sort,[[x2,y2,vertex2]], axis = 0)
        new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        
        indexQuad += 1
        new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        new_vertex = {'V':tv1.iloc[2,0], 'x':tv1.iloc[2,1], 'y':tv1.iloc[2,2], 'Q':indexQuad}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':int(indexQuad)}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
        tableQuad = tableQuad.append(new_vertex,ignore_index=True)
        indexQuad += 1
        plotPointsQuadrilate(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
        plotPointsQuadrilateWithout(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
    return tableQuad, sort

# Firs Indirect method
def indirectMethod1(tableVertex2,tableTriangle2,sort,fileName,convexClosure):
    tableVertex = tableVertex2.copy()
    tableTriangle = tableTriangle2.copy()
    tableEdges = pd.DataFrame(columns = ['Distance', 'V0', 'V1','t0','t1'])
    tableQuad = pd.DataFrame(columns = ['V', 'x', 'y','Q']) 
    indexQuad = 0
    for i in range(0,len(tableTriangle)):
        ind = 4
        while (ind < 7):
            location = tableTriangle.iloc[i,ind]
            if (location != -1):
                container1 = tableTriangle.loc[i,'V0':'V2'].values
                container2 = tableTriangle.loc[location,'V0':'V2'].values
                vertex = []
                for j in container1:
                    if (j in container2):
                        vertex.append(j)
                x1 = sort[vertex[0],0]
                y1 = sort[vertex[0],1]
                x2 = sort[vertex[1],0]
                y2 = sort[vertex[1],1]
                dist = math.dist([x1,y1], [x2,y2])
                new_vertex = {'Distance':dist, 'V0':vertex[0], 'V1':vertex[1], 't0':i, 't1':location}
                tableEdges = tableEdges.append(new_vertex,ignore_index=True)
                for k  in range(4,7):
                    if(tableTriangle.iloc[location,k] == i):
                        tableTriangle.iloc[location,k] = -1
            ind += 1
    tableEdges = tableEdges.astype({'Distance': float, 'V0':int, 'V1':int, 't0':int, 't1':int})
    tableEdges = tableEdges.sort_values(by=['Distance'],ascending=False)
    tableEdges = tableEdges.reset_index(drop = True)
    for k in range(0,len(tableEdges)):
        tem1 = tableEdges.iloc[k,:].values
        triangle1 = tableVertex2[tableVertex2['t']==int(tem1[3])]
        triangle1 = triangle1[triangle1.V != int(tem1[1])]
        triangle1 = triangle1[triangle1.V != int(tem1[2])]
        triangle1 = triangle1.reset_index(drop = True)
        triangle2 = tableVertex2[tableVertex2['t']==int(tem1[4])]
        triangle2 = triangle2[triangle2.V != int(tem1[1])]
        triangle2 = triangle2[triangle2.V != int(tem1[2])]
        triangle2 = triangle2.reset_index(drop = True)
        p1x = triangle1.iloc[0,1]
        p1y = triangle1.iloc[0,2]
        p3x = triangle2.iloc[0,1]
        p3y = triangle2.iloc[0,2]
        p2x = sort[int(tem1[1]),0]
        p2y = sort[int(tem1[1]),1]
        p4x = sort[int(tem1[2]),0]
        p4y = sort[int(tem1[2]),1]
        p1, p2, p3, p4 = map(Point, [(p1x,p1y), (p2x,p2y), (p3x,p3y), (p4x,p4y)])
        poly = Polygon(p1, p2, p3, p4 )
        point = [p1, p2, p3, p4]
        flag = True
        #print('\n')
        for i in range(0,4):
            angle = math.degrees(poly.angles[point[i]].evalf())
            #print(angle)
            if (angle >= 180):
                flag = False
        
        if ((int(tem1[3]) in tableTriangle.t.values) and (int(tem1[4]) in tableTriangle.t.values) and flag):
            
            #To mark the two triangles as cluster, they are removed from the list to not be used again.
            tableTriangle = tableTriangle[tableTriangle.t != int(tem1[3])]
            tableTriangle = tableTriangle[tableTriangle.t != int(tem1[4])]
            tableTriangle = tableTriangle.reset_index(drop = True)
            
            # Extract the triangle information V, X, Y, T
            tv1 = tableVertex[tableVertex['t']==int(tem1[3])]
            tv1 = tv1.reset_index(drop = True)
            tv2 = tableVertex[tableVertex['t']==int(tem1[4])]
            tv2 = tv2.reset_index(drop = True)
            
            #Remove the triangle to be cluster from tableVertex to not be used again
            tableVertex = tableVertex[tableVertex.t != int(tem1[3])]
            tableVertex = tableVertex[tableVertex.t != int(tem1[4])]
            tableVertex = tableVertex.reset_index(drop = True)
            
            ver = [int(tem1[1]),int(tem1[2])]
            exist = tv1.index[tv1['V'] == ver[0]].tolist()
            
            # create the cluster and add them for new TableQuad
            if(exist[0] == 2):
                if(tv1.iloc[0,0] ==  ver[1]):
                    #Find the vertex to insert
                    vertex = tv1[tv1.V != ver[0]]
                    vertex = vertex[vertex.V != ver[1]]
                    vertex = vertex.reset_index(drop = True)

                    new_vertex = {'V':vertex.iloc[0,0], 'x':vertex.iloc[0,1], 'y':vertex.iloc[0,2], 'Q':indexQuad}
                    
                    #Replace the t value for index of quadrilate
                    tv2 = tv2.replace({"t":int(tem1[4])}, indexQuad)
                    
                    #Find the position of second common vertex
                    position1 = tv2.index[tv2['V'] == ver[1]].tolist()

                    tv2 = tv2.rename(columns={'t': 'Q'})
                    
                    #Create cluster
                    if(position1 == 2):
                        tv2 = tv2.append(new_vertex,ignore_index=True)
                    else:
                        container3 = tv2.iloc[:position1[0] + 1,:]
                        container4 = tv2.iloc[(position1[0] + 1):,:]
                        container3 = container3.append(new_vertex,ignore_index=True)
                        container3 = container3.append(container4,ignore_index=True)
                        container3 = container3.reset_index(drop = True)
                        tv2 = container3
                    tableQuad = tableQuad.append(tv2,ignore_index=True)
                    indexQuad += 1
                else:
                    #Position of second common vertex
                    position1 = 1
                    
                    #Find the vertex to insert
                    vertex = tv2[tv2.V != ver[0]]
                    vertex = vertex[vertex.V != ver[1]]
                    vertex = vertex.reset_index(drop = True)

                    new_vertex = {'V':vertex.iloc[0,0], 'x':vertex.iloc[0,1], 'y':vertex.iloc[0,2], 'Q':indexQuad}
                    
                    #Replace the t value for index of quadrilate
                    tv1 = tv1.replace({"t":int(tem1[3])}, indexQuad)
                    tv1 = tv1.rename(columns={'t': 'Q'})
                    
                    #Create cluster
                    container3 = tv1.iloc[:position1 + 1,:]
                    container4 = tv1.iloc[(position1 + 1):,:]
                    container3 = container3.append(new_vertex,ignore_index=True)
                    container3 = container3.append(container4,ignore_index=True)
                    container3 = container3.reset_index(drop = True)
                    tv1 = container3
                    tableQuad = tableQuad.append(tv1,ignore_index=True)
                    indexQuad += 1
            else:
                if(tv1.iloc[exist[0] + 1,0] ==  ver[1]):
                    #Find the vertex to insert
                    vertex = tv1[tv1.V != ver[0]]
                    vertex = vertex[vertex.V != ver[1]]
                    vertex = vertex.reset_index(drop = True)

                    new_vertex = {'V':vertex.iloc[0,0], 'x':vertex.iloc[0,1], 'y':vertex.iloc[0,2], 'Q':indexQuad}
                    
                    #Replace the t value for index of quadrilate
                    tv2 = tv2.replace({"t":int(tem1[4])}, indexQuad)
                    
                    #Find the position of second common vertex
                    position1 = tv2.index[tv2['V'] == ver[1]].tolist()

                    tv2 = tv2.rename(columns={'t': 'Q'})
                    
                    #Create cluster
                    if(position1 == 2):
                        tv2 = tv2.append(new_vertex,ignore_index=True)
                    else:
                        container3 = tv2.iloc[:position1[0] + 1,:]
                        container4 = tv2.iloc[(position1[0] + 1):,:]
                        container3 = container3.append(new_vertex,ignore_index=True)
                        container3 = container3.append(container4,ignore_index=True)
                        container3 = container3.reset_index(drop = True)
                        tv2 = container3
                    tableQuad = tableQuad.append(tv2,ignore_index=True)
                    indexQuad += 1
                else:
                    #Position of second common vertex
                    position1 = tv1.index[tv1['V'] == ver[1]].tolist()
                    
                    #Find the vertex to insert
                    vertex = tv2[tv2.V != ver[0]]
                    vertex = vertex[vertex.V != ver[1]]
                    vertex = vertex.reset_index(drop = True)

                    new_vertex = {'V':vertex.iloc[0,0], 'x':vertex.iloc[0,1], 'y':vertex.iloc[0,2], 'Q':indexQuad}
                    
                    #Replace the t value for index of quadrilate
                    tv1 = tv1.replace({"t":int(tem1[3])}, indexQuad)
                    tv1 = tv1.rename(columns={'t': 'Q'})
                    
                    #Create cluster
                    if(position1 == 2):
                        tv1 = tv1.append(new_vertex,ignore_index=True)
                    else:
                        container3 = tv1.iloc[:position1[0] + 1,:]
                        container4 = tv1.iloc[(position1[0] + 1):,:]
                        container3 = container3.append(new_vertex,ignore_index=True)
                        container3 = container3.append(container4,ignore_index=True)
                        container3 = container3.reset_index(drop = True)
                        tv1 = container3
                    tableQuad = tableQuad.append(tv1,ignore_index=True)
                    indexQuad += 1

            plotPointsIndiretQuadrilate(str(indexQuad - 1) + '_' +'Indirect1_' + fileName,sort,tableQuad,convexClosure)
            plotPointsIndiretQuadrilateWithout(str(indexQuad - 1) + '_' +'Indirect1_' + fileName,sort,tableQuad,convexClosure)
            
            
    tableVertex = tableVertex.rename(columns={'t': 'Q'})      
    while( len(tableVertex) > 0):
        value = tableVertex.iloc[0,3]
        tvt = tableVertex[tableVertex['Q']==value]
        tvt = tvt.reset_index(drop = True)
        tableVertex = tableVertex[tableVertex.Q != value]
        tableVertex = tableVertex.reset_index(drop = True)
        tvt = tvt.replace({'Q':value}, indexQuad)
        indexQuad += 1
        
        tableQuad = tableQuad.append(tvt,ignore_index=True)
        
# =============================================================================
#         tableVertex = tableVertex.replace({'Q':value}, indexQuad)
#         tableVertex = tableVertex.reset_index(drop = True)
#         tv3 = tableVertex[tableVertex['Q']==indexQuad]
#         tv3 = tv3.reset_index(drop = True)
#         tableVertex = tableVertex[tableVertex.Q != indexQuad]
#         indexQuad += 1
# 
#         tableQuad = tableQuad.append(tv3,ignore_index=True)
# =============================================================================
        
        plotPointsIndiretQuadrilate(str(indexQuad) + '_' +'Indirect1_' + fileName,sort,tableQuad,convexClosure)
        plotPointsIndiretQuadrilateWithout(str(indexQuad - 1) + '_' +'Indirect1_' + fileName,sort,tableQuad,convexClosure)

    return tableQuad, tableEdges

#Find the center of polygon
def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     return(_x, _y)

# Second Indirect method
def indirectMethod2(tableVertex2,tableTriangle2,sort,fileName,convexClosure,tableEdges):
    tableVertex = tableVertex2.copy()
    tableTriangle = tableTriangle2.copy()
    tableQuad = pd.DataFrame(columns = ['V', 'x', 'y','Q']) 
    indexQuad = 0
    limit = tableVertex['Q'].max()
    numVertex = tableVertex['V'].max()
    for i in range(0,limit + 1):
        tv1 = tableVertex[tableVertex['Q']== i]
        tv1 = tv1.reset_index(drop = True)
        if(len(tv1) == 4):
            new_vertex = {'V':tv1.iloc[0,0], 'x':tv1.iloc[0,1], 'y':tv1.iloc[0,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            x1,y1 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[1,1],tv1.iloc[1,2])
            exist = tableQuad.index[tableQuad['x'] == x1].tolist()
            if (len(exist) != 0):
                vertex1 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y1):
                        vertex1 = tableQuad.iloc[ind,0]
                if(vertex1 == -1):
                    numVertex += 1
                    vertex1 = numVertex
                    sort = np.append(sort,[[x1,y1,vertex1]], axis = 0)
            else:
                numVertex += 1
                vertex1 = numVertex
                sort = np.append(sort,[[x1,y1,vertex1]], axis = 0)
            new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            centerX, centerY = centroid(((tv1.iloc[0,1],tv1.iloc[0,2]),(tv1.iloc[1,1],tv1.iloc[1,2]),(tv1.iloc[2,1],tv1.iloc[2,2]),
                                        (tv1.iloc[3,1],tv1.iloc[3,2])))
            numVertex += 1
            centerNum = numVertex
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            sort = np.append(sort,[[centerX,centerY,centerNum]], axis = 0)
            
            x4,y4 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[3,1],tv1.iloc[3,2])
            exist = tableQuad.index[tableQuad['x'] == x4].tolist()
            if (len(exist) != 0):
                vertex4 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y4):
                        vertex4 = tableQuad.iloc[ind,0]
                if(vertex4 == -1):
                    numVertex += 1
                    vertex4 = numVertex
                    sort = np.append(sort,[[x4,y4,vertex4]], axis = 0)
            else:
                numVertex += 1
                vertex4 = numVertex
                sort = np.append(sort,[[x4,y4,vertex4]], axis = 0)
            new_vertex = {'V':vertex4, 'x':x4, 'y':y4, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            #Second quadrilater
            indexQuad += 1
            new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':tv1.iloc[1,0], 'x':tv1.iloc[1,1], 'y':tv1.iloc[1,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            x2,y2 = midpoint(tv1.iloc[1,1],tv1.iloc[1,2],tv1.iloc[2,1],tv1.iloc[2,2])
            exist = tableQuad.index[tableQuad['x'] == x2].tolist()
            if (len(exist) != 0):
                vertex2 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y2):
                        vertex2 = tableQuad.iloc[ind,0]
                if(vertex2 == -1):
                    numVertex += 1
                    vertex2 = numVertex
                    sort = np.append(sort,[[x2,y2,vertex2]], axis = 0)
            else:
                numVertex += 1
                vertex2 = numVertex
                sort = np.append(sort,[[x2,y2,vertex2]], axis = 0)
            new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            #Third quadrilater
            indexQuad += 1
            new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':tv1.iloc[2,0], 'x':tv1.iloc[2,1], 'y':tv1.iloc[2,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            x3,y3 = midpoint(tv1.iloc[2,1],tv1.iloc[2,2],tv1.iloc[3,1],tv1.iloc[3,2])
            exist = tableQuad.index[tableQuad['x'] == x3].tolist()
            if (len(exist) != 0):
                vertex3 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y3):
                        vertex3 = tableQuad.iloc[ind,0]
                if(vertex3 == -1):
                    numVertex += 1
                    vertex3 = numVertex
                    sort = np.append(sort,[[x3,y3,vertex3]], axis = 0)
            else:
                numVertex += 1
                vertex3 = numVertex
                sort = np.append(sort,[[x3,y3,vertex3]], axis = 0)
            new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            #Fourth quadrilater
            indexQuad += 1
            new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':tv1.iloc[3,0], 'x':tv1.iloc[3,1], 'y':tv1.iloc[3,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':vertex4, 'x':x4, 'y':y4, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            plotPointsQuadrilate2(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
            plotPointsQuadrilate2without(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
            indexQuad += 1
            
        else:
            new_vertex = {'V':tv1.iloc[0,0], 'x':tv1.iloc[0,1], 'y':tv1.iloc[0,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            x1,y1 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[1,1],tv1.iloc[1,2])
            exist = tableQuad.index[tableQuad['x'] == x1].tolist()
            if len(exist) != 0:
                vertex1 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y1):
                        vertex1 = tableQuad.iloc[ind,0]
                if(vertex1 == -1):
                    numVertex += 1
                    vertex1 = numVertex
                    sort = np.append(sort,[[x1,y1,vertex1]], axis = 0)
            else:
                numVertex += 1
                vertex1 = numVertex
                sort = np.append(sort,[[x1,y1,vertex1]], axis = 0)
            new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            centerX = (tv1.iloc[0,1] + tv1.iloc[1,1] + tv1.iloc[2,1])/3
            centerY = (tv1.iloc[0,2] + tv1.iloc[1,2] + tv1.iloc[2,2])/3
            numVertex += 1
            centerNum = numVertex
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            sort = np.append(sort,[[centerX,centerY,centerNum]], axis = 0)
            
            x3,y3 = midpoint(tv1.iloc[0,1],tv1.iloc[0,2],tv1.iloc[2,1],tv1.iloc[2,2])
            exist = tableQuad.index[tableQuad['x'] == x3].tolist()
            if len(exist) != 0:
                vertex3 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y3):
                        vertex3 = tableQuad.iloc[ind,0]
                if(vertex3 == -1):
                    numVertex += 1
                    vertex3 = numVertex
                    sort = np.append(sort,[[x3,y3,vertex3]], axis = 0)
            else:
                numVertex += 1
                vertex3 = numVertex
                sort = np.append(sort,[[x3,y3,vertex3]], axis = 0)
            new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            #Second quadrilater
            indexQuad += 1
            new_vertex = {'V':vertex1, 'x':x1, 'y':y1, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':tv1.iloc[1,0], 'x':tv1.iloc[1,1], 'y':tv1.iloc[1,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            x2,y2 = midpoint(tv1.iloc[1,1],tv1.iloc[1,2],tv1.iloc[2,1],tv1.iloc[2,2])
            exist = tableQuad.index[tableQuad['x'] == x2].tolist()
            if len(exist) != 0:
                vertex2 = -1
                for ind in exist:
                    if(tableQuad.iloc[ind,2] == y2):
                        vertex2 = tableQuad.iloc[ind,0]
                if(vertex2 == -1):
                    numVertex += 1
                    vertex2 = numVertex
                    sort = np.append(sort,[[x2,y2,vertex2]], axis = 0)
            else:
                numVertex += 1
                vertex2 = numVertex
                sort = np.append(sort,[[x2,y2,vertex2]], axis = 0)
            new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            #Third quadrilater
            indexQuad += 1
            new_vertex = {'V':vertex2, 'x':x2, 'y':y2, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':tv1.iloc[2,0], 'x':tv1.iloc[2,1], 'y':tv1.iloc[2,2], 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':vertex3, 'x':x3, 'y':y3, 'Q':int(indexQuad)}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':indexQuad}
            tableQuad = tableQuad.append(new_vertex,ignore_index=True)
            
            plotPointsQuadrilate2(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
            plotPointsQuadrilate2without(str(i) + '_' + fileName,sort,tableQuad,tableVertex)
            indexQuad += 1
            
    return tableQuad, sort    
         
# Makes points at random
def randomPoint(nPoint,file,lowLimit,upperLimit):
    n = int(nPoint)
    x = np.random.randint(lowLimit,upperLimit, size=n)
    y = np.random.randint(lowLimit,upperLimit, size=n)
    for a in range(0, n):
        file.write(str(x[a])+ "   " + str(y[a]) + "\n")
    file.close()

def dualGraphGenerator(fileName,tableVertex,sort):
    dualGraph = pd.DataFrame(columns = ['V', 'x', 'y','t'])
    numVertex = tableVertex['V'].max()
    limit = tableVertex['t'].max()
    for i in range(0,limit + 1):
        tv1 = tableVertex[tableVertex['t']== i]
        tv1 = tv1.reset_index(drop = True)
        print(tv1)
        numVertex += 1
        
        centerX = (tv1.iloc[0,1] + tv1.iloc[1,1] + tv1.iloc[2,1])/3
        centerY = (tv1.iloc[0,2] + tv1.iloc[1,2] + tv1.iloc[2,2])/3
        centerNum = numVertex
        
        new_vertex = {'V':centerNum, 'x':centerX, 'y':centerY, 'Q':-1}
        dualGraph = dualGraph.append(new_vertex,ignore_index=True)
        sort = np.append(sort,[[centerX,centerY,centerNum]], axis = 0)
        plotPointsTrianglesPlusGraph(fileName,sort,tableVertex,dualGraph)
    return dualGraph, sort
        
        
        
                        
                        
                

if __name__ == '__main__':
    
    theEnd = False
    while not theEnd:
        
        flag = True
    
        # Verify that the input option is valid
        while flag:
            print("\n1. Create new point cloud")
            print("2. Delaunay Triangulation")
            print("3. Catnull-Clark-based quadrilaterals")
            print("4. First indirect method")
            print("5. Second indirect method plus catnull-clark")
            print("6. Exit")
            
            option = input()
            if(option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6'):
                flag = False
                
        if (option == '1'):
            order = 0
            nPoint = input("Enter the number of points ")
            try:
                if(isinstance(int(nPoint), int) or int(nPoint) < 0):
                    upperLimit = input("Enter Upper Limit ")
                    try:
                        if(isinstance(int(upperLimit), int) or int(nPoint) < 0):
                            lowerLimit = input("Enter Lower Limit ")
                            try:
                                if(isinstance(int(lowerLimit), int) or int(nPoint) < 0):
                                    order = 1
                                else:
                                    print("Invalid number")
                            except Exception:
                                print ("Invalid number")
                        else:
                            print("Invalid number")
                    except Exception:
                        print ("Invalid number")
                else:
                    print("Invalid number")
            except Exception:
                print ("Invalid number")
            
            
            if(order == 1):
                nPoitn = int(nPoint)
                if(int(lowerLimit) > int(upperLimit)):
                    aux = int(lowerLimit)
                    lowerLimit = int(upperLimit)
                    upperLimit = aux
                else:
                    lowerLimit = int(lowerLimit)
                    upperLimit = int(upperLimit)
                
                filePoint = open(path + 'nuvem' + str(nPoint) + '.txt', 'w')
                randomPoint(nPoint, filePoint,lowerLimit,upperLimit)
                
        elif(option == '2'):
            
            # upload all files of folder Files
            try:
                fileList = glob.glob(path + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            
            timeControl = open(path2 + "Delaunay/" + "Time.txt", 'a')
            
            for name in fileList:
                #name = fileList[n]
                fileName = name.split('\\')[1]
                x,y = np.loadtxt(name,dtype=int,unpack=True)
                lista = np.linspace(0, len(x) - 1, len(x))
                puntos = np.array([x,y]).T
                sort = puntos[np.argsort(puntos[:,0])]
                sort = np.hstack((sort,np.atleast_2d(lista).T))
                sort = sort.astype(int)
                tableVertex = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
                tableTriangle = pd.DataFrame(columns = ['t', 'V0', 'V1','V2','t0','t1','t2'])
                plotPoints(fileName,sort)
                #print(sort)
                convexClosure = []
                new_vertex = {'V':0, 'x':sort[0,0], 'y':sort[0,1], 't':0}
                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                ang1, ang2 = findAngle(sort[0,0],sort[0,1],sort[1,0],sort[1,1],sort[2,0],sort[2,1])
                #print(ang1,ang2)
                
                tableVertex = dataforAngles(ang1,ang2,sort[1,2],sort[1,0],sort[1,1],sort[2,2],sort[2,0],sort[2,1],0,tableVertex,sort[0,0])
                convexClosure = tableVertex['V'].values.flatten()
                ElapsedTime = 0
                
                start_time2 = time()
                # Incremental triangulation
                start_time = time()
                for j in range(3,len(sort)):
                    i = 0
                    lastInsert = 0
                    while (i < len(convexClosure)):
                        #print(f'i = {i}, tamano = {len(convexClosure)}')
                        if (i != len(convexClosure) - 1):
                            ax = sort[convexClosure[i],0]
                            ay = sort[convexClosure[i],1]
                            bx = sort[convexClosure[i+1],0]
                            by = sort[convexClosure[i+1],1]
                            cx = sort[j,0]
                            cy = sort[j,1]
                            if pointRight(ax, ay, bx, by, cx, cy):
                                maximo = tableVertex['t'].max()
                                new_vertex = {'V':sort[j,2], 'x':cx, 'y':cy, 't':maximo+1}
                                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                                ang1, ang2 = findAngle(cx, cy, ax, ay, bx, by)
                                #print(ax,ay)
                                #print(ang1,ang2)
                                tableVertex = dataforAngles(ang1,ang2,sort[convexClosure[i],2],ax, ay,sort[convexClosure[i+1],2],bx, by,maximo+1,tableVertex,cx)
                                if(sort[j,2] != lastInsert):
                                    lastInsert = sort[j,2]
                                    convexClosure = np.insert(convexClosure,i + 1,sort[j,2])
                                    i += 1
                                else:
                                    convexClosure = np.delete(convexClosure,i)
                                    i -= 1
                        else:
                            ax = sort[convexClosure[i],0]
                            ay = sort[convexClosure[i],1]
                            bx = sort[convexClosure[0],0]
                            by = sort[convexClosure[0],1]
                            cx = sort[j,0]
                            cy = sort[j,1]
                            if pointRight(ax, ay, bx, by, cx, cy):
                                maximo = tableVertex['t'].max()
                                new_vertex = {'V':sort[j,2], 'x':cx, 'y':cy, 't':maximo+1}
                                tableVertex = tableVertex.append(new_vertex,ignore_index=True)
                                ang1, ang2 = findAngle(cx, cy, ax, ay, bx, by)
                                tableVertex = dataforAngles(ang1,ang2,sort[convexClosure[i],2],ax, ay,sort[convexClosure[0],2],bx, by,maximo+1,tableVertex,cx)
                                if(sort[j,2] != lastInsert):
                                    lastInsert = sort[j,2]
                                    convexClosure = np.insert(convexClosure,i + 1,sort[j,2])
                                    i += 1
                                else:
                                    convexClosure = np.delete(convexClosure,i)
                                    i -= 1
                        i += 1

                tableVertex.to_csv(path2 + 'Delaunay/Vertex/' + 'TableVertexTriangles' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ') 
                ElapsedTime += (time() - start_time)
                
                np.save(path2 + 'Delaunay/ListVertexSorted/' + 'sort' + fileName[5: len(fileName) - 4]  + '.npy',sort)
                np.save(path2 + 'Delaunay/ConvexClosure/' + 'convexClosure' + fileName[5: len(fileName) - 4]  + '.npy',convexClosure)
                
                plotPointsOutline(fileName,sort,convexClosure)
                plotPointsTriangles(fileName,sort,tableVertex)
                
                # Triangle table construction
                start_time = time()
                tableTriangle = triangleTable(tableVertex,tableTriangle)
                tableTriangle.to_csv(path2 + 'Delaunay/Triangles/' + 'TableTriangles' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ') 
                            
                ElapsedTime += (time() - start_time)       
                start_time = time()
        
                change = False
                k = 0
                count = 0
                imagen = 0
                while (k < len(tableTriangle) or not change):
                    for i in range(4,7):
                        t1 = tableTriangle.iloc[k,0]
                        t2 = tableTriangle.iloc[k,i] 
                        #print(f't1 = {t1}, t2 = {t2}')
                        if(t2 != -1):
                            state, equal, differ = convex(t1,t2,sort,tableTriangle) 
                            #print(f'state = {state}')
                            if state:
                                if (needinvertEdge(t1,t2,equal,differ,sort,tableTriangle)):
                                    tableVertex2 = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
                                    new_vertex = {'V':differ[0], 'x':sort[differ[0],0], 'y':sort[differ[0],1], 't':t1}
                                    tableVertex2 = tableVertex2.append(new_vertex,ignore_index=True)
                                    
                                    ang1, ang2 = findAngle(sort[differ[0],0],sort[differ[0],1],sort[differ[1],0],sort[differ[1],1],sort[equal[0],0],sort[equal[0],1])
                                    tableVertex2 = dataforAngles(ang1,ang2,differ[1],sort[differ[1],0],sort[differ[1],1],equal[0],sort[equal[0],0],sort[equal[0],1],t1,
                                                                  tableVertex2,sort[differ[0],0])
                                    passk = tableVertex2.values
                                    tableVertex.loc[tableVertex.t == t1] = passk
                                    
                                    tableVertex2 = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
                                    new_vertex = {'V':differ[1], 'x':sort[differ[1],0], 'y':sort[differ[1],1], 't':t2}
                                    tableVertex2 = tableVertex2.append(new_vertex,ignore_index=True)
                                    
                                    ang1, ang2 = findAngle(sort[differ[1],0],sort[differ[1],1],sort[differ[0],0],sort[differ[0],1],sort[equal[1],0],sort[equal[1],1])
                                    tableVertex2 = dataforAngles(ang1,ang2,differ[0],sort[differ[0],0],sort[differ[0],1],equal[1],sort[equal[1],0],sort[equal[1],1],t2,
                                                                  tableVertex2,sort[differ[1],0])
                                    passk = tableVertex2.values
                                    tableVertex.loc[tableVertex.t == t2] = passk
                                    tableTriangle = pd.DataFrame(columns = ['t', 'V0', 'V1','V2','t0','t1','t2'])
                                    tableTriangle = triangleTable(tableVertex,tableTriangle)
                                    change = True
                                    plotPointsTriangles(str(imagen) + '_' + fileName,sort,tableVertex)
                                    imagen += 1
                    k += 1
                    if(change and k == len(tableTriangle)):
                        k = 0
                        change = False
                    elif(change):
                        change = False
                    elif(not change and k == len(tableTriangle) ):
                        if(count == 2):
                            change = True
                        else:
                            count += 1
                            k = 0
                tableTriangle = pd.DataFrame(columns = ['t', 'V0', 'V1','V2','t0','t1','t2'])
                tableTriangle = triangleTable(tableVertex,tableTriangle)
                df2 = tableTriangle.loc[:,'V0':'V2']
                tableVertex.to_csv(path2 + 'Delaunay/Vertex/' + 'TableVertexTriangles' + fileName[5: len(fileName) - 4]  + "_Final.txt", index=False, sep=' ')
                tableTriangle.to_csv(path2 + 'Delaunay/Triangles/' +'TableTriangles' +  fileName[5: len(fileName) - 4]  + "_Final.txt", index=False, sep=' ') 
                np.savetxt(path2 +'Delaunay/' +  'dalaunay' + fileName[5: len(fileName) - 4] + '.txt', df2.values, fmt='%d')
                
                np.save(path2 + 'Delaunay/ListVertexSorted/' + 'sort' + fileName[5: len(fileName) - 4]  + '_Delaunay.npy',sort)
                np.save(path2 + 'Delaunay/ConvexClosure/' + 'convexClosure' + fileName[5: len(fileName) - 4]  + '_Delaunay.npy',convexClosure)
                
                
                ElapsedTime += (time() - start_time)
                ElapsedTime2 = (time() - start_time2)
                timeControl.write(f'{fileName[: len(fileName) - 4]}   {ElapsedTime2}\n')
            timeControl.close()
            
        elif(option == '3'):
            timeQuadrila = open(path2 + 'Catnull-Clark/' + "QuadTime.txt", 'a')
            try:
                fileList = glob.glob(path2 + 'Delaunay/Vertex/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList2 = glob.glob(path2 + 'Delaunay/Triangles/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList3 = glob.glob(path2 + 'Delaunay/ListVertexSorted/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList4 = glob.glob(path2 + 'Delaunay/ConvexClosure/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
            
            for n in range(0,len(fileList)):
                
                name = fileList3[n]
                fileName = name.split('\\')[1]
                fileName = 'nuvem' + fileName[4:]
                
                tableVertex = pd.read_csv(fileList[n], sep=' ')
                tableTriangle = pd.read_csv(fileList2[n], sep=' ') 
                sort = np.load(fileList3[n])
                convexClosure = np.load(fileList4[n], allow_pickle=True)

                #Catnull-Clark-based quadrilaterals
                quadTime = time()
                tableQuad, sortQ = catnullQuad(tableVertex,sort,fileName,convexClosure)
                tableQuad = tableQuad.astype({'V': int, 'x': float, 'y':float, 'Q':int})
                tableQuad.x = tableQuad.x.round(2)
                tableQuad.y = tableQuad.y.round(2)
                tableQuad.to_csv(path2 + 'Catnull-Clark/' + 'TableVertexQuadrilateral' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
                quadElapseTiem = (time() - quadTime)
                timeQuadrila.write(f'{fileName[: len(fileName) - 4]}:   {quadElapseTiem}\n')
            
            timeQuadrila.close()
            
        elif(option == '4'):  
            timeIndirect1 = open(path2 + 'Indirect1/' + 'Indirect1Time.txt', 'a')
            try:
                fileList = glob.glob(path2 + 'Delaunay/Vertex/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList2 = glob.glob(path2 + 'Delaunay/Triangles/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList3 = glob.glob(path2 + 'Delaunay/ListVertexSorted/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList4 = glob.glob(path2 + 'Delaunay/ConvexClosure/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
                
            for n in range(0,len(fileList)):
                name = fileList3[n]
                fileName = name.split('\\')[1]
                fileName = 'nuvem' + fileName[4:]
                #print(fileName)
                tableVertex = pd.read_csv(fileList[n], sep=' ')
                tableTriangle = pd.read_csv(fileList2[n], sep=' ') 
                sort = np.load(fileList3[n])
                convexClosure = np.load(fileList4[n], allow_pickle=True)
                             
                # First indirect method
                indirect1Time = time()
                TableQuad2, tableEdgesSort = indirectMethod1(tableVertex,tableTriangle,sort,fileName,convexClosure)
                TableQuad2.to_csv(path2 + 'Indirect1/Vertex/' + 'TableVertexIndirect1_' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
                tableEdgesSort.to_csv(path2 + 'Indirect1/Edges/' + 'TableEdgesIndirect1_' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
                indirect1ElapseTiem = (time() - indirect1Time)
                timeIndirect1.write(f'{fileName[: len(fileName) - 4]}:   {indirect1ElapseTiem}\n')
            
            timeIndirect1.close()
            
        elif(option == '5'):
            timeIndirect2 = open(path2 + 'Indirect2/' + 'Indirect2Time.txt', 'a')
            try:
                fileList = glob.glob(path2 + 'Indirect1/Vertex/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList2 = glob.glob(path2 + 'Delaunay/Triangles/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList3 = glob.glob(path2 + 'Delaunay/ListVertexSorted/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList4 = glob.glob(path2 + 'Delaunay/ConvexClosure/' + '*.npy')
            except Exception:
                print("Problem to Read txt Files\n")
            try:
                fileList5 = glob.glob(path2 + 'Indirect1/Edges/' + '*.txt')
            except Exception:
                print("Problem to Read txt Files\n")
            
            for n in range(0,len(fileList)):
                name = fileList3[n]
                fileName = name.split('\\')[1]
                fileName = 'nuvem' + fileName[4:]
                print(fileName)
                tableVertex = pd.read_csv(fileList[n], sep=' ')
                tableTriangle = pd.read_csv(fileList2[n], sep=' ')
                tableEdges = pd.read_csv(fileList5[n], sep=' ')
                sort = np.load(fileList3[n])
                convexClosure = np.load(fileList4[n], allow_pickle=True)
                
                # second indirect method
                indirect1Time = time()
                TableQuad3, sortQ = indirectMethod2(tableVertex,tableTriangle,sort,fileName,convexClosure,tableEdges)
                TableQuad3 = TableQuad3.astype({'V': int, 'x': float, 'y':float, 'Q':int})
                TableQuad3.x = TableQuad3.x.round(2)
                TableQuad3.y = TableQuad3.y.round(2)
                TableQuad3.to_csv(path2 + 'Indirect2/Vertex/' + 'TableVertexIndirect2_' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
                indirect1ElapseTiem = (time() - indirect1Time)
                timeIndirect2.write(f'{fileName[: len(fileName) - 4]}:   {indirect1ElapseTiem}\n')
            
            timeIndirect2.close()
            
        elif(option == '6'):
            theEnd = True
            
            
# =============================================================================
#         elif(option == '6'):
#             Hamiltonian = open(path2 + 'Hamiltonian/' + 'HamiltonianTime.txt', 'a')
#             try:
#                 fileList = glob.glob(path2 + 'Delaunay/Vertex/' + '*.txt')
#             except Exception:
#                 print("Problem to Read txt Files\n")
#             try:
#                 fileList2 = glob.glob(path2 + 'Delaunay/Triangles/' + '*.txt')
#             except Exception:
#                 print("Problem to Read txt Files\n")
#             try:
#                 fileList3 = glob.glob(path2 + 'Delaunay/ListVertexSorted/' + '*.npy')
#             except Exception:
#                 print("Problem to Read txt Files\n")
#             try:
#                 fileList4 = glob.glob(path2 + 'Delaunay/ConvexClosure/' + '*.npy')
#             except Exception:
#                 print("Problem to Read txt Files\n")
#             
#             
# # =============================================================================
# #             for n in range(0,len(fileList)):
# # =============================================================================
#             for n in range(1,2):
#                 name = fileList3[n]
#                 fileName = name.split('\\')[1]
#                 fileName = 'nuvem' + fileName[4:]
#                 print(fileName)
#                 tableVertex = pd.read_csv(fileList[n], sep=' ')
#                 tableTriangle = pd.read_csv(fileList2[n], sep=' ')
#                 sort = np.load(fileList3[n])
#                 convexClosure = np.load(fileList4[n], allow_pickle=True)
#                 
#                 # second indirect method
#                 indirect1Time = time()
#                 dualGraph, sortG = dualGraphGenerator(fileName,tableVertex,sort)
# # =============================================================================
# #                 TableQuad3, sortQ = indirectMethod2(tableVertex,tableTriangle,sort,fileName,convexClosure)
# #                 TableQuad3 = TableQuad3.astype({'V': int, 'x': float, 'y':float, 'Q':int})
# #                 TableQuad3.x = TableQuad3.x.round(2)
# #                 TableQuad3.y = TableQuad3.y.round(2)
# #                 TableQuad3.to_csv(path2 + 'Indirect2/Vertex/' + 'TableVertexIndirect2_' + fileName[5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
# # =============================================================================
#                 indirect1ElapseTiem = (time() - indirect1Time)
#                 Hamiltonian.write(f'{fileName[: len(fileName) - 4]}:   {indirect1ElapseTiem}\n')
#             
#             Hamiltonian.close()
# =============================================================================
                
# =============================================================================
#     # upload all files of folder Files
#     try:
#         fileList = glob.glob(path + '*.txt')
#     except Exception:
#         print("Problem to Read txt Files\n")
#       
#     timeControl = open(path2 + "Time.txt", 'a')
#     timeQuadrila = open(path2 + "QuadTime.txt", 'a')
#     timeIndirect1 = open(path2 + "Indirect1Time.txt", 'a')
#     
# # =============================================================================
# #     for name in fileList:
# # =============================================================================
#     for n in range(1,2):
#         name = fileList[n]
#         fileName = name.split('\\')[1]
#         x,y = np.loadtxt(name,dtype=int,unpack=True)
#         lista = np.linspace(0, len(x) - 1, len(x))
#         puntos = np.array([x,y]).T
#         sort = puntos[np.argsort(puntos[:,0])]
#         sort = np.hstack((sort,np.atleast_2d(lista).T))
#         sort = sort.astype(int)
#         tableVertex = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
#         tableTriangle = pd.DataFrame(columns = ['t', 'V0', 'V1','V2','t0','t1','t2'])
#         plotPoints(fileName,sort)
#         #print(sort)
#         convexClosure = []
#         new_vertex = {'V':0, 'x':sort[0,0], 'y':sort[0,1], 't':0}
#         tableVertex = tableVertex.append(new_vertex,ignore_index=True)
#         ang1, ang2 = findAngle(sort[0,0],sort[0,1],sort[1,0],sort[1,1],sort[2,0],sort[2,1])
#         #print(ang1,ang2)
#         
#         tableVertex = dataforAngles(ang1,ang2,sort[1,2],sort[1,0],sort[1,1],sort[2,2],sort[2,0],sort[2,1],0,tableVertex,sort[0,0])
#         convexClosure = tableVertex['V'].values.flatten()
#         ElapsedTime = 0
#         
#         start_time2 = time()
#         # Incremental triangulation
#         start_time = time()
#         for j in range(3,len(sort)):
#             i = 0
#             lastInsert = 0
#             while (i < len(convexClosure)):
#                 #print(f'i = {i}, tamano = {len(convexClosure)}')
#                 if (i != len(convexClosure) - 1):
#                     ax = sort[convexClosure[i],0]
#                     ay = sort[convexClosure[i],1]
#                     bx = sort[convexClosure[i+1],0]
#                     by = sort[convexClosure[i+1],1]
#                     cx = sort[j,0]
#                     cy = sort[j,1]
#                     if pointRight(ax, ay, bx, by, cx, cy):
#                         maximo = tableVertex['t'].max()
#                         new_vertex = {'V':sort[j,2], 'x':cx, 'y':cy, 't':maximo+1}
#                         tableVertex = tableVertex.append(new_vertex,ignore_index=True)
#                         ang1, ang2 = findAngle(cx, cy, ax, ay, bx, by)
#                         #print(ax,ay)
#                         #print(ang1,ang2)
#                         tableVertex = dataforAngles(ang1,ang2,sort[convexClosure[i],2],ax, ay,sort[convexClosure[i+1],2],bx, by,maximo+1,tableVertex,cx)
#                         if(sort[j,2] != lastInsert):
#                             lastInsert = sort[j,2]
#                             convexClosure = np.insert(convexClosure,i + 1,sort[j,2])
#                             i += 1
#                         else:
#                             convexClosure = np.delete(convexClosure,i)
#                             i -= 1
#                 else:
#                     ax = sort[convexClosure[i],0]
#                     ay = sort[convexClosure[i],1]
#                     bx = sort[convexClosure[0],0]
#                     by = sort[convexClosure[0],1]
#                     cx = sort[j,0]
#                     cy = sort[j,1]
#                     if pointRight(ax, ay, bx, by, cx, cy):
#                         maximo = tableVertex['t'].max()
#                         new_vertex = {'V':sort[j,2], 'x':cx, 'y':cy, 't':maximo+1}
#                         tableVertex = tableVertex.append(new_vertex,ignore_index=True)
#                         ang1, ang2 = findAngle(cx, cy, ax, ay, bx, by)
#                         tableVertex = dataforAngles(ang1,ang2,sort[convexClosure[i],2],ax, ay,sort[convexClosure[0],2],bx, by,maximo+1,tableVertex,cx)
#                         if(sort[j,2] != lastInsert):
#                             lastInsert = sort[j,2]
#                             convexClosure = np.insert(convexClosure,i + 1,sort[j,2])
#                             i += 1
#                         else:
#                             convexClosure = np.delete(convexClosure,i)
#                             i -= 1
#                 i += 1
#                 #print(convexClosure)
#         
# # =============================================================================
# #         print(tableVertex)
# #         print(convexClosure)
# # =============================================================================
#         tableVertex.to_csv(path2 + 'TableVertexTriangles' + fileName[len(fileName) - 5: len(fileName) - 4]  + ".txt", index=False, sep=' ') 
#         ElapsedTime += (time() - start_time)
#         
#         plotPointsOutline(fileName,sort,convexClosure)
#         plotPointsTriangles(fileName,sort,tableVertex)
#         
#         # Triangle table construction
#         start_time = time()
#         tableTriangle = triangleTable(tableVertex,tableTriangle)
#         tableTriangle.to_csv(path2 + 'TableTriangles' + fileName[len(fileName) - 5: len(fileName) - 4]  + ".txt", index=False, sep=' ') 
# 
# # =============================================================================
# #         #Catnull-Clark-based quadrilaterals
# #         quadTime = time()
# #         tableQuad, sortQ = catnullQuad(tableVertex,sort,fileName,convexClosure)
# #         tableQuad = tableQuad.astype({'V': int, 'x': float, 'y':float, 'Q':int})
# #         tableQuad.x = tableQuad.x.round(2)
# #         tableQuad.y = tableQuad.y.round(2)
# #         tableQuad.to_csv(path2 + 'TableVertexQuadrilateral' + fileName[len(fileName) - 5: len(fileName) - 4]  + ".txt", index=False, sep=' ')
# #         quadElapseTiem = (time() - quadTime)
# #         timeQuadrila.write(f'{fileName[: len(fileName) - 4]}:   {quadElapseTiem}\n')
# # =============================================================================
#         
# # =============================================================================
# #         indirect1Time = time()
# #         TableQuad2 = indirectMethod1(tableVertex,tableTriangle,sort,fileName,convexClosure)
# #         indirect1ElapseTiem = (time() - indirect1Time)
# #         timeIndirect1.write(f'{fileName[: len(fileName) - 4]}:   {indirect1ElapseTiem}\n')
# # =============================================================================
#         
# # =============================================================================
# #         tableQuad2, tableVertexQ2 = indirectMethod1(tableVertex,tableTriangle,sort)
# # =============================================================================
# 
# 
# # =============================================================================
# #         print(tableTriangle)
# #         print(type(tableTriangle))
# #         print(type(tableVertex))
# # =============================================================================
#                     
#         ElapsedTime += (time() - start_time)
#         #print(tableTriangle)
#         
#         start_time = time()
# 
#         change = False
#         k = 0
#         count = 0
#         while (k < len(tableTriangle) or not change):
#             for i in range(4,7):
#                 t1 = tableTriangle.iloc[k,0]
#                 t2 = tableTriangle.iloc[k,i] 
#                 #print(f't1 = {t1}, t2 = {t2}')
#                 if(t2 != -1):
#                     state, equal, differ = convex(t1,t2,sort,tableTriangle) 
#                     #print(f'state = {state}')
#                     if state:
#                         if (needinvertEdge(t1,t2,equal,differ,sort,tableTriangle)):
#                             tableVertex2 = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
#                             new_vertex = {'V':differ[0], 'x':sort[differ[0],0], 'y':sort[differ[0],1], 't':t1}
#                             tableVertex2 = tableVertex2.append(new_vertex,ignore_index=True)
#                             
#                             ang1, ang2 = findAngle(sort[differ[0],0],sort[differ[0],1],sort[differ[1],0],sort[differ[1],1],sort[equal[0],0],sort[equal[0],1])
#                             tableVertex2 = dataforAngles(ang1,ang2,differ[1],sort[differ[1],0],sort[differ[1],1],equal[0],sort[equal[0],0],sort[equal[0],1],t1,
#                                                           tableVertex2,sort[differ[0],0])
#                             passk = tableVertex2.values
#                             tableVertex.loc[tableVertex.t == t1] = passk
#                             
#                             tableVertex2 = pd.DataFrame(columns = ['V', 'x', 'y','t']) 
#                             new_vertex = {'V':differ[1], 'x':sort[differ[1],0], 'y':sort[differ[1],1], 't':t2}
#                             tableVertex2 = tableVertex2.append(new_vertex,ignore_index=True)
#                             
#                             ang1, ang2 = findAngle(sort[differ[1],0],sort[differ[1],1],sort[differ[0],0],sort[differ[0],1],sort[equal[1],0],sort[equal[1],1])
#                             tableVertex2 = dataforAngles(ang1,ang2,differ[0],sort[differ[0],0],sort[differ[0],1],equal[1],sort[equal[1],0],sort[equal[1],1],t2,
#                                                           tableVertex2,sort[differ[1],0])
#                             passk = tableVertex2.values
#                             tableVertex.loc[tableVertex.t == t2] = passk
#                             tableTriangle = pd.DataFrame(columns = ['t', 'V0', 'V1','V2','t0','t1','t2'])
#                             tableTriangle = triangleTable(tableVertex,tableTriangle)
#                             change = True
#                             plotPointsTriangles(str(k) + '_' + fileName,sort,tableVertex)
#                             print('\ntableVertex')
#                             print(tableVertex)
#                             print('ok')
#             k += 1
#             if(change and k == len(tableTriangle)):
#                 k = 0
#                 change = False
#             elif(change):
#                 change = False
#             elif(not change and k == len(tableTriangle) ):
#                 if(count == 2):
#                     change = True
#                 else:
#                     count += 1
#                     k = 0
#                     
#         df2 = tableTriangle.loc[:,'V0':'V2']
#         tableVertex.to_csv(path2 + 'TableVertexTriangles' + fileName[len(fileName) - 5: len(fileName) - 4]  + "_Final.txt", index=False, sep=' ')
#         tableTriangle.to_csv(path2 + 'TableTriangles' +  fileName[len(fileName) - 5: len(fileName) - 4]  + "_Final.txt", index=False, sep=' ') 
#         np.savetxt(path2 + 'dalaunay' + fileName[len(fileName) - 5: len(fileName) - 4] + '.txt', df2.values, fmt='%d')
#         #print(df2)
#         
# # =============================================================================
# #         quadTime = time()
# #         tableQuad, sortQ = catnullQuad(tableVertex,sort,fileName,convexClosure)
# #         tableQuad = tableQuad.astype({'V': int, 'x': float, 'y':float, 'Q':int})
# #         tableQuad.x = tableQuad.x.round(2)
# #         tableQuad.y = tableQuad.y.round(2)
# #         tableQuad.to_csv(path2 + 'TableVertexQuadrilateral' + fileName[len(fileName) - 5: len(fileName) - 4]  + "_Delaynay.txt", index=False, sep=' ')
# #         quadElapseTiem = (time() - quadTime)
# #         timeQuadrila.write(f'{fileName[: len(fileName) - 4]} Delaunay:   {quadElapseTiem}\n')
# # =============================================================================
#         
#         indirect1Time = time()
#         TableQuad2 = indirectMethod1(tableVertex,tableTriangle,sort,fileName,convexClosure)
#         indirect1ElapseTiem = (time() - indirect1Time)
#         timeIndirect1.write(f'{fileName[: len(fileName) - 4]} Delaunay:   {indirect1ElapseTiem}\n')
# 
#         
#         ElapsedTime += (time() - start_time)
#         ElapsedTime2 = (time() - start_time2)
#         timeControl.write(f'{fileName[: len(fileName) - 4]}   {ElapsedTime2}\n')
#     timeControl.close()
#     timeQuadrila.close()
#     timeIndirect1.close()
# =============================================================================
        

