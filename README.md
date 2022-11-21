# Reservation System Assesment

This repository is an implementation of TEST CODE TASK for Global Talents Hub.

## How to run it

1. Create a virtual environment.
2. Activate the environment and install the required libraries using the following command:
```bash
pip install -r requirements.txt
```
3. Go to reservation_system/settings.py and set up a database. For the simplicity, I have used sqlite3.
4. Migrate the database migration files using the following command:
```bash
python manage.py migrate
```
5. After running the project, you'll find a json response containing the required reservation list data in the browser. 
6. To do the unit testing of the view, run the following command:
```bash
python manage.py test reservation_system/home
```
