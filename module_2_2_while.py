my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
step_ = 0
while step_ < (len(my_list)):
    if my_list[step_] < 0:
        break
    if my_list[step_] != 0:
        print(my_list[step_])
        step_ = step_ + 1
    if my_list[step_] == 0:
        step_ = step_ + 1
        continue
