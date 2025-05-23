## Background
This project was inspired by the paper "A Theoretical Framework for Distribution-Aware Dataset Search" (https://arxiv.org/pdf/2503.21235), which uses a Range Tree as part of framework. That led me to explore and implement a basic version of the range tree as a small learning project.

One of the key references I looked at is "Orthogonal Range Tree Visualization" (https://github.com/ZhouJoseph/Orthogonal-range-tree-visualization) project, which features a fully interactive GUI built with JavaScript, HTML, and CSS.

In contrast, this project is implemented purely in Python and focuses more on learning the core concepts. While the visualization is not interactive, you can view the result through static graphs in a Jupyter Notebook.

## Objective
- Implements a basic 2D range tree from scratch using Python
- Supports range queries in 2D space
- Visualizes the structure using a static graph
- Can be run and tested in a Jupyter Notebook

## Project Structure
- `core` – Includes the core logic to build the range tree, perform range queries, and visualizing the structure.
- `test.ipynb` – A Jupyter Notebook for testing the result.
- `range_tree_graph.png` – Output.
- `README.md` – This file.

## How to Use

Run `test.ipynb` in Jupyter to try it out. It builds a range tree from sample points, performs a query over a defined rectangular region, and shows a visual graph of the structure.

You can also modify the input nodes and the query rectangle directly in the notebook to see how the tree and the result change visually.
