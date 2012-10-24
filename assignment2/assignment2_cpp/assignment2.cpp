// assignment2_cpp.cpp : Defines the entry point for the console application.
//

#include "common.h"
#include <algorithm>

using namespace std;

class Vertex;
class NodeList
{
	map<int, Vertex> nodes;

public:
	NodeList()
	{

	}

	void Add(Vertex& n);
	~NodeList()
	{
	}
};

class Adjacencylist;

class Vertex {
private:
	int ID;
	int color;
	Adjacencylist* neighbors;

public:
	
	Vertex() {
		ID = 0;
		color = 0;
	}

	Vertex(int id_in, int color_in = 0) {
		ID = id_in;
		color = color_in;
	}

	Vertex(int id_in, int color_in, Adjacencylist* neighbors_in) {
		ID = id_in;
		neighbors = neighbors_in;
		color = color_in;
	}

	~Vertex()
	{
		delete neighbors;
	}

	int getColor() { 
		return color;
	}
	
	int setColor(int color_in) {
		color = color_in;
	}
	
	int getID() {
		return ID;
	}

	int setID(int id_in) {
		return ID;
	}
};

class Edge {
	Vertex neighbor;

public:

	const Vertex& getNeighbor() {
		return neighbor;
	}

	Edge(Vertex& neighbor_in) {
		neighbor = neighbor_in;
	}
};

class Adjacencylist {
	std::vector<Edge> neighbors;

public:

	Adjacencylist(Edge e) {
		neighbors.push_back(e);
	}

	Edge& operator[](int idx) {
		neighbors[idx];
	}

	bool containsKey(int key)
	{
		
	}
};

class Graph {
	NodeList nodes;
public:
	// Creates an empty graph
	void createGraph();
	void addEdge(Vertex v1, Vertex v2);
	const Adjacencylist* getNeigbours (Vertex v);
	void sortGraphbyDegree();
	Color chooseColor(Vertex v);
	int assignColors();
	void print();
};

void Graph::createGraph()
{
	
}

void Graph::addEdge(Vertex v1, Vertex v2)
{
	
}

const Adjacencylist* Graph::getNeigbours(Vertex v)
{
	return 0;
}

void Graph::sortGraphbyDegree()
{

}
Color Graph::chooseColor(Vertex v)
{
	return RED;
}
int Graph::assignColors()
{
	return 0;
}
void print()
{
	return;
}


void NodeList::Add(Vertex& n)
{
	nodes[n.getID()] = n;
}
	

int main(int argc, char* argv[]) {

	return 0;
}

