# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def test_case_one():
    #returns simplest little diamond graph as list of edges
    return [[1,2],[1,3],[2,4],[3,4]]
    
def test_case_two():
    #returns three triangular cycles connected by one edge each
    return [[1,2],[2,3],[2,4],[3,1],[4,7],[4,5],[5,6],[6,4],[7,8],[8,9],[9,7]]
 
#%%   
def txt_2_edge_list(filename):
    max_element=0
    edge_list=[]
    f=open(filename,'r')
    while(True):
        a=f.readline()
        if a=='':
            break
        a=a.split()
        a=[int(i) for i in a]
        edge_list.append(a)
        if a[0]>max_element or a[1]>max_element:
            max_element=max(a)
    print("successfully read input file")
    return edge_list,max_element
    
#%%    
current_layer=0

def set_current_layer(graph):
    global current_layer
    current_layer=len(graph.keys())
    
def topSort(graph,reverseQ):
    print("graph successfully received by topSort")
    #computes a topological sorting of an acyclic directed graph
    #inputs: graph is a dictionary- key=nodeID, value=node object (see node class)
    #inputs: reverseQ- a boolean option for whether to traverse the graph in reverse

    set_current_layer(graph)
    if not reverseQ:
        SCC=[0,0,0,0,0]
        num_remain=current_layer
    
    def DFS(graph, node, reverseQ=False):
    #depth first search on graph starting from node (see above for how graph is represented)
    #if reverseQ then we're going "backwards" in depth first search
        global current_layer
        node.explored=True
        
        if reverseQ:
            for neighbor in node.incoming_neighborhood:
                if not neighbor.explored:
                    DFS(graph,neighbor,reverseQ)
        else:
            for neighbor in node.outgoing_neighborhood:
                if not neighbor.explored:
                    DFS(graph,neighbor,reverseQ)
        node.layer=current_layer
        current_layer-=1
            
    for nodeID in graph.keys():
        node=graph[nodeID]
        if not node.explored:
            DFS(graph, node,reverseQ)
            if not reverseQ:
                if num_remain-current_layer>min(SCC):
                    SCC[SCC.index(min(SCC))]=num_remain-current_layer
                num_remain-=num_remain-current_layer
    print("topSort successfully completed: reverseQ==%s"%str(reverseQ))
    if not reverseQ:
        return SCC
#%%            
class node(object):
    
    def __init__(self,ID,outgoing_neighborhood,incoming_neighborhood,layer=0,explored=False):
        self.ID=ID
        self.outgoing_neighborhood=outgoing_neighborhood
        self.incoming_neighborhood=incoming_neighborhood
        self.layer=layer
        self.explored=explored
        
    def __repr__(self):
        return("a node with ID: %s, at layer %d"%(str(self.ID),self.layer))
        
        
#%%
def init_graph(edge_list,max_element):
    graph={i:node(i,[],[]) for i in range(1,max_element+1)}
    for edge in edge_list:
        graph[edge[0]].outgoing_neighborhood.append(graph[edge[1]])
        graph[edge[1]].incoming_neighborhood.append(graph[edge[0]])
    print("graph successfully instantiated")
    return graph
    
#%%
def relabel(graph):
    print("graph successfully received for relabeling")
    graph2={}
    for key in graph.keys():
        graph2[graph[key].layer]=graph[key]
        graph[key].explored=False
    print("relabeled graph successfully constructed")
    return graph2

#%%
def compute_SCC(filename):
    edge_list,max_element=txt_2_edge_list(filename)
    graph=init_graph(edge_list,max_element)
    topSort(graph,reverseQ=True)
    graph=relabel(graph)
    return topSort(graph,False)