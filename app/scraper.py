#import bibliotek
import requests
from bs4 import BeautifulSoup
import pprint
import json

#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion, selector,attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        else:
            return opinion.select(selector).pop(0).text.strip()
    except IndexError:
        return None



#słownik z atrybutami opinii i ich selektrorami
selectors={
        "author":["span.user-post__author-name"],
        "recommendation":["span.user-post__author-recomendation > em"],
        "stars":["span.user-post__score-count"],
        "content":["div.user-post__text"],
        "cons":["div.review-feature__col:has(>div.review-feature__title--negatives)"],
        "pros":["div.review-feature__col:has(>div.review-feature__title--positives)"],
        "useful":["button.vote-yes>span"],
        "useless":["button.vote-no >span "],
        "opinion_date":["span.user-post__published>time:nth-child(1)", "datetime"],
        "purchase_date":["span.user-post__published>time:nth-child(2)", "datetime"]
        }

def scraper(product_id):
    #adres url pierwszej strony z opiniami o produkcie
    url_prefix="https://www.ceneo.pl"
    #product_id=input("podaj identyfikator produktu: ")
    url_postfix="#tab=reviews"
    url=url_prefix+"/"+product_id+url_postfix


    #pusta lista na opinie konsumentów:
    all_opinions=[]



    while url:
        #pobranie kodu pojedynczej strony z opiniami o produkcie:
        response=requests.get(url)
        page_dom=BeautifulSoup(response.text, 'html.parser')
        
        #wydobycie z kodu strony fragmentów odpowiadających opiniom konsumentów
        # select zawsze zwróci listę
        opinions=page_dom.select("div.js_product-review")


        #dla wszystkich opinii z danej strony wydobycie ich składowych
        for opinion in opinions:
            features={key:extract_feature(opinion, *args)
                        for key, args in selectors.items()}
            features["opinion_id"]=opinion["data-entry-id"]
            features["useful"]=int(features["useful"])
            features["useless"]=int(features["useless"])
            features["stars"]=float(features["stars"].split('/')[0].replace(',','.'))
            features['content']=features['content'].replace('\n',' ').replace('\r',' ')
            try:
                features['cons']=features['cons'].replace('\n',', ').replace('\r',', ').replace("Wady, ", "")
            except AttributeError:
                pass
            try:
                features['pros']=features['pros'].replace('\n',', ').replace('\r',', ').replace("Zalety, ", "")
            except AttributeError:
                pass
            all_opinions.append(features)

            # author=extract_feature(opinion,"div.reviewer-name-line")
            # recommendation=extract_feature(opinion,"div.product-review-summary > em")
            # stars=extract_feature(opinion,"span.review-score-count")
            # content=extract_feature(opinion,"p.product-review-body")
            # cons=extract_feature(opinion,"div.cons-cell > ul")
            # pros=extract_feature(opinion,"div.pros-cell > ul")
            # useful=extract_feature(opinion,"button.vote-yes>span")
            # useless=extract_feature(opinion,"button.vote-no >span ")
            # opinion_date=extract_feature(opinion,"span.review-time > time:nth-child(1)",'datetime')
            # purchase_date=extract_feature(opinion,"span.review-time > time:nth-child(2)",'datetime')
            

    # print(opinion_id, author, recommendation, stars, content, cons, pros, useful, useless, opion_date, purchase_date)
        try:
            url=url_prefix+page_dom.select("a.pagination__next").pop()["href"]
        except IndexError:
            url=None
        print(len(all_opinions))
        print(url)

    with open("opinions_json/"+product_id+".json",'w', encoding="utf-8") as fp:
        json.dump(all_opinions, fp, indent=4, ensure_ascii=False)


#pprint.pprint(all_opinions)

