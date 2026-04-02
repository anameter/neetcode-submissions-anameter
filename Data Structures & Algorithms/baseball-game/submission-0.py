class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = list()

        for x in operations:
            if x == "+":
               n = int(record[-2]) + int(record[-1])
               record.append(n)
            elif x == "C":
                record.pop()
            elif x == "D":
                record.append(int(2*record[-1]))
            else:
                record.append(int(x))

        print(record)
        sum = 0
        for x in record:
            sum=sum + x
        
        return sum