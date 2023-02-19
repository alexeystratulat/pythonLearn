"""
Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку і на одну клітинку по горизонталі, чи навпаки.
Дані дві різні клітини шахівниці, визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
Клітина шахівниці задається одним рядком, що складається з символу a-h та цифри 1-8: a2, e2, e4, h7, d1, і т.і.
"""


mas_vertital = ['8', '7', '6','5','4','3','2','1']
mas_horizontal = ['a','b','c','d','e','f','g','h']

chessboard_mas = [mas_horizontal] * 8
print(chessboard_mas, "ffifiif",end = ' ')



for i in range(len(chessboard_mas)):
    for j in range(len(chessboard_mas)):

        chessboard_mas[i][j] = str(mas_horizontal[j])+str(mas_vertital[j])
        print(chessboard_mas[i][j], end = ' ')
    print()
print(chessboard_mas)