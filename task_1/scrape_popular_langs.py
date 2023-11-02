import requests

from dataclasses import dataclass
from bs4 import BeautifulSoup
from task_1.utils import get_wiki_int


@dataclass
class WebsiteLaguages:
    website: str
    popularity: int
    frontend: str
    backend: str
    database: str
    notes: str


def load_table_data(table_url: str) -> list:
    """
    Ф-ция парсит данные из таблицы с Википедии,
    создает и возвращает лист из датаклассов
    """
    with requests.get(table_url) as response:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})

        # Лист для хранения всех рядов таблицы в виде датаклассов
        table_data = []

        # Итерируем по рядам таблицы
        for row in table.find('tbody').find_all('tr'):
            columns = row.find_all('td')

            # убеждаемся, что спарсили все ряды и создаем инстанс датакласа каждую итерацию
            if len(columns) == 6:
                website = columns[0].text.strip()
                popularity = get_wiki_int(columns[1].text.strip())
                frontend = columns[2].text.strip()
                backend = columns[3].text.strip()
                database = columns[4].text.strip()
                notes = columns[5].text.strip()

                table_data.append(WebsiteLaguages(
                    website, popularity, frontend, backend, database, notes))

        return table_data
