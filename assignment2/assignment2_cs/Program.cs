using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace assignment2_cs
{
    class Program
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
            public object Data { get;set; }
            public Node Left { get;set; }
            public Node Right { get;set; }
            public string ID { get;set; }
            

            #region constructors
            public Node() : this(null, string.Empty) { }
            public Node(object data, string id ) : this(data:data, left:null, right:null, id:id)
            {
            }

            public Node(object data, Node left, Node right, string id)
            {
                this.Data = data;
                this.Left = left;
                this.Right = right;
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

            public virtual EdgeToNeighbor this[int index]
            {
                get { return (EdgeToNeighbor)base.InnerList[index]; }
                set { base.InnerList[index] = value; }
            }
        }

        class NodeList : IEnumerable
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

            }

            public virtual NodeList GetNeighbors(Node n)
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

        static void Main(string[] args)
        {
            Graph web = new Graph();
            web.AddNode(id:"80 Feet Road", data:null);
            web.AddNode(id: "CMH Road", data: null);
            web.AddNode(id: "Halasaru", data: null);
            web.AddNode(id: "Trinity", data: null);
            web.AddNode(id: "MG Road", data: null);
            web.AddNode(id: "100 Feet Road", data: null);
            web.AddNode(id: "Domlur Flyover", data: null);
            web.AddNode(id: "Victoria Road", data: null);

            web.AddEdge(web.Nodes["80 Feet Road"], web.Nodes["CMH Road"]);
            web.AddEdge(web.Nodes["CMH Road"], web.Nodes["Halasaru"]);
            web.AddEdge(web.Nodes["Halasaru"], web.Nodes["Trinity"]);
            web.AddEdge(web.Nodes["Trinity"], web.Nodes["MG Road"]);
            
            web.AddEdge(web.Nodes["80 Feet Road"], web.Nodes["100 Feet Road"]);
            web.AddEdge(web.Nodes["100 Feet Road"], web.Nodes["Domlur Flyover"]);
            web.AddEdge(web.Nodes["Domlur Flyover"], web.Nodes["Victoria Road"]);
            web.AddEdge(web.Nodes["Victoria Road"], web.Nodes["Trinity"]);
        }
    }
}
