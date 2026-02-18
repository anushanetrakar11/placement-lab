from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()   # stores indices
    result = []

    for i in range(len(nums)):
        # remove elements outside window
        if dq and dq[0] == i - k:
            dq.popleft()

        # remove smaller elements from right
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # start adding results after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# -------- TEST --------
if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums, k))
