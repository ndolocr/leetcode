class PalindromString:
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
        :type x: str
        :rtype: bool
        """

        first_index = 0
        original_string = x
        original_string_len = len(x)
        last_index = original_string_len -1
        original_string_mid_value = original_string_len // 2

        while original_string_mid_value >= 0:

            if x[first_index] != x[last_index]:
                return False
            
            last_index = last_index - 1
            first_index = first_index + 1
            original_string_mid_value -= 1

        return True

def main():
    obj = PalindromString()
    palindrom = obj.isPalindrome("abcdedcbag")
    print(f"Is Palindrom -> {palindrom}")

if __name__ == "__main__":
    main()