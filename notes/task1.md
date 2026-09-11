# Poetry — шпаргалка по командам

## Установка / версия

```bash
# установка Poetry (официальный способ)
curl -sSL https://install.python-poetry.org | python3 -

# проверка версии
poetry --version

# обновление Poetry
poetry self update
```

## Управление окружением (venv)

```bash
# создать/переключить окружение на конкретный интерпретатор
poetry env use python3.12

# показать инфо о текущем окружении (путь, версия python)
poetry env info

# список всех окружений, созданных для проекта
poetry env list

# удалить конкретное окружение
poetry env remove python3.12

# удалить вообще все окружения проекта
poetry env remove --all
```

## Установка зависимостей

```bash
# установить всё из pyproject.toml (основные + группа dev)
poetry install

# установить без установки самого проекта как пакета
poetry install --no-root

# установить с дополнительной optional-группой
poetry install --with stage-model

# установить только определённые группы (без dev)
poetry install --only main

# синхронизировать окружение строго по lock-файлу (удалит лишнее)
poetry install --sync
```

## Добавление / удаление пакетов

```bash
# добавить пакет в основные зависимости
poetry add shap

# добавить с конкретной версией
poetry add "shap=^0.52.0"

# добавить в конкретную группу (например dev)
poetry add --group dev ruff

# добавить в optional-группу
poetry add --group stage-model mlflow

# удалить пакет
poetry remove shap
```

## Lock-файл

```bash
# пересоздать poetry.lock под текущий pyproject.toml
poetry lock

# проверить, что lock-файл соответствует pyproject.toml (без установки)
poetry check
```

> `poetry.lock` обязательно коммитить в git вместе с `pyproject.toml` — 
> это гарантирует одинаковые версии пакетов у всех участников команды.

## Запуск команд внутри окружения

```bash
# запустить скрипт в окружении проекта
poetry run python checklist.py

# запустить с аргументами
poetry run python script.py --arg value

# зайти в shell окружения (требует плагин в Poetry 2.x)
poetry self add poetry-plugin-shell
poetry shell
```

## Полезное для отладки

```bash
# посмотреть дерево зависимостей
poetry show --tree

# инфо о конкретном пакете
poetry show shap

# показать путь до python-интерпретатора окружения
poetry env info --path

# список установленных пакетов
poetry show
```

## Типичный workflow для этого проекта

```bash
# 1. первичная настройка
poetry env use python3.12
poetry install

# 2. кто-то добавил новую зависимость -> после git pull
poetry install

# 3. сам добавляешь зависимость
poetry add <package>
git add pyproject.toml poetry.lock
git commit -m "add <package> dependency"

# 4. проверка окружения
poetry run python -c "import numpy, pandas, sklearn, joblib, shap; print('OK')"
```