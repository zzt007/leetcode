MAPPING = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
from typing import List
import sys


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans: List[str] = []
        path = [''] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                print(ans)
                return

            for c in MAPPING[int(digits[i])]:
                print(c)
                path[i] = c
                dfs(i + 1)

        dfs(0)
        return ans


def main() -> None:
    digits = sys.argv[1] if len(sys.argv) > 1 else '23'
    sol = Solution()
    res = sol.letterCombinations(digits)
    print(res)


if __name__ == '__main__':
    main()

