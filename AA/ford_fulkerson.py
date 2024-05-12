def ford_fulkerson(allpaths):
    maximum_flow = 0
    for paths in allpaths:
        bolltle_neck = float('inf')

        for i in range(len(paths)-1):
            edge =  graph[paths[i]][paths[i+1]]       
            if edge < bolltle_neck:
                bolltle_neck = edge

        if bolltle_neck == 0:
            print(f'Path: {paths} not possible')
            continue
        
        for i in range(len(paths)-1):
            graph[paths[i]][paths[i+1]] -= bolltle_neck
        maximum_flow += bolltle_neck
    return maximum_flow

def find_possiblepath(graph, source, target, path=[]):
    path = path + [source]
    if source == target:
        return [path]
    if source not in graph:
        return []
    paths = []
    for neighbours in graph[source]:
        if neighbours not in path:
            new_paths = find_possiblepath(graph, neighbours, target, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

graph = {
    '1':{'2':8, '3':10},
    '2':{'4':2, '5':7},
    '3':{'2':3, '5':12},
    '4':{'6':10},
    '5':{'4':4, '6':8}
}

source = '1'
target = '6'
possible_paths = find_possiblepath(graph, source, target)
print(f'Possible Paths: {possible_paths}')
max_flow = ford_fulkerson(possible_paths)
print(f'Maximum Flow: {max_flow}')
