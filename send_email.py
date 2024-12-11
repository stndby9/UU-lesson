def send_email(messsage, recipient, sender='university.help@gmail.com'):
    a = ['.com', '.ru', '.net']
    b = False
    for i in range(0, 3):
        if a[i] in recipient:
            b = True
            break
    c = False
    for j in range(0, 3):
        if a[j] in sender:
            c = True
            break
    d = False
    if '@' in recipient and '@' in sender:
        d = True
    if b == False or c == False or d == False:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recipient)
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

    return messsage, recipient, sender


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
