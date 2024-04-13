# CS50 Equations
#### YouTube demo: https://youtu.be/dKqZgGuM210?si=IjWT4t-4n4WKfji6
##### By Jessica Hagihara

## What is it?
###### This website is designed to help users calculate certain equations, such as the Quadratic Formula, Area and Volume equations for various shapes. This is a quick way to get simple answers that might otherwise take longer to calculate by hand.

## Home Page
### Functions
###### This is the main page for the CS50 Equations website. It includes the main navbar at the top and also includes descriptions for each equation that the website offers.
### Design
###### The navbar at the top allows the users to easily navigate through the functions of the website. TUnder a pool themed border, there is also a welcome message that introduces the users to the website. Under that, there are three buttons that the users can click that explain the three equations. Under the bottom pool themed border, there is a meme of a confused lady doing math, which was added for comedic purposes.
### Code
###### * Layout.html was used to set up the navbar, headers, and the title. It also includes links to bootstrap and the styles.css file used for the css design of the website, and also allows the website to be mobile-user friendly
###### * Home.html is an extension of layout.html that displays the text of the welcome message. It uses a class in styles.css that changes the font color and alignment. It also includes a dropdown button from the bootstrap library used to explain the different equations. It also includes the pool themed borders used by inserting images into paragraph tags. At the end, it includes the img tag that was used to add the confused lady meme and a footer that says my name and where I'm from

## Quadratic Formula
### Design
###### In between beach themed borders, there is the quadratic equation setup and input fields for each coefficient that the user must input. This was added to aid the user and clarify what was meant to be in the input fields. Under these borders is a picture of what a quadratic function looks like for further user clarification. Upon clicking the solve button, the user is then redirected to a page that between borders includes the quadratic formula and the positive and negative root answers that was calculated. The quadratic formula was included for further user clarification. Styles.css was used similarly to the homepage.
### Code
###### * In app.py, a function was created that allows user input through POST and then GET. The quadratic() function gets user input from quadratic.html. If the user doesn't input anything, an apology message inspired by CS50 finance will be printed. When the user inputs coefficients, the calcquadratic function is called and then these answers are submitted to quadsolved.html where the answer is printed out
###### * In helpers.py, a function called calcquadratic(pos or neg) is called with three arguments (the a,b,c coefficients). It calculates the number under the sqrt and if it's negative then the answer is not real, if it's positive, the rest of the quadratic formula is output. The function returns two values, one is whether or not the squared value was negative and the second is the answer. App.py then checks if it was a real answer and sends the real answer or the not real answer to quadsolved.html

## Area
### Design
###### In between beach themed borders, there is a picture of 2d shapes in the coordinate plane that signifies area. There is a dropdown field that lets users choose which shape they want to find the area of. Once the shape is clicked on, the user is redirected to a shape specific page that includes a labeled diagram of the shape and another input field to input variables. Once solved, the user is redirected to another page that outputs the area. There is a picture of Area 51 which is a play on words since area is being solved for, included for comedic purposes. Classes used for font size and color is from the styles.css file and has similar style related syntax as the previous pages.
### Code
###### * If the request method is POST, app.py will gather input from the user as to what shape they chose from the form tag and option tag from area.html. If the shape is a square, for exmaple, the user will then be redirected to the square.html page which includes the diagram of the square and then input fields for the variables needed to calculate area. There, input from square.html is sent to square() in app.py
###### * In square(), an apology is sent back if the user did not input variables. If they did, the calcarea function is called and the answer is sent to areasolved.html that outputs the area
###### * Calcarea() in helpers.py takes a few arguments related to the specific variable names for each shape, as well as the name of the shape. If the shape is a specific one, a certain formula and those specific variables are used to calculate the area. For those answers including pi, the answer is cast to a string and the char of pi is concatened to the answer and returned.
##### * This process is similar for all the shapes (rectangle.html, triangle.html, etc.)

## Volume
### Design
###### In between water themed borders, there is an image of 3d shapes that the user can find the volume of. There is a dropdown menu similar to the area page where the user can choose from a few shapes to find the volume of. Once the user clicks choose shape, the user will be redirected to a shape specific page where there is a labeled diagram and input fields for the variables. After hitting solve, the user will be redirected to a page that outputs the volume answer. There is a picture of the volume sound bar used for iPhone's as a play on words, for comedic purposes. CSS was used similarly to the previous pages
### Code
###### * In app.py, the volume() is used to see if the user uses POST, and if so, will get what shape the user selected from the volume.html select tag. Then, depending the the shape selected, will redirect the user to the shape specific app.py path and then redirect that to the shape specific html page. For example, if the user chooses a cube, the user will be sent to cube.html and then app.py's cube() will look for the variable inputs.
###### * Once given those inputs, cube() will call upon calcvolume() from helpers.py. Calcvolume() takes a few arguments such as the variables and the shape type. Depending on the shape chosen, a different formula will be used to calculate the volume. This function returns the volume answer and sends that back to cube() which sends that back to volumesolved.html
###### * volumesolved.html then outputs the volume answer that was sent by cube(). This process is then repeated for the other shapes and their respective html and app.py routes.

## Other Info
###### * Python, HTML, CSS, flask, jinja were used to create this website. Bootstrap was also utilized for certain deisgn features.
###### * In the future, would like to include more complicated equations and automate more complex processes like derivation, integration, etc.
###### * For cs50 final, thank you :)