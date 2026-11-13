# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline:
    # keep track of index and value with enumerate, then compare the value at current index to all values in a list 
    # of current index + 1:. returning index1+ index2 + 1 because we need to add all of the places that were lost when i sliced the list
    for index1, value in enumerate(nums):
        for index2, compare in enumerate(nums[index1 + 1:]):
            if value + compare == target:
                return [index1, index1 + index2 + 1]

def max_profit(prices):
     # Outline:
    # creating list of all possible values, and return max of that list 
    # subtract number after by initial number to get profit
    if len(prices) <= 1: # not possible to calculate profit in this case
        return 0

    profits = []
    for index, value in enumerate(prices):
        for index2, value2 in enumerate(prices[index + 1:]):
            profits.append(value2 - value)

    if max(profits) < 0:
        return 0
    else: return max(profits)


def max_subarray(nums):
    # Outline:
    # for each item in nums, sum the whole list forward from that item, then cut off the last item each time
    # every time i finish summing something, add that sum to the subarray_sums list. Return max of that list
    if not nums:
        return None
    
    subarray_sums = []

    for i in range(len(nums)):
        end = len(nums)
        # every time i start a new loop, start at the next index, until the last index
        
        for j in range(len(nums[i:end])):
            subarray_sums.append(sum(nums[i:end]))
            end -= 1
            if end == 0:
                break;
        
    return max(subarray_sums)

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    pass

if __name__ == "__main__":
    main()
