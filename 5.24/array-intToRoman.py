'''
罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
给定一个整数，将其转换为罗马数字。

'''


class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: "I", 5:"V", 10: "X", 50:"L", 100:"C", 500:"D", 1000:"M"}

        s = ''

        while num >= 1000:
            s += dic[1000]
            num -= 1000

        if num >= 900:                      
            s = s + dic[100] + dic[1000]
            num -= 900    

        if num >= 500:
            s = s + dic[500]
            num -= 500
        
        if num >= 400:
            s = s + dic[100] + dic[500]
            num -= 400
        
        while num >= 100 :
            s += dic[100]
            num -= 100
        
        if num >= 90:                      
            s = s + dic[10] + dic[100]
            num -= 90   

        if num >= 50:
            s = s + dic[50]
            num -= 50
        
        if num >= 40:
            s = s + dic[10] + dic[50]
            num -= 40
        
        while num >= 10:
            s += dic[10]
            num -= 10
        
        while num >= 100 :
            s += dic[100]
            num -= 100
        
        if num >= 9:                      
            s = s + dic[1] + dic[10]
            num -= 9 

        if num >= 5:
            s = s + dic[5]
            num -= 5
        
        if num >= 4:
            s = s + dic[1] + dic[5]
            num -= 4

        while num > 0:
            s += dic[1]
            num -= 1

        return s
        