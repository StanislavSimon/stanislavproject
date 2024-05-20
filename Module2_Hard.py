# n = int(input('Inter password'))
# numbers=[]
#
# for i in range(1, n ):
#     for j in range(i+1,n+1):
#         z = i + j
#         if n % z == 0:
#             numbers.append((i, j))
#
#
# result=""
# for numbers in numbers:
#     result += str(numbers[0]) + str(numbers [1])
#     continue
# print(result)
while True:
      n = int(input("Введите число от 3 до 20: "))
      pairs = []
      for i in range(1, n):
            for j in range(i+1, n+1):
                  z = i + j
                  if n % z == 0:
                        pairs.append((i, j))
      res = ""
      for pair in pairs:
                  res += str(pair[0]) + str(pair[1])
      print(res)