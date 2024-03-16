import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import tkinter.messagebox as tkmessagebox
from PIL import ImageTk, Image
import sqlite3
import re

connection = sqlite3.connect('db/games.db')
cursor = connection.cursor()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def create_content(button_text):
    clear_window()
    label = ctk.CTkLabel(root, text=button_text, font=("Helvetica", 16))
    label.pack(pady=20)

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
    NewsCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    NewsCanva.pack(fill=tk.X, pady=0)

    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"

    frame1 = tk.Frame(NewsCanva, bg="#4F9BE1", bd=0)
    frame1.pack(side=tk.LEFT, padx=10, pady=40)

    titleNews1 = tk.Label(frame1, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack()

    descNews1 = tk.Text(frame1, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack()

    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    image_label1 = ctk.CTkLabel(master=NewsCanva, image=new1, text="")
    image_label1.pack(side=tk.RIGHT, padx=40)

    NewsCanva2 = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    NewsCanva2.pack(fill=tk.X, pady=10)

    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = "2"')
    result = cursor.fetchone()

    if result:
        titleNews2_text, descNews2_text = result
    else:
        titleNews2_text = "Заголовок не найден"
        descNews2_text = "Описание не найдено"

    frame2 = tk.Frame(NewsCanva2, bg="#4F9BE1", bd=0)
    frame2.pack(side=tk.LEFT, padx=10, pady=40)

    titleNews2 = tk.Label(frame2, text=titleNews2_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews2.pack()

    descNews2 = tk.Text(frame2, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews2.insert(tk.END, descNews2_text)
    descNews2.configure(state="disabled", bd=0, highlightthickness=0)
    descNews2.pack()

    new2 = ctk.CTkImage(light_image=Image.open("image/Group_253.png"), size=(250, 250))
    image_label2 = ctk.CTkLabel(master=NewsCanva2, image=new2, text="")
    image_label2.pack(side=tk.RIGHT, padx=40)

def create_shed():
    ShedCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    ShedCanva.pack(fill=tk.X, pady=0)

    screen_width = root.winfo_screenwidth()

    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"

    frame1 = tk.Frame(ShedCanva, bg="#4F9BE1", bd=0)
    frame1.pack(side=tk.LEFT, padx=10, pady=40)

    titleNews1 = tk.Label(frame1, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack(padx=5, pady=50)

    descNews1 = tk.Text(frame1, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack()

    cursor.execute('SELECT date, time FROM Schedule WHERE id_New = 1')
    result = cursor.fetchone()

    if result:
        date1_text, time1_text = result
    else:
        date1_text = "Дата не найдена"
        time1_text = "Время не найдено"

    dateNews1 = tk.Label(ShedCanva, text=date1_text, font=("Helvetica", 20), bg="#4F9BE1")
    dateNews1.pack(pady=5)

    time1 = tk.Label(ShedCanva, text=time1_text, font=("Helvetica", 20), bg="#4F9BE1")
    time1.pack()

    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    image_label1 = ctk.CTkLabel(master=ShedCanva, image=new1, text="")
    

    image_position1 = min(screen_width - 90 - 50, 50)
    
    image_label1.pack(side=tk.RIGHT, padx=image_position1, pady=10) 

    ShedCanva2 = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    ShedCanva2.pack(fill=tk.X, pady=10)

    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = "2"')
    result = cursor.fetchone()

    if result:
        titleNews2_text, descNews2_text = result
    else:
        titleNews2_text = "Заголовок не найден"
        descNews2_text = "Описание не найдено"

    frame2 = tk.Frame(ShedCanva2, bg="#4F9BE1", bd=0)
    frame2.pack(side=tk.LEFT, padx=10, pady=40)

    titleNews2 = tk.Label(frame2, text=titleNews2_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews2.pack()

    descNews2 = tk.Text(frame2, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1", bd=0)
    descNews2.insert(tk.END, descNews2_text)
    descNews2.configure(state="disabled", bd=0, highlightthickness=0)
    descNews2.pack()

    cursor.execute('SELECT date, time FROM Schedule WHERE id_New = 2')
    result = cursor.fetchone()

    if result:
        date2_text, time2_text = result
    else:
        date2_text = "Дата не найдена"
        time2_text = "Время не найдено"

    dateNews2 = tk.Label(ShedCanva2, text=date2_text, font=("Helvetica", 20), bg="#4F9BE1")
    dateNews2.pack(pady=5)

    time2 = tk.Label(ShedCanva2, text=time2_text, font=("Helvetica", 20), bg="#4F9BE1")
    time2.pack()

    new2 = ctk.CTkImage(light_image=Image.open("image/Group_253.png"), size=(250, 250))
    image_label2 = ctk.CTkLabel(master=ShedCanva2, image=new2, text="")
    
    image_position2 = min(screen_width - 10 - 50, 50)
    
    image_label2.pack(side=tk.RIGHT, padx=image_position2, pady=10) 
def create_adress():
    adressCanva = ctk.CTkCanvas(root, width=500, height=300, bg="#4F9BE1")
    adressCanva.pack(fill=tk.X, pady=0)

    cursor.execute('SELECT title_New, desc_new FROM New WHERE id_New = 1')
    result = cursor.fetchone()

    if result:
        titleNews1_text, descNews1_text = result
    else:
        titleNews1_text = "Заголовок не найден"
        descNews1_text = "Описание не найдено"

    new1 = ctk.CTkImage(light_image=Image.open("image/Group_252.png"), size=(250, 250))
    new1_label = ctk.CTkLabel(master=adressCanva, image=new1, text="")
    new1_label.pack(side=tk.RIGHT, padx=60, pady=40)
    
    titleNews1 = tk.Label(adressCanva, text=titleNews1_text, font=("Helvetica", 20), bg="#4F9BE1")
    titleNews1.pack(side=tk.TOP, padx=10, pady=20)

    descNews1 = tk.Text(adressCanva, font=("Helvetica", 20), wrap="word", width=60, height=5, bg="#4F9BE1")
    descNews1.insert(tk.END, descNews1_text)
    descNews1.configure(state="disabled", bd=0, highlightthickness=0)
    descNews1.pack(side=tk.TOP, padx=10, pady=20)

    cursor.execute('SELECT country, town, street, house_number FROM Address WHERE id_New = "1"')
    result = cursor.fetchone()

    if result:
        country_text, town_text, street_text, house_number_text = result
    else:
        country_text = "Заголовок не найден"
        town_text = "Заголовок не найден"
        street_text = "Заголовок не найден"
        house_number_text = "Заголовок не найден"


    address_label = tk.Label(adressCanva, text="Адрес:", font=("Helvetica", 20), bg="#4F9BE1")
    address_label.pack(side=tk.LEFT, padx=50, pady=20)

    countryNews1 = tk.Label(adressCanva, text=country_text, font=("Helvetica", 20), bg="#4F9BE1")
    countryNews1.pack(side=tk.LEFT, padx=30, pady=20)

    town = tk.Label(adressCanva, text=town_text, font=("Helvetica", 20), bg="#4F9BE1")
    town.pack(side=tk.LEFT, padx=30, pady=20)

    street = tk.Label(adressCanva, text=street_text, font=("Helvetica", 20), bg="#4F9BE1")
    street.pack(side=tk.LEFT, padx=30, pady=20)

    house_number = tk.Label(adressCanva, text=house_number_text, font=("Helvetica", 20), bg="#4F9BE1")
    house_number.pack(side=tk.LEFT, padx=30, pady=20)
def players():
    

    tree = ttk.Treeview(root, columns=("id", "name", "second_Name", "patronic", "sex", "age", "specialization"), show="headings")
    tree.heading("id", text="Номер")
    tree.heading("name", text="Имя")
    tree.heading("second_Name", text="Фамилия")
    tree.heading("patronic", text="Отчество")
    tree.heading("sex", text="Пол")
    tree.heading("age", text="Возраст")
    tree.heading("specialization", text="Специализация")

    def sort_tree(column_index, descending):
        column = tree["columns"][column_index]
        russian_column = column_names_dict.get(column, column)
        data = [(int(tree.set(child, column)), child) if column == "id" or column == "age" else (tree.set(child, column), child) for child in tree.get_children("")]
        data.sort(reverse=descending)
        for i, item in enumerate(data):
            tree.move(item[1], "", i)

    def on_sort(column_index, descending):
        sort_tree(column_index, descending)

    def update_columns():
        combo["values"] = russian_column_names  

    russian_column_names = [
        "Номер",
        "Имя",
        "Фамилия",
        "Отчество",
        "Пол",
        "Возраст",
        "Специализация"
    ]

    column_names_dict = {
        "id": "Номер",
        "name": "Имя",
        "second_Name": "Фамилия",
        "patronic": "Отчество",
        "sex": "Пол",
        "age": "Возраст",
        "specialization": "Специализация"
    }
    
    frame = tk.Frame(root, bg="#BAD7DF")  
    frame.pack(side=tk.TOP, pady=10)  

    combo = ttk.Combobox(frame, values=russian_column_names, state="readonly", width=15)
    combo.pack(side=tk.LEFT, padx=5)  

    def update_combobox_text(event):
        selected_column = combo.get() 
        russian_name = column_names_dict.get(selected_column, "")  
        combo.set(russian_name) 

    combo.bind("<FocusOut>", update_combobox_text)

    btn_sort_asc = tk.Button(frame, text="\u2191", command=lambda: on_sort(combo.current(), False))
    btn_sort_asc.pack(side=tk.LEFT, padx=5) 

    btn_sort_desc = tk.Button(frame, text="\u2193", command=lambda: on_sort(combo.current(), True))
    btn_sort_desc.pack(side=tk.LEFT, padx=5)

    tree.pack(side=tk.TOP, pady=10, padx=10) 

    tree.bind("<Configure>", lambda event: update_columns())

    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players_data = cursor.fetchall()
    for row in players_data:
        tree.insert("", "end", values=row)

def save_data(entries, tree):
    for key, value in entries.items():
        if key != "Отчество" and not value.get(): 
            tkmessagebox.showerror("Ошибка", f"Поле '{key}' не заполнено")
            return
    tkmessagebox.showinfo("Успех", "Данные успешно сохранены")
    for item in tree.get_children():
        tree.delete(item)


def create_players():
    tree = ttk.Treeview(root, columns=("id", "name", "second_Name", "patronic", "sex", "age", "specialization"), show="headings")
    tree.heading("id", text="Номер")
    tree.heading("name", text="Имя")
    tree.heading("second_Name", text="Фамилия")
    tree.heading("patronic", text="Отчество")
    tree.heading("sex", text="Пол")
    tree.heading("age", text="Возраст")
    tree.heading("specialization", text="Дисциплина")
    tree.pack(side=tk.TOP, padx=10, pady=10)

    registration_label = tk.Label(root, text="Форма регистрации", font=("Helvetica", 16), bg="#b1dcfc")
    registration_label.pack(side=tk.TOP, padx=10, pady=10)

    label_texts = ["Имя", "Фамилия", "Отчество"]
    entries = {}

    for label_text in label_texts:
        label = tk.Label(root, text=label_text, bg="#b1dcfc")
        label.pack(side=tk.TOP, padx=10, pady=5)

        entry = ttk.Entry(root, validate="key")
        entry.pack(side=tk.TOP, padx=10, pady=5)
        entry.config(validatecommand=(root.register(lambda P: len(P) <= 50 and P.strip() == P), '%P'))

        # Всплывающее сообщение
        Tooltip(entry, f"Максимум 50 символов для поля '{label_text}'")

        entries[label_text] = entry

    # Создание поля для ввода возраста
    age_label = tk.Label(root, text="Возраст", bg="#b1dcfc")
    age_label.pack(side=tk.TOP, padx=10, pady=5)

    age_entry = ttk.Entry(root, validate="key")
    age_entry.pack(side=tk.TOP, padx=10, pady=5)

    age_entry.config(validatecommand=(root.register(lambda P: len(P) <= 3 and P.strip() == P), '%P'))
    entries["Возраст"] = age_entry

    age_tooltip_text = "Допустимый возраст от 12 до 100 лет"
    Tooltip(age_entry, age_tooltip_text)

    # Создание чекбокса для поля "Пол"
    sex_label = tk.Label(root, text="Пол", bg="#b1dcfc")
    sex_label.pack(side=tk.TOP, padx=10, pady=5)

    sex_var = tk.StringVar(root, "Мужской")  # По умолчанию выбрано "Мужской"

    male_checkbox = tk.Radiobutton(root, text="Мужской", variable=sex_var, value="Мужской", bg="#b1dcfc")
    male_checkbox.pack(side=tk.TOP, padx=10, pady=2)

    female_checkbox = tk.Radiobutton(root, text="Женский", variable=sex_var, value="Женский", bg="#b1dcfc")
    female_checkbox.pack(side=tk.TOP, padx=10, pady=2)

    entries["Пол"] = sex_var

    specialization_label = tk.Label(root, text="Дисциплина", bg="#b1dcfc")
    specialization_label.pack(side=tk.TOP, padx=10, pady=5)

    cursor.execute("SELECT title_specialization FROM specialization")
    specialization_data = cursor.fetchall()
    specialization_options = [row[0] for row in specialization_data]

    specialization_var = tk.StringVar(root)
    specialization_var.set(specialization_options[0]) 

    specialization_menu = tk.OptionMenu(root, specialization_var, *specialization_options)
    specialization_menu.pack(side=tk.TOP, padx=10, pady=5)

    entries["Специализация"] = specialization_var

    save_button = tk.Button(root, text="Сохранить", command=lambda: save_data(entries, tree), bg="#B0E8FF", width=20, border=1)
    save_button.pack(side=tk.TOP, padx=10, pady=10)

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players = cursor.fetchall()

    for row in players:
        tree.insert("", "end", values=row)

    tree.pack_forget()

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x = self.widget.winfo_rootx() + self.widget.winfo_width()
        y = self.widget.winfo_rooty() - 20
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="#FFFFE0", relief="solid", borderwidth=1)
        label.pack(ipadx=5)

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
def create_spec():
    tree = ttk.Treeview(root)
    tree["columns"] = ("Номер", "Название", "Описание")
    
    tree.heading("Номер", text="Номер")
    tree.column("Номер", anchor="center", width=50)

    tree.heading("Название", text="Название")
    tree.column("Название", anchor="center", width=150)

    tree.heading("Описание", text="Описание")
    tree.column("Описание", anchor="center", width=1000)

    cursor.execute("SELECT id_specialization, title_specialization, desc_specialization FROM specialization")
    specialization = cursor.fetchall()
    for row in specialization:
        tree.insert("", "end", values=row)

    tree.pack( fill="both", padx=30, pady=10)  

def save_data(entries, tree):
    name = entries["Имя"].get().strip()
    second_name = entries["Фамилия"].get().strip()
    patronic = entries["Отчество"].get().strip()
    sex = entries["Пол"].get()
    age = entries["Возраст"].get().strip()
    specialization = entries["Специализация"].get()

    # Проверка на ввод цифр и спец. символов в поля имя, фамилия и отчество
    if not re.match(r'^[a-zA-Zа-яА-ЯёЁ]*$', name) or not re.match(r'^[a-zA-Zа-яА-ЯёЁ]*$', second_name) or not re.match(r'^[a-zA-Zа-яА-ЯёЁ]*$', patronic):
        tk.messagebox.showerror("Ошибка", "Имя, фамилия и отчество не должны содержать цифры или специальные символы.")
        return

    # Проверка на ввод только цифр в поле возраста
    if not age.isdigit():
        tk.messagebox.showerror("Ошибка", "Возраст должен содержать только цифры.")
        return

    # Преобразование возраста в целое число
    age = int(age)

    # Проверка на допустимый возраст
    if age < 12 or age > 100:
        tk.messagebox.showerror("Ошибка", "Извините, вы не подходите по возрасту!")
        return

    cursor.execute("SELECT MAX(id_Players) FROM Players")
    last_id = cursor.fetchone()[0]

    if last_id is None:
        last_id = 0

    new_number = last_id + 1

    cursor.execute("INSERT INTO Players (name, second_Name, patronic, sex, age, specialization) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, second_name, patronic, sex, age, specialization))
    connection.commit()

    tk.messagebox.showinfo("Успех", f"Успешная регистрация, ваш номер: {new_number}")

    for entry in entries.values():
        if isinstance(entry, tk.StringVar):
            entry.set('')
        else:
            entry.delete(0, tk.END)
    update_players_tree(tree)

    tk.messagebox.showinfo("Успех", "Вы успешно подали заявку!")

def update_players_tree(tree):
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players = cursor.fetchall()

    for row in players:
        tree.insert("", "end", values=row)
    
def initialize_menu():
    clear_window()

    BaseCanvas = ctk.CTkCanvas(root, width=500, height=150, bg="#17658F")
    BaseCanvas.pack(fill=tk.X, pady=0)

    my_image = ctk.CTkImage(light_image=Image.open("image/loll.png"), size=(110, 110))
    image_label = ctk.CTkLabel(master=BaseCanvas, image=my_image, text="")
    image_label.place(x=10, y=10)

    MenuCanvas = ctk.CTkCanvas(BaseCanvas, width=820, height=100, bg="#196E9C", highlightthickness=0, bd=0)
    MenuCanvas.place(x=500, y=45)

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
        CTkButton.pack(side=tk.LEFT, padx=10, pady=10)
        x_position += CTkButton.winfo_reqwidth() + 25

    create_news()





root = tk.Tk()
root.configure(background="#b1dcfc")
root.title("Всероссийские игры умных городов!")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

initialize_menu()

root.mainloop()

connection.close()