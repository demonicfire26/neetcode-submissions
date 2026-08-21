class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt = [amount+1]*(amount+1)
        
        # initialising the first element of the amt list to 0
        amt[0] = 0

        # making the first for loop to iterate towards the 'amount' number
        for i in range(1, amount+1):
            # making the second for loop to iterate through the 'coins' list
            for j in range(len(coins)):
                # checking if the 'amount' number is greater than the element present in the 'coins' list
                if i >= coins[j]:
                    #applying the mathematical formula
                    amt[i] = min(amt[i], 1+amt[i-coins[j]])
        # if the element in the 'amt' list is lesser than the 'amount' value adding 1, we just return the item from the 'amt' list where its index is the 'amount' value
        if amt[amount] < amount + 1:
            return amt[amount]
        return -1