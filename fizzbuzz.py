class Solution(object):
    def fizzBuzz(self, n: int) -> list[str]:
        z=[]
        for i in range(n+1):
            if i%3 != 0 and i%5 != 0:
                i= str(i)
                z.append(i)
            elif i % 3 == 0 and i % 5 == 0:
                i = "FizzBuzz"
                z.append(i)
            elif i % 3 == 0:
                i = "Fizz"
                z.append(i)
            elif i % 5 == 0:
                i ="Buzz"
                z.append(i)
        return z[1:]