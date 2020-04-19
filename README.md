# CeneoScraperProject
## etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                          |Nazwa zmiennej |
|------------------------|--------------------------------------------------|-------------- |
|opinia                  |li.js_product-review                              |opinion        |
|id opinii               |["data-entry-id"]                                 |opinion_id     |
|autor opinii            |div.reviewer-name-line                            |author         |
|rekomendacja            |div.product-review-sumary > em                    |recommendation |
|ocena                   |span.review-score-count                           |stars          |
|treść opinii            |p.product-review-body                             |content        |
|lista wad               |div.cons-cell > ul                                |cons           |
|lista zalet             |div.pros-cell > ul                                |pros           |
|przydatna               |button.vote-yes>span                              |useful         |
|nieprzydatna            |button.vote-no >span                              |useless        |
|data wystawienia opinii |span.review-time > time:first-child['datetime']   |opinion_date   |
|data zakupu             |span.review-time > time:nth-child(2)['datetime']  |purchase_date  |
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
