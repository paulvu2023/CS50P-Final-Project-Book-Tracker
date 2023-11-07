# CS50P-Final-Project-Book-Tracker
This was my final project for Harvard's CS50P from March 2023. I left all of the code the same.

#### Video Demo:  <https://youtu.be/_GAeIAt-2Ks>

#### Description:
It was very difficult to think of what I should do for my final project. The first question I asked myself is, "What software would I use?" I began to think of my hobbies and interests which include reading, playing volleyball, working out, and learning about business and software development. I was very excited when I thought of an idea; a fitness software. This software would ask for the user's input on their height, bodyweight, and how many days and hours a week they want to work out. Then, it would use their height and bodyweight to estimate their daily caloric intake. The days and hours a week the user inputted would be used to calculate the best workout split/routine for the user. 

The problem with the fitness software idea, was that I would be able to do it easily with a bunch of if-statements. I wanted something more challenging. I wanted something that incorporated more of the things that I learned throughout taking the CS50P course. So, I came up with the idea of a book tracking software. It's something that is valuable to something like me because I usually type out what page I'm on and what book I'm reading on my "Notes" app on my phone and it's very organized. I read my books online so I don't have a bookmark to use.

The book tracking software allows the user to input books, delete books, easily keep track of pages, write notes, and rate the books. This software creates "Book" objects with "bookname", "page", "notes", and "rating" attributes that store exactly what they sound like. These objects are stored inside a list and then that list is updated into a csv file called "books.csv". This csv file acts as a database. Because the "Book" objects stored inside the lists are erased everytime the program is done running, I needed to use a csv file to store the values inside the list after the program stops runniing. My code for my software is in "project.py". "test_project.py" contains tests for my program to ensure that each function operates correctly.
