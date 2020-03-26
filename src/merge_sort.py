import time 

def merge_sort(data,draw_data,time_tick):
    merge_sort_alg(data,0,len(data) -1,draw_data,time_tick)

def merge_sort_alg(data,left, right,draw_data,time_tick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data,left,middle,draw_data,time_tick)
        merge_sort_alg(data, middle + 1,right, draw_data,time_tick)
        merge(data, left, middle, right, draw_data,time_tick)

def merge(data,left,middle,right,draw_data,time_tick):
    draw_data(data,get_color(len(data),left, middle, right))
    time.sleep(time_tick)
    
    left_part = data[left:middle+1]
    right_part = data[middle + 1: right + 1]

    left_index = right_index = 0

    for data_index in range(left,right + 1):
        if left_index < len(left_part) and right_index < len(right_part):
            if left_part[left_index] <= right_part[right_index]:
                data[data_index] = left_part[left_index]
                left_index += 1
            else:
                data[data_index] = right_part[right_index]
                right_index += 1 
        elif left_index < len(left_part):
            data[data_index] = left_part[left_index]
            left_index += 1 
        else:
            data[data_index] = right_part[right_index]
            right_index += 1
    draw_data(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(time_tick)
    

def get_color(len, left, middle, right):
    color_array = []

    for i in range(len):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                color_array.append("yellow")
            else:
                color_array.append("pink")
        else:
            color_array.append("white")
    return  color_array