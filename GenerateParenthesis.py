from typing import List


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_parenthesis(0, 0, result, n, "")
        return result

    def generate_parenthesis(self, left_count, right_count, result, n, path):
        if left_count > n or right_count > n:
            return
        if left_count < right_count:
            return
        if left_count == n and right_count == n:
            result.append(path)

        self.generate_parenthesis(left_count + 1, right_count, result, n, path + "(")
        self.generate_parenthesis(left_count, right_count + 1, result, n, path + ")")
