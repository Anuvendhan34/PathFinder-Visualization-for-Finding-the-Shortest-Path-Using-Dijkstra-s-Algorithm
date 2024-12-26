# Dijkstra's Algorithm Random Graph Visualizer

This project is a Python application that visualizes the shortest path in a randomly generated graph using Dijkstra's Algorithm. The application is built using `Tkinter` for the user interface, `networkx` for graph management, and `matplotlib` for visualization.

## Features
- Generate random weighted graphs with a specified number of nodes and maximum edge weights.
- Visualize the generated graph and the shortest path calculated using Dijkstra's Algorithm.
- Interactive GUI built with `Tkinter` for user input.

## Prerequisites
Make sure you have the following dependencies installed:

- Python 3.6+
- `matplotlib`
- `networkx`
- `numpy`

You can install the required packages using pip:
```bash
pip install matplotlib networkx numpy
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dijkstra-visualizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dijkstra-visualizer
   ```
3. Run the script:
   ```bash
   python dijkstra_visualizer.py
   ```

## Usage
1. Enter the number of nodes you want in the graph.
2. Specify the maximum weight for edges.
3. Click the "Generate Graph and Find Shortest Path" button.
4. The program will generate a random graph, calculate the shortest path from a random starting node, and display:
   - The shortest distances in a pop-up message box.
   - A visualization of the graph with the shortest path highlighted in red.

## Files
- `dijkstra_visualizer.py`: Main script for the application.

## Example
### Input:
- Number of Nodes: 5
- Max Weight for Edges: 10

### Output:
1. Pop-up showing shortest distances:
   ```
   Shortest distances from node 0:
   0 -> 0: 0
   0 -> 1: 4
   0 -> 2: 2
   0 -> 3: 5
   0 -> 4: 7
   ```
2. Graph visualization with the shortest path highlighted.

## Screenshots
### Application GUI:
(Add a screenshot of the Tkinter application here)

### Graph Visualization:
(Add a screenshot of the graph visualization here)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The `networkx` and `matplotlib` libraries for graph management and visualization.
- Inspiration from Dijkstra's Algorithm for shortest path finding.

