import time
def partition(data,head,tail,draw_data,time_tick):
    border = head
    pivot = data[tail]

    draw_data(data,get_colour(len(data),head,tail,border,border))
    time.sleep(time_tick)
    for j in range(head, tail):
        if data[j] < pivot:
            draw_data(data,get_colour(len(data),head,tail,j,True))
            time.sleep(time_tick)
            data[border],data[j] = data[j], data[border]
            border += 1 
        draw_data(data,get_colour(len(data),head,tail,border,border,j))
        time.sleep(time_tick)
    #swap pivot with border value 
    draw_data(data,get_colour(len(data),head,tail,border,tail,True))
    time.sleep(time_tick)
    data[border], data[tail] = data[tail],data[border]
    return border

def quick_sort(data, head, tail, draw_data,time_tick):
    if head < tail: 
        partition_index= partition(data,head,tail,draw_data,time_tick)

        #left partition
        quick_sort(data,head,partition_index -1, draw_data,time_tick)

        #right partition
        quick_sort(data,partition_index + 1,tail,draw_data,time_tick)

def get_colour(data_len,head,tail,border,curr_index,is_swaping = False):
    color_array = []
    for i in range(data_len): 
        if head >= i or i  <= tail:
            color_array.append('grey')
        else:
            color_array.append('white')

        if i == tail:
            color_array[i] = 'blue'
        elif i == border:
            color_array[i] = 'red'
        elif i == curr_index:
            color_array[i] = 'yellow'
        
        if is_swaping:
            if i == border or i == curr_index:
                color_array[i] = 'green'
    return color_array