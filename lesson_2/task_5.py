"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке."""


for symbol in range(32, 127+1):
    print(f'order: {symbol} is: {chr(symbol)}|', end='')
    if symbol % 10 == 1:
        print()
