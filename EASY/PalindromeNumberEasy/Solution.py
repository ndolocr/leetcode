class Solution(object):
    """
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
    Constraints:

    -231 <= x <= 231 - 1
    

    Follow up: Could you solve it without converting the integer to a string?
    
    """
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        original_number = x
        reversed_number = 0

        while x > 0:
            last_number = x % 10

            # Set reversed Number
            reversed_number = ((reversed_number * 10) + last_number)
            # Update 
            x = x//10

        return original_number == reversed_number

        
def main():
    obj = Solution()
    val_1 = 12343210
    status = obj.isPalindrome(val_1)
    print(f"IsPalindrome:- {status}")

if __name__=="__main__":
    main()
        