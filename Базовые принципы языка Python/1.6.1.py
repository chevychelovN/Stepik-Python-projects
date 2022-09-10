""" 
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Вам необходимо отвечать на запросы, является ли один класс предком другого класса
"""
def find_path(graph, end, start, path = []):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, end, node, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

size = int(input())
graph = {}

for i in range(size):
    a, *b = input().replace(":", " ").split()
    if a not in graph:
        graph[a] = b
    else:
        for elem in b:
            if elem not in graph[a]:
                graph[a] += elem
                

classes = int(input())

for i in range(classes):
    first, last = input().split()
    if find_path(graph, first, last):
        print("Yes")
    else:
        print("No")
