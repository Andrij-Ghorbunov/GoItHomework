def get_cats_info(path):
    try:
        lines = []
        with open(path, 'r') as filehandler:
            lines = [line.rstrip('\n') for line in filehandler.readlines() if line] # тільки непорожні рядки
        # не тримати файл відкритим під час подальшої обробки даних
        if not len(lines):
            return []
        splitLines = [line.split(',') for line in lines]
        dictionaries = [{"id":s[0], "name":s[1], "age":s[2]} for s in splitLines]
        return dictionaries
    except Exception as e:
        print('An error occured', e)
        return []

def main():
    cats_info = get_cats_info("cats.txt")
    print(cats_info)

if __name__ == "__main__":
    main()
