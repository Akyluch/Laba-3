import numpy as np

def get_solution_distance(solution, distance_matrix):
    distance = 0
    for i in range(len(solution)):
        j = (i + 1) % len(solution)
        distance += distance_matrix[solution[i], solution[j]]
    return distance

def get_two_opt_move(solution, i, j):
    move = []
    move.extend(solution[:i])
    move.extend(reversed(solution[i:j+1]))
    move.extend(solution[j+1:])
    return move

def improve_solution(solution, distance_matrix):
    n = len(solution)
    best_distance = get_solution_distance(solution, distance_matrix)
    for i in range(n):
        for j in range(i+1, n):
            move = get_two_opt_move(solution, i, j)
            distance = get_solution_distance(move, distance_matrix)
            if distance < best_distance:
                return True, move
    return False, solution

def solve_tsp(distance_matrix, max_iterations=10000):
    n = len(distance_matrix)

    # Generate initial solution
    solution = list(range(n))
    np.random.shuffle(solution)
    best_solution = solution.copy()

    # Compute initial distance
    best_distance = get_solution_distance(solution, distance_matrix)

    # Perform iterative improvement
    i = 0
    while i < max_iterations:
        improved, solution = improve_solution(solution, distance_matrix)
        if improved:
            distance = get_solution_distance(solution, distance_matrix)
            if distance < best_distance:
                best_solution = solution.copy()
                best_distance = distance
                i = 0
        else:
            i += 1

    return best_solution, best_distance

def main():
    # Read distance matrix from file
    distance_matrix = np.loadtxt('graph_1.txt')

    # Solve TSP using iterative improvement
    best_solution, best_distance = solve_tsp(distance_matrix)

    # Print results
    print("Best solution:", best_solution)
    print("Best distance:", best_distance)

if __name__ == '__main__':
    main()
