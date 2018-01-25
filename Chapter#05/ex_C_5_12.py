       
if __name__ == '__main__':

    arr = [list(range(4)),list(range(1,5)),list(range(2,6)),list(range(3,7))]

    summation = 0
    summation = sum([sum(inner_arr) for inner_arr in arr])
    print(arr)
    print(summation)
