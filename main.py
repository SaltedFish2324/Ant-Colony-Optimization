import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import Graph
from ant import AntColonyOptimization
import time

def animate_ant_movement(graph, best_path):
    G = graph.create_graph()

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    for i in range(graph.num_nodes - 1):
        ax.cla()
        nx.draw(G, graph.pos, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, graph.pos, edge_labels=labels)

        x = [graph.coordinates[best_path[i]][0], graph.coordinates[best_path[i + 1]][0]]
        y = [graph.coordinates[best_path[i]][1], graph.coordinates[best_path[i + 1]][1]]
        ax.plot(x, y, 'r-', linewidth=2)
        plt.draw()
        canvas.draw()
        time.sleep(0.5)
        #This is a test for github pull and push request
    plt.show()

def start_application():
    num_points = int(num_points_entry.get())
    if num_points < 2:
        messagebox.showerror("Error", "Number of points should be at least 2.")
        return

    clicked_points = []

    def on_click(event):
        nonlocal num_points, clicked_points
        if num_points > 0:
            x, y = event.xdata, event.ydata
            clicked_points.append([x, y])
            ax.plot(x, y, 'ro')
            plt.draw()
            num_points -= 1

            if num_points == 0:
                plt.close()

    fig, ax = plt.subplots()
    ax.set_title(f"Click {num_points} point(s) on the graph.")
    cid = fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

    if num_points == 0:
        graph = Graph(num_nodes=len(clicked_points))
        graph.calculate_distances(clicked_points)
        graph.visualize_graph(clicked_points)

        aco = AntColonyOptimization(num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, rho=0.5, q=100.0)
        aco.num_nodes = graph.num_nodes
        aco.distances = graph.distances

        best_path, best_length = aco.ant_colony_optimization()
        best_path_str = ' -> '.join(str(node) for node in best_path)
        messagebox.showinfo("Best Path", f"Best Path: {best_path_str}\nBest Length: {best_length}")
        animate_ant_movement(graph, best_path)
        root.destroy()

root = tk.Tk()
root.title("Ant Colony Optimization")
root.geometry("300x150")

num_points_label = tk.Label(root, text="Number of Points:")
num_points_label.pack()

num_points_entry = tk.Entry(root)
num_points_entry.pack()

start_button = tk.Button(root, text="Start", command=start_application)
start_button.pack()

root.mainloop()
