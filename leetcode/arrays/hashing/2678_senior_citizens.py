class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for passengers in details:
            age = int(passengers[11:13])
            if (age > 60):
                counter+=1

        return counter
        