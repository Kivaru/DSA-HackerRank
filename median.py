def lonelyinteger(array):
    array.sort()
    length = len(array)

    return array[length//2]

if __name__ == '__main__':
    array = [1,2,3,4,3,2,1]
    lonelyinteger(array)