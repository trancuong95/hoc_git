li = [12, 24, 35, 70, 88, 120, 155]

#for i in li:
#    if li.index(i) == 0 or li.index(i) == 2 or li.index(i) == 4 or li.index(i) == 6:
#        li.remove(i)
# kết quả: [24, 35, 88, 120]
# Có kết quả này là vì mỗi khi xoá đi
# một thắng thì chỉ số sẽ giảm đi 1 đơn vị
# vị vậy kết quả cho ra không mong muốn
# do list li đã bị xoá dần trong lúc làm
# khiến chỉ số sụt giảm nên kết quả không như ý muốn\

# Vì vậy để li không bị biến dạng thay đổi
# ta nên dùng pop
for i in li:
    if li.index(li[0]) == 0 or li.index(li[2]) == 2 or li.index(li[4]) == 4 or li.index(li[6]) == 6:
        li.pop(li.index(i))

print(li)
