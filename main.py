import math
import random
import time


def kef_list_in_file():

    N=int(input('введите степень многочлена \n-->'))
    kef_list = ["k = " + str(N) + "-->  " +
                str(random.randint(0, 100)) + " + "]
    file = open("kef_list_file.txt", "w")
    try:
        if (N == 1):
            kef_list[0] += (str(random.randint(0, 100)) + "*x")
        elif N == 2:
            kef_list[0] += (str(random.randint(0, 100)) + "*x + ") +\
                           (str(random.randint(0, 100)) + "*(x^2) ")
        elif N < 0:
            print("отрицательна степень? сирийозно?")
        elif N == 0:
            kef_list = [str(random.randint(0, 100)) ]
        else:
            kef_list[0] += (str(random.randint(0, 100)) + "*x + ") + \
                           (str(random.randint(0, 100)) + "*(x^2) + ")
            for i in range(2,N):
                if i ==N-1:
                    kef_list[0] += (str(random.randint(0, 100)) + "*(x**" + str(i+1) + ") = 0 ")
                else:
                    kef_list[0] += ( str(random.randint(0, 100)) + "*(x**"+ str(i+1)+") + ")

        print(kef_list)
        for element in kef_list:
            file.write(element)
    except:
        print("oh something wrong")
        file.close()



def sum_polinoms():
    print("сначала сгенерируем 2 файла с рандомными многочленами")
    N1 = int(input('введите степень  первого многочлена \n-->'))
    N2 = int(input('введите степень  второго многочлена \n-->'))
    # создаем списки с первым элементом полинома - х в степени 0 те число
    kef_list1 = [str(random.randint(0, 100)) + " + "]
    kef_list2 = [str(random.randint(0, 100)) + " + "]
    # открываем файлы в режие запись
    polinka1 = open("kef_list_file1.txt", "w")
    polinka2 = open("kef_list_file2.txt", "w")
    try:
        # создаем первый полином и сохраняем в файл kef_list_file2.txt
        if (N2 == 1):
            kef_list2[0] += (str(random.randint(0, 100)) + "*x")
        elif N2 == 2:

            kef_list2[0] += (str(random.randint(0, 100)) + "*x + ") + \
                           (str(random.randint(0, 100)) + "*(x^2) ")
        elif N2 < 0:
            print("отрицательна степень? сирийозно?")
        elif N1 == 0:

            kef_list2 = [str(random.randint(0, 100))]
        else:

            kef_list2[0] += (str(random.randint(0, 100)) + "*x + ") + \
                           (str(random.randint(0, 100)) + "*(x^2) + ")
            for i in range(2, N2):
                if i == N2 - 1:

                    kef_list2[0] += (str(random.randint(0, 100)) + "*(x^" + str(i + 1) + ") = 0 ")
                else:

                    kef_list2[0] += (str(random.randint(0, 100)) + "*(x^" + str(i + 1) + ") + ")

        # создаем второй полином и сохраняем в файл kef_list_file1.txt

        if (N1 == 1):
            kef_list1[0] += (str(random.randint(0, 100)) + "*x")
        elif N1 == 2:
            kef_list1[0] += (str(random.randint(0, 100)) + "*x + ") + \
                           (str(random.randint(0, 100)) + "*(x^2) ")

        elif N1 < 0:
            print("отрицательна степень? сирийозно?")
        elif N1 == 0:
            kef_list1 = [str(random.randint(0, 100))]

        else:
            kef_list1[0] += (str(random.randint(0, 100)) + "*x + ") + \
                           (str(random.randint(0, 100)) + "*(x^2) + ")

            for i in range(2, N1):
                if i == N1 - 1:
                    kef_list1[0] += (str(random.randint(0, 100)) + "*(x^" + str(i + 1) + ") = 0 ")

                else:
                    kef_list1[0] += (str(random.randint(0, 100)) + "*(x^" + str(i + 1) + ") + ")


        print(kef_list1 )
        print(kef_list2,"\n")
        for element in kef_list1:
            polinka1.write(element)
        for element in kef_list2:
            polinka2.write(element)
        print("после чего открыть их, \n извлечь коэффициенты")

        file1 = open("kef_list_file1.txt", "r")

        for line in file1:
            kef_list1.append(line.strip())
        kef_list1 = kef_list1[0].replace(" +", "").replace("*", "").replace("x", ""). \
            replace("^", "").replace("(", " ").replace(")", "").replace("=", "") \
            .split(" ")
        for i in range(3,len(kef_list1),2):
            kef_list1[i]=""
        kef_list1 = list(filter(None, kef_list1))
        print(kef_list1)


        file2 = open("kef_list_file2.txt", "r")
        for line in file2:
            kef_list2.append(line.strip())
        kef_list2=kef_list2[0].replace(" +","").replace("*","").replace("x","").\
            replace("^","").replace("("," ").replace(")","").replace("=","")\
            .split(" ")



        for i in range(3,len(kef_list2),2):
            kef_list2[i]=""
        kef_list2 = list(filter(None, kef_list2))
        print(kef_list2)
        kef_sum=[]
        if (len(kef_list2) > len(kef_list1)):
            for item in range(len(kef_list1)):
                kef_sum.append(str(int(kef_list1[item]) + int(kef_list2[item])))
            for item in range(len(kef_list1), len(kef_list2)):
                kef_sum.append(kef_list2[item])
        else:
            for item in range(len(kef_list2)):
                kef_sum.append(str(int(kef_list1[item]) + int(kef_list2[item])))
            for item in range(len(kef_list2), len(kef_list1)):
                kef_sum.append(kef_list1[item])
        print(F"\nи просуммировать их между собой\n{kef_sum}")
        print("\nа теперь запишем в файл уже известным способом\n: ")

        #ЗАПИСЬ СУММАРНОГО ПОЛИНОМА В Файл

        kef_sum_wide = len(kef_sum)
        total_polinom = ["k = " + str(kef_sum_wide-1) + "-->  " +
                    kef_sum[0] + " + "]
        file = open("kef_sum.txt", "w")

        if (kef_sum_wide == 2):
            total_polinom[0] += (kef_sum[1] + "*x")
        elif kef_sum_wide == 3:
           total_polinom[0] += kef_sum[1] + "*x + " + \
                           kef_sum[2] + "*(x^2) "

        elif (kef_sum_wide == 1) :
            print(f"{kef_sum[0]}=0 ?")
        else:
            total_polinom[0] += kef_sum[1] + "*x + " + \
                           kef_sum[2] + "*(x^2) + "
            for i in range(2, kef_sum_wide):
                if i == kef_sum_wide - 1:
                    total_polinom[0] += kef_sum[kef_sum_wide - 1] + "*(x^" + str(i ) + ") = 0 "
                else:
                    total_polinom[0] += kef_sum[i] + "*(x^" + str(i ) + ") + "

        print(total_polinom)
        for element in total_polinom:
            file.write(element)

    except:
        print("oh something wrong")
        polinka1.close()
        polinka2.close()
        file.close()

