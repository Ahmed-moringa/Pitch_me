# PitchMe

## Author

[Ahmed Mohamed](https://github.com/Ahmed-moringa)

# Description
 An application that allows users submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
The pitches are organized by category. You can have different categories like movies lines, music pitch, art pitch and genaral pitches.


## User Story
1. As a user, I would like to see the pitches other people have posted.
2. As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
3. As a user, I would like to be signed in for me to leave a comment
4. As a user, I would like to receive a welcoming email once I sign up.
5. As a user, I would like to view the pitches I have created in my profile page.
6. As a user, I would like to comment on the different pitches and leave feedback.
7. As a user, I would like to submit a pitch in any category.
8. As a user, I would like to view the different categories.


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/Ahmed-moringa/Pitch_me.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd Pitch_me
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/pitchme'
  ```
4. Running the application
  ```bash
  python3 manage.py server
  ```
5. Testing the application
  ```bash
  python3 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* [Postgresql](https://www.postgresql.org/)

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## License
* *MIT License:*
* Copyright (c) 2021 **Ahmed Mohamed**