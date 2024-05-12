from flask import Flask
import random

app = Flask(__name__)

gercekler = ["yazı","tura"]

@app.route("/")
def hello_world():
    
    return f'<h1>selam</h1>   <a href="/giris">giriş sayfasına git!</a>  <a href="/oyun">oyun sayfasına git!</a>'  

@app.route("/giris")
def giris():
    
    return f'<h1>girişe hoşgeldiniz</h1>  <a href="/">ana sayfaya git!</a>  <a href="/oyun">oyun sayfasına git!</a>'

@app.route("/oyun")
def oyun():
    
    return f'<h1>Bakalım yazı mı tura mı?</h1><h1>{random.choice(gercekler)}</h1>  <a href="/">ana sayfaya git!</a>     <a href="/giris">giriş sayfasına git!</a>'
    
app.run(debug=True)