class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        check1 = check1a = check1b = True
        check2 = check2a = check2b = True
        L = len(a)
        for i in range(L//2):
            j = L - i - 1

            if not check1 or a[i] != b[j]:
                check1 = False
                if check1a and a[i] != a[j]:
                    check1a = False
                if check1b and b[i] != b[j]:
                    check1b = False

            if not check2 or b[i] != a[j]:
                check2 = False
                if check2a and a[i] != a[j]:
                    check2a = False
                if check2b and b[i] != b[j]:
                    check2b = False
                    
        is_s1_palindrome = check1 or check1a or check1b
        is_s2_palindrome = check2 or check2a or check2b
        return is_s1_palindrome or is_s2_palindrome

if __name__ == "__main__":
    solution = Solution()
    assert solution.checkPalindromeFormation("x", "y")
    assert solution.checkPalindromeFormation("xyy", "aax")
    assert solution.checkPalindromeFormation("xbyy", "axxx")
    assert solution.checkPalindromeFormation("yyax", "xxxa")
    assert solution.checkPalindromeFormation("yyxx", "xxaa")

    a = "pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    for i in range(len(a)):
        a_p, a_s = a[:i], a[i:]
        b_p, b_s = b[:i], b[i:]
        s1 = a_p + b_s
        s2 = b_p + a_s
        if s1 == s1[::-1]:
            print(s1, i, a_p, b_s)
            break
        elif s2 == s2[::-1]:
            print(s2, i, b_p, a_s)
            break
    assert solution.checkPalindromeFormation(a, b)

