

# 1. Мы импортируем библиотеки requests и BeautifulSoup, 
#       которые позволяют отправлять HTTP-запросы и извлекать данные из HTML-страниц.
# 2. Указываем URL для сайта dotabuff.com и создаем пустые список list_of_hero_url, list_of_enemy_pick.
# 3. Задаем заголовки для HTTP-запроса. Это необходимо для обеспечения корректной работы запросов.
# 4. Определяем функцию handled_heroes, которая принимает список и выводит каждый элемент списка вместе с количеством его повторений.
# 5. Создаем функцию get_list_of_url_enemy_pick, чтобы получить список вражеских персонажей от пользователя. Мы делаем это 5 раз.
# 6. Определяем функцию get_all_counter_enemy_hero, которая принимает список вражеских персонажей и ищет персонажей, 
#       которые являются "контрпиками" для каждого вражеского персонажа.
# 7. В функции main вызываем get_list_of_url_enemy_pick для получения списка вражеских персонажей, 
#       а затем вызываем get_all_counter_enemy_hero с полученным списком. Затем передаем полученный список в функцию handled_heroes для обработки.



import requests

from bs4 import BeautifulSoup

list_of_enemy_pick = []

url = 'https://www.dotabuff.com/heroes'

headers = {
		'Accept': '*/*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
	}

def get_list_of_url_enemy_pick(list_of_enemy_picks):
    list_of_enemy_pick_urls = []
    for enemy_pick in list_of_enemy_picks:
        for _ in range(3):
            enemy_pick_url = url + r'/' + enemy_pick.lower() + r'/counters'
            list_of_enemy_pick_urls.append(enemy_pick_url)
    return list_of_enemy_pick_urls


def get_all_counter_enemy_hero(list_of_enemy_pick):
    list_of_counters = []
    for hero_url in list_of_enemy_pick:
        response = requests.get(hero_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        counters = soup.find(class_='counter-outline')

        if counters is not None:
            list_heroes = counters.find_all("tr")
            for item in list_heroes:
                count = item.find('td')
                if count is not None:
                    name = count.find('img').get('alt')
                    list_of_counters.append(name)
        else:
            print(f"The class 'counter-outline' was not found in the HTML for URL {hero_url}")

    return list_of_counters


def main():
	get_list_of_url_enemy_pick()
	
	list_of_counter_picks = get_all_counter_enemy_hero(list_of_enemy_pick)

if __name__ == '__main__':
	main()