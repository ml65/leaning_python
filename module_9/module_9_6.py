# Домашнее задание по теме "Генераторы"

#

def all_variants(text):
    for width in range(1,len(text)+1):
        begin = 0
        while (begin + width <= len(text)):
            resp = text[begin:begin + width]
            begin += 1
            yield resp


text = "abc"
print(f"begin={text[0]}")
a = all_variants("abc")
for i in a:
    print(i)
