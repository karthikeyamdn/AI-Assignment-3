# 🚀 AI Search Algorithms Assignment

## 📌 Overview

This project implements:

1. Dijkstra’s Algorithm for Indian cities (road distances)
2. UGV navigation with static obstacles using A*
3. UGV navigation with dynamic obstacles using replanning (D*)

---

## 📂 Files Description

### 1. dijkstra.py

* Implements Dijkstra’s algorithm
* Uses Indian cities dataset
* Finds shortest path between cities

### 2. indiancities_throughroads.csv

* Contains cities and road distances
* Used as input for graph

### 3. ugv_static.py

* Simulates a 70x70 grid
* Uses A* algorithm
* Obstacles are known beforehand

### 4. ugv_dynamic.py

* Simulates dynamic obstacles
* Uses replanning strategy (D* concept)
* Path updates during execution

---

## ⚙️ Algorithms Used

### Dijkstra’s Algorithm

* Finds shortest path in weighted graph
* Time Complexity: O(E log V)

### A* Algorithm

* Uses heuristic:
  f(n) = g(n) + h(n)

### Dynamic Replanning (D*)

* Updates path when obstacles change

---

## 📊 Measures of Effectiveness

* Path length
* Execution time
* Nodes explored
* Success rate

---

## ▶️ How to Run

### Run Dijkstra

```bash
python dijkstra.py
```

### Run Static UGV

```bash
python ugv_static.py
```

### Run Dynamic UGV

```bash
python ugv_dynamic.py
```

---

## 📌 Requirements

* Python 3.x
* Libraries:

  * numpy
  * matplotlib (optional for visualization)

---

## 🎯 Conclusion

This project demonstrates how classical search algorithms like Dijkstra and A* are applied in real-world path planning problems including robotics and navigation.

---
