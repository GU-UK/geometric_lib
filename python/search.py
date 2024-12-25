import sys
import webbrowser

def search_function(query):
    search_url = f"https://www.google.com/search?q={query} что за функция?"
    webbrowser.open(search_url)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_function(sys.argv[1])
    else:
        print("Ошибка: необходимо передать текст для поиска.")