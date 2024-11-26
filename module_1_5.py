# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var= 1.1, 2.2, 3.3, 4.4, [1,2,3,4], 'буквы, слова, предлрожения', True, False
print (immutable_var)
immutable_var=( 1.1, 2.2, 3.3, 4.4, [1,2,3,4], 'буквы, слова, предлрожения', True, False)*3
print (immutable_var)
immutable_var= immutable_var[0:6]
print (immutable_var)
immutable_var[4][0]=4
immutable_var[4][1]=3
immutable_var[4][2]=1.9
immutable_var[4][3]=1
print (immutable_var)
immutable_var= immutable_var[4:5]
print (immutable_var)
immutable_var= immutable_var,'ТЕКСТ'
print (immutable_var)
print (immutable_var[1])
print (immutable_var[0])
#immutable_var[1]= 'СЛОВО' (не вазможно т.к. текст являеться не изменным элементом кортежа)
