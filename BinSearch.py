#бинарный поиск в отсортированном массиве

# На вход подаётся целочисленный массив и число. На выходе - индекс элемента или -1, 
# в случае если искомого элемента нет в массиве.


def binary_search(list, numberToFind):
    # определяем индексы первого и последнего элемента - границы поиска
    firstElem = 0  
    lastElem = len(list) - 1 
    middle = int((len(list))/2) #определяем середину
    #пока мы не дошли до конца области поиска
    while firstElem <= lastElem:  
        if numberToFind == list[middle]: # если значение середины равно искомому числу
            return middle # возвращаем индекс искомого элемента
        if numberToFind < list[middle]: # сравниваем середину с искомым числом
            lastElem = middle - 1 # если число меньше, первый элемент переносим в середину области поиска
        if numberToFind > list[middle]: 
            firstElem = middle + 1 # если искомое число больше, центрального числа, последний элемент переходит на середину
       
        middle = int((firstElem + lastElem) / 2)  # берем число в середине области поиска

    return -1 # если элемента в массиве нет, возвращаем -1


ourList = [1,2,3,7,8,9,11,15,18,19,27]
print("hello")
print(binary_search(ourList, 8))
print(binary_search(ourList, 19))