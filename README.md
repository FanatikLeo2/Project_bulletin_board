# Project_bulletin_board
Проект Доска объявлений

* Созданы модели объявлений (Post) и откликов (Reply)
* Реализовано представление списка объявлений (Post) 
* Реализована возможность для авторизованного пользователя создавать объявления, а так же редактировать только свои объявления
* Предоставлена возможность авторизованному пользователю создавать отклики на объявления (кроме своих)
* Реализовано представление списка откликов (Reply) с выводом откликов только на объявления автора
* Предоставлена возможность менять статус отклика на принятый и отклоненный
* Добавлена возможность фильтрации по постам в представлении списка откликов
* Реализована отправка писем при создании отклика на объявление, а так же при подтверждении отклика
* Реализована авторизация пользователей с помощью библиотеки allauth с подтверждением почты
* Реализоана авторизация пользователей через 4-х значный код, отправленный на почту через приложение accounts (allauth отключен с возможностью подключения)