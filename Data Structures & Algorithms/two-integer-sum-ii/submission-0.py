class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if i!=j:
                    if numbers[i]+numbers[j] == target:
                        new_list.append(i+1)
                        new_list.append(j+1)
        return new_list

