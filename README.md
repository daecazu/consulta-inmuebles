# Servicio de consulta de inmuebles
- Analizare las tablas de la base de datos conectandome remotamente al servidor de la base de datos, por medio de comandos sql
- posteriormente se diseñara la API Rest en docker utlizando los principios de Twelve-factor app por medio de docker, se implementaran una vista y los serializadores que permitan formar los datos que se necesitan en el endpoint, se utilizaran tambien los filtros necesarios para mostrar solamente el ultimo estado de cada inmueble y solamente mostrar los inmuebles que se encuentrar en disponibles “pre_venta”,“en_venta”. en la vista se habilitara la busqueda por Año de construcción, Ciudad, Estado, 
- se realizara un test de los modelos (TDD)
- se abordara el desarrollo primero reconstruyendo el esquema de la base de datos
construida en mysql. se obtendran los modelos de la base de datos utilizando el comando "manage.py inspectdb > models.py"
- se realizara un test del primer endpoint (view), para garantizar el funcionamiento de los filtros(TDD)
- se realizara un test para el funcionamiento de los serializadores
- se implementara el primer endpoint
 
## tecnologias utilizadas
esta es una lista de las tecnologias utilizadas y estaran listadas en un archivo requirements.txt
- docker / docker-compose
- python 3.9
- django 3.2
- django rest framework DRF 3.12.4
- mysql 
- flake8 
- django-environ 0.4.5