"""
Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (пробіли та переведення на новий рядок важливі!).
Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:
    Please enter an integer number: 1234
    Next number for number 1234 is 1235.
    Previous number for number 1234 is 1233.
"""
while True:
    try:
        a = int(input('Please enter an integer number: '))
        print('Next number for number ',a,'is ',a+1,'\n' 'Previous number for number ',a,'is ',a-1)
        break
    except ValueError:
        print('not an integer')
