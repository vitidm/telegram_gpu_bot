En scrapping_test.py utilizaremos:
        DATABASE_URL = os.environ.get('DATABASE_URL')
        connection = psycopg2.connect(DATABASE_URL)     en las filas 50 y 51 antes del commit en la función connect() para que funcione en el cloud con postgree de Heroku

En caso contrario, para ejecutarlo en local con nuestra propia bbdd:
conn = psycopg2.connect(
                user="postgres",
                password="47468180K.",
                host="localhost",
                port="5432",
                database="postgres")
                connection = conn

Apuntamos a la bbdd de Heroku:
conn = psycopg2.connect(
                user="ibvqhpzxrcovsc",
                password="153004037d5e3e3238451ec4ec6c87dc78fda17838a5dcc4695de1d122e9146f",
                host="ec2-3-220-214-162.compute-1.amazonaws.com",
                port="5432",
                database="d9l22mp3132eec")

------------------------------------------------------------

COMANDOS PARA LOGS DE HEROKU
git init
heroku login
heroku git:remote -a telegram_bot_gpus
git add .
git push heroku main
