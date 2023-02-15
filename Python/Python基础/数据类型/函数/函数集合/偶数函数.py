number = int(input("数字："))


def OShu(number):
    if(number % 2 == 0):
        result = "该值是偶数"
    if(number % 2 != 0):
        result = "该值是奇数"
    return result


print(OShu(number))
