       
if __name__ == '__main__':

    arr = [list(range(4)),list(range(1,5)),list(range(2,6)),list(range(3,7))]

    summation = 0
    for inner_arr in arr:
        for element in inner_arr:
            summation += element
    print(arr)
    print(summation)
