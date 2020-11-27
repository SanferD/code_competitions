"""
This in terms of ops.
A - add, X - replace, D - delete.
LOWERCASE, UPPERCASE, DIGIT can be fixed with one A or X operation for each violation.
Repeating characters of 3 or more are violations.
Notice that
1. if the repeating characters are exactly 3, only one A,X,D op is needed
2. if the repeating characters are some multiple of 3, will need one A,X,D op to reduce the number of 3-sequence runs by 1
3. generally, will need (run%3 + 1) number of A,X,D ops to reduce the number of 3-sequence runs by 1
SMALL: need 6 - len(password) A ops, some of which can be used to fix any of the aforementioned violations
LARGE: need len(password) - 20 D ops, some of which can be used to fix any repeating character violations.
-when fixing repeating characters by deletion, fix the ones that require least number of operations
"""

SMALL = "small"
LARGE = "large"
LOWERCASE = "lowercase"
UPPERCASE = "uppercase"
DIGIT = "digit"

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        steps = 0
        is_strong, violations, runs = self.isStrongPassword(password)
        if not is_strong:
            if SMALL in violations:
                diff = 6 - len(password)
                steps += diff
                violations.remove(SMALL)
                while runs:
                    diff -= 1
                    runs.pop()
                    _, violations = self.updateSimpleViolations(steps, violations)
                while diff > 0:
                    _, violations = self.updateSimpleViolations(steps, violations)
                    diff -= 1

            if LARGE in violations:
                D = len(password) - 20
                steps += D
                violations.remove(LARGE)
                while D > 0 and runs:
                    parts = [(run%3, i) for i, run in enumerate(runs)]
                    parts.sort(reverse=True)
                    ops, i = parts.pop()
                    delta = min(D, ops + 1)
                    runs[i] -= delta
                    D -= delta
                    if runs[i] < 3:
                        runs.pop(i)

            for run in runs:
                for _ in range(run//3):
                    if violations:
                        steps, violations = self.updateSimpleViolations(steps, violations)
                    else:
                        steps += 1
            while violations:
                steps, violations = self.updateSimpleViolations(steps, violations)
        return steps

    def updateSimpleViolations(self, steps, violations):
        delta = 1
        if LOWERCASE in violations:
            violations.remove(LOWERCASE)
        elif UPPERCASE in violations:
            violations.remove(UPPERCASE)
        elif DIGIT in violations:
            violations.remove(DIGIT)
        else:
            delta = 0
        steps += delta
        return steps, violations

    def isStrongPassword(self, password):
        violations = list()

        if len(password) < 6:
            violations.append(SMALL)
        if len(password) > 20:
            violations.append(LARGE)

        meets_requirement = list()
        for ch in password:
            if ch.isalnum():
                if ch.isdigit():
                    meets_requirement.append(DIGIT)
                elif ch.islower():
                    meets_requirement.append(LOWERCASE)
                elif ch.isupper():
                    meets_requirement.append(UPPERCASE)
        violations += list(set([DIGIT, LOWERCASE, UPPERCASE]) - set(meets_requirement))
        runs = self.findRuns(password)
        is_strong_password = not violations and not runs
        return is_strong_password, violations, runs

    def findRuns(self, s):
        runs = list()
        i = 0
        while i < len(s):
            run = [s[i]]
            i += 1
            while i < len(s) and run[0] == s[i]:
                run.append(s[i])
                i += 1
            if len(run) >= 3:
                runs.append(len(run))
        return runs

if __name__ == "__main__":
    solution = Solution()
    assert solution.strongPasswordChecker("a") == 5
    assert solution.strongPasswordChecker("abcdefg") == 2
    assert solution.strongPasswordChecker("aBcdef1") == 0
    assert solution.strongPasswordChecker("abeeef1") == 1
    assert solution.strongPasswordChecker("123456") == 2
    assert solution.strongPasswordChecker("1U3456") == 1
    assert solution.strongPasswordChecker("1Ue456") == 0
    assert solution.strongPasswordChecker("UUUe45") == 1
    assert solution.strongPasswordChecker("01234567890123456789aU") == 2
    assert solution.strongPasswordChecker("01234567890123456789aa") == 3
    assert solution.strongPasswordChecker("000000aA") == 2
    assert solution.strongPasswordChecker("111111") == 2
    assert solution.strongPasswordChecker("A11111") == 1
    assert solution.strongPasswordChecker("01234567890129990999Ab") == 2
    assert solution.strongPasswordChecker("01234567890123999999Abcd") == 4
    assert solution.strongPasswordChecker("01234567890123999999Ab") == 3
    assert solution.strongPasswordChecker("01234568888881999999Ab") == 4
    assert solution.strongPasswordChecker("012345688a88199a99Ab") == 0
    assert solution.strongPasswordChecker("111111111111111") == 5
    assert solution.strongPasswordChecker("UUUeA") == 1
    assert solution.strongPasswordChecker("111eA") == 1
    assert solution.strongPasswordChecker("01234567890123456789") == 2
    assert solution.strongPasswordChecker("0123456789012345678900000") == 7
    assert solution.strongPasswordChecker("0123456789012300000000000") == 7
    assert solution.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA") == 23

