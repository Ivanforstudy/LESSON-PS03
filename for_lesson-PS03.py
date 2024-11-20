from bs4 import BeautifulSoup
import requests

# Парсинг для ссылок
#url = "http://quotes.toscrape.com/"
#response = requests.get(url)
#html = response.text
#soup = BeautifulSoup(html, "html.parser")
#links = soup.find_all("a")
#for link in links:
 #   print(link.get('href'))

#Мы попробовали парсинг ссылок, теперь перейдём к парсингу цитат.
#На сайте https://quotes.toscrape.com/ мы видим цитаты, их авторов и теги.

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#Создадим отдельную переменную text, куда будут сохраняться все цитаты
text = soup.find_all("span", class_="text")

#Создадим отдельную переменную author, куда будут сохраняться все авторы
#author = soup.find_all("small", class_="author")

#С помощью функции range(len) определим общее количество цитат
#for i in range(len(text)):
#Присвоим номер каждой цитате так, чтобы нумерация шла с 1
#    print(f"Цитата номер - {i + 1}")

#Выводим автора цитаты
#    print(f"Автор цитаты - {author[i].text}\n")




#   Попробуем работать с другим сайтом — randomword.com
#   Здесь постоянно выдаются рандомные слова, с которыми мы создадим мини-игру.

#Создаём функцию, которая будет получать информацию

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except:
        print("Произошла ошибка")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()