def Pi_kak_tochno():
    d = input(" введите точность в виде 0,1\n"
            "число знаков после запятой равносильно числу знаков числа пи\n"
            "d = ")

    if (float(d) > 0.1) or (float(d) < 0):
        print("неверный формат ввода")
    else:
        print(round(math.pi, len(str(d)) - 2))

def sympler():
    number = int(input("введите число \n"
                       "-->"))
    sympl_mult=[]
    sympler_now = 2

    while sympler_now * sympler_now <= number:
        if number % sympler_now ==0:
            sympl_mult.append(sympler_now)
            number//=sympler_now
            print(number)
        else:
            sympler_now+=1
    if not number==0:
        sympl_mult.append(number)
    print(f"простые множители числа {number}\n:"
          f"{sympl_mult}")



def ya_je_individealnost1111():
    no_indiv_list = []
    indiv_list = []

    # create list

    for wide in range(0,random.randint(5,25)):
        no_indiv_list.append( int (random.randint(0,9)))


    print("генерируем случайный список\n --//  ",

        sorted(no_indiv_list))


    # check dublicates

    for wide in range(1,len(no_indiv_list)):
        if not no_indiv_list[wide] in no_indiv_list[0:wide]:
            if not no_indiv_list[wide] in no_indiv_list[wide+1:]:
                indiv_list.append( no_indiv_list[wide])
    print("и выводим неповторяющиеся элемены в новый список\n --//  ",
        sorted(indiv_list))

def go_escho():
    input("нажмите ENTER для продолжения")
    main()


def main():
    Task_number=int(input("какое задание будем проверять?: \n"
                          "\n0-выйти из программы\n"
                          "\n1-Вычислить число c заданной точностью d\n"
                          "\n2-Задайте натуральное число N. \n"
                          "Напишите программу, которая составит список простых множителей числа N.\n"
                          "\n3-Задайте последовательность чисел. "
                          "Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности\n"
                          "\n4-Задана натуральная степень k. "
                          "Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена \n"
                          "и записать в файл многочлен степени k.\n"
                          "\n5-Даны два файла, в каждом из которых находится запись многочлена. \n"
                          "Задача - сформировать файл, \n"
                          "содержащий сумму многочленов (складываются числа, у которых х в одинаковых степенях)\n"
                          "\n-->"))
    if Task_number == 1:
        Pi_kak_tochno()

    elif Task_number == 2:
        sympler()

    elif Task_number == 3:
        ya_je_individealnost1111()

    elif Task_number == 4:
        kef_list_in_file()

    elif Task_number == 5:
       sum_polinoms()

    elif Task_number == 0:
        print("goodbay...")
        time.sleep(3)
        exit()
    else:
        print("oh..something wrong")
    go_escho()

if __name__ == "__main__":
    main()




