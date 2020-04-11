import time

def insertion_sort(data, draw_data, time_tick): 
    for i in range(len(data)):
        j = i
        while j > 0 and data[j - 1 ] > data[j]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
            draw_data(data,color_array(data,j,i))
            time.sleep(time_tick)
    draw_data(data,['green' for n in range(len(data))])
   
def color_array(data,j,i):
    arr = []
    for x in range(len(data)):
        if x == j:
            arr.append('green')
        elif x < i:
            arr.append('light grey') 
        else:
            arr.append('red')

    return arr