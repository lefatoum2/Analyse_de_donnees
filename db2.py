import mysql.connector as mysqlpyth
import pandas as pd

db = mysqlpyth.connect(
    host="localhost",
    user="root",
    passwd="root",
    port=3306,
    db="netflix4"
)

data1 = pd.read_csv('data/netflix_titlesd2000.csv')

list_in = list(data1["listed_in"].values)
country = list(data1["country"].values)
actor = list(data1["cast"].values)
director = list(data1["director"].values)
director_set = set()
actor_set = set()
country_set = set()
list_in_set = set()
cur = db.cursor()


# Country ....
for i in range(len(country)):
    liste = country[i]
    coun = liste.split(",")
    for y in coun:
        country_set.add(y)

for item2, item in enumerate(country_set):
    cur.execute("INSERT INTO country(id_country,country_name) VALUES(%s,%s)", (item2, item))
    db.commit()


# listed_in-set catégorie......
for i in range(len(list_in)):
    liste = list_in[i]
    dir = liste.split(",")
    for y in dir:
        list_in_set.add(y)

for item2, item in enumerate(list_in_set):
    cur.execute("INSERT INTO listed_in(id_liste,liste_name) VALUES(%s,%s)", (item2, item))
    db.commit()

# director ....
for i in range(len(director)):
    liste = director[i]
    dir = liste.split(",")
    for y in dir:
        director_set.add(y)

for item2, item in enumerate(director_set):
    cur.execute("INSERT INTO director(id_director,director_name) VALUES(%s,%s)", (item2, item))
    db.commit()


# actor ....
for i in range(len(actor)):
    liste = actor[i]
    act = liste.split(",")
    for y in act:
        actor_set.add(y)

for item2, item in enumerate(actor_set):
    cur.execute("INSERT INTO actor(id_actor,actor_name) VALUES(%s,%s)", (item2, item))
    db.commit()

cur.close()
