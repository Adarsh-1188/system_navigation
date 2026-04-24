#  Smart Navigation System (BFS & DFS)

##  Overview

This project is a simple **Smart Navigation System** that finds a path between nodes in a graph using:

*  Breadth-First Search (BFS)
*  Depth-First Search (DFS)

It includes:

* A **Python implementation** (`sys.py`)
* An **interactive web interface** (`index.html`)

---

##  Problem Statement

Given a graph, the goal is to determine a valid path between a **start node** and a **goal node** using BFS and DFS algorithms.

---

##  Algorithms Used

###  Breadth-First Search (BFS)

* Explores nodes level by level
* Guarantees the **shortest path** in an unweighted graph

###  Depth-First Search (DFS)

* Explores nodes deeply before backtracking
* Does **not guarantee shortest path**

---

##  Project Structure

```bash
 smart-navigation-system
│── sys.py          # Python implementation of BFS & DFS
│── index.html      # Interactive web interface
│── README.md       # Project documentation
```

---

##  How to Run (Python Version)

1. Open terminal in project folder
2. Run the script:

```bash
python sys.py
```

3. Enter inputs:

```text
Enter start node: A
Enter goal node: E
```

---

##  How to Run (Website)

1. Open `index.html` in any browser
   **OR**

2. Use Live Server in VS Code for better experience

3. Enter start and goal nodes in the UI

---

##  Sample Output

### Python Output

```text
BFS Path: ['A', 'B', 'D', 'E']
DFS Path: ['A', 'C', 'D', 'E']
```

### Website Output

```text
BFS Path: A → B → D → E
DFS Path: A → C → D → E
```

---

##  Features

* User input for start and goal nodes
* Handles invalid inputs
* BFS and DFS path comparison
* Interactive web interface
* Clean and simple implementation

---

##  Requirements

* Python 3.x
* Web browser (for HTML interface)

---

##  Future Improvements

* User-defined graph input
* Graph visualization (nodes & edges)
* Weighted graph support (Dijkstra’s Algorithm)
* Deployment using GitHub Pages

---

##  Author

**Adarsh G**
**Registration Number:** RA2411026050016

---

##  License

This project is open-source and available under the MIT License.
