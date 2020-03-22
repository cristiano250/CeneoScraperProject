# CeneoScraperProject
## etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                          |Nazwa zmiennej |
|------------------------|--------------------------------------------------|-------------- |
|opinia                  |li.js_product-review                              |               |
|id opinii               |["data-entry-id"]                                 |               |
|autor opinii            |div.reviewer-name-line                            |               |
|rekomendacja            |div.product-review-sumary > em                    |               |
|ocena                   |span.review-score-count                           |               |
|treść opinii            |p.product-review-body                             |               |
|lista wad               |div.cons-cell > ul                                |               |
|lista zalet             |div.pros-cell > ul                                |               |
|przydatna               |button.vote-yes>span                              |               |
|nieprzydatna            |button-vote-np >span                              |               |
|data wystawienia opinii |span.review-time > time:first-child['datetime']   |               |
|data zakupu             |span.review-time > time:nth-child(2)['datetime']  |               |
## etap2 - pobranie składowych pojedynczej opinii
## - pobranie kodu jednej strony z opiniami o konkretnym produkcie
## - wyciągnięcie z kodu stronny fragmentów odpowiadających poszczególnym opiniom
## - zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii 
## znak większości - bezpośredni potomek