# Генерация SBOM (Software Bill of Materials)

## Установка cyclonedx-py

1. Установите cyclonedx-py с помощью pip:
   ```bash
   pip install cyclonedx-py
   ```

2. Убедитесь, что инструмент установлен:
   ```bash
   cyclonedx-py --version
   ```

## Генерация SBOM для Python проекта

### Базовая генерация SBOM

Выполните команду в корневой директории проекта:
```bash
cyclonedx-py --format json --output sbom.json
```

### Расширенная генерация SBOM с дополнительной информацией

```bash
cyclonedx-py \
  --format json \
  --output sbom.json \
  --include-license-text \
  --include-file-hashes \
  --include-component-type \
  --include-component-scope
```

### Анализ конкретного файла или директории

Для анализа конкретного файла:
```bash
cyclonedx-py --format json --output sbom.json --source app.py
```

Для анализа всей директории проекта:
```bash
cyclonedx-py --format json --output sbom.json --source .
```

## Параметры командной строки

- `--format json`: Формат вывода (JSON)
- `--output <filename>`: Имя выходного файла
- `--include-license-text`: Включить текст лицензий
- `--include-file-hashes`: Включить хэши файлов
- `--include-component-type`: Включить тип компонента
- `--include-component-scope`: Включить область компонента
- `--source <path>`: Путь к анализируемому файлу или директории

## Примеры использования

### 1. Быстрая генерация базового SBOM
```bash
cyclonedx-py --format json --output quick-sbom.json
```

### 2. Генерация подробного SBOM с хэшами
```bash
cyclonedx-py \
  --format json \
  --output detailed-sbom.json \
  --include-file-hashes \
  --include-license-text
```

### 3. Генерация SBOM для конкретной зависимости
```bash
cyclonedx-py \
  --format json \
  --output dependency-sbom.json \
  --source requirements.txt
```

## Интерпретация результатов

Сгенерированный SBOM файл будет содержать:

- **metadata**: Метаданные о проекте
- **components**: Список компонентов (зависимостей)
- **dependencies**: Зависимости между компонентами
- **externalReferences**: Внешние ссылки
- **properties**: Дополнительные свойства

## Интеграция с Dependency-Track

1. Сгенерируйте SBOM файл:
   ```bash
   cyclonedx-py --format json --output sbom.json
   ```

2. Загрузите SBOM в Dependency-Track:
   - Откройте веб-интерфейс Dependency-Track
   - Перейдите в раздел "Projects"
   - Создайте новый проект
   - Загрузите sbom.json файл через интерфейс

## Устранение неполадок

### Ошибка "No dependencies found"
Убедитесь, что вы находитесь в директории Python проекта с файлом requirements.txt или setup.py.

### Ошибка "Permission denied"
Запустите команду с правами администратора или убедитесь, что у вас есть доступ на запись в директорию.

### Проверка сгенерированного SBOM
```bash
# Проверка JSON синтаксиса
python -m json.tool sbom.json

# Проверка структуры CycloneDX
cyclonedx-py validate --input sbom.json
```