using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

namespace assignment2_cs
{
    class Program
    {
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
