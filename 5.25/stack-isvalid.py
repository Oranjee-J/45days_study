'''

20. 有效的括号

提示
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。


示例 1：
    输入：s = "()"
    输出：true

示例 2：
    输入：s = "()[]{}"
    输出：true

示例 3：
    输入：s = "(]"
    输出：false

示例 4：
    输入：s = "([])"
    输出：true

示例 5：
    输入：s = "([)]"
    输出：false

提示：
    1 <= s.length <= 104
    s 仅由括号 '()[]{}' 组成

'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in mapping.keys():
                stack.append(mapping[ch])       #  把右括号压入
            else:
                if not stack or stack.pop() != ch :
                    return False
        
        return not stack
    

class Solution_2:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in mapping.keys():
                stack.append(ch)
            else:
                if not stack or mapping[stack.pop()] != ch:     # 这里如果不弹出那么下面要写弹出栈，不然栈顶永远不会变化
                    return False
            
                
            
        return not stack
            