menu = [['coffee',150,2],['tea',100,8],['icecream',80,9],['pizza',300,6],['pepsi',90,7]]
print('Добро пожаловать!')
while True:
    for key,value in enumerate(menu):
        print(f'{key+1}.{value[0]},{value[1]} руб. {value[2]} кол-во.')
    try:
        num = int(input('Введите пожалуйста номер заказа или 0 для выхода '))
        if num == 0 :
            break
        if 0< num <=len(menu):
            product = menu[num-1][0]
            price = menu[num-1][1]
            print(f"Ваш заказ: {product}, стоимость: {price} руб.")
            input("Нажмите Enter для продолжения")
        if menu[num-1][2]  != 0:
            menu[num-1][2] = menu[num-1][2] -1
        else:
            print('К сожалению данный напиток закончился')
            menu.pop(num-1)
    except Exception:
        print('Введите новое значение')
print('Приходите ещё!')