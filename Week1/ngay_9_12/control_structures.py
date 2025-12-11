#1 if, else
# x = int(input("Nhap so nguyen: "))
#
# if x < 0:
#     x = 0
#     print("Doi gia tri thanh 0")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Single")
# else:
#     print("More")
# print("-----------------------------")
#
# #2 for
# words = ['pancake', 'source', 'ketchup']
# for w in words:
#     print("Word:", w, "Length:", len(w))
# print("-----------------------------")
#
# #3 range
# for i in range(5,10):
#     print("Number:", i)
# print("-----------------------------")
#
# a = ['Mayry', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print("Workds:", a[i], "Length:", len(a[i]))
# print("-----------------------------")

#4 FizzBuzz
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


result = fizzBuzz(50)
print(result)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break

for n in range(2,10):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")