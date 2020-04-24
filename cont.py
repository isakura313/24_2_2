num = 0
while num < 15:
    num += 1
    if num % 3 == 0:
        continue
        #continue будет выкидывать числа, которые без остатка делятся на 3
    else:
        print(num)