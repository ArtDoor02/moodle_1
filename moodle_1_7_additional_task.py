def average(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum += mylist[i]
    return sum / len(mylist)


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict = {}
index = 0
for keys in students:
    dict[keys] = grades[index]
    index += 1  # не смог придумать решения без индекса
    print("мой индекс", index)  # проверочная строка индкса

print("cловарь\n", dict)

print("средняя оценка Johnny: ", average(dict["Johnny"]))
print("средняя оценка Bilbo: ", average(dict["Bilbo"]))
print("средняя оценка Steve: ", average(dict["Steve"]))
print("средняя оценка Khendrik: ", average(dict["Khendrik"]))
print("средняя оценка Aaron: ", average(dict["Aaron"]))
