# FitnessCalc
Микросервис создан для рассчета необходимой суточной нормы бжу, каллорий и воды у человека.
Написан на Flask с использованием базы данных PostgreSQL 13.3. 

Имеет 3 метода подсчета:
суточная норма бжу, суточная норма каллорий и суточная норма воды.

Все методы являются  POST - запросами.

Принцип работы:

* Отправляется POST - запрос в виде json; 
* Из json достается и проверяется переданная информация;
* Инициализируется класс;
* Вызываются необходимые функции к методу;
* Происходит запись полученного значения в базу данных;
* Выдается json ответ.

## Setup Development Environment

* Установка зависимостей

`docker-compose build`

* Запуск базы данных

`docker - compose up -d pgsql`

* Запуск сервера

`docker-compose up server`

## Usage example

Запрос:


    POST /calc/api/v1.0/bju HTTP/1.1
    Host: 127.0.0.1:5000
    Content-Type: application/json
    Content-Length: 111
    
    {
    "gender": "female",
    "weight": 60,
    "height": 178,
    "age": 23,
    "exercise_stress": "Short"
    }

Ответ (в случае успеха):

`{
"result_bju": 1626.209
}`

Запрос:

    POST /calc/api/v1.0/water HTTP/1.1
    Host: 127.0.0.1:5000
    Content-Type: application/json
    Content-Length: 111
    
    {
    "gender": "female",
    "weight": 60,
    "height": 178,
    "age": 23,
    "exercise_stress": "Short"
    }

Ответ (в случае успеха):

`{
"result_water": 2100.0
}`

Запрос:

    POST /calc/api/v1.0/callories HTTP/1.1
    Host: 127.0.0.1:5000
    Content-Type: application/json
    Content-Length: 111
    
    {
    "gender": "female",
    "weight": 60,
    "height": 178,
    "age": 23,
    "exercise_stress": "Short"
    }

Ответ (в случае успеха):

`{
"result_callories": 1951.4508
}`

Запрос:

`GET /calc/api/v1.0/param HTTP/1.1
Host: 127.0.0.1:5000`

Ответ (в случае успеха) выводятся значения из таблицы базы данных