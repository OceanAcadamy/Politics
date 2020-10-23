import pyrebase
from flask import Flask, render_template, request, flash, session, redirect, url_for, make_response, jsonify
from firebase_admin import credentials, firestore, initialize_app

app=Flask(__name__)

app.config['SECRET_KEY'] = '1456780765656546'

firebaseConfig = {
    "apiKey": "AIzaSyCwq7_NPTY6efJqjI24i0H4tvHiMdfE-i8",
    "authDomain": "politics-32519.firebaseapp.com",
    "databaseURL": "https://politics-32519.firebaseio.com",
    "projectId": "politics-32519",
    "storageBucket": "politics-32519.appspot.com",
    "messagingSenderId": "373212664538",
    "appId": "1:373212664538:web:c907da78e85b56baa74be3",
    "measurementId": "G-EG417775R4"
  };

cred = credentials.Certificate('service.json')
default_app = initialize_app(cred)
db = firestore.client()
firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()
#login page
@app.route("/login", methods=['GET','POST'])
def login():
    email = request.form['email']
    password = request.form['pass']
    print(email)
    try:
        if auth.sign_in_with_email_and_password(email, password):
            print("1")
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    except:
        return render_template('login.html')



#landing page after signin
@app.route("/home", methods=['GET','POST'])
def home():
    res = db.collection('home').document('details').get().to_dict()
    return render_template('home.html', res= res)


@app.route("/submit", methods=['GET','POST'])
def submit():
    print("welcome")

    return render_template('home.html')


# home page data can be stored in DB
# -----------------------------------
@app.route("/", methods=['GET','POST'])
def index():
    return render_template('login.html')

# for components (Menu)
# ---------------------------
@app.route("/menu", methods=['GET','POST'])
def menu():
    return render_template('menu.html')

# for menu page (my_profile)
# ---------------------------
@app.route("/my_profile",  methods=['GET','POST'])
def my_profile():
    return render_template('my_profile.html')

# for menu (govt_office)
#-----------------------
@app.route("/govt_office",  methods=['GET','POST'])
def govt_office():
    return render_template('govt_office.html')

# for menu page (police_station)
# -------------------------------
@app.route("/police_station",  methods=['GET','POST'])
def police_station():
    return render_template('police_station.html')

# for menu page (hospitals)
# ---------------------------
@app.route("/hospitals",  methods=['GET','POST'])
def hospitals():
    return render_template('hospitals.html')

# for menu page (schools)
# ---------------------------
@app.route("/schools",  methods=['GET','POST'])
def schools():
    return render_template('schools.html')

# for menu page (colleges)
# ---------------------------
@app.route("/colleges",  methods=['GET','POST'])
def colleges():
    return render_template('colleges.html')

# for menu page (gallery)
# ---------------------------
@app.route("/gallery",  methods=['GET','POST'])
def gallery():
    return render_template('gallery.html')

# for menu page (events)
# ---------------------------
@app.route("/events",  methods=['GET','POST'])
def events():
    return render_template('events.html')

# for menu page (notification)
# ---------------------------
@app.route("/notification",  methods=['GET','POST'])
def notification():
    return render_template('notification.html')

# for menu page (complaints)
# ---------------------------
@app.route("/complaints",  methods=['GET','POST'])
def complaints():
    return render_template('complaints.html')

# for menu page (testimonials)
# ---------------------------
@app.route("/testimonials",  methods=['GET','POST'])
def testimonials():
    return render_template('testimonials.html')

# for menu page (contact us)
# ---------------------------
@app.route("/contact_us",  methods=['GET','POST'])
def contact_us():
    return render_template('contact_us.html')

# for govt_office (collector office)
#------------------------------------
@app.route("/collector_office",  methods=['GET','POST'])
def collector_office():
    return render_template('collector_office.html')

# for govt_office (Thasildhar office)
#------------------------------------
@app.route("/thasildhar_office",  methods=['GET','POST'])
def thasildhar_office():
    return render_template('thasildhar_office.html')

# for govt_office (civil supply office office)
#--------------------------------------------
@app.route("/civil_supply",  methods=['GET','POST'])
def civil_supply():
    return render_template('civil_supply.html')

# for govt_office (Electricity Board)
#--------------------------------------------
@app.route("/electricity_board",  methods=['GET','POST'])
def electricity_board():
    return render_template('electricity_board.html')

# for govt_office (PWD)
#--------------------------------------------
@app.route("/pwd",  methods=['GET','POST'])
def pwd():
    return render_template('pwd.html')

# for govt_office (court)
#--------------------------------------------
@app.route("/court",  methods=['GET','POST'])
def court():
    return render_template('court.html')

# for govt_office (post office)
#--------------------------------------------
@app.route("/post_office",  methods=['GET','POST'])
def post_office():
    return render_template('post_office.html')

if __name__=="__main__":
    app.run(debug=True)