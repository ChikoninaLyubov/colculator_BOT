from aiogram import types
from loader import dp
import numpy as np

@dp.message_handler(commands=['calc'])
def calc(message):
    try:
        
        num1, num2 = message.text.split()[1:]

        
        if 'j' in num1:
            num1 = np.complex(num1)
        else:
            num1 = float(num1)

        if 'j' in num2:
            num2 = np.complex(num2)
        else:
            num2 = float(num2)   
     

        add = num1 + num2
        sub = num1 - num2
        mul = num1 * num2
        div = num1 / num2

        
        dp.reply_to(message, f'Дополнение: {add}\nВычетание: {sub}\nУмножение: {mul}\nДеление: {div}')
    except Exception as e:
        dp.reply_to(message, 'Неверный ввод')

dp.polling()