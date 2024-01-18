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

    cursor.execute("SELECT id_Players, name, second_Name, patronic, sex, age, specialization FROM Players")
    players = cursor.fetchall()
    for row in players:
        tree.insert("", "end", values=row)

    tree.pack(side=tk.TOP, pady=170, padx=(10, 10), anchor="center")
def create_players():

    tree = ttk.Treeview(root, columns=("id", "name", "second_Name", "patronic", "sex", "age", "specialization"), show="headings")

    tree.heading("id", text="Номер")
    tree.heading("name", text="Имя")
    tree.heading("second_Name", text="Фамилия")
    tree.heading("patronic", text="Отчество")
    tree.heading("sex", text="Пол")
    tree.heading("age", text="Возраст")
    tree.heading("specialization", text="Специализация")

    tree.pack(side=tk.TOP, padx=10, pady=10)

    registration_label = tk.Label(root, text="Форма регистрации", font=("Helvetica", 16), bg="#b1dcfc")
    registration_label.pack(side=tk.TOP, padx=10, pady=10)

    label_texts = ["Имя", "Фамилия", "Отчество", "Пол", "Возраст"]
    entries = {}

    for label_text in label_texts:
        label = tk.Label(root, text=label_text, bg="#b1dcfc")
        label.pack(side=tk.TOP, padx=10, pady=5)

        entry = ttk.Entry(root)
        entry.pack(side=tk.TOP, padx=10, pady=5)

        entries[label_text] = entry

    specialization_label = tk.Label(root, text="Специализация", bg="#b1dcfc")
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
    name = entries["Имя"].get()
    second_name = entries["Фамилия"].get()
    patronic = entries["Отчество"].get()
    sex = entries["Пол"].get()
    age = entries["Возраст"].get()
    specialization = entries["Специализация"].get()

    if not all([name, second_name, patronic, sex, age, specialization]):
        tk.messagebox.showerror("Ошибка", "Все поля формы должны быть заполнены.")
        return

    cursor.execute("INSERT INTO Players (name, second_Name, patronic, sex, age, specialization) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, second_name, patronic, sex, age, specialization))
    connection.commit()

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