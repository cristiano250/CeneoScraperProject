# CeneoScraperProject
## etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                                                    |Nazwa zmiennej |
|------------------------|----------------------------------------------------------------------------|-------------- |
|opinia                  |div.js_product-review                                                       |opinion        |
|id opinii               |["data-entry-id"]                                                           |opinion_id     |
|autor opinii            |span.user-post__author-name                                                 |author         |
|rekomendacja            |span.user-post__author-recomendation > em                                   |recommendation |
|ocena                   |span.user-post__score-count                                                 |stars          |
|treść opinii            |div.user-post__text                                                         |content        |
|lista wad               |div.review-feature__col:has(>div.review-feature__title--negatives)          |cons           |
|lista zalet             |div.review-feature__col:has(>div.review-feature__title--positives)          |pros           |
|przydatna               |button.vote-yes>span                                                        |useful         |
|nieprzydatna            |button.vote-no >span                                                        |useless        |
|data wystawienia opinii |span.user-post__published>time:nth-child(1)", "datetime"                    |opinion_date   |
|data zakupu             |span.user-post__published>time:nth-child(2)", "datetime"                    |purchase_date  |
## etap2 - pobranie składowych pojedynczej opinii
 - pobranie kodu jednej strony z opiniami o konkretnym produkcie
 - wyciągnięcie z kodu stronny fragmentów odpowiadających poszczególnym opiniom
 - zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii 
### znak większości - bezpośredni potomek
# Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- zapisanie do złożonej struktury danych wszystkich opinii z pojedynczej strony
- przechodzenie po kolejnych stronach z opiniami
- zapis wsyzstkich opionii o pojedynczym produkcie w pliku
# Etap 4
- transformacja i wyczyszczenie
- refaktoring kodu
- parametryzacja
# Etap 5 (Pandas, Matplotlib)
-wczytanie opinii do ramki danych
-policzenie podstawowych statystyk
-narysowanie wykresów funkcji
# Etap 6 - interfejs webowy dla scrapera (FLASK)
>    /Nowy folder (10)
>>        /run.py
>>        /config.py
>>        /app
>>>             /__init__.py
>>>             /views.py
>>>             /models.py
>>>             /static/
>>>>                /main.css
>>>>                /figures_png
>>>             /templates/
>>>>                /layout.html
>>>>                /extract.html
                /opinions_json
>>>             /requirements.txt
>>>             /.venv