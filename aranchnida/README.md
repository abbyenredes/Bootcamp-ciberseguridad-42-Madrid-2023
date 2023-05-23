<h1 align="center"> aranchnida paso a paso </h1>

## Índice:
* [Descripción del proyecto](#descripción-del-proyecto)

* [Tecnologías utilizadas](#tecnologías-utilizadas)

* [Estado del proyecto](#Estado-del-proyecto)

* [Pseudocódigo](#Pseudocódigo)

* [Paso a paso](#paso-a-paso)

* [Recursos y bibliografía](#recursos-y-bibliografía)

## Descripción del proyecto
El objetivo de este proyecto es crear dos instrumentos de web scraping que nos permitirán extraer información automáticamente de la web y después analizarla para conocer o eliminar datos sensibles.
 Puedes utilizar funciones o librerías que te permitan crear peticiones HTTP y manejar archivos, pero la lógica de
cada programa debe estar desarrollada por ti. Es decir, utilizar **wget o scrapy** será
considerado cheat y supondrá suspender el proyecto.
### Spider
El programa spider permitirá extraer todas las imágenes de un sitio web, de manera
recursiva, proporcionando una url como parámetro.

Deberemos gestionar las siguientes opciones del programa: ./spider [-rlpS] URL

* Opción -r : descarga de forma recursiva las imágenes en una URL recibida como
parámetro.

* Opción -r -l [N] : indica el nivel profundidad máximo de la descarga recursiva.
En caso de no indicarse, será 5.

* Opción -p [PATH] : indica la ruta donde se guardarán los archivos descargados.

* En caso de no indicarse, se utilizará ./data/.

* El programa descargará por defecto las siguientes extensiones:
 
  .jpg/jpeg
 
  .png
 
  .gif
 
  .bmp

### Scorpion
recibirá archivos de imagen como parámetros y será
capaz de analizarlos en busca datos EXIF y otros metadatos, mostrándolos en pantalla.
El programa será compatible, al menos, con las mismas extensiones que gestiona spider.
Deberá mostrar atributos básicos como la fecha de creación, así como otros datos EXIF.

El formato en el que se muestren los metadatos queda a tu elección.
`./scorpion FILE1 [FILE2 ...]`

| Archivos a entregar |
|---------------------|
| spider.py |
| scorpion.py |

## Tecnologías utilizadas
* Python 3.7
* Entorno virtual de Conda

## Estado del proyecto
<h4 align="center">
:construction: Proyecto en construcción :construction:
</h4>

## Pseudocódigo
### Spider:

> #### Análisis
>> Crear un script en python que extraiga todas las imagenes de manera recursiva [.jpg/.jpeg .png .gif .bmp] de un sitio web, usando como párametro su URL. 
> #### Entrada
>> `./spider [-rlps] URL` 
>> 
>> -r: descarga de forma recursiva (basicamente significa descargarlo de forma automatica).
>> 
>> -r -l [N]: El nivel de profundidad que queremos descargar (se refiere a los números de clic que hacen falta para llegar a un contenido de la web.) el máx son 5 niveles.
>> 
>> -p [PATH]: La ruta en la que se guardará las imagenes, en caso de no poner nada sera `./data/.` por defecto.
>> 
> #### Salida
>>  Descarga de las imagenes, puede mostrar en la terminal las imagenes descargadas y al finalizar el programa abrir la carpeta donde estan alojadas dichas imagenes.

### Scorpion:

> #### Análisis
>> Crear un script en python que extraiga los metadatos y datos EXIF de las imagenes y me los muestre en pantalla.
> #### Entrada
>> `./scorpion FILE1 [FILE2 ...]` siendo file cualquier archivo de imagen.
> #### Salida
>> Mostrar en pantalla los atributos básicos como la fecha de creación y otros datos EXIF.

## Paso a paso


## Recursos y bibliografía
