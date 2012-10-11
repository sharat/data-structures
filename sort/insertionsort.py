#insertion sort

def insertion_sort(list):
    for index in range(1,len(list)):  # no need of the 0th element
        value = list[index]
        i = index - 1
        while i >= 0:
            if  value < list[i] :
                print list
                list[i+1] = list[i]
                list[i] = value
                i -= 1
            else:
                break

sort_items = [55,15,33,18,21,41,25,53]
insertion_sort(sort_items)
print sort_items

