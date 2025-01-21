import datetime
import pandas

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict


def get_correct_form_word_year(age_difference):
    delta_new = age_difference % 100
    if 21 > delta_new > 4:
        return "лет"
    delta_new = age_difference % 10
    if delta_new == 1:
        return "год"
    elif 1 < delta_new < 5:
        return "года"
    return "лет"


def get_information_excel_table():
    excel_wine_2 = pandas.read_excel('wine3.xlsx', na_values=' ', keep_default_na=False)
    wines = excel_wine_2.to_dict(orient='records')
    sorted_wines = defaultdict(list) 

    for wine in wines:
        sorted_wines[wine['Категория']].append(wine)

    category_order = ['Белые вина', 'Красные вина', 'Напитки']
    ordered_wines = {}
    
    for category in category_order:
        if category in sorted_wines:
            ordered_wines[category] = sorted_wines[category]

    return ordered_wines


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    date_creation = 1920
    today_date = datetime.datetime.now()

    age_difference = today_date.year - date_creation

    year_shape = get_correct_form_word_year(age_difference)
    wines = get_information_excel_table()

    rendered_page = template.render(
        age_of_wine=age_difference,
        year=year_shape,
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
