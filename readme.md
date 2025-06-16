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
 <img width="40" title="PyCharm" src="https://upload.wikimedia.org/wikipedia/commons/1/1d/PyCharm_Icon.png">
  <img width="40" title="Python" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.png">
  <img width="40" title="Pytest" src="https://raw.githubusercontent.com/SerhiiCho/icon-pack/main/icons/pytest.png">
  <img width="40" title="Selene" src="https://raw.githubusercontent.com/yashaka/selene/master/docs/_static/selene-logo.png">
  <img width="40" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
  <img width="40" title="Jenkins" src="https://www.jenkins.io/images/logos/jenkins/jenkins.png">
  <img width="40" title="Selenoid" src="https://user-images.githubusercontent.com/ваш-id/selenoid.png">
  <img width="40" title="Allure Report" src="https://avatars.githubusercontent.com/u/68425100?s=200&v=4">
  <img width="5%" title="Telegram" src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png">
</p>

## Список проверок, реализованных в автотестах
### UI
- [x] Лендинг. Переход на https://demoqa.com/automation-practice-form
- [x] Авторизация. Успешная авторизация 

### API

- [x] Проверка успешной авторизации - POST  https://demoqa.com/Account/v1/Login   Ожидаемый статус-код: 200 OK
- [x] Проверка неуспешной авторизации (неверный пароль) POST https://demoqa.com/Account/v1/Login  Ожидаемый статус-код: 401 User not found!



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
pytest tests/ # Запуск всех тестов в проекте
```

```sh
pytest -v tests/  # Запуск всех тестов с детальным логом
```

```sh
pytest --alluredir=allure-results  # Запуск с сохранением отчёта Allure
```



## <img width="3%" title="Jenkins" src="logo/jenkins.png"> Запуск проекта в Jenkins
[Job](https://jenkins.autotests.cloud/job/Diploma_ED_2025/)

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