import random
def DezToChar(nummer):
    text=""
    num=str(nummer)
    Cycle_Length=len(num)
    Count_Length=len(num)
    i=0
    while Cycle_Length!=0:
        if((i <= Count_Length - 1) and (i+1 <= Count_Length - 1) and (i+2<=Count_Length-1) and (int(num[i]+num[i+1]+num[i+2])<255)):
            number=int(num[0+i]+num[1+i]+num[2+i])
            string=chr(number)
            text += string
            i+=3
            Cycle_Length-=3
        elif((i <= Count_Length - 1) and (i+1 <= Count_Length - 1)):
            number=int(num[0+i]+num[1+i])
            string=chr(number)
            text += string
            i+=2
            Cycle_Length-=2
    print(text)
my_dict={
  "Artem": 88005553535, "Markaryan": 89566677795, "Podnebesny": 80529111337
}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(f"номер Артема {my_dict['Artem']}")
my_dict["Karibidis"]=87654321012
my_dict["IIo3uTuB4uK"]=81616161616
print(f"мой новый словарь:\n{my_dict}")
del my_dict["IIo3uTuB4uK"]
my_dict.update({"Kac": 115111989710797 , "StasAK": 11697103105108}) #ладно, лень функцию под восьмерку адаптировать
print(f"обновленный словарь:\n{my_dict}")
print(f"больше без позитивчика (( {my_dict.get('IIo3uTuB4uK')}")
print("Kac:")
DezToChar(my_dict.get("Kac"))
print("StasAK:")
DezToChar(my_dict.get("StasAK"))
temp=my_dict.pop("StasAK")
my_dict["StasAK"]=my_dict.pop("Kac")
my_dict["Kac"]=temp
print(my_dict.items())
print("Kac:")
DezToChar(my_dict.get("Kac"))
print("StasAK:")
DezToChar(my_dict.get("StasAK"))
print("\n")
#следующее задание
print("\n")
my_set={1,2,3,4,3,2,1,1,True,True,False,2.24,3.14,4,58,"Ivan","Ivan","Ivan"}
my_list=[1,2,3,4,3,2,1,1,True,True,False,2.24,3.14,4,58,"Ivan","Ivan","Ivan"]
print(my_list)
set(my_list) #здесь мы преобразовали лист в сет во ВРЕМЕННУЮ ПЕРЕМЕННУЮ
print(my_list)
print(set(my_list),"\n") #здесь мы преобразовали лист в сет во ВРЕМЕННУЮ ПЕРЕМЕННУЮ И ВЫВЕЛИ ЕЁ

print(my_set)
print(set(my_set)) #а здесь разницы нет
my_set.add(random.randint(1,100))
my_set.add(random.randint(1,100))
print("мой сет с двумя новыми элементами:",my_set)
my_set.discard(False)
print("мой сет без элемента False:",my_set)
