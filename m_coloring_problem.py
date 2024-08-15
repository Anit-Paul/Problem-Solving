def is_safe(graph,idx,color,c):
    for j in range(len(graph)):
        if(graph[idx][j]==1):
            if color[j]==c:
                return False
    return True
def compute_result(graph,k,v,idx,color):
    if idx==v:
        return True
    for i in range(k):
        if is_safe(graph,idx,color,i):
            color[idx]=i
            if(compute_result(graph,k,v,idx+1,color)):
                return True
            color[idx]=-1
    return False
        
def graphColoring(graph, k, v):
    color=[-1 for _ in range(v)]
    return compute_result(graph,k,v,0,color)
