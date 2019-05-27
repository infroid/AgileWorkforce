python manage.py makemigrations
git add .
git commit -m "Made some changes"
git push origin master
git push heroku master
python manage.py migrate