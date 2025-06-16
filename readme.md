##  Дипломный проект UI+APIMore 

- [Ссылка на занятие](https://school.qa.guru/pl/teach/control/lesson/view?id=334954986&editMode=0) 
- [Инструкция по проверке диплома](https://rainbow-spleen-3c9.notion.site/QA-GURU-PYTHON-ff276648b76a4e6b8bb538051ddf6fb4)




# Проект тестирования "demoqa.com" UI+API 



## Проект реализован с использованием 
<p align="left">
  <img width="5%" title="Pycharm" src="logo/pycharm.png"> 
  <img width="5%" title="Python" src="logo/python.png">
  <img width="5%" title="Pytest" src="logo/pytest.png">
  <img width="5%" title="Selene" src="logo/selene.png">
  <img width="5%" title="GitHub" src="logo/github.png">
  <img width="5%" title="Jenkins" src="logo/jenkins.png">
  <img width="5%" title="Selenoid" src="logo/selenoid.png">
  <img width="5%" title="Allure Report" src="logo/icon_allure.png">
  <img width="5%" title="Allure TestOps" src="logo/allure_testops.png">
  <img width="5%" title="Telegram" src="logo/tg.png">
</p>

## Список проверок, реализованных в автотестах
### UI
- [x] Лендинг. Открытие страницы - наличие логотипа
- [x] Лендинг. Открытие страницы - открытие формы регистрации
- [x] Лендинг. Переход на https://arda.digital/
- [x] Авторизация. Отправка пустой формы
- [x] Авторизация. Неверный логин
- [x] Авторизация. Неверный пароль
- [x] Авторизация. Успешная авторизация 

### API
- [x] Проверка доступности и статуса GET - https://it.arda.digital/ Ожидаемый статус-код: 200 OK
- [x] Проверка редиректа GET - http://it.arda.digital/ Должно редиректить на https://
- [x] Проверка некорректных URL - GET https://it.arda.digital/blabla Статус: 404 Not Found
- [x] Проверка успешной авторизации - POST https://it.arda.digital/api/users/verify Ожидаемый статус-код: 200 OK
- [x] Проверка неуспешной авторизации (неверный пароль) POST https://it.arda.digital/api/users/verify Ожидаемый статус-код: 400 Bad Request



## Установка
```sh
pip install -r requirements.txt  # Установка зависимостей

```

## Запуск тестов

```
--alluredir=./allure-results - #run configuration, additional arguments (указать для каждого файла и директории с тестами 
для формирования аллюр отчета)
```

```sh
pytest arda_tests/ # Запуск всех тестов в проекте
```

```sh
pytest -v arda_tests/  # Запуск всех тестов с детальным логом
```

```sh
pytest --alluredir=allure-results  # Запуск с сохранением отчёта Allure
```



### Основные ключи `pytest`:
- `-v` (verbose) — подробный вывод результатов тестирования.
- `-s` (show output) — показывает `print` внутри тестов.
- `--maxfail=N` — завершает тестирование после `N` неудачных тестов.
- `-k 'substring'` — запускает только тесты, содержащие `substring` в названии.
- `--tb=short` — сокращенный вывод трейсбека ошибок.
- `allure serve tests/allure-results` — запускает локальный сервер с отчетом Allure.

## <img width="3%" title="Jenkins" src="logo/jenkins.png"> Запуск проекта в Jenkins
[Job](https://jenkins.autotests.cloud/job/AnastasiyaKZC_Homework_L14/)

При нажатии на "Build with Parameters", а затем "Build" начнется сборка тестов и их прохождение через виртуальную машину в Selenide.
![Jenkins Screenshot](logo/jenkins_screen.png)

## <img width="3%" title="Allure Report" src="logo/icon_allure.png"> Allure report
После прохождения тестов, результаты можно посмотреть в Allure отчете, где также содержится ссылка на Jenkins.
![Allure Dashboard](logo/allure_report.png)

Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритизации, по времени прохождения и др.
![Allure Graphs](logo/graphs.png)

Во вкладке Suites находятся собранные тест-кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста.
![Allure Suites](logo/suites.png)

Видео прохождения теста:
![Test Video](logo/test.gif)

## <img width="3%" title="Allure TestOps" src="logo/allure_testops.png"> Интеграция с Allure TestOps
[Dashboard](https://allure.autotests.cloud/launch/45474)

Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![Allure TestOps Dashboard](logo/testOps.png)

Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д.

![Allure TestOps Suites](logo/testops_suites.png)

## <img width="3%" title="Telegram" src="logo/tg.png"> Интеграция с Telegram
После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестовом прогоне.
<img width="40%" title="Telegram Bot" src="logo/tg_bot.png">