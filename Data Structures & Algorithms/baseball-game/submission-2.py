class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = list()

        sum=0
        for x in operations:
            if x == "+":
                n = (record[-2]) + (record[-1])
                record.append(n)
                sum=sum+record[-1]
            elif x == "C":
                sum=sum-int(record[-1])
                record.pop()                
            elif x == "D":
                record.append((2*record[-1]))
                sum=sum+record[-1]
            else:
                record.append(int(x))
                sum=sum+record[-1]
                
        return sum