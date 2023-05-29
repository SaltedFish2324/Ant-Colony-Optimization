import numpy as np

class Ant:
    def __init__(self, num_nodes):
        self.path = [np.random.randint(num_nodes)]
        self.path_length = 0.0

class AntColonyOptimization:
    def __init__(self, num_ants, num_iterations, alpha, beta, rho, q):
        self.num_nodes = 0
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        self.pheromone = None
        self.distances = None

    def update_pheromone(self, ants):
        self.pheromone *= self.rho
        for ant in ants:
            delta_pheromone = self.q / ant.path_length
            for i in range(self.num_nodes - 1):
                start, end = ant.path[i], ant.path[i + 1]
                self.pheromone[start][end] += delta_pheromone
                self.pheromone[end][start] += delta_pheromone

    def ant_colony_optimization(self):
        best_path = None
        best_length = float('inf')
        for _ in range(self.num_iterations):
            ants = self.generate_ants()
            self.move_ants(ants)
            self.update_pheromone(ants)
            for ant in ants:
                if ant.path_length < best_length:
                    best_length = ant.path_length
                    best_path = ant.path
        return best_path, best_length

    def generate_ants(self):
        ants = []
        for _ in range(self.num_ants):
            ant = Ant(self.num_nodes)
            ants.append(ant)
        return ants

    def move_ants(self, ants):
        for ant in ants:
            start = ant.path[-1]
            visited = set(ant.path)
            pheromone = self.pheromone[start] ** self.alpha
            attractiveness = ((1.0 / self.distances[start]) ** self.beta) * pheromone
            unvisited_nodes = [node for node in range(self.num_nodes) if node not in visited]
            probabilities = attractiveness[unvisited_nodes] / np.sum(attractiveness[unvisited_nodes])
            selected_node = np.random.choice(unvisited_nodes, p=probabilities)
            ant.path.append(selected_node)
            ant.path_length += self.distances[start][selected_node]
