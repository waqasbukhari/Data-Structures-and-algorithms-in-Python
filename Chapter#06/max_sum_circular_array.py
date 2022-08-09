def maxSubarraySumCircular(nums) :
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

if __name__ == "__main__":
    nums = [-3, 4, 6, 4, -8, 8]
    nums = [1,-2,3,-2]
    nums = [5,-3,5]
    nums = [-3,-2,-3]
    nums = [5, -7, -4, -8, -1, -5]
    nums = [9, -5, -1, 1, 7, 8]
    print(maxSubarraySumCircular( nums))


