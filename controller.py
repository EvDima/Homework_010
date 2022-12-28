import user_interface as user
import modul_sum as modul
import modul_div 
import modul_mult
import modul_sub
import logger

def button_click():
    print('Комплексное = 1, Рациональное = 2')
    value_item = int(input('Выберите значение: '))

    if value_item == 1:
        value_a = user.input_complex()
        value_b = user.input_complex()

    if value_item == 2:
        value_a = user.input_data()
        value_b = user.input_data()

    print('Выберите функцию: 1:Деление 2:Умноженик 3:Сложение 4:Вычитание')

    value_modul = int(input('выберите значение: '))  

    if value_modul == 1:
        modul_div.init(value_a, value_b)
        result = modul_div.div()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "/", result)

    if value_modul == 2:
        modul_mult.init(value_a, value_b)
        result = modul_mult.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "*", result)
    
    if value_modul == 3:
        modul.init(value_a, value_b)
        result = modul.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "+", result)  

    if value_modul == 4:
        modul_sub.init(value_a, value_b)
        result = modul_sub.do_it()
        user.view_data(result)
        logger.log_to_file(value_a, value_b, "-", result)
    



