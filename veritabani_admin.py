import sqlite3 
baglanti = sqlite3.connect("personel.db")  
imlec = baglanti.cursor()  


sorgu = "CREATE TABLE IF NOT EXISTS personel (id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT , email TEXT , sifre TEXT , tur TEXT, bolum TEXT)"  
imlec.execute(sorgu) 
baglanti.commit 

sorgu = "INSERT INTO personel (ad, email, sifre, tur, bolum) VALUES ('dogukan','d@gmail.com','1234','admin' , 'admin')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur, bolum) VALUES ('sevim','d@gmail.com','1234','admin', 'admin')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO personel (ad, email, sifre, tur , bolum) VALUES ('osman','o@gmail.com','12345' ,'kullanici', 'gida')"
imlec.execute(sorgu)
baglanti.commit()






sorgu = "CREATE TABLE IF NOT EXISTS gida (id INTEGER PRIMARY KEY AUTOINCREMENT,ad TEXT , kalori TEXT , durum TEXT)"  
imlec.execute(sorgu) 
baglanti.commit 

sorgu = "INSERT INTO gida (ad, kalori, durum) VALUES ('elma','60','yararlı')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO gida (ad, kalori, durum) VALUES ('armut','45','yararlı')"
imlec.execute(sorgu)
baglanti.commit()

sorgu = "INSERT INTO gida (ad, kalori, durum) VALUES ('erik','35','yararlı')"
imlec.execute(sorgu)
baglanti.commit()





