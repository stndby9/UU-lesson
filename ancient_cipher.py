def get_pass(numb_):
    list_ = []
    for i in range(1, int(numb_)):
        for j in range(1, int(numb_)):
            if j >= int(numb_) or j == i:
                break
            if int(numb_) % (i + j) == 0:
                list_.append([j, i])
                list_.sort()
    return list_


for k in range(3, 21):
    res = get_pass(numb_=k)
    print('Значение:', k, ' пароль :', res)
