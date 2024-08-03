def all_variants(text):
    n = len(text)
    for value in range(1, n + 1):
        for start in range(n - value + 1):
            yield text[start:start + value]


a = all_variants("abc")
for i in a:
    print(i)




    