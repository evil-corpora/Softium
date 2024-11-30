import os

# Путь к файлу hosts
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Строки, которые нужно удалить
lines_to_remove = [
    "127.0.0.1 yandex.ru",
    "127.0.0.1 www.yandex.ru",
    "127.0.0.1 youtube.com",
    "127.0.0.1 www.youtube.com",
    "127.0.0.1 vk.com",
    "127.0.0.1 www.vk.com",
    "127.0.0.1 roblox.com",
    "127.0.0.1 www.roblox.com",
    "127.0.0.1 store.steampowered.com",
    "127.0.0.1 www.store.steampowered.com",
    "127.0.0.1 rutube.ru",
    "127.0.0.1 www.rutube.ru",
    "127.0.0.1 igroutka.ru",
    "127.0.0.1 vseigru.net",
    "127.0.0.1 ru.pinterest.com",
    "127.0.0.1 vkvideo.ru",
    "127.0.0.1 vkplay.ru",
    "127.0.0.1 minigames.mail.ru",
    "127.0.0.1 www.twitch.tv",
    "127.0.0.1 gx.games",
    "127.0.0.1 pikabu.ru",
    "127.0.0.1 dzen.ru",
    "127.0.0.1 chromewebstore.google.com",
    "127.0.0.1 www.wildberries.ru",
    "127.0.0.1 www.avito.ru",
    "127.0.0.1 music.yandex.ru",
    "127.0.0.1 music.youtube.com",
    "127.0.0.1 vk.com",
    "127.0.0.1 web.telegram.org",
    "127.0.0.1 www.min2win.ru",
    "127.0.0.1 poki.com",
    "127.0.0.1 www.utorrent.com",
    "127.0.0.1 www.bluestacks.com",
    "127.0.0.1 tankionline.com"
]

try:
    # Читаем содержимое файла
    with open(hosts_path, 'r') as file:
        content = file.readlines()

    # Удаляем строки, которые нужно убрать
    new_content = [line for line in content if line.strip() not in lines_to_remove]

    # Записываем обновленное содержимое обратно в файл
    with open(hosts_path, 'w') as file:
        file.writelines(new_content)

    print("Строки удалены из файла hosts.")

except PermissionError:
    print("Ошибка: Не хватает прав для изменения файла hosts. Запустите скрипт от имени администратора.")
except FileNotFoundError:
    print("Ошибка: Файл hosts не найден. Проверьте путь к файлу.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
