def diagonalDifference(arr):
    # Write your code here
    length = len(arr)
    
    sum_left_to_right = sum_right_to_left = 0
    #sum of left-to-right diagonal
    for i in range(0,length):
        sum_left_to_right += arr[i][i]
        sum_right_to_left += arr[i][length-i-1]
    
    difference = sum_left_to_right - sum_right_to_left
    
    return abs(difference)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()