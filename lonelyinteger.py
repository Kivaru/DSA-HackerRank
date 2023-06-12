def lonelyinteger(array):
    for i in array:
        if array.count(i) == 1:
            print(i)
                

if __name__ == '__main__':
    array = [1,2,3,4,3,2,1]
    lonelyinteger(array)