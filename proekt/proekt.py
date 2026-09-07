import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound
import time
start_time = time.time()
# Создаем главное окно
root = tk.Tk()
root.title("Категории")
root.state("zoomed")  # на весь экран

# Создаем Canvas для рисования кругов и фона
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Фон
try:
    background_image = Image.open("images/fonn.jpg").resize((root.winfo_screenwidth(), root.winfo_screenheight()),
                                                            Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")
except Exception as e:
    print(f"Ошибка загрузки изображения: {e}")

# Параметры круга
circle_diameter = 233
circle_radius = circle_diameter // 2
circle_coords = [(200, 200), (800, 200), (1400, 200), (500, 500), (1230, 500)]
labels = ["Цвета", "Живые существа", "Съедобное", "Части тела", "Разное"]


def play_sound(sound_file):
    try:
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)  # Воспроизведение WAV файла
    except Exception as e:
        print(f"Ошибка воспроизведения звука: {e}")


# Функция для открытия окна с изображением и звуком
def open_creature_image_with_sound(image_path, sound_path, title):
    creature_image_window = tk.Toplevel(root)
    creature_image_window.title(title)
    creature_image_window.geometry(
        "644x556+{}+{}".format((root.winfo_screenwidth() - 644) // 2, (root.winfo_screenheight() - 556) // 2))

    try:
        image = Image.open(image_path).resize((644, 516), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(creature_image_window, image=photo)
        label.image = photo
        label.pack()

        tk.Button(creature_image_window, text="Прослушать", font=("Comic Sans MS", 14), bg='#BFEFFF',
                  command=lambda: play_sound(sound_path)).place(x=246, y=500)
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")


# Функция для открытия формы "Цвета" с цветными панелями
def open_colors_window():
    colors_window = tk.Toplevel(root)
    colors_window.title("Цвета")
    colors_window.geometry(
        "817x633+{}+{}".format((root.winfo_screenwidth() - 817) // 2, (root.winfo_screenheight() - 633) // 2))
    colors_window.configure(bg='white')

    # Рисуем круг для формы
    canvas = tk.Canvas(colors_window, width=817, height=633, bg='lightblue', highlightthickness=0)
    canvas.pack()
    canvas.create_oval(0, 0, 817, 633, fill='white', outline='')

    # Цвета панелей, их изображения и звуки
    colors = ["red", "yellow", "green", "blue", "pink", "white", "black"]
    image_paths = ["images/красный.png", "images/желтый.png", "images/зеленый.png", "images/синий.png",
                   "images/розовый.png", "images/белый.png", "images/черный.png"]
    sound_paths = ["sounds/red.wav", "sounds/yellow.wav", "sounds/green.wav", "sounds/blue.wav",
                   "sounds/pink.wav", "sounds/white.wav", "sounds/black.wav"]
    panel_positions = [(120, 100), (344, 100), (568, 100), (120, 256), (344, 256), (568, 256), (344, 412)]

    # Добавление цветных панелей с черной обводкой и событием открытия изо-бражения
    for i, pos in enumerate(panel_positions):
        panel = tk.Frame(colors_window, bg=colors[i], width=137, height=89)
        panel.place(x=pos[0], y=pos[1])
        canvas.create_rectangle(pos[0], pos[1], pos[0] + 137, pos[1] + 89, outline='black', width=2)
        # Привязываем событие нажатия к каждой панели
        panel.bind("<Button-1>", lambda event, img=image_paths[i],
                   snd=sound_paths[i]:  open_creature_image_with_sound(img, snd, colors[i]))

    tk.Button(colors_window, text="Выход", command=colors_window.destroy, font=("Comic Sans MS", 12),
                            height=1, width=10, bg='white', fg='black').place(x=355, y=540)


# Функция для открытия формы "Живые существа"
def open_creatures_window():
    creatures_window = tk.Toplevel(root)
    creatures_window.title("Живые существа")
    creatures_window.geometry(
        "817x633+{}+{}".format((root.winfo_screenwidth() - 817) // 2, (root.winfo_screenheight() - 633) // 2))
    creatures_window.configure(bg='white')

    # Рисуем круг для формы
    canvas = tk.Canvas(creatures_window, width=817, height=633, bg='lightblue', highlightthickness=0)
    canvas.pack()
    canvas.create_oval(0, 0, 817, 633, fill='white', outline='')

    creature_data = [
        ("images/sheep.png", "images/овечка.png", "sounds/sheep.wav", "Овца"),
        ("images/обезьяна.png", "images/обезьянка.png", "sounds/monkey.wav", "Обезьяна"),
        ("images/орел.png", "images/орелл.png", "sounds/eagle.wav", "Орёл"),
        ("images/рыба.png", "images/рыбка.png", "sounds/fish.wav", "Рыба")]
    positions = [(120, 128), (344, 128), (552, 128), (344, 304)]

    for i, (image_path, display_path, sound_path, title) in enumerate(creature_data):
        try:
            image = Image.open(image_path).resize((169, 145), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(creatures_window, image=photo, bg='white', bd=0, highlightthickness=0)
            label.image = photo
            label.place(x=positions[i][0], y=positions[i][1])
            label.bind("<Button-1>", lambda event, path=display_path, sound=sound_path,
                       title=title: open_creature_image_with_sound(path, sound, title))
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")

    tk.Button(creatures_window, text="Выход", command=creatures_window.destroy,font=("Comic Sans MS", 12), height=1,
              width=10, bg='white', fg='black').place(x=376, y=480)


# Функция для открытия формы "Съедобное"
def open_edible_window():
    edible_window = tk.Toplevel(root)
    edible_window.title("Съедобное")
    edible_window.geometry(
        "817x633+{}+{}".format((root.winfo_screenwidth() - 817) // 2, (root.winfo_screenheight() - 633) // 2))
    edible_window.configure(bg='white')

    # Рисуем круг для формы
    canvas = tk.Canvas(edible_window, width=817, height=633, bg='lightblue', highlightthickness=0)
    canvas.pack()
    canvas.create_oval(0, 0, 817, 633, fill='white', outline='')

    edible_data = [
        ("images/свекла.png", "images/свеклаа.png", "sounds/beet.wav", "Свекла"),
        ("images/морковь.png", "images/морковка.png", "sounds/carrot.wav", "Морковь"),
        ("images/ягода.png", "images/ягодка.png", "sounds/berry.wav", "Ягода"),
        ("images/гриб.png", "images/грибок.png", "sounds/mushroom.wav", "Гриб")]
    positions = [(120, 128), (344, 128), (552, 128), (344, 304)]

    for i, (image_path, display_path, sound_path, title) in enumerate(edible_data):
        image = Image.open(image_path).resize((169, 145), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(edible_window, image=photo, bg='white', bd=0, highlightthickness=0)
        label.image = photo
        label.place(x=positions[i][0], y=positions[i][1])
        label.bind("<Button-1>", lambda event, path=display_path, sound=sound_path,
                   title=title: open_creature_image_with_sound(path, sound, title))

    tk.Button(edible_window, text="Выход", command=edible_window.destroy, font=("Comic Sans MS", 12), height=1,
              width=10, bg='white', fg='black').place(x=376, y=480)


# Функция для открытия формы "Части тела"
def open_body_parts_window():
    body_parts_window = tk.Toplevel(root)
    body_parts_window.title("Части тела")
    body_parts_window.geometry(
        "817x633+{}+{}".format((root.winfo_screenwidth() - 817) // 2, (root.winfo_screenheight() - 633) // 2))
    body_parts_window.configure(bg='white')

    canvas = tk.Canvas(body_parts_window, width=817, height=633, bg='lightblue', highlightthickness=0)
    canvas.pack()
    canvas.create_oval(0, 0, 817, 633, fill='white', outline='')

    body_parts_data = [
        ("images/щека.png", "images/щекаа.png", "sounds/cheek.wav", "Щека"),
        ("images/подбородок.png", "images/подбородокк.png", "sounds/chin.wav", "Подбородок"),
        ("images/глаз.png", "images/глазз.png", "sounds/eye.wav", "Глаз"),
        ("images/колено.png", "images/коленоо.png", "sounds/knee.wav", "Колено")]
    positions = [(120, 128), (344, 128), (552, 128), (344, 304)]

    for i, (image_path, display_path, sound_path, title) in enumerate(body_parts_data):
        image = Image.open(image_path).resize((169, 145), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(body_parts_window, image=photo, bg='white', bd=0, highlightthickness=0)
        label.image = photo
        label.place(x=positions[i][0], y=positions[i][1])
        label.bind("<Button-1>", lambda event, path=display_path, sound=sound_path,
                   title=title: open_creature_image_with_sound(path, sound, title))

    tk.Button(body_parts_window, text="Выход", command=body_parts_window.destroy, font=("Comic Sans MS", 12), height=1,
              width=10, bg='white', fg='black').place(x=376, y=480)


# Функция для открытия формы "Разное"
def open_various_window():
    various_window = tk.Toplevel(root)
    various_window.title("Разное")
    various_window.geometry(
        "817x633+{}+{}".format((root.winfo_screenwidth() - 817) // 2, (root.winfo_screenheight() - 633) // 2))
    various_window.configure(bg='white')

    canvas = tk.Canvas(various_window, width=817, height=633, bg='lightblue', highlightthickness=0)
    canvas.pack()
    canvas.create_oval(0, 0, 817, 633, fill='white', outline='')

    various_data = [
        ("images/песок.png", "images/песокк.png", "sounds/sand.wav", "Песок"),
        ("images/сердце.png", "images/сердцее.png", "sounds/heart.wav", "Сердце"),
        ("images/пальто.png", "images/котт.png", "sounds/coat.wav", "Пальто"),
        ("images/чай.png", "images/тигрр.png", "sounds/tea.wav", "Чай"),
        ("images/кукла.png", "images/куклаа.png", "sounds/doll.wav", "Кукла"),
        ("images/свисток.png", "images/свистокк.png", "sounds/whistle.wav", "Свисток")]
    positions = [(120, 100), (344, 100), (552, 100), (120, 280), (344, 280), (552, 280)]

    for i, (image_path, display_path, sound_path, title) in enumerate(various_data):
        image = Image.open(image_path).resize((169, 145), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(various_window, image=photo, bg='white', bd=0, highlightthickness=0)
        label.image = photo
        label.place(x=positions[i][0], y=positions[i][1])
        label.bind("<Button-1>",lambda event, path=display_path, sound=sound_path,
                   title=title: open_creature_image_with_sound(path, sound, title))

    tk.Button(various_window, text="Выход", command=various_window.destroy, font=("Comic Sans MS", 12), height=1,
              width=10, bg='white', fg='black').place(x=373, y=480)


# Функция для проверки знаний
def open_knowledge_check_window():
    check_window = tk.Toplevel(root)
    check_window.title("Проверка знаний")
    check_window.geometry("400x400+{}+{}".format(
        (check_window.winfo_screenwidth() // 2 - 200),
        (check_window.winfo_screenheight() // 2 - 200)))
    check_window.configure(bg="lightblue")

    tk.Label(check_window, text="Слово на английском:", font=("Comic Sans MS", 14), bg="lightblue").pack(pady=5)
    entry_english = tk.Entry(check_window, font=("Comic Sans MS", 14))
    entry_english.pack(pady=5)

    tk.Label(check_window, text="Слово на русском:", font=("Comic Sans MS", 14), bg="lightblue").pack(pady=5)
    entry_russian = tk.Entry(check_window, font=("Comic Sans MS", 14))
    entry_russian.pack(pady=5)

    translations = {
        "sheep": "овца", "monkey": "обезьяна", "eagle": "орёл", "fish": "рыба",
        "red": "красный цвет", "yellow": "желтый цвет", "green": "зеленый цвет",
        "blue": "синий цвет", "pink": "розовый цвет", "white": "белый цвет",
        "black": "черный цвет", "beet": "свекла", "carrot": "морковь", "berry": "ягода",
        "mushroom": "гриб", "cheek": "щека", "chin": "подбородок", "eye": "глаз",
        "knee": "колено", "sand": "песок", "heart": "сердце", "coat": "пальто",
        "tea": "чай", "doll": "кукла", "whistle": "свисток"}

    # Метка для отображения результата
    lbl_result = tk.Label(check_window, text="", font=("Comic Sans MS", 16), bg="lightblue")
    lbl_result.pack(pady=7)

    # Функция для записи результатов в файл
    def log_result(english_word, russian_word, correct):
        with open("knowledge_check_results.txt", "a", encoding="utf-8") as file:
            result = "Правильно" if correct else "Неправильно"
            file.write(f"Слово: {english_word} / Ответ: {russian_word} / Результат: {result}\n")

    # Функция для проверки перевода
    def check_translation():
        english_word = entry_english.get().strip().lower()
        russian_word = entry_russian.get().strip().lower()

        if translations.get(english_word) == russian_word:
            lbl_result.config(text="Правильно, молодец!", fg="green")
            log_result(english_word, russian_word, True)
        else:
            lbl_result.config(text="Неправильно, попробуй еще раз!", fg="red")
            log_result(english_word, russian_word, False)

    # Функция для генерации случайного слова на английском
    def random_word():
        english_word = random.choice(list(translations.keys()))
        entry_english.delete(0, tk.END)
        entry_english.insert(0, english_word)

    # Функция для генерации случайного перевода на русском и вставки в поле
    def random_russian_word():
        russian_word = random.choice(list(translations.values()))
        entry_russian.delete(0, tk.END)  # Очищаем поле ввода
        entry_russian.insert(0, russian_word)  # Вставляем случайный перевод

    tk.Button(check_window, text="Случайное слово на английском", font=("Comic Sans MS", 12),
              command=random_word).pack(pady=5)
    tk.Button(check_window, text="Случайное слово на русском", font=("Comic Sans MS", 12),
              command=random_russian_word).pack(pady=5)
    tk.Button(check_window, text="Проверить", font=("Comic Sans MS", 12), command=check_translation).pack(pady=5)


tk.Button(root, text="Проверка знаний!", font=("Comic Sans MS", 13,"bold"), height=2, width=20, bg='#66B2FF',fg='white',
          command=open_knowledge_check_window).place(x=900, y=650)


# Функция для создания круга с текстом
def create_circle(x, y, text):
    x1, y1, x2, y2 = x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius
    canvas.create_oval(x1, y1, x2, y2, fill="#3399FF", outline="black", width=2)

    # Связь текста с действиями
    actions = {
        "Цвета": open_colors_window, "Живые существа": open_creatures_window, "Съедобное": open_edible_window,
        "Части тела": open_body_parts_window, "Разное": open_various_window }

    if text == "Живые существа":
        # Разделяем текст на две строки
        label_id_1 = canvas.create_text(x, y - 25, text="Живые", font=("Comic Sans MS", 30, "bold"), fill="white")
        label_id_2 = canvas.create_text(x, y + 25, text="существа", font=("Comic Sans MS", 30, "bold"), fill="white")
        canvas.tag_bind(label_id_1, "<Button-1>", lambda event: open_creatures_window())
        canvas.tag_bind(label_id_2, "<Button-1>", lambda event: open_creatures_window())
    else:
        label_id = canvas.create_text(x, y, text=text, font=("Comic Sans MS", 30, "bold"), fill="white")
        if text in actions:
            canvas.tag_bind(label_id, "<Button-1>", lambda event: actions[text]())


# Создаем круги с текстами
for i, (x, y) in enumerate(circle_coords):
    create_circle(x + circle_radius, y + circle_radius, labels[i])
elapsed_time = time.time() - start_time
print(f"Время создания интерфейса: {elapsed_time:.4f} секунды")
root.mainloop()
