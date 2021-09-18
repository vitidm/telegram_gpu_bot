En el fichero de schedule, debemos de poner en el nombre "schedule.py". Para ejecutarlo en nuestro entorno local pondremos "schedule1.py"
--------------------

En scrapping_test.py utilizaremos:
        DATABASE_URL = os.environ.get('DATABASE_URL')
        connection = psycopg2.connect(DATABASE_URL)     en las filas 50 y 51 antes del commit en la función connect() para que funcione en el cloud con postgree de Heroku

En caso contrario, para ejecutarlo en local con nuestra propia bbdd:
        # conn = psycopg2.connect(
        #     user="postgres",
        #     password="47468180K.",
        #     host="localhost",
        #     port="5432",
        #     database="postgres")
        # connection = conn
