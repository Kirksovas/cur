Перед запуском со стороны пользователя на его персональном компьютере или ноутбуке должен быть установлено следующие программное обеспечение:
Python 3.10 и выше при необходимости.
Также для корректной работы следует проверить установлены ли следующие библиотеки:
1) pip;
2) tkinter;
3) customtkinter;
4) Pillow;
5) sqlite;
6) pyinstaller.
Если одна или несколько библиотек отсутствует или не работают, то ниже представлены команды для установки, которые надо вводит в командную строку (cmd), внутри папки с продуктом.

Библиотека pip, должна автоматически быть установлена с python. Если pip уже установлен, вы можете обновить его до последней версии. 
Введите следующую команду в командной строке или терминале:
python -m pip install --upgrade pip

Библиотека tkinter, как и pip, устанавливаются автоматически. Для проверки наличия tkinter:
Откройте командную строку (Command Prompt) и введите:
python -m tkinter
Если у вас уже установлен Python, вы можете обновить его до последней версии:
pip install --upgrade python

Установека сторонней библиотеки customtkinter:
pip install customtkinter / python pip install customtkinter (возможны расхождения в зависимости от версии Python).
Обновление библиотеки customtkinter:
pip install customtkinter --upgrade / python pip install customtkinter --upgrade (возможны расхождения в зависимости от версии Python).

Для установки библиотеки Pillow, вы можете использовать pip. 
Откройте командную строку (Command Prompt) и выполните следующую команду:
pip install Pillow / python pip install Pillow (возможны расхождения в зависимости от версии Python).

Библиотека SQLite входит в стандартную библиотеку Python, и обычно нет необходимости устанавливать ее отдельно. 
Она включена в распространенные дистрибутивы Python. Но если есть какие-то проблемы, то откройте командную строку (Command Prompt) и выполните следующую команду:
pip install sqlite / python pip install sqlite (возможны расхождения в зависимости от версии Python).

Установка PyInstaller:
Выполните команду в командной строке (если вы используете pip):
pip install pyinstaller / python pip install pyinstaller (возможны расхождения в зависимости от версии Python).

После проверки наличия нужных библиотек, их установки или обновления, можно без проблем запускать exe файл (расположенный в \cur\dist\main) и пользоваться программой.

В случае запуска программы со стороны разработчка, то также стоит установить следующее программное обеспечение:
1) Visual Studio Code / Pycharm или иные среды разработки;
2) SQLite версии 3.12.2 и выше.

После проверки наличия нужных библиотек, их установки или обновления, а также установки нужного программного обсепечения,
можно без проблем запускать exe файл (расположенный в \cur\dist\main) и пользоваться программой или же открывать проект в вашей среде разработки и осуществлять все необходимые изменения.



