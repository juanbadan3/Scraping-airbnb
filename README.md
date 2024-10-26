# Proceso de Scraping de Propiedades

![web-scraping](https://github.com/user-attachments/assets/634cdd58-1a0c-44df-b05c-1b0455c39e29)

Este documento detalla el proceso de scraping implementado para extraer datos de propiedades vacacionales de Airbnb en Barcelona.

## Estructura del Proyecto
- `scraping.py`: Código de scraping de propiedades.
- `merge_data_final.csv`: Dataset final consolidado.
- `airbnb_barcelona.csv`: Dataset original obtenido del scraping.
- `ETL.ipynb`: Pipeline de ETL (extracción, transformación, carga).
- `EDA.ipynb`: Análisis exploratorio de datos.
- `requirements.txt`: Dependencias del proyecto.

## Configuración del entorno
1. Crear un entorno virtual:
   ```bash
   python -m venv prueba_tecnica

  Activar el entorno:
    
          
    Windows: prueba_tecnica\Scripts\activate
  
          
Instalar dependencias:


    pip install -r requirements.txt




## Descripción del Script

- **scraper.py**: Script que utiliza Selenium para extraer información de propiedades en Barcelona.
- Extrae los siguientes datos:
  - Nombre de la propiedad
  - Ubicación
  - Precio por noche
  - Comodidades
  - Puntuación de reseñas

## Configuración

1. Instalar las dependencias necesarias:

   ```bash
   pip install selenium
   pip install pandas
  
## Requisitos

- Python 3.x
- Selenium
- pandas
- WebDriver para Chrome (ChromeDriver)
- Bibliotecas: `csv`, `time`, `traceback`

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu máquina.
2. Instala Selenium usando pip:
3. instala pandas usando pip

   ```bash
   pip install selenium
   pip installpandas

   
Descarga ChromeDriver desde [aquí](https://chromedriver.chromium.org/downloads) y asegúrate de que sea compatible con la versión de tu navegador Chrome.

Coloca el ejecutable de ChromeDriver en tu PATH o en el mismo directorio que el script.


## Uso

    Clona el repositorio:

    git clone <url_del_repositorio>
    cd <nombre_del_repositorio>
## Ejecuta el script:

    python scraper.py
Una vez completado, encontrarás el archivo properties_data.csv en el directorio del proyecto, que contendrá los datos extraídos.
Ejecución
Ejecuta el script:

## Funcionamiento del Script
**Configuración del Controlador**: Se inicializa el controlador de Chrome y se carga la URL de búsqueda de propiedades.

**Esperas de Elementos**: Utiliza funciones de espera para asegurar que los elementos de la página estén completamente cargados antes de interactuar con ellos.

**Extracción de Datos**: Extrae información relevante de cada propiedad, incluyendo:

- Nombre
- Ubicación
- Precio
- Número de huéspedes
- Número de habitaciones
- Número de camas
- Número de baños
- Puntuación
  
  **Navegación**: Permite navegar a través de múltiples páginas de resultados.

  **Guardar en CSV**: Los datos extraídos se guardan en un archivo CSV.

## Notas
La estructura de la página web de Airbnb puede cambiar con el tiempo, lo que puede requerir ajustes en los selectores XPath utilizados en el código.
Asegúrate de cumplir con los términos de servicio de Airbnb al utilizar este scraper.

## Manejo de Paginas
El script navega a través de las propiedades y hace clic en cada una para extraer la información. Se maneja la paginación regresando a la página anterior después de extraer los datos.

## Desafíos Encontrados
- Manejo de ventanas emergentes.
  
- Tiempo de carga de las páginas.+

- No todas las propiedades contaban con la informacion completa.

- Solo habian dispobibles 68 propiedades en barcelona, no las 100 requeridad.

# Proceso de Limpieza de Datos


Este documento describe el proceso de limpieza de los datasets obtenidos.

## Archivos

- `scraping.py`: Código de scraping de propiedades.
- `merge_data_final.csv`: Dataset final consolidado.
- `airbnb_barcelona.csv`: Dataset original obtenido del scraping.
- `ETL.ipynb`: Pipeline de ETL (extracción, transformación, carga).
- `EDA.ipynb`: Análisis exploratorio de datos.
- `requirements.txt`: Dependencias del proyecto.


## Limpieza Realizada

- Eliminación de caracteres innecesarios en la columna de precio.
- Eliminación de filas con valores nulos.
- Cambio del formato de las fechas.
- Eliminar caracteres innecesarios.
- Creacion de columnas auxiliares.
- Visualizacion y correccion de inconsistencias.
- Union de Dataframes
- Creacion de una Base de Datos en Mysql

## Ejecución

Ejecuta el script:

      ETL.ipynb 

# Proceso ETL

Este documento detalla el proceso de ETL (Extracción, Transformación y Carga) realizado sobre los datasets.

## Archivos

- **ETL.ipynb**: Script para realizar el proceso ETL.
- **merged_data.csv**: Dataset consolidado.

## Proceso

1. Carga de datasets limpios de propiedades y reservas.
2. Fusión de los datasets en un solo archivo.

## Ejecución

Ejecuta el script:

    python ETL.ipynb
    
# Análisis Exploratorio de Datos (EDA)

Este documento describe el proceso de Análisis Exploratorio de Datos (EDA) realizado sobre el dataset consolidado de propiedades vacacionales y reservas.

## Objetivo

El objetivo de este EDA es obtener una comprensión profunda de los datos, identificar patrones, tendencias y posibles áreas de mejora en el desempeño de las propiedades vacacionales en Barcelona.

## Archivos

- **EDA.ipynb**: Script que realiza el análisis exploratorio.
- **merged_data_final.csv**: Dataset consolidado utilizado para el análisis.

## Herramientas Utilizadas

- Python 3.x
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`

## Análisis Realizados

El análisis incluye, pero no se limita a:

1. **Distribución de Precios**: Visualización de la distribución de precios de las propiedades para identificar rangos de precios comunes.
   
2. **Relación entre Precio y Puntuación**: Análisis de cómo el precio afecta la puntuación de las propiedades. Esto puede ayudar a determinar si hay una correlación positiva entre ambos.

3. **Cantidad de Habitaciones y Precio**: Evaluación de cómo el número de habitaciones afecta el precio. Se pueden visualizar los datos mediante gráficos de dispersión.

4. **Ubicación de las Propiedades**: Análisis de la ubicación de las propiedades en un mapa o mediante gráficos de barras para identificar las áreas más populares.

5. **Análisis de Reservas**: Si se incluye el dataset de reservas, se puede analizar la cantidad de reservas por propiedad y cómo se relaciona con las propiedades disponibles.

## Ejecución

Para realizar el análisis, ejecuta el siguiente comando:


    python EDA.ipynb

Esto generará visualizaciones y estadísticas descriptivas que ayudarán a entender el comportamiento de los datos.

## Ejemplos de Visualizaciones
**Histograma de Precios**: Un gráfico que muestra la distribución de precios de las propiedades.
**Gráfico de Dispersión**: Visualización que muestra la relación entre el precio y la puntuación de las propiedades.
**Gráfico de Barras**: Un gráfico que ilustra el número de propiedades en diferentes ubicaciones.
## Conclusiones
El proyecto proporciona un pipeline completo para la recopilación, limpieza y análisis de datos, permitiendo al usuario tomar decisiones informadas basadas en datos externos y propios.

El EDA proporciona una base sólida para la toma de decisiones estratégicas, ayudando a identificar tendencias y áreas de mejora en la oferta de propiedades vacacionales. Los resultados pueden utilizarse para ajustar la estrategia de precios, identificar propiedades subrepresentadas o mejorar la experiencia del cliente.

## Desafíos Encontrados


**Bloqueo por parte del sitio web durante el scraping**: El sitio web bloqueaba las solicitudes debido a demasiadas peticiones en un corto período de tiempo.

**Datos Faltantes**: Se manejaron adecuadamente los datos faltantes para evitar sesgos en el análisis.

**Datos duplicados en las propiedades**: El scraping y la fusión de datasets genero duplicados de algunas propiedades.

**Fusión de datasets con diferentes esquemas**:Al intentar fusionar los datasets, se encontraron esquemas de las tablas no coinciden del todo

**Gestión de fechas y formatos incorrectos**: Se encontraron problemas con formatos inconsistentes (fechas en formato DD-MM-YYYY vs YYYY/MM/DD).





