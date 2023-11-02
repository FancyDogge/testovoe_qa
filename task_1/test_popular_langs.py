import pytest

from task_1.scrape_popular_langs import load_table_data, WebsiteLaguages


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
            error_message = f"{data.website} (Frontend:{data.frontend}|Backend:{data.backend}) has {data.popularity} unique visitors per month. (Expected more than {expected_popularity})\n\n"
            errors.append(error_message)
    # более-менее красиво оформляем принт ошибок
    assert not errors, f"\n{''.join(errors)}"
