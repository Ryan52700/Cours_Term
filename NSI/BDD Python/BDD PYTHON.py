import sqlite3
conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()
recherche = (1960, 8)
cur.execute('SELECT titre FROM LIVRES WHERE ann_publi < ? AND note > ?', recherche)
conn.commit()
liste = cur.fetchall()
cur.close()
conn.close()