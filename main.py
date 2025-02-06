from flask import Flask ,render_template ,redirect,session ,request , url_for
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import io
import sys
import html
from sorgular import select , insert , delete , update
# # #site yönlendirmesi


app =Flask(__name__)
app.secret_key="1234"

@app.route("/")            
def anasayfa(): 
        
        if "ad" in session and session ["ad"] != None:
            kullaniciadi = session.get('ad')
            return render_template("index.html",kullaniciadi=kullaniciadi)
        else:
            
             return render_template("giris.html")


@app.route("/python")            
def python(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("python.html")
    else: 
        return redirect("/giris")
    


@app.route("/bolum")
def bolum():
    if "ad" in session and session ["ad"] != None:
        return render_template("kg.html")
    else: 
        return redirect("/giris")
    
 





@app.route("/muhyazilim")            
def muhyazilim(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("yazilimmuhendisi.html")
    else: 
        return redirect("/giris")
    

@app.route("/giris")            
def giris():
    if "ad" in session and session ["ad"] != None:    
        kullaniciadi = session.get('ad')
        if "user_type" in session  and session["user_type"] == "admin":
            return render_template("admin.html",kullaniciadi=kullaniciadi)
        else: 
            return render_template("index.html",kullaniciadi=kullaniciadi)
        
    else:
        return render_template("giris.html",)
   
   




@app.route("/kayit")            
def kayit(): 
    if "ad" in session and session ["ad"] != None:
        return render_template("kayit.html")
    else:
        return redirect("/giris")
         



@app.route("/admin_panel")
def admin_panel():
    if "user_type" in session  and session["user_type"] == "admin":
        return render_template("admin.html")
    else:
        return redirect("/")

    

# @app.route("/kullanici")
# def kullanici():
#     if "ad" in session and session ["ad"] != None:
#         return render_template("kayit.html")
#     else:
#       return redirect("/giris")
    
@app.route("/php")
def php():
    if "ad" in session and session ["ad"] != None:
        return render_template("php.html")
    else:
      return redirect("/giris")
    

@app.route("/C++")
def c_plus():
    if "ad" in session and session ["ad"] != None:
        return render_template("c++.html")
    else:
      return redirect("/giris")




@app.route("/muhbilgisayar")
def muhbilgisayar():
    if "ad" in session and session ["ad"] != None:
        return render_template("muhbilgisayar.html")
    else:
      return redirect("/giris")








@app.route("/loginbilgilerikontrol", methods=["POST"])
def login_kontrol():    
    if request.method == "POST":
        kullaniciadi = html.escape(request.form.get("kullaniciadi"))
        sifre = html.escape(request.form.get("sifre"))
        
        sorgu = f"SELECT * FROM personel WHERE ad = '{kullaniciadi}' AND sifre = '{sifre}'"
        kayitlar = select(sorgu)
        
        if kayitlar and len(kayitlar) != 0:
            session["ad"] = kullaniciadi
            
            if kayitlar[0][-1] == 'admin':
                session["user_type"] = "admin"
                return render_template("admin.html", kullaniciadi=kullaniciadi)
            else:
                session["user_type"] = "user"
                return render_template("index.html", kullaniciadi=kullaniciadi)
        else:
            return render_template("giris.html", hata="Kullanıcı bilgileri hatalı!")

        







@app.route("/admin_panel/kullanici_bilgileri", methods=["GET", "POST"])
def kullanici_bilgileri():
    if "ad" in session and session ["ad"] != None:
          sorgu = "SELECT * FROM personel"
          kayitlar = select(sorgu)          
          return render_template("kullanicilar.html", personel = kayitlar)
    else:
          return redirect("/giris")
    










@app.route("/bolumler")            
def bolumler(): 
    if "ad" in session and session ["ad"] != None:
        sorgu = "SELECT * FROM gida"
        kayitlar = select(sorgu)          
        return render_template("gida.html", gida = kayitlar)
    else:
          return redirect("/giris")










@app.route("/bolumkontrol", methods=["POST"])
def bolumkontrol():  
    if request.method == "POST":
        kullaniciadi = html.escape(request.form.get("kullaniciadi"))
        sifre = html.escape(request.form.get("sifre"))
        
        sorgu = f"SELECT bolum FROM personel WHERE ad = '{kullaniciadi}' AND sifre = '{sifre}'"
        kayitlar = select(sorgu)
        
        if kayitlar and len(kayitlar) != 0:
            session["ad"] = kullaniciadi

            # Kullanıcının bölüm bilgisini al
            user_bolum = kayitlar[0][-1]  # İlk satırın ilk sütunu
            
            # Kullanıcıyı bölümüne göre yönlendir
            if user_bolum == 'gida':
                sorgu = "SELECT * FROM gida"
                kayitlar = select(sorgu)          
                return render_template("gida.html", gida = kayitlar)
            elif user_bolum == 'admin':
                return render_template("admin.html")
            elif user_bolum == 'zirrat':
                return render_template("ziraat.html")
            else:
                return render_template("kg.html", hata="Bilinmeyen bölüm!")
        else:
            return render_template("kg.html", hata="Bilinmeyen bölüm!")





@app.route("/admin_panel/kullanici_bilgileri/sil/<id>")                                   #    anasayfa açıldığında ne yapayım
def kullanici_sil(id): 
     if "ad" in session and session ["ad"] != None:
            sorgu = f"DELETE FROM personel WHERE id={int(id)}"
            delete(sorgu)
            sorgu = "SELECT * FROM personel"
            kayitlar = select(sorgu)          
            return render_template("kullanicilar.html", personel = kayitlar)
     else:
          return redirect("/giris")
     



@app.route("/gida/guncelle",methods=["post"])
def gida_guncelle():
    if "ad" in session and session ["ad"] != None:
        id = request.form["id"]
        ad = request.form["ad"]
        kalori = request.form["kalori"]
        durum = request.form["durum"]

        sorgu = f"UPDATE gida SET ad= '{ad}',  kalori= '{kalori}', durum= '{durum}' WHERE id={int(id)}"
        update(sorgu)
        return render_template("gidagn.html")
    else:
      return redirect("/giris")




@app.route("/gida/guncelle/<id>")                                   #    anasayfa açıldığında ne yapayım
def gida_gn(id):  
    if "ad" in session and session ["ad"] != None:
        sorgu = f"SELECT * FROM gida WHERE id={int(id)}"
        kayit = select(sorgu)                      
        return render_template ("gidagn.html", gida = kayit[0])
    else:
        return redirect("/giris")
      




@app.route("/admin_panel/kullanici_bilgileri/guncelle/<id>")                                   #    anasayfa açıldığında ne yapayım
def kullanici_gn(id):  
    if "ad" in session and session ["ad"] != None:
        sorgu = f"SELECT * FROM personel WHERE id={int(id)}"
        kayit = select(sorgu)                      
        return render_template ("kullanicign.html", personel = kayit[0])
    else:
        return redirect("/giris")








        
@app.route("/admin_panel/kullanici_bilgileri/guncelle" ,methods=["post"])                                   #    anasayfa açıldığında ne yapayım
def kullanici_gnn():  
    if "ad" in session and session ["ad"] != None:
        id = request.form["id"]
        ad = request.form["ad"]
        email = request.form["email"]
        sifre = request.form["sifre"]
        tur = request.form["tur"]
        bolum = request.form["bolum"] 

        sorgu = f"UPDATE personel SET ad= '{ad}',  email= '{email}', sifre= '{sifre}', tur= '{tur}', bolum='{bolum}' WHERE id={int(id)}"
        update(sorgu)
        return redirect("/admin_panel/kullanici_bilgileri")
    else:
        return redirect("/giris")








@app.route("/admin_panel/kullanici_ekle",methods=['GET','POST'])                                 
def kullanici_ekle():  

    if "user_type" in session  and session["user_type"] == "admin":    
        if "ad" in session and session ["ad"] != None:
            if request.method == "POST":
                ad = request.form["ad"]
                email = request.form["email"]
                sifre = request.form["sifre"]
                tur = request.form["tur"]
                bolum = request.form["bolum"]   
                
                sorgu = f"INSERT INTO personel (ad,email,sifre,tur,bolum) VALUES ('{ad}','{email}' ,'{sifre}','{tur}','{bolum}')"
                insert(sorgu)
                
                return redirect("/admin_panel/kullanici_bilgileri")
            else:
                return render_template("kullaniciekle.html")
        else:
            return redirect("/giris")








@app.route("/cikis")                                
def cikis():
    if "user_type" in session  and session["user_type"] == "admin":
        del session["ad"]
        return render_template("giris.html")
    else:
        del session["ad"]
        return render_template("giris.html")




app.run(debug=True)