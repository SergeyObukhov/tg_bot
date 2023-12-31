# Проект 2. Игра "Камень ножницы бумага"

## Оглавление  
[1. Описание проекта](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#описание-проекта)  
[2. Какой кейс решаем?](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#какой-кейс-решаем)  
[3. Описание взаимодействия с ботом](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#описание-взаимодействия-с-ботом)  
[4. Этапы работы над проектом](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#этапы-работы-над-проектом)  
[5. Результаты](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#результаты)  
[6. Выводы](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#выводы)  
  
### Описание проекта  
Телеграм-бот, с которым можно играть в игру "Камень, ножницы, бумага"
  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление)
  
  
### Какой кейс решаем?  
Чтобы на примере продемонстрировать работу с обычными кнопками и шаблоном проекта, а также иметь возможность играть с ботом в простую игру.
  
**Что бот должен уметь?**  
1. Отправлять пользователю клавиатуру с обычными кнопками выбора: камень, ножницы, бумага.
2. Генерировать случайный элемент в игре из списка "камень, ножницы, бумага".
3. Обрабатывать выбор пользователя и сообщать, кто победил

  
**Что практикуем**  
- Учимся программировать с использованием модульной файловой структуры.
- Практикуем работу с обычными кнопками.
  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление)

### Описание взаимодействия с ботом  
1. Пользователь отправляет команду /start боту (или стартует его, найдя в поиске)
2. Бот приветствует пользователя и предлагает сыграть в игру "Камень, ножницы, бумага", отправляя клавиатуру с ответами "Давай!" и "Не хочу!", а также предлагает пользователю прочитать подробные правила, отправив команду /help
3. На этом этапе пользователь может совершить 4 действия:
    1. Согласиться играть с ботом в игру, нажав на обычную кнопку "Давай!"
    2. Не согласиться играть с ботом, нажав на обычную кнопку "Не хочу!"
    3. Отправить в чат команду /help
    4. Отправить в чат любое другое сообщение
4. Пользователь нажимает на обычную кнопку "Давай!":
    1. Бот присылает в чат сообщение "Отлично! Делай свой выбор!"
    2. Бот отправляет в чат клавиатуру с кнопками выбора "Камень", "Ножницы" и "Бумага"
    3. На этом этапе пользователь может совершить 3 действия:
        1. Нажать на одну из кнопок выбора ("Камень", "Ножницы" или "Бумага")
        2. Отправить в чат команду /help
        3. Отправить в чат любое другое сообщение
    4. Пользователь нажимает на одну из кнопок выбора ("Камень", "Ножницы" или "Бумага"):
        1. Бот генерирует случайный ответ из того же списка
        2. Бот проверяет кто победил 
        3. Бот сообщает пользователю кто победил
        4. Бот отправляет пользователю предложение сыграть еще раз и клавиатуру для выбора с кнопками "Давай!" и "Не хочу!"
5. Пользователь нажимает на кнопку "Не хочу!":
    1. Клавиатура сворачивается
    2. Бот присылает сообщение "Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!"
6. Пользователь отправляет в чат команду /help:
    1. Бот присылает в чат правила игры, предложение сыграть и клавиатуру с кнопками "Давай!" и "Не хочу!"
7. Пользователь отправляет в чат любое другое сообщение:
    1. Бот присылает в чат сообщение, что не понимает пользователя
  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление)
  
  
### Этапы работы над проектом:  
1. **Разработка структуры программы.**
2. **Прячем чувствительные данные в переменную окружения *.env***
3. **Пишем точку входа в программу - *bot.py***
4. **Разработка клавиатур для бота.**
5. **Запишем все ответы бота в *lexicon.py***
6. **Пишем пакет хендлеров *handlers***
7. **Реализуем игровую логику в модуле *services.py***

  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление) 
  
  
### Результаты  
- Я практиковался в написании модульных приложений.
- Я отработал приёмы работы с обычными кнопками.
  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление) 
  
  
### Выводы  
Я справился с поставленной задачей:
написал игру "Камень ножницы бумага". 
  
:arrow_up: [к оглавлению](https://github.com/SergeyObukhov/tg_bot/blob/master/game_rsp_bot#оглавление)