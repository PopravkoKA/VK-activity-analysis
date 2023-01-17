# VK-activity-analysis
***
I created an online status parser for the social network VK In this project. I made this for my university python course.
![image](https://user-images.githubusercontent.com/116553139/212963313-2b7381f6-848b-4ae4-b763-2b569bd380aa.png)

***
__Основные возможности скрипта__

•	Обработка и представление информации о статусе человека в течение дня

•	Обработка и представление информации о статусе активности нескольких человек

***
__Инструкция по использованию__

0. Скачать файл data.py и plot.py в директорию.

Парсер данных
1. Открыть файл data.py, указать данные для авторизации в соц. сети Vk, указать список наблюдаемых страниц в формате vk.com/id......
2. Скорректировать (если необходимо) частоту итераций и количество наблюдений.
3. После окончания работы скрипта (можете прервать скрипт до его окончания) создастся (если еще не существует) txt файл с данными о активности.
4. Можете запускать скрипт дополнять txt файлы.

Визуализация данных
1. Вы можете построить графики активности страниц за опредеделенный интервал времени.
2. Для этого вам нужно открыть файл plot.py, указать ссылки и интервал.
3. Запустить скрипт, после чего вы можете наблюдать чудесную визуализацию.

***
__Проблемы и недостатки данного проекта__

•	Проблема с входом в браузер при подключении к некоторым вайфай сетям (просит капчу). Решение – автоматический ввод капчи

•	Проблема с долгой загрузки страниц. Решение – использовать другую либу, которая не будет полностью загружать страницу, а только брать ее код.

•	Следствие из предыдущей проблемы – трудности с проходом по нескольким страницам (неточная дата получения онлайн статуса). Решение – поправить код, либо решить предыдущую проблему.

•	Проблема – стремная визуализация активности. Решение – круче не надо.
