# Композиционный анализ ПО - Учебное задание

## Описание проекта

Данный проект реализует учебное задание по дисциплине "Организационно-правовые основы разработки программного обеспечения" на тему "Композиционный анализ ПО". Проект включает в себя:

1. Развертывание системы Dependency-Track для анализа уязвимостей
2. Разработка консольного приложения с использованием внешних зависимостей
3. Генерация SBOM (Software Bill of Materials) для анализа компонентов

## Структура проекта

```
MAI_SCA_Lab1_KKK/
├── docker-compose.yml          # Конфигурация Docker для Dependency-Track
├── dependency-track-setup.md   # Инструкция по настройке Dependency-Track
├── app.py                      # Основное приложение Hello World
├── requirements.txt            # Зависимости Python
├── setup.py                   # Настройка пакета Python
├── __init__.py                # Инициализация пакета
├── sbom-generation.md         # Инструкция по генерации SBOM
└── README.md                  # Документация проекта
```

## Этапы выполнения задания

### 1. Развертывание Dependency-Track

#### Требования
- Установленный Docker
- Docker Compose

#### Шаги развертывания

1. Перейдите в корневую директорию проекта
2. Выполните команду для запуска контейнеров:
   ```bash
   docker-compose up -d
   ```

3. Дождитесь запуска сервисов (1-2 минуты)
4. Откройте веб-браузер и перейдите по адресу: http://localhost:8080
5. Используйте данные для входа:
   - Логин: `admin`
   - Пароль: `admin`

#### Проверка работы
- Dependency-Track доступен на порту 8080
- PostgreSQL база данных доступна на порту 5432

Подробная инструкция доступна в файле [dependency-track-setup.md](dependency-track-setup.md).

### 2. Разработка программного модуля

#### Структура проекта
Проект использует стандартную структуру Python пакета с следующими компонентами:

- **app.py** - основное приложение с функциональностью Hello World
- **requirements.txt** - файл зависимостей
- **setup.py** - скрипт установки пакета
- **__init__.py** - файл инициализации пакета

#### Функциональность приложения
Приложение демонстрирует использование следующих внешних библиотек:
- **requests** (v2.31.0) - для работы с HTTP запросами
- **click** (v8.1.7) - для создания CLI интерфейса
- **colorama** (v0.4.6) - для кросс-платформенной работы с цветами

Приложение выводит:
- Информацию о версиях зависимостей
- Системную информацию
- Данные из внешнего API (JSONPlaceholder)

#### Установка зависимостей
```bash
pip install -r requirements.txt
```

#### Запуск приложения
```bash
python app.py
```

### 3. Генерация SBOM

#### Установка инструмента
```bash
pip install cyclonedx-py
```

#### Генерация SBOM
Выполните команду в корневой директории проекта:
```bash
cyclonedx-py --format json --output sbom.json
```

Для расширенного анализа:
```bash
cyclonedx-py \
  --format json \
  --output sbom.json \
  --include-license-text \
  --include-file-hashes \
  --include-component-type
```

Подробная инструкция доступна в файле [sbom-generation.md](sbom-generation.md).

### 4. Интеграция SBOM с Dependency-Track

1. Сгенерируйте SBOM файл:
   ```bash
   cyclonedx-py --format json --output sbom.json
   ```

2. Зайдите в веб-интерфейс Dependency-Track (http://localhost:8080)
3. Создайте новый проект
4. Загрузите сгенерированный sbom.json файл

## Примеры работы

### Запуск приложения
```
==================================================
  COMPOSITIONAL ANALYSIS DEMO  
==================================================

Информация о зависимостях:
Python: 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)]
Click: 8.1.7
Requests: 2.31.0
Colorama: 0.4.6

Информация о системе:
  platform: Windows
  platform_version: 10.0.19045
  python_version: 3.9.7
  architecture: AMD64

Данные из внешнего API:
  ID: 1
  Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
  Body: quia et suscipit
  ...

==================================================
  Анализ компонентов успешно завершен!  
==================================================
```

### Пример SBOM
Сгенерированный SBOM содержит информацию о всех зависимостях проекта:
- Прямые зависимости (из requirements.txt)
- Косвенные зависимости (подзависимости)
- Информацию о лицензиях
- Хэши файлов (при включении опции)

## Используемые ресурсы

### Официальная документация
- [Dependency-Track Documentation](https://dependencytrack.org/docs/)
- [CycloneDX Specification](https://cyclonedx.org/)
- [Python Package Index (PyPI)](https://pypi.org/)

### Инструменты
- [Docker](https://www.docker.com/)
- [cyclonedx-py](https://github.com/CycloneDX/cyclonedx-python)
- [requests](https://requests.readthedocs.io/)
- [click](https://click.palletsprojects.com/)
- [colorama](https://pypi.org/project/colorama/)

### Стандарты
- [CycloneDX: SBOM Standard](https://cyclonedx.org/)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [ISO/IEC 19770-2:2015](https://www.iso.org/standard/64846.html)

## Лабораторная работа

### Цель работы
Изучение методов композиционного анализа программного обеспечения с использованием современных инструментов.

### Задачи
1. Настроить среду для анализа зависимостей
2. Разработать приложение с использованием внешних библиотек
3. Сгенерировать SBOM для анализа компонентов
4. Проанализировать уязвимости с помощью Dependency-Track

### Ожидаемые результаты
- Развернутая система Dependency-Track
- Работающее приложение с внешними зависимостями
- Сгенерированный SBOM файл
- Проанализированные уязвимости компонентов

## Лицензия

Данный проект создан в образовательных целях. Все права защищены.

## Контакты

Студент: 2-й курс, 3-й институт МАИ  
Дисциплина: Организационно-правовые основы разработки ПО  
Контакт: student@mai.ru