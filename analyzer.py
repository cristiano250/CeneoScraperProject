#import bibliotek
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt



#wyświetlenie zawartości katalogu opinions_json
input_directory="./opinions_json"
print(*os.listdir(input_directory))

#wczytqanie identyfikatora produktu, którego opinie będą analizowe
product_id=input("podaj identyfikator produktu: ")

#wczytanie do ramki danych opinii o pojedynczym produkcie
opinions=pd.read_json(input_directory+'/'+product_id+'.json')
opinions=opinions.set_index('opinion_id')

#PODSTAWOWE STATYSTYKI
#averaga_score =opinions['stars'].mean().round(2)
average_score=opinions.stars.mean().round(2)
pros=opinions.pros.count()
cons=opinions.cons.count()
print(f'Średnia ocena: {average_score}\nLiczba opinii z zaletami: {pros}\nLiczba opinii z wadami: {cons}')

#HISTOGRAM CZĘSTOŚCI WYSTĘPOWANIA POSZCZEGÓLNYCH GWIAZDEK
stars=opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)),fill_value=0)
fig, ax =plt.subplots()
stars.plot.bar(color="#00FF00")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.xticks(rotation=0)
#ax.axvline(average_score, color='blue',linewidth=2)
#plt.show()
plt.savefig('figures_png/'+product_id+"_bar.png")
plt.close()

#UDZIAŁ POSZCZEGÓLNYCH REKOMENDACJI W OGÓLNEJ LICZBIE OPINII
recoommendation=opinions.recommendation.value_counts()
fig, ax= plt.subplots()
recoommendation.plot.pie(label="",autopct="%1.1f%%", colors=['#00FF00','red'])
plt.title("Rekomendacja")
#plt.show()
plt.savefig('figures_png/'+product_id+"_pie.png")
plt.close()

#print(opinions.purchase_date==None)
opinions['purchased'] = opinions['purchase']= opinions['purchase_date']!=None
print(opinions['purchased'])
stars_purchased=pd.crosstab(opinions['stars'], opinions['purchased'])
print(stars_purchased)