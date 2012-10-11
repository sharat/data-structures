# Linear search
def search(search_items, x):
	for num in search_items:
		print "Comparing " + str(num)
		if(x == num):
			print "Found Value" + str(x);
			return
	print "Unable to find required value"

#binary search	
def binary_search(search_items, x):
	print "Searching for " + str(x) + " in " + str(search_items)
	low = 0
	high = len(search_items)
	
	while(low <= high):
		print 
		mid = (low+high-1)/2
		print "searching in " + str(search_items[low:high]) + " comparing " + str(search_items[mid]) + " and " + str(x)
		if search_items[mid] == x:
			print "Found " + str(x)
			return x
		elif search_items[mid] < x:
			low = mid + 1
		else:
			high = mid - 1

search_items = [15,18,21,25,33,41,53,55]
number_to_search = int(raw_input("Enter value to search"))
search(search_items, number_to_search)
print ""
binary_search(search_items, number_to_search)