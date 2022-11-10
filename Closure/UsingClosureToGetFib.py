
if __name__ == '__main__':
    def fib(n):
        a, b = 0, 1
        num_list = []

        def add():
            nonlocal a, b
            count = 0
            while count < n:
                num_list.append(a)
                a, b = b, a + b
                count += 1
            result = ''
            for i in num_list:
                result += str(i) + ','
            return result.strip(',')

        return add

    test = fib(9)
    print(test())
