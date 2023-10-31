import requests
import pytest

from dataclasses import dataclass
from bs4 import BeautifulSoup


def get_wiki_int(parsed_str: str) -> int:
    """
    Вспомогательная ф-ция для очистки данных 
    в колонке Popularity из таблицы с Википедии
    """
    result = []
    for i in parsed_str:
        if i == '[':
            break
        if i.isdigit():
            result.append(i)
    return int(''.join(result))


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
            if len(columns) == 5:
                website = columns[0].text.strip()
                popularity = get_wiki_int(columns[1].text.strip())
                frontend = columns[2].text.strip()
                backend = columns[3].text.strip()
                database = columns[4].text.strip()
                notes = columns[5].text.strip()

                table_data.append(WebsiteLaguages(
                    website, popularity, frontend, backend, database, notes))

        return table_data


# С помощью фикстуры все сохраненные датаклассы будут доступны для последующих тестов
@pytest.fixture(scope="module")
def website_data():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    return load_table_data(url)


def test_load_table_data(website_data):
    # Проверяем, что website_data не пуста
    assert website_data

    # Проверяем, что лист состоит только из датаклассов
    for data in website_data:
        assert isinstance(data, WebsiteLaguages)


@pytest.mark.parametrize("expected_popularity", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_expected_popularity(website_data, expected_popularity):

    errors = []

    for data in website_data:
        if data.popularity < expected_popularity:
            error_message = f"{data.website} (Frontend:{data.frontend}|Backend:{data.backend}) has {data.popularity} unique visitors per month. (Expected more than {expected_popularity})\n"
            errors.append(error_message)

    assert not errors, f"\n{''.join(errors)}"


if __name__ == "__main__":
    pytest.main([__file__])
