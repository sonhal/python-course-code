

from urllib import request


def text_file_to_list(url):
    with request.urlopen(url) as file:
        words = file.read().decode("utf-8").split()
        return words


def print_nav_facts():
    with request.urlopen(
            "https://gist.githubusercontent.com/sonhal/db9c2f7869c6937bdfed009c5381f2de/raw/a63d7b16a14247e13ddebfe4f064a2987b3ae011/python_course_data.txt") as file:
        words = file.read().decode("utf-8").split()

        numbers_in_the_text = []
        for word in words:
            if word.isdigit():
                int_word = int(word)
                numbers_in_the_text.append(int_word)
        print(numbers_in_the_text)
