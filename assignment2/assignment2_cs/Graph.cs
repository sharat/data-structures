using System;
using System.Collections;

namespace assignment2_cs
{
    enum Color
    {
        Violet,
        Indigo,
        Blue,
        Green,
        Yellow,
        Orange,
        Red
    }


    class Node
    {
        public object Data { get; set; }
        public AdjacencyList Neighbours { get; set; }
        public string ID { get; set; }


        #region constructors
        public Node() : this(null, string.Empty) { }
        public Node(object data, string id)
            : this(data: data, id: id, neighbors: new AdjacencyList())
        {
        }

        public Node(string id, object data, AdjacencyList neighbors)
        {
            this.Data = data;
            this.Neighbours = neighbors;
            this.ID = id;
        }
        #endregion
    }

    class EdgeToNeighbor
    {
        public Node Neighbour { get; set; }

        public EdgeToNeighbor(Node neighbour)
        {
            this.Neighbour = neighbour;
        }
    }

    class AdjacencyList : CollectionBase
    {
        protected internal virtual void Add(EdgeToNeighbor e)
        {
            base.InnerList.Add(e);
        }

        public virtual EdgeToNeighbor this[string index]
        {
            get { return (EdgeToNeighbor)base.InnerList[index]; }
            set { base.InnerList[index] = value; }
        }
    }



    class Graph
    {
        public NodeList Nodes { get; set; }

        public Graph()
        {
            this.Nodes = new NodeList();
        }

        public void AddNode(string id, object data)
        {
            Nodes.Add(new Node(data, id));
        }
        
        public virtual void AddEdge(Node v1, Node v2)
        {
            if (Nodes.ContainsKey(v1.ID) && Nodes.ContainsKey(v2.ID))
            {
                Nodes[v1.ID].Neighbours.Add(new EdgeToNeighbor(v2));
            }
            else
                throw new Exception("One more nodes specified are not existing");
        }

        public virtual Graph GetNeighbors(Node n)
        {
            return null;
        }

        public void SortGraphbyDegree()
        {

        }

        Color ChooseColor(Node n)
        {
            return Color.Blue;
        }
    }

    class NodeList : System.Collections.IEnumerable
    {
        private Hashtable data = new Hashtable();

        public virtual void Add(Node n)
        {
            data.Add(n.ID, n);
        }

        public void Remove(Node n)
        {
            data.Remove(n.ID);
        }

        public virtual bool ContainsKey(int key)
        {
            return data.ContainsKey(key);
        }

        public void Clear()
        {
            data.Clear();
        }

        // properties
        public virtual Node this[string key]
        {
            get
            {
                return (Node)data[key];
            }
        }
        public IEnumerator GetEnumerator()
        {
            return new NodeListEnumerator(data.GetEnumerator());
        }
    }

    #region enumerator
    class NodeListEnumerator : IEnumerator, IDisposable
    {
        IDictionaryEnumerator list;
        public NodeListEnumerator(IDictionaryEnumerator coll)
        {
            list = coll;
        }

        public void Reset()
        {
            list.Reset();
        }

        public bool MoveNext()
        {
            return list.MoveNext();
        }

        public Node Current
        {
            get
            {
                return (Node)((DictionaryEntry)list.Current).Value;
            }
        }

        // The current property on the IEnumerator interface:
        object IEnumerator.Current
        {
            get
            {
                return (Current);
            }
        }

        public void Dispose()
        {
            list = null;
        }
    }
    #endregion 
}
