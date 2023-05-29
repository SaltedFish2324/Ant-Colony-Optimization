# ACO - Ant Colony Optimization

ACO is a metaheuristic algorithm that finds optimal solutions to numerous optimization problems by simulating the foraging behavior of ants. It has been successfully applied to solving problems such as the traveling salesman problem, vehicle routing problem, and maximum cut problem.

## How ACO Works

In ACO, a set of artificial ants are placed on a graph representing the problem domain. Each ant starts at a random node and iteratively moves to adjacent nodes. The probability of an ant migrating to a specific node is determined by the pheromone trail left behind by other ants. The strength of the pheromone trace is influenced by the recency of ant visits to a particular node.

The formula for calculating the probability of ant k moving from node i to node j is as follows:

$$
P_{ij}^k = \frac{{\tau_{ij}^\alpha \cdot \eta_{ij}^\beta}}{{\sum_{l \in N_i} (\tau_{il}^\alpha \cdot \eta_{il}^\beta)}}
$$


Where:
- P_{ij}^k is the probability of ant k moving from node i to node j.
- \tau_{ij} represents the pheromone trail intensity between nodes i and j.
- \eta_{ij} represents the desirability factor between nodes i and j.
- \alpha and \beta are the parameters controlling the influence of the pheromone trail and desirability factor, respectively.
- N_i represents the set of neighboring nodes of node i.

As the ants explore the graph, they construct potential solutions to the problem. The best solution discovered by any ant is communicated to the rest of the colony. This process continues until a termination criterion is met, such as reaching a maximum number of iterations or achieving a minimum solution improvement.

## Key Features of ACO

- Effective for a broad range of optimization problems
- Relatively easy to implement and parallelize
- Robust and insensitive to initial conditions

## Applications of ACO

ACO has been successfully applied in various industries for different purposes:

- Telecommunications: Designing optimal networks for call routing.
- Manufacturing: Scheduling production lines for efficient operations.
- Logistics: Planning optimal delivery routes to minimize time and cost.
- Finance: Managing risk in financial operations.

ACO is a powerful tool that can be employed to solve a wide range of optimization issues. Its ease of implementation, parallelizability, and robustness make it an attractive choice for solving complex problems.


## Usage
Run the application by using the following command or [Ctrl + Shift + F10]
```
python main.py || python3 main.py
```

## Dependency Needed 
- Matplotlib
- tkinter
