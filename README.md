# credenciales de funcionamiento del servicio
es necesario crear un archivo .env con la siguiente estructura en la raiz del respositorio, se dejo fuera del repositorio para evitar
dejar las credenciales expuestas en un repo público.
MYSQL_DB=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=

# Servicio de consulta de inmuebles
- Analizare las tablas de la base de datos conectandome remotamente al servidor de la base de datos, por medio de comandos sql
- posteriormente se diseñara la API Rest en docker utlizando los principios de Twelve-factor app por medio de docker, se implementaran una vista y los serializadores que permitan formar los datos que se necesitan en el endpoint, se utilizaran tambien los filtros necesarios para mostrar solamente el ultimo estado de cada inmueble y solamente mostrar los inmuebles que se encuentrar en disponibles “pre_venta”,“en_venta”. en la vista se habilitara la busqueda por Año de construcción, Ciudad, Estado, 
- se realizara un test de los modelos (TDD)
- se abordara el desarrollo primero reconstruyendo el esquema de la base de datos
construida en mysql. se obtendran los modelos de la base de datos utilizando el comando "manage.py inspectdb > models.py"
- se realizara un test del primer endpoint (view), para garantizar el funcionamiento de los filtros(TDD)
- se realizara un test para el funcionamiento de los serializadores
- se implementara el primer endpoint
- ejemplo de filtro implementado http://localhost:8000/api/v1/inmuebles?year=2018&status=en_venta&city=bogota
 
## tecnologias utilizadas
esta es una lista de las tecnologias utilizadas y estaran listadas en un archivo requirements.txt
- docker / docker-compose
- python 3.9
- django 3.2
- django rest framework DRF 3.12.4
- mysql 
- flake8
- django-environ 0.4.5
- gunircorn
### Comandos de funcionamiento de docker
- construcción del servicio de django docker-compose build
- levantar el servicio django docker-compose build
- Testing and flake8 docker-compose run --rm Django sh -c 'python manage.py test && flake8'

### problemas encontrados
- tuve un problema con la imagen python 3.9 alpine la cual no era compatible directamente con mysql e inverti mucho tiempo en la instalación de las librerias necesarias, por lo cual decidi usar la imagen de python 3.7 alpine que no presentaba este problema
- no pude filtrar solamente el estado más reciente de los inmuebles y lamentablemente aparecen varios estados de los inmuebles con estados permitidos, por lo cual no pasan las pruebas unitarias definidas

