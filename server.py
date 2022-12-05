import json
from flask import Flask,render_template,request,redirect,flash,url_for
import helper1 as HELPER

app = Flask(__name__)
app.secret_key = "something_special"


@app.route("/")
def index():
    return render_template("index.html")




@app.route("/showSummary", methods=["POST"])
def show_summary():
    selected_club = HELPER.get_club_by_mail(mail=request.form["email"])
    if selected_club is None:
        print("pas trouvé !")
        flash("Sorry, that email wasn't found !!")
        return render_template("index.html")

    

    if selected_club :

        HELPER.USER_CLUB = selected_club
        print("trouvé !")
        return render_template(
            "welcome.html",
            club=HELPER.USER_CLUB,
            competitions=HELPER.COMPETITIONS,
        )

    flash("Email address not found")
    return render_template("index.html")



@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )
   
    if purchase_is_valid:
        
        selected_competition["numberOfPlaces"] = int(selected_competition["numberOfPlaces"]) - int(places_required)
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=HELPER.COMPETITIONS,
        )
    
    
    flash("Vous avez depassée le nombre de places maximum par compétition qui est de 12 !!")


    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=HELPER.COMPETITIONS,
    )


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))