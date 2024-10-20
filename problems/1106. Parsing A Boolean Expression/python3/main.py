class Solution:
    def __get_inner_expressions(self, expression: str) -> list[str]:
        inners = []
        last_idx = -1

        # print(f"expr: {expression}")
        expression += ","

        nested = 0
        for i in range(len(expression)):
            if expression[i] == "," and not nested:
                inners.append(expression[last_idx + 1 : i])
                last_idx = i

            if expression[i] == "(":
                nested += 1
            if expression[i] == ")":
                nested -= 1

        # print(f"inners: {inners}")
        return inners

    def parseBoolExpr(self, expression: str) -> bool:
        if expression == "f":
            return False
        if expression == "t":
            return True

        inner = expression[2:-1]

        if expression[0] == "!":
            return not self.parseBoolExpr(inner)

        elif expression[0] == "&":
            inner_expr = self.__get_inner_expressions(inner)
            print(f"outer: {expression} - inner: {inner_expr}")
            return all([self.parseBoolExpr(ie) for ie in inner_expr])

        elif expression[0] == "|":
            inner_expr = self.__get_inner_expressions(inner)
            print(f"outer: {expression} - inner: {inner_expr}")
            return any([self.parseBoolExpr(ie) for ie in inner_expr])

        raise Exception(f"error with expr: {expression}")


if __name__ == "__main__":
    assert Solution().parseBoolExpr("t") == True
    assert Solution().parseBoolExpr("f") == False
    assert Solution().parseBoolExpr("!(t)") == False
    assert Solution().parseBoolExpr("!(f)") == True
    assert Solution().parseBoolExpr("|(f,t)") == True
    assert Solution().parseBoolExpr("&(f,t)") == False
    assert Solution().parseBoolExpr("!(&(f,t))") == True
    assert Solution().parseBoolExpr("|(&(t,f,t),!(t))") == False
