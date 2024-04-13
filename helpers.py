import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid
import math

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def calcquadraticpos(a, b, c):
    """Calculate positive root quadratic formula"""
    square = float((b**2) - ((4.0) * (a) * (c)))
    posans = 0
    negsquare = 0
    if square < 1:
        negsquare = 1
    else:
        posans = (((-1.0 * b) + (math.sqrt(square))) / (2.0 * (a)))

    return posans, negsquare


def calcquadraticneg(a, b, c):
    """Calculate negative root quadratic formula"""
    square = float((b**2) - ((4.0) * (a) * (c)))
    negans = 0
    negsquare = 0

    if square < 1:
        negsquare = 1
    else:
        negans = (((-1.0 * b) - (math.sqrt(square))) / (2.0 * (a)))

    return negans, negsquare


def calcarea(a,b,h,r,x,y,shape):
    """Calculate area"""

    area = 0

    if shape == "Square":
        area = x * x
    elif shape == "Rectangle":
        area = x * y
    elif shape == "Triangle":
        area = (b * h) / 2.0
    elif shape == "Circle":
        area = str(r**2) + "π"
    elif shape == "Trapezoid":
        area = ((a + b) / 2.0) * h

    return area


def calcvolume(x,l,w,h,r,shape):
    """Calculates volume"""

    volume = 0
    if shape == "Cube":
        volume = x * x * x
    elif shape == "Rectangular Prism":
        volume = l * w * h
    elif shape == "Cylinder":
        volume = str((r * r) * h) + "π"
    elif shape == "Cone":
        volume = str((r * r) * (h / 3.0)) + "π"
    elif shape == "Pyramid":
        volume = (l * w * h) / 3.0
    elif shape == "Sphere":
        volume = str((4.0 / 3) * (r * r * r)) + "π"

    return volume
