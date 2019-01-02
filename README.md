### Install Project

#### 1. Install Python
```console
brew install python3
```
#### 2. Install Virtual Environment
```console
sudo pip3 install virtualenv
```
#### 3. Make project folder and setup virtual environment
```console
mkdir project
```
copy this project in project folder
```console
cd project
virtualenv venv -p python3
source venv/bin/activate
cd mysite
python manage.py makemigrations
python manage.py migrate

```
Create admin user by command
```console
python manage.py createsuperuser
```
Input username, email, password and enter 'y'.

#### 4. Run the server
```console
python manage.py runserver
```
Check localhost:8000 in web browser.<br>
Check localhost:8000/admin for admin site.
