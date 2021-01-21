import math

class Solution:
    def decrypt(self, code, k):
        back = code[:]
        for i in range(len(code)):
            s = 0
            sign = int(math.copysign(1, k))
            for j in range(1, sign*k + 1):
                idx = (i + sign*j) % len(code)
                s += code[idx]
            back[i] = s
        return back

if __name__ == "__main__":
    values = [
        ([5, 7, 1, 4], 3, [12, 10, 16, 13]), 
        ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
        ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
    ]
    for code, k, desired in values:
        result = Solution().decrypt(code=code, k=k)
        assert result == desired, f"{code} {k} result: {result} desired: {desired}"

