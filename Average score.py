# Практическое задание по модулю: "Базовые структуры данных."
# Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # исходные данные
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # исходные данные
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}) # преобразование в список
students.sort() # сортировка по возрастанию
# вычесление ср. балла
arn = sum (grades[0]) / len (grades[0])
blb = sum (grades[1]) / len (grades[1])
jhn = sum (grades[2]) / len (grades[2])
knd = sum (grades[3]) / len (grades[3])
stv = sum (grades[4]) / len (grades[4])
scores = [arn, blb, jhn, knd, stv] # список баллов
a_score = dict (zip (students, scores)) # объединение списков в словарь
print (a_score)
