python3.10 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt

docker-compose up

python3.10 manage.py migrate

python3.10 manage.py runserver
