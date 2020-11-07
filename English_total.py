# импорт модулей и запрос параметров
import openpyxl
import random
import sys

right = 0 #правильный ответ
wrong = 0 #неправильный ответ

print ('Какой урок от 1-10?')    #с проверкой что цифра и в нужном диапазоне
status = True
while status:
    try:
        modul=int(input())
        status = False   
        if  10 < modul or modul < 1:
            print ('Урок от 1-10 - укажи еще раз')
    except:
        print('Какой-какой?')


print('Перевод р-а или а-р?')   #с проверкой что правильно ввели
while True:
    language = input() 
    if language =='р-а' or language == 'а-р':
        break
    else:
        print('Лень ввести?')
 

print('Какое количество попыток?')
status = True
while status:
    try:
        i = int(input())
        status = False
    except:
        print('Какое-какое?')

print("Добавить баллов за правильный ответ (кол-во)")
status = True
while status:
    try:
        right_score = int(input())
        status = False
    except:
        print('Сколько?')

print("Вычесть баллы за НЕправильный ответ (кол-во)")
status = True
while status:
    try:
        wrong_score = int(input())
        status = False
    except:
        print('Сколько?')


print('Какое количество баллов для приза?')
while True:
    try:
        priz_score = int(input())
        if priz_score >= 10:
            break
        elif  priz_score < 10:
            print('А не маловато ли?')
    except:
        print('Проверь, что ввела?') 
 
priz = 'priz' #Какой приз? можно сделать вводом

# импортэксель-файла с данными и октрытие нужного листа
source_file = openpyxl.load_workbook((r'C:\Users\user\Desktop\Питон\Слова_английский(correct).xlsx'))
first_sheet = source_file.worksheets[modul-1] #открытие активного листа - модуль 2- это лист 1

  
# создание словаря из данных в случае р-а и а-р
slovar = {}
if language == 'а-р':
    for cell_slovo,cell_perevod in first_sheet:
        cell_perevod=str(cell_perevod.value)
        cell_perevod1=cell_perevod.split(',') #перевод в форме списка
        slovar[cell_slovo.value] = cell_perevod1
#print(slovar)
#если нужно только первое слово в переводе, то cell_perevod1=cell_perevod.replace(';'or':',',').split(',')[0]
if language == 'р-а':
    for cell_slovo,cell_perevod in first_sheet:
        slovar[cell_perevod.value] = cell_slovo.value  #заменила ключ и значение в словаре


#сама программа
status = True
while True:
    slovo = random.choice(list(slovar.keys()))   #если случайный выбор ключа (может повторяться)
    n = 0 #количество попыток
    while n < i :
        print("Перевод слова:",slovo,sep = ' ')  #проверка что введено не пустое слово
        while True:
            perevod = input()
            if perevod != '':
                break
            else:
                print('Какое-какое?')            
                  
        perevod = perevod.lower()
        if perevod == 'exit':
            sys.exit()
            print ("Вы остановили программу")
        elif perevod in slovar[slovo]:
            break
        else:
            print('Это неправильный ответ')
            n = n + 1

    if n == i: #если неправильный ответ
        if language == 'а-р':
            print ("Правильный ответ - ",','.join(slovar[slovo]),sep =' ')
        elif language == 'р-а':
            print ("Правильный ответ - ",slovar[slovo],sep =' ' ) #ключ уже не нужно делать строкой
        wrong = wrong + 1
        total_score = right_score * right - wrong_score * wrong
        print('Набрано очков:',str(total_score),'Правильных ответов и ошибок:',str(right),"и",str(wrong),sep=' ',end='\n\n')  
    elif perevod in slovar[slovo]:  #если правильный ответ
        right = right + 1
        total_score = right_score * right - wrong_score * wrong
        print("Молодец - ты угадала с",str(n),"попытки.",end='\n')
        print('Набрано очков:',str(total_score),'Правильных ответов и ошибок:',str(right),"и",str(wrong),sep=' ',end='\n\n')
        del slovar[slovo]     #удалить угаданное слово, чтобы больше не показывалось
    
    if total_score == priz_score:   #если баллов на приз
        print ('Ты выиграла приз -', priz,'!!!',sep=' ')
        break
               
   
    
