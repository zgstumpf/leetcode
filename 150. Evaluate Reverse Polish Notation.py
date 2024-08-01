class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                # get numbers in reverse order
                num2 = stack.pop()
                num1 = stack.pop()

                # int() makes division truncate toward zero
                stack.append(int(eval(f"{num1}{token}{num2}")))
            else:
                stack.append(token)
        return int(stack.pop())
