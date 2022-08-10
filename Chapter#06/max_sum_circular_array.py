import random
def maxSubarraySumCircular_simple(nums) :
    n = len(nums)
    max_e = max(nums)
    c_tmp = [i for i in nums]
    [print('{:3d}'.format(a), end=' ') for a in c_tmp]
    print()
    for k in range(1,n):
        tmp_ = [c_tmp[i] + nums[(i+k)%n] for i in range(n)]
        if max(tmp_) > max_e:
            max_e = max(tmp_)

        c_tmp = tmp_
        [print('{:3d}'.format(a), end=' ') for a in tmp_]
        print()
        #print(tmp_)

    return max_e # , max_row, max_col)
def circular_sum(nums, i):
    '''
    Find circular sum around index i. 
    '''
    n = len(nums)
    tmp_arr = [None] * n # len(nums)
    tmp_arr[0] = nums[i] 
    for j in range(1,n):
        tmp_arr[j] = tmp_arr[j-1] + nums[(i+j)%n] 

    return tmp_arr

def max_idx(arr):
    '''returns max and its index. '''
    max_arr = max(arr)
    max_idx = arr.index(max_arr)

    return max_arr, max_idx

def max_value_in_region(nums, element_idx):
    """
    Find a possible maximum value in a region starting from eleemnt_idx
    returns the maximum value and the ending index until which search is made. 
    """
    n = len(nums)
    arr_sum = circular_sum(nums, element_idx)
    max_val, max_index = max_idx(arr_sum) 

    next_max_val = max_val

    # iterate to search max_val in the trace. 
    for _ in range(max_index, 0,-1):
        # max value for the next element. 
        next_max_val = next_max_val - nums[element_idx] 
        if next_max_val > max_val:
            max_val = next_max_val

        element_idx += 1
        if element_idx == n:
            break;

    return max_val, element_idx

def maxSubarraySumCircular(nums) :
    max_element_idx = len(nums) - 1
    element_idx = 0
    max_value = nums[0]
    while True:
        tmp_max_val, element_idx = max_value_in_region(nums, element_idx)
        if tmp_max_val > max_value:
            max_value = tmp_max_val
        element_idx += 1
        if element_idx > max_element_idx:
            break; 

    element_idx = 0
    nums = nums[::-1]
    while True:
        tmp_max_val, element_idx = max_value_in_region(nums, element_idx)
        if tmp_max_val > max_value:
            max_value = tmp_max_val
        element_idx += 1
        if element_idx > max_element_idx:
            break; 

    return max_value


if __name__ == "__main__":
    while True:
        nums = random.choices(list(range(-50,50)), k=20)
        a = maxSubarraySumCircular( nums)
        b = maxSubarraySumCircular_simple( nums)

        print()

        if a != b:
            print(a,b)
            break

    print()

    print(nums)


