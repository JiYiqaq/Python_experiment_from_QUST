def partition(array,low,high):
    """
    分解过程
    :param array:整体数据
    :param low:数据的最左端
    :param high:数据的最右端
    :return:基准值的位置
    """
    left = low - 1
    pivot = array[high]
    for right in range(low,high):
        if array[right] <= pivot:
            left += 1
            array[left],array[right] = array[right],array[left]
    array[left+1],array[high] = array[high],array[left+1]
    return left+1
def quickSort(array,low,high):
    """
    快速排序函数，无返回值，直接改变列表内容
    :param array:整体数据
    :param low:数据的最左端
    :param high:数据的最右端
    """
    if low < high:
        pivot = partition(array,low,high)
        quickSort(array,low,pivot-1)
        quickSort(array,pivot+1,high)
if __name__ == "__main__":
    list01 = [9,3,1,5,8,6,2,4]
    quickSort(list01,0,len(list01)-1)
    print(list01)
