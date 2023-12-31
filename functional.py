
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


#How does this solution ensure data immutability?
#Is this solution a pure function? Why or why not?
#Is this solution a higher order function? Why or why not?
#Would it have been easier to solve this problem using a different programming style?
#Why in particular is functional programming a helpful paradigm when solving this problem?