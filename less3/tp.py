# tup = [1,2,3,4,5]
# a,b,c,d,e = tup
# print(a,b,c)

def y(a,b,c, **kwargs):
    result = a*b*c
    return result


d = {'a':2,'b':2,'c':3,'d':4}

# print(y(2,2,3))

print(y(**d))



# a = "safdafaasdasdfasdsa"
# print(a.split(' '))
# b = ""
# for i in a.split(' '):
#     b = b + i.lower().capitalize() + " "
#     # ' '.join(i[:1]).upper() + i[1:]
#     # b.append
#     print(i)
# print (b)


# x = input("Введите слово: ")
# print(a.lower().capitalize())
# print(a.isspace()


# print(a.lower().capitalize())