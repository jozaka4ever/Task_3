# Task_3 — веб-тесты Stellar Burgers

Кроссбраузерные UI-тесты учебного сервиса Stellar Burgers:
`https://qa-stellarburgers.education-services.ru/`.

## Покрытие

- восстановление пароля;
- личный кабинет, история заказов и выход;
- навигация между конструктором и лентой заказов;
- модальные окна ингредиента и заказа;
- добавление ингредиентов и оформление заказа;
- отображение заказа в истории, общей ленте и списке «В работе»;
- обновление счётчиков выполненных заказов.

Все 17 сценариев автоматически запускаются в Google Chrome и Mozilla Firefox.
Пользователи создаются через API перед тестами и удаляются после них.

## Структура

```text
Task_3/
├── api/                 # API-клиент для тестовых пользователей
├── locators/            # отдельный набор локаторов для каждого Page Object
├── pages/               # Page Object Model
├── tests/               # тесты по функциональным областям
├── allure_results/      # результаты последнего запуска Allure
├── config.py
├── conftest.py
├── data.py
├── pytest.ini
├── requirements.txt
├── texts.py
└── urls.py
```

## Запуск

Нужен Python 3.10 или новее, а также установленные Chrome и Firefox.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest
```

Запуск только одного браузера:

```bash
pytest -k chrome
pytest -k firefox
```

Результаты Allure создаются автоматически в `allure_results`.

```bash
allure serve allure_results
```
