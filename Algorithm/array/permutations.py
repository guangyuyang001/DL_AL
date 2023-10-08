def permutation(arr):
    def backtrack(start):

        if start == len(arr) - 1:
            out.append(arr[:])
        else:
            for i in range(start, len(arr)):
                arr[start], arr[i] = arr[i], arr[start]
                print(start, i)
                backtrack(start+1)
                arr[start], arr[i] = arr[i], arr[start]
    out = []
    backtrack(0)
    return out

def permute(nums):
    if len(nums) == 1:
        return [nums]
    permutations = []

    for i in range(len(nums)):
        for perm in permute(nums[:i] + nums[i+1: ]):
            permutations.append([nums[i]] + perm)

    return  permutations

print(*permute([1, 2, 3]))