import os
from flask import Flask 
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,  "bookdatabase.db"))

application = Flask (__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = database_file
db =SQLAlchemy(application)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

    @application.route("/", methods=["GET", "POST"])
    def home():
        if request.form:
         try:
           book = Book(title=request.form.get("title"))
           db.session.add(book)
           db.session.commit()
         except Exception as e:
            print("Failed to add book .....")
            print(e)
        books = Book.query.all()
 
        return render_template("home.html", books=books)

    @application.route("/Update", methods=["POST"])
    def update():
        try:
            newtitle = request.form.get("newtitle")
            oldtitle = request.form.get("oldtitle")
            book = Book.query.filter_by(title=oldtitle).first()
            book.title = newtitle
            db.session.commit()
        except Exception as e:
            print("Couldn't update title")
            print(e)
    
        return redirect("/")
    
    @application.route("/delete", methods=["POST"])
    def delete():
        title = request.form.get("title")
        book = Book.query.filter_by(title=title).first()
        db.session.delete(book)
        db.session.commit()
        return redirect("/")
    

if __name__ == "__main__":
    application.run(debug=True)