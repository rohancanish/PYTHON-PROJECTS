def greedy_best_first_search(start, goal):
    """
    Perform a greedy best-first search from the start node to the goal node.
    """
    current_node = start
    visited = set()  # Set to keep track of visited nodes

    while current_node not in visited:
        # Print the current node
        print(current_node, end=' -> ')

        # Mark the current node as visited
        visited.add(current_node)

        # Check if the current node is the goal
        if current_node == goal:
            print("Goal found!")
            return

        # Prepare to find the next node to explore
        next_node = None
        min_heuristic = float('inf')  # Initialize to a very large value

        # Check the neighbors of the current node
        for neighbor in graph[current_node]:
            # If this neighbor has a smaller heuristic value, update the next node
            if heuristic[neighbor] < min_heuristic:
                min_heuristic = heuristic[neighbor]
                next_node = neighbor

        # Move to the next node with the smallest heuristic value
        if next_node:
            current_node = next_node
        else:
            # No valid neighbor found, goal is not reachable
            print("Goal not found.")
            return

    # Final check to print if goal was not found
    if current_node != goal:
        print("Goal not found.")

# Get user input for the starting node
start_node = input("Enter the starting node: ").strip()
goal_node = 'G'  # Define the goal node

# Define the graph and heuristic values
graph = {
    'S': ['A', 'B'],
    'A': [],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E', 'G'],
    'E': ['G'],
    'G': []
}

heuristic = {
    'S': 21,
    'A': 20,
    'B': 22,
    'C': 18,
    'D': 30,
    'E': 31,
    'G': 0
}



# Perform the search
greedy_best_first_search(start_node, goal_node)
