def numbers_less_than_twenty():
    counter = 0
    less_num_list = []
    while counter < len(num_list):
        item = num_list[counter]
        if item > 20:
            num_list.remove(item)
            less_num_list.append(item)
        else:
            counter += 1
    print("List that doesn't contain numbers greate than 20:- ",num_list)
    return "initial list "+" "+ str(less_num_list)

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
print(numbers_less_than_twenty())