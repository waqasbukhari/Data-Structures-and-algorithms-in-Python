def maxSubarraySumCircular_simple(nums) :
    n = len(nums)
    max_e = max(nums)
    c_tmp = [i for i in nums]
    print(c_tmp)
    for k in range(1,n):
        tmp_ = [c_tmp[i] + nums[(i+k)%n] for i in range(n)]
        if max(tmp_) > max_e:
            max_e = max(tmp_)

        c_tmp = tmp_
        print(tmp_)

    return max_e # , max_row, max_col)
def circular_sum(nums, i):
    '''
    Find circular sum around index i. 
    '''
    n = len(nums)
    tmp_arr = [None] * n # len(nums)
    tmp_arr[0] = nums[i] 
    for j in range(1,n):
        tmp_arr[j] = tmp_arr[j-1] + nums[j%n] 

    return tmp_arr

def max_idx(arr):
    '''returns max and its index. '''
    max_arr = max(arr)
    max_idx = idx(max_arr)

    return max_arr, max_idx


def maxSubarraySumCircular(nums) :
    n = len(nums)
    element_idx = 0
    arr_sum = circular_sum(nums, element_idx)
    print(arr_sum)
    max_val, max_index = max_idx(arr_sum) 
    print(max_val, max_index)

    next_max_val = max_val

    for _ in range(max_index, 0,-1):
        # 
        # max value for the next element. 
        next_max_val = next_max_val - nums[element_idx] 
        if next_max_val > max_val:
            max_val = next_max_val

        element_idx += 1

    print(max_val, element_idx)


if __name__ == "__main__":
    nums = [-3, 4, 6, 4, -8, 8]
    nums = [1,-2,3,-2]
    nums = [5,-3,5]
    nums = [-3,-2,-3]
    nums = [5, -7, -4, -8, -1, -5]
    nums = [9, -5, -1, 1, 7, 8]
    nums = [-1, 3, -1, 8, 4, 7]
    print(maxSubarraySumCircular( nums))


