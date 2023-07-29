from collections import defaultdict
import heapq
def dijkstra(source, adjlist, node_count):
    # Initialize the distance of all the nodes from the source node to infinity
    distance = [float('inf')] * node_count
    # Distance of source node to itself is 0
    distance[source] = 0

    # Use a priority queue (heap) to efficiently get the node with the shortest distance from the source
    priority_queue = [(0, source)]

    while priority_queue:
        # Get the node with the smallest distance from the source
        dist, current_source_node = heapq.heappop(priority_queue)

        # Skip if the node has already been visited
        if dist > distance[current_source_node]:
            continue

        for adjnode in adjlist[current_source_node]:
            # Edge relaxation
            if distance[adjnode] > distance[current_source_node] + 1:
                distance[adjnode] = distance[current_source_node] + 1
                heapq.heappush(priority_queue, (distance[adjnode], adjnode))

    return distance