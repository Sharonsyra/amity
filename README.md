# Amity
This is a full stack console application that adds people and rooms to the amity system, allocates these people
to rooms, reallocates them to different rooms and adds them to a waiting list if the rooms are fully occupied.

## Getting Started
These instructions should help you run the code on your machine.

### Prerequisites
The code is written in Python3

### Installing

start by cloning the repository from GitHub:

for https use
```
$ git clone https://github.com/Sharonsyra/amity.git
```

for ssh use
```
git clone git@github.com:Sharonsyra/amity.git
```

Change Directory into the project folder
```
$ cd amity
```

Install the application's dependencies from `requirements.txt`
```
$ pip install -r requirements.txt
```

### Running the program

To browse your database, download the [sqlite browser](http://sqlitebrowser.org/)

Run the Console application by typing:
```
$ python app.py -i
```

### Major Libraries Used
- [SQLite](https://docs.python.org/2/library/sqlite3.html) - SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.
