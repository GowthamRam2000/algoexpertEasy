def sortedSquaresArray(array):
    sortedSquares=[0 for _ in array]
    for id in range(len(array)):
        value=array[id]
        sortedSquares[id]=value*value
    sortedSquares.sort()
    return sortedSquares
sortedSquaresArray([4,5,6,8,98,9,6,7,8,9,6])
