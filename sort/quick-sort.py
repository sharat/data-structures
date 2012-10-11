# Quick Sort
def quick_sort(list):

    if list == []:
        return []

    print list
    pivot = list[0]

    lesser = quick_sort([x for x in list[1:] if x < pivot])
    greater = quick_sort([x for x in list[1:] if x >= pivot])
    return lesser + [pivot] + greater

def main():
    sort_items = [55,15,33,18,21,41,25,53]
    print "Result: " + str(quick_sort(sort_items))
    pass

if __name__ == '__main__':
    main()