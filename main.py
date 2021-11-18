#Задача №2*
#n=int(input())
#generator1 = (i for i in range(1, n + 1, 2))
#for i in range(1, n//2 + 2):
#    print(next(generator1))


#Задача №1
#n = int(input())
#def generator1(n):
#    for nn in range(1, n + 1, 2):
#        yield nn
#gen = generator1(n)
#for i in range(1, n//2 + 2):
#   print(next(gen))

#Задача №3VVV
#itertools import zip_longest
#tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Елена', 'Елена', 'Елена']
#klasses = ('9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А')
#generator = zip_longest(tutors, klasses[:len(tutors)])
#print(list(generator))



#Задача №4VVV
#scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#basket = [scr[i] for i in range(2,len(scr)) if scr[i] > scr[i-1]]
#print(basket)


#Задача №5
#scr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#basket = [scr[i] for i in range(2,len(scr)) if scr.count(scr[i]) > 0 and scr.count(scr[i]) < 2]
#print(basket)


