import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as tkmessagebox
from PIL import ImageTk, Image
import sqlite3

connection = sqlite3.connect('db/games.db')
cursor = connection.cursor()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def create_content(button_text):
    clear_window()
    # Создаем лейбл с названием кнопки
    label = ctk.CTkLabel(root, text=button_text, font=("Helvetica", 16))
    label.pack(pady=20)

    # Создаем кнопку для возврата в начальное окно
    return_button = ctk.CTkButton(root, text="Назад", command=initialize_menu)
    return_button.place(x=10, y=10)

    if button_text == "Дата проведения":
        create_shed()
    elif button_text == "Участники":
        players()
    elif button_text == "Место проведения":
        create_adress()
    elif button_text == "Дисциплины":
        create_spec()
    elif button_text == "Подать заявку":
        create_players()

def create_news():
    # Создаем основной прямоугольник
    NewsCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    NewsCanva.pack(fill=tk.X, pady=0)

    # Выполняем запрос к базе данных
    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"

    # Создаем Frame для текста и изображения
    frame1 = tk.Frame(NewsCanva, bg="#4F9BE1", bd=0)
    frame1.pack(side=tk.LEFT, padx=10, pady=40)

    # Создаем лейбл с заголовком
    titleNews1 = tk.Label(frame1, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack()

    # Создаем Text с описанием
    descNews1 = tk.Text(frame1, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack()

    # Загружаем изображение логотипа
    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    image_label1 = ctk.CTkLabel(master=NewsCanva, image=new1, text="")
    image_label1.pack(side=tk.RIGHT, padx=40)

    # Создаем основной прямоугольник2
    NewsCanva2 = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    NewsCanva2.pack(fill=tk.X, pady=10)

    # Выполняем запрос к базе данных
    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = "2"')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        titleNews2_text, descNews2_text = result
    else:
        titleNews2_text = "Заголовок не найден"
        descNews2_text = "Описание не найдено"

    # Создаем Frame для текста и изображения
    frame2 = tk.Frame(NewsCanva2, bg="#4F9BE1", bd=0)
    frame2.pack(side=tk.LEFT, padx=10, pady=40)

    # Создаем лейбл с заголовком
    titleNews2 = tk.Label(frame2, text=titleNews2_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews2.pack()

    # Создаем Text с описанием
    descNews2 = tk.Text(frame2, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews2.insert(tk.END, descNews2_text)
    descNews2.configure(state="disabled", bd=0, highlightthickness=0)
    descNews2.pack()

    # Загружаем изображение логотипа
    new2 = ctk.CTkImage(light_image=Image.open("image/Group_253.png"), size=(250, 250))
    image_label2 = ctk.CTkLabel(master=NewsCanva2, image=new2, text="")
    image_label2.pack(side=tk.RIGHT, padx=40)

def create_shed():
    # Создаем основной прямоугольник
    ShedCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    ShedCanva.pack(fill=tk.X, pady=0)

    # Получаем ширину экрана
    screen_width = root.winfo_screenwidth()

    # Выполняем запрос к базе данных
    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"

    # Создаем Frame для текста и изображения
    frame1 = tk.Frame(ShedCanva, bg="#4F9BE1", bd=0)
    frame1.pack(side=tk.LEFT, padx=10, pady=40)

    # Создаем лейбл с заголовком
    titleNews1 = tk.Label(frame1, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack(padx=5, pady=50)

    # Создаем Text с описанием
    descNews1 = tk.Text(frame1, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack()

    # Выполняем запрос к базе данных для расписания
    cursor.execute('SELECT date, time FROM Schedule WHERE id_New = 1')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        date1_text, time1_text = result
    else:
        date1_text = "Дата не найдена"
        time1_text = "Время не найдено"

    # Создаем лейблы с датой и временем
    dateNews1 = tk.Label(ShedCanva, text=date1_text, font=("Helvetica", 20), bg="#4F9BE1")
    dateNews1.pack(pady=5)

    time1 = tk.Label(ShedCanva, text=time1_text, font=("Helvetica", 20), bg="#4F9BE1")
    time1.pack()

    # Загружаем изображение логотипа
    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    image_label1 = ctk.CTkLabel(master=ShedCanva, image=new1, text="")
    
    # Рассчитываем позицию изображения относительно ширины экрана
    image_position1 = min(screen_width - 90 - 50, 50)
    
    image_label1.pack(side=tk.RIGHT, padx=image_position1, pady=10)  # Увеличили отступ до 10 пикселей

    # Создаем основной прямоугольник2
    ShedCanva2 = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    ShedCanva2.pack(fill=tk.X, pady=10)

    # Выполняем запрос к базе данных для второго элемента расписания
    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = "2"')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        titleNews2_text, descNews2_text = result
    else:
        titleNews2_text = "Заголовок не найден"
        descNews2_text = "Описание не найдено"

    # Создаем Frame для текста и изображения
    frame2 = tk.Frame(ShedCanva2, bg="#4F9BE1", bd=0)
    frame2.pack(side=tk.LEFT, padx=10, pady=40)

    # Создаем лейбл с заголовком
    titleNews2 = tk.Label(frame2, text=titleNews2_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews2.pack()

    # Создаем Text с описанием
    descNews2 = tk.Text(frame2, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews2.insert(tk.END, descNews2_text)
    descNews2.configure(state="disabled", bd=0, highlightthickness=0)
    descNews2.pack()

    # Выполняем запрос к базе данных для второго элемента расписания
    cursor.execute('SELECT date, time FROM Schedule WHERE id_New = 2')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        date2_text, time2_text = result
    else:
        date2_text = "Дата не найдена"
        time2_text = "Время не найдено"

    # Создаем лейблы с датой и временем
    dateNews2 = tk.Label(ShedCanva2, text=date2_text, font=("Helvetica", 20), bg="#4F9BE1")
    dateNews2.pack(pady=5)

    time2 = tk.Label(ShedCanva2, text=time2_text, font=("Helvetica", 20), bg="#4F9BE1")
    time2.pack()

    # Загружаем изображение логотипа
    new2 = ctk.CTkImage(light_image=Image.open("image/Group_253.png"), size=(250, 250))
    image_label2 = ctk.CTkLabel(master=ShedCanva2, image=new2, text="")
    
    # Рассчитываем позицию изображения относительно ширины экрана
    image_position2 = min(screen_width - 10 - 50, 50)
    
    image_label2.pack(side=tk.RIGHT, padx=image_position2, pady=10)  # Увеличили отступ до 10 пикселей
def create_adress():
    # Создаем основной прямоугольник
    adressCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    adressCanva.pack(fill=tk.X, pady=0)

    # Выполняем запрос к базе данных
    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    # Проверяем, есть ли данные
    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"
        
    # Загружаем изображение логотипа
    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    new1_label = ctk.CTkLabel(master=adressCanva, image=new1, text="")
    new1_label.pack(side=tk.RIGHT, padx=60, pady=40)
    
    # Создаем лейбл с заголовком
    titleNews1 = tk.Label(adressCanva, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack(side=tk.TOP, padx=10, pady=20)

    # Создаем Text с описанием
    descNews1 = tk.Text(adressCanva, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1")
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack(side=tk.TOP, padx=10, pady=20)

    cursor.execute('SELECT country, town, street, house_number FROM Address WHERE id_New = "1"')
    result = cursor.fetchone()
    # Проверяем, есть ли данные
    if result:
        country_text, town_text, street_text, house_number_text = result
    else:
        country_text = "Заголовок не найден"
        town_text = "Заголовок не найден"
        street_text = "Заголовок не найден"
        house_number_text = "Заголовок не найден"

    # Создаем лейбл "Адрес:"
    address_label = tk.Label(adressCanva, text="Адрес:", font=("Helvetica", 20), bg="#4F9BE1")
    address_label.pack(side=tk.LEFT, padx=50, pady=20)

    # Создаем лейблы с заголовком
    countryNews1 = tk.Label(adressCanva, text=country_text, font=("Helvetica", 20), bg="#4F9BE1")
    countryNews1.pack(side=tk.LEFT, padx=30, pady=20)

    town = tk.Label(adressCanva, text=town_text, font=("Helvetica", 20), bg="#4F9BE1")
    town.pack(side=tk.LEFT, padx=30, pady=20)

    street = tk.Label(adressCanva, text=street_text, font=("Helvetica", 20), bg="#4F9BE1")
    street.pack(side=tk.LEFT, padx=30, pady=20)

    house_number = tk.Label(adressCanva, text=house_number_text, font=("Helvetica", 20), bg="#4F9BE1")
    house_number.pack(side=tk.LEFT, padx=30, pady=20)

def players():
    # Создание виджета Treeview
    tree = ttk.Treeview(root, columns=("id", "name", "second_Name", "patronic", "sex", "age", "specialization"), show="headings")

    # Установка заголовков столбцов
    tree.heading("id", text="Номер")
    tree.heading("name", text="Имя")
    tree.heading("second_Name", text="Фамилия")
    tree.heading("patronic", text="Отчество")
    tree.heading("sex", text="Пол")
    tree.heading("age", text="Возраст")
    tree.heading("specialization", text="Специализация")

    # Получение данных из базы данных и добавление их в таблицу
    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players = cursor.fetchall()
    for row in players:
        tree.insert("", "end", values=row)

    # Размещение виджета Treeview в центре окна
    tree.pack(side=tk.TOP, pady=170, padx=(10, 10), anchor="center")
def create_players():
    # Создание виджета Treeview
    tree = ttk.Treeview(root, columns=("id", "name", "second_Name", "patronic", "sex", "age", "specialization"), show="headings")

    # Установка заголовков столбцов
    tree.heading("id", text="Номер")
    tree.heading("name", text="Имя")
    tree.heading("second_Name", text="Фамилия")
    tree.heading("patronic", text="Отчество")
    tree.heading("sex", text="Пол")
    tree.heading("age", text="Возраст")
    tree.heading("specialization", text="Специализация")

    # Размещение виджета Treeview в центре окна с использованием pack
    tree.pack(side=tk.TOP, padx=10, pady=10)

    # Добавляем лейбл "Форма регистрации"
    registration_label = tk.Label(root, text="Форма регистрации", font=("Helvetica", 16))
    registration_label.pack(side=tk.TOP, padx=10, pady=10)

    # Добавляем форму регистрации игрока
    label_texts = ["Имя", "Фамилия", "Отчество", "Пол", "Возраст", "Специализация"]
    entries = {}

    for label_text in label_texts:
        label = tk.Label(root, text=label_text)
        label.pack(side=tk.TOP, padx=10, pady=5)

        entry = ttk.Entry(root)
        entry.pack(side=tk.TOP, padx=10, pady=5)

        entries[label_text] = entry

    # Создание кнопки для сохранения данных
    save_button = tk.Button(root, text="Сохранить", command=lambda: save_data(entries, tree))
    save_button.pack(side=tk.TOP, padx=10, pady=10)

    for item in tree.get_children():
        tree.delete(item)

    # Получаем обновленные данные из базы данных
    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players = cursor.fetchall()

    # Вставляем новые данные в Treeview
    for row in players:
        tree.insert("", "end", values=row)

def create_spec():
    # Создание Treeview
    tree = ttk.Treeview(root)
    tree["columns"] = ("Номер", "Название", "Описание")
    
    tree.heading("Номер", text="Номер")
    tree.column("Номер", anchor="center", width=50)

    tree.heading("Название", text="Название")
    tree.column("Название", anchor="center", width=150)

    tree.heading("Описание", text="Описание")
    tree.column("Описание", anchor="center", width=1000)

    # Пример данных (замените этот блок кода на ваш запрос к базе данных)
    cursor.execute("SELECT id_specialization, title_specialization, desc_specialization FROM specialization")
    specialization = cursor.fetchall()
    for row in specialization:
        tree.insert("", "end", values=row)

    # Размещение виджета Treeview в центре окна
    tree.pack( fill="both", padx=30, pady=10)  

def save_data(entries, tree):
    try:
        # Получаем значения из полей
        name_value = entries["Имя"].get()
        last_name_value = entries["Фамилия"].get()
        patronic_value = entries["Отчество"].get()
        sex_value = entries["Пол"].get().capitalize()
        age_value = entries["Возраст"].get()
        spec_value = entries["Специализация"].get()

        # Выводим значения для отладки
        print(f"Имя: {name_value}")
        print(f"Фамилия: {last_name_value}")
        print(f"Отчество: {patronic_value}")
        print(f"Пол: {sex_value}")
        print(f"Возраст: {age_value}")
        print(f"Специализация: {spec_value}")

        # Вставляем данные в таблицу Players
        cursor.execute('''
            INSERT INTO Players (name, second_Name, patronic, sex, age, specialization)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name_value, last_name_value, patronic_value, sex_value, age_value, spec_value))

        # Сохраняем изменения в базе данных
        connection.commit()
        # Печатаем успешное сообщение
        print("Данные успешно вставлены в базу данных.")
        update_players_tree(tree)

        # Очищаем поля ввода после добавления
        for entry in entries.values():
            entry.delete(0, tk.END)

        # Уведомление об успешной регистрации
        tk.messagebox.showinfo("Успешная регистрация", "Вы успешно зарегистрированы!")

    except Exception as e:
        # Выводим сообщение об ошибке
        print(f"Произошла ошибка при вставке данных: {e}")

def initialize_menu():
    clear_window()

    # Создаем основной прямоугольник
    BaseCanvas = ctk.CTkCanvas(root, width=500, height=150, bg="#17658F")
    BaseCanvas.pack(fill=tk.X, pady=0)

    # Создаем меню прямоугольник
    MenuCanvas = ctk.CTkCanvas(BaseCanvas, width=820, height=100, bg="#196E9C", highlightthickness=0, bd=0)
    MenuCanvas.pack(fill=tk.X, pady=50)

    # Налагаем MenuCanvas на BaseCanvas
    BaseCanvas.create_window(600, 40, anchor=tk.NW, window=MenuCanvas)

    # Загружаем изображение логотипа
    my_image = ctk.CTkImage(light_image=Image.open("image/loll.png"), size=(110, 110))
    image_label = ctk.CTkLabel(master=BaseCanvas, image=my_image, text="")
    image_label.place(x=10, y=10)

    # Создаем кнопки
    button_texts = [
        "Дата проведения",
        "Участники",
        "Место проведения",
        "Дисциплины",
        "Подать заявку"
    ]
    x_position = 10
    for text in button_texts:
        CTkButton = ctk.CTkButton(MenuCanvas, height=40, text=text, fg_color="#1D82B8", compound="bottom", command=lambda t=text: create_content(t))
        MenuCanvas.create_window(x_position, 50, anchor=tk.W, window=CTkButton)
        x_position += CTkButton.winfo_reqwidth() + 25
    create_news()


# Инициализация главного окна
root = ctk.CTk()
root.title("Всероссийские игры умных городов!")
# Открываем на полный экран
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Инициализация меню
initialize_menu()

root.mainloop()

# Закрытие соединения после завершения работы приложения
connection.close()