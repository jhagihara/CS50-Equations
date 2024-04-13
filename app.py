import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import apology, calcquadraticpos, calcquadraticneg, calcarea, calcvolume

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def home():
    """Defines home page"""
    return render_template("home.html")

@app.route("/quadratic", methods=["GET", "POST"])
def quadratic():
    """Calculate quadratic formula."""

    if request.method == "POST":
        a = (request.form.get("a"))
        b = (request.form.get("b"))
        c = (request.form.get("c"))

        if not a or not b or not c:
            return apology("Must input a coefficient")
        a = float(a)
        b = float(b)
        c = float(c)

        positiveans = calcquadraticpos(a,b,c)
        negativeans = calcquadraticneg(a,b,c)

        notreal1 = "real"
        notreal2 = "real"

        if positiveans[1] == 1:
            notreal1 = "Answer not real"
        if negativeans[1] == 1:
            notreal2 = "Answer not real"
        return render_template("quadsolved.html", positiveans=positiveans[0], negativeans=negativeans[0], notreal1=notreal1, notreal2=notreal2)
    else:
        return render_template("quadratic.html")


@app.route("/area", methods=["GET", "POST"])
def area():
    """Calculate area"""
    # Make sure to handle if user inputs a negative value

    if request.method == "POST":

        shape = request.form.get("shape")
        if not shape:
            return apology("Must input a shape")
        if shape == "Square":
            return redirect("/squarearea")
        elif shape == "Rectangle":
            return redirect("/rectanglearea")
        elif shape == "Triangle":
            return redirect("/trianglearea")
        elif shape == "Circle":
            return redirect("/circlearea")
        elif shape == "Trapezoid":
            return redirect("/trapezoidarea")

        return redirect("areasolved.html")
    else:
        return render_template("area.html")


@app.route("/squarearea", methods=["GET", "POST"])
def square():
    """When user chooses square shape, this is the page it gets redirected to"""

    if request.method == "POST":
        x = request.form.get("x")
        if not x:
            return apology("Must input a value")
        x = int(x)
        if x <= 0:
            return apology("Must input a valid, positive side value")
        squarearea = calcarea(0,0,0,0,x,0,"Square")
        return render_template("areasolved.html", areaans=squarearea, shape="Square")
    else:
        return render_template("square.html")


@app.route("/rectanglearea", methods=["GET", "POST"])
def rectangle():

    if request.method == "POST":
        x = request.form.get("x")
        y = request.form.get("y")
        if not x:
            return apology("Must input a value")
        if not y:
            return apology("Must input a value")
        x = int(x)
        y = int(y)
        if x <= 0:
            return apology("Must input a valid, positive side (x) value")
        if y <= 0:
            return apology("Must input a valid, positive (y) value")

        rectanglearea = calcarea(0,0,0,0,x,y,"Rectangle")
        return render_template("areasolved.html", areaans=rectanglearea, shape="Rectangle")
    else:
        return render_template("rectangle.html")


@app.route("/trianglearea", methods=["GET", "POST"])
def triangle():

    if request.method == "POST":
        b = request.form.get("b")
        h = request.form.get("h")
        if not b:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        b = int(b)
        h = int(h)
        if b <= 0:
            return apology("Must input a valid, positive base value")
        if h <= 0:
            return apology("Must input a valid, positive height value")

        trianglearea = calcarea(0,b,h,0,0,0,"Triangle")
        return render_template("areasolved.html", areaans=trianglearea, shape="Triangle")
    else:
        return render_template("triangle.html")


@app.route("/circlearea", methods=["GET", "POST"])
def circle():

    if request.method == "POST":
        r = request.form.get("r")
        if not r:
            return apology("Must input a value")
        r = int(r)
        if r <= 0:
            return apology("Must input a valid, positive radius value")

        circlearea = calcarea(0,0,0,r,0,0,"Circle")
        return render_template("areasolved.html", areaans=circlearea, shape="Circle")

    else:
        return render_template("circle.html")


@app.route("/trapezoidarea", methods=["GET", "POST"])
def trapezoid():

    if request.method == "POST":
        a = request.form.get("a")
        b = (request.form.get("b"))
        h = (request.form.get("h"))
        if not a:
            return apology("Must input a value")
        if not b:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        a = int(a)
        b = int(b)
        h = int(h)
        if a <= 0:
            return apology("Must input a valid, positive top side (a) value")
        if b <= 0:
            return apology("Must input a valid, positive bottom side (b) value")
        if h <= 0:
            return apology("Must input a valid, positive height value")
        trapezoidarea = calcarea(a,b,h,0,0,0,"Trapezoid")
        return render_template("areasolved.html", areaans=trapezoidarea, shape="Trapezoid")
    else:
        return render_template("trapezoid.html")


@app.route("/volume", methods=["GET", "POST"])
def volume():

    if request.method == "POST":

        shape = request.form.get("shapev")
        if not shape:
            return apology("Must input a shape")
        if shape == "Cube":
            return redirect("/cubevolume")
        elif shape == "Rectangular Prism":
            return redirect("/prismvolume")
        elif shape == "Cylinder":
            return redirect("/cylindervolume")
        elif shape == "Cone":
            return redirect("/conevolume")
        elif shape == "Pyramid":
            return redirect("/pyramidvolume")
        elif shape == "Sphere":
            return redirect("/spherevolume")

        return redirect("volumesolved.html")
    else:
        return render_template("volume.html")


@app.route("/cubevolume", methods=["GET", "POST"])
def cube():

    if request.method == "POST":
        x = (request.form.get("xv"))
        if not x:
            return apology("Must input a value")
        x = int(x)
        if x <= 0:
            return apology("Must input a valid, positive side value")
        cubevolume = calcvolume(x,0,0,0,0,"Cube")
        return render_template("volumesolved.html", volumeans=cubevolume, shape="Cube")
    else:
        return render_template("cube.html")


@app.route("/prismvolume", methods=["GET", "POST"])
def prism():

    if request.method == "POST":
        l = (request.form.get("lv"))
        w = (request.form.get("wv"))
        h = (request.form.get("hv"))
        if not l:
            return apology("Must input a value")
        if not w:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        l = int(l)
        w = int(w)
        h = int(h)
        if l <= 0:
            return apology("Must input a valid, positive length value")
        if w <= 0:
            return apology("Must input a valid, positive width value")
        if h <= 0:
            return apology("Must input a valid, positive height value")
        prismvolume = calcvolume(0,l,w,h,0,"Rectangular Prism")
        return render_template("volumesolved.html", volumeans=prismvolume, shape="Rectangular Prism")
    else:
        return render_template("prism.html")


@app.route("/cylindervolume", methods=["GET", "POST"])
def cylinder():

    if request.method == "POST":
        r = (request.form.get("rv"))
        h = (request.form.get("hv"))

        if not r:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        r = int(r)
        h = int(h)

        if r <= 0:
            return apology("Must input a valid, positive radius value")
        if h <= 0:
            return apology("Must input a valid, positive height value")
        cylindervolume = calcvolume(0,0,0,h,r,"Cylinder")
        return render_template("volumesolved.html", volumeans=cylindervolume, shape="Cylinder")
    else:
        return render_template("cylinder.html")


@app.route("/conevolume", methods=["GET", "POST"])
def cone():

    if request.method == "POST":
        r = request.form.get("rv")
        h = request.form.get("hv")

        if not r:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        r = int(r)
        h = int(h)
        if r <= 0:
            return apology("Must input a valid, positive radius value")
        if h <= 0:
            return apology("Must input a valid, positive height value")
        conevolume = calcvolume(0,0,0,h,r,"Cone")
        return render_template("volumesolved.html", volumeans=conevolume, shape="Cone")
    else:
        return render_template("cone.html")


@app.route("/pyramidvolume", methods=["GET", "POST"])
def pyramid():

    if request.method == "POST":
        l = (request.form.get("lv"))
        w = (request.form.get("wv"))
        h = (request.form.get("hv"))
        if not l:
            return apology("Must input a value")
        if not w:
            return apology("Must input a value")
        if not h:
            return apology("Must input a value")
        l = int(l)
        w = int(w)
        h = int(h)
        if l <= 0:
            return apology("Must input a valid, positive length value")
        if w <= 0:
            return apology("Must input a valid, positive width value")
        if h <= 0:
            return apology("Must input a valid, positive height value")
        pyramidvolume = calcvolume(0,l,w,h,0,"Pyramid")

        return render_template("volumesolved.html", volumeans=pyramidvolume, shape="Pyramid")
    else:
        return render_template("pyramid.html")


@app.route("/spherevolume", methods=["GET", "POST"])
def sphere():

    if request.method == "POST":
        r = (request.form.get("rv"))
        if not r:
            return apology("Must input a value")
        r = int(r)
        if r <= 0:
            return apology("Must input a valid, positive radius value")
        spherevolume = calcvolume(0,0,0,0,r,"Sphere")
        return render_template("volumesolved.html", volumeans=spherevolume, shape="Sphere")
    else:
        return render_template("sphere.html")
