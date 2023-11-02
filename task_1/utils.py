def get_wiki_int(parsed_str: str) -> int:
    """
    Вспомогательная ф-ция для получения int 
    в колонках с числами из таблиц Википедии
    """
    result = []
    for i in parsed_str:
        if i == '[':
            break
        if i.isdigit():
            result.append(i)
    return int(''.join(result))
