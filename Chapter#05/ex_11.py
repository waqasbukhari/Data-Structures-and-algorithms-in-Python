"""sum of the list of lists"""
def sum_list_of_lists(matrix):
    # sum over the rows and then overall summ
    return sum([sum(inner_arr) for inner_arr in matrix])

if __name__ == '__main__':

    arr = [list(range(4)),list(range(1,5)),list(range(2,6)),list(range(3,7))]
    print(sum_list_of_lists(arr))
