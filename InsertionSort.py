def insertion(array):
    for i in range(1,len(array)):
        if array[i] >= array[i-1]:
            continue
        for j in range(i):
            if array[i] < array[j]:
                array[j],array[j+1:i+1] = array[i],array[j:i]
                break

#TIming
if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import insertion")
    print(t.timeit())
