##  Дипломный проект UI+APIMore 

- [Ссылка на занятие](https://school.qa.guru/pl/teach/control/lesson/view?id=334954986&editMode=0) 
- [Инструкция по проверке диплома](https://rainbow-spleen-3c9.notion.site/QA-GURU-PYTHON-ff276648b76a4e6b8bb538051ddf6fb4)




# Проект тестирования "demoqa.com" UI+API 


## 🌐 DemoQA — учебный веб-сайт для практики тестирования

![DemoQA Screenshot](https://demoqa.com/images/Toolsqa.jpg)

**[DemoQA](https://demoqa.com)** — это учебный веб-сайт, предназначенный для практики тестирования веб-приложений.  
Он предоставляет различные интерактивные элементы и сценарии, такие как:

- формы,
- кнопки,
- таблицы,
- всплывающие окна,
- фреймы,
- демо-приложение книжного магазина.

Это идеальная платформа для тренировки навыков UI- и API-тестирования.




## Проект реализован с использованием 
<p align="left">
  <img width="5%" title="PyCharm" src="https://raw.githubusercontent.com/JetBrains/logos/master/pycharm/pycharm.png">
  <img width="5%" title="Python" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.png">
  <img width="5%" title="Pytest" src="https://raw.githubusercontent.com/SerhiiCho/icon-pack/main/icons/pytest.png">
  <img width="5%" title="Selene" src="https://raw.githubusercontent.com/yashaka/selene/master/docs/_static/selene-logo.png">
  <img width="5%" title="GitHub" src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Github.svg">
  <img width="5%" title="Jenkins" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jenkins/jenkins-original.png">
  <img width="5%" title="Selenoid" src="https://aerokube.com/images/selenoid-logo.png">
  <img width="5%" title="Allure Report" src="https://docs.qameta.io/img/allure.svg">
  <img width="5%" title="Allure TestOps" src="https://avatars.githubusercontent.com/u/68425100?s=200&v=4">
  <img width="5%" title="Telegram" src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png">
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




## <img width="3%" title="Telegram" src="logo/tg.png"> Интеграция с Telegram
После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестовом прогоне.
<img width="40%" title="Telegram Bot" src="logo/tg_bot.png">