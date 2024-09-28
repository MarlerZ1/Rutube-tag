# ЦИФРОВОЙ ПРОРЫВ. СЕЗОН ИИ. Генерация тегов для видео
# Команда Ботики
#### Анна Сазонова
#### Кирилл Мерзляков
#### Андрей Гуськов
#### Ева Демина
## Описание проекта
Данный проект представляет собой систему автоматического тегирования видео на основе их _названия_, _описания_, а также _аудио/видеоряда_. Система использует список тегов, предоставленный Rutube, который охватывает широкий спектр тем и подтем, чтобы обеспечить точное и эффективное тегирование видео.
## Принцип работы системы

1. Загрузка видео: Пользователь загружает видео, которое необходимо проставить тегами.

    1.2 Анализ аудиоряда:
Audios данные извлекаются и анализируются с помощью Whisper.
Полученный текст суммаризируется для последущей обработки моделью ruBERT и формирования тегов. Путь до файла обучения модели ... Обученная модель .....

    1.3 Анализ видеоряда:
Видеоряд анализируется с использованием BLIP. Полученный текст переводится на русский с помощью модели Helsinki.
Краткие описания создаются с помощью BART. Текст поступает на модель ruBERT для получения тегов. Путь до файла обучения модели ... Обученная модель ...
2. Получение названия и описания.

   RuBERT генерирует релевантные теги на основе названия и описания. Путь до файла обучения модели ... Обученная модель ...
3. Получение финальных тегов.

   Поскольку каждый тег имеет собственную метрику, они отсортировываются в порядке убывания. Повторяющиеся теги усредняются. Благодаря сортировке выводятся наиболее релевантые теги.

## Запуск системы
Данное руководство написано под систему Windows. Запуск докера и консоли на других системах может отличаться.

1. Перейти в папку Rutube_hack
2. Скачать архив по ссылке: https://drive.google.com/file/d/1esmbAqQL0acdllcBXRx0R32d6k0o5-gM/view
3. Выгрузить папку "saved_models" из скачанного архива в открытую папку Rutube_hack вместе со всем содержимым. Иерархия проекта должна быть такой:
   - Корень проекта
       - прочие файлы и папки
       - FrontVseRos
       - Rutube_hack
           - прочие файлы и папки
           - Rutube_hack
           - saved_model  <- скачанная папка
4. Перейти корень проекта, открыть в нем консоль CMD
5. Выполнить консольную команду docker compose up. Важно, для выполнения этой команды должен быть установлен и запущен Docker Desktop, включена виртуализация. После запуска команды начнется процесс сборки. Он может занять около часа. При сборке проекта пропадет возможность вводить команды в это окно консоли. Пока она снова не появится, закрывать консоль нельзя.
6. После успешной сборки проекта появится возможность снова писать текст в окно консоли. Нужно вписать команду docker compose run. Проект запустится. Консоль нельзя закрывать до тех пор, пока проект не будет протестирован.
7. В браузере перейти по адресу: http://127.0.0.1:8501/
8. После тестирования проекта можно закрыть консоль.
