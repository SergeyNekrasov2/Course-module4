# Course-module4
Курсовая работа по модулю 4.
# HeadHunter Vacancy Project
<<<<<<< HEAD
## Использование

Проект запрашивает вакансии с hh.ru и сохраняет их в формате JSON. 

### Основные классы и их функциональность:
- **`BaseApi`** - базовый класс для создания API-классов, таких, как `HeadHunterApi`.
- **`HeadHunterApi`** - отвечает за запрос вакансий с сайта hh.ru и сохранение их в файл формата JSON.
- **`BaseJsonSaver`** - базовый класс для создания классов сохранения данных, таких как `JsonSaver`.
- **`JsonSaver`** - позволяет сохранять, добавлять и удалять вакансии в/из JSON-файла.
- **`Vacancy`** - класс для создания объектов вакансий с параметрами:<br> 
`name`
`url`
`salary`
`snippet`.

Модуль `user_interaction` содержит функции для взаимодействия с классами и фильтрации вакансий.  
Взаимодействие всех классов и функций с пользователем реализовано в модуле `main.py`.
=======
## Description
Проект создан для получения актуальных вакансий, полученных из API HeadHunter.
Внутренняя функциональность позволяет фильтровать полученные вакансии по вашим предпочтениям.
## Structure
Проект состоит из папки виртуального окружения, других системных файлов, содержащих данные о зависимостях, установленных пакетах и т.д.
Также в проекте есть основная папка содержащая основной код, а в нем подразделение на папку тестов, папку с файлами для базы данных, папку с модулями, где реализованы классы для создания экземпляров вакансий, сохранения списков этих экземпляров в файлы, их добавлени и удаление.
## Using
В папке project_folder.src содержится модуль main.py, запустив который автоматически запрашиваются необходимые данные для получения актуальных вакансий, фильтрации по количеству, словам в описании, примерного уровня зарплаты.
## License
На проект распространяется MIT License. В корневой директори содержится файл LICENSE, с которым можно ознакомится.

