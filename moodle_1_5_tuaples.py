import random
immutable_var=(1,2,3.46,True,False,"Artem")
print(immutable_var)
#immutable_var[0]=5 неккоректно, так как тип неизменяемый по аналогии с перечислениями enum из c++
mutable_list=[1,2,3,4,5]
print(mutable_list)
for i in range(len(mutable_list)):
  mutable_list[i]=random.randint(1,100)
print(mutable_list)