from ete2 import Tree

def create_Tree():
	return Tree()

def insert_to_tree(t, value):
	iterator = t.traverse("preorder")
	for node in iterator:
		if int(value) < int(node.name):
			t.add_child(name= str(value))
			return

def print_tree(t):
	print t
	t.render("output.png")

def prepare_data(t):
	tree_items = [15,18,21,25,33,41,53,55]
	
	for item in tree_items:
		insert_to_tree(t, item)

t = Tree()
prepare_data(t)
print_tree(t)
