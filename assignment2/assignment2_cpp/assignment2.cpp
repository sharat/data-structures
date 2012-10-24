// assignment2_cpp.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <list>
using namespace std;

class Vertex;
typedef list<Vertex> ListVertex;

enum Color
{
	VIOLET, INDIGO, BLUE, GREEN, YELLOW, ORANGE, RED
};

char* ColorString[] = {  
	"VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"
};

// Vertex class
class Vertex
{
	int color;
	int id;
	list<Vertex> neighbours;

public:

	int getColor() { 
		return color;
	}
	
	int setColor(int color_in) {
		color = color_in;
	}
	
	int getID() {
		return id;
	}

	int setID(int id_in) {
		return id;
	}

	Vertex()
	{
		setColor(0);
		setID(0);
		neighbours.clear();
	}

	Vertex(int id_in, int color_in, ListVertex& neighbors_in )
	{
		setColor(0);
		setID(0);
		neighbours = neighbors_in;
	}
};

class Graph
{
public:
	// Creates an empty graph
	static Graph createGraph();
	static Graph addEdge(Graph g, Vertex v1, Vertex v2);
	static Graph getNeigbours(Graph g, Vertex v);
	static ListVertex getNeighbors(Graph g, Vertex v);
	static Graph sortGraphbyDegree(Graph);

private:

};

int main(int argc, char* argv[])
{

	return 0;
}

