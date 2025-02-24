# YOLO 11 - Instalación y Uso

## Instalación de YOLO 11

YOLO 11 es básicamente una librería de Python, por lo que podemos instalarla usando `pip`. En el vídeo lo hemos instalado con los siguientes comandos:

```bash
# Linux: Creamos un entorno virtual para tener todas las dependencias en un solo entorno 
virtualenv env

#Windows: Creamos un entorno virtual para tener todas las dependencias en un solo entorno 
python -m virtualenv env

# Activamos el entorno virtual LINUX
source env/bin/activate

# Activamos en entorno virtual en Windows
env\Scripts\activate

# Instalamos YOLO 11
pip install ultralytics===8.3.27
```

---

## Procesando imágenes con YOLO 11 y Python

Después de la instalación, hemos procesado imágenes programáticamente con Python para crear nuestras propias aplicaciones. Esto es similar a lo que hemos hecho por línea de comandos.

---

## Procesando vídeo de la webcam con YOLO 11 y Python

Para ampliar el ejemplo, hemos procesado vídeo en tiempo real desde la webcam para ver la potencia de YOLO 11.

---

## Fine-tuning con YOLO 11

El fine-tuning es un proceso esencial en el campo de la visión por computadora (y redes neuronales en general). Para la mayoría de nosotros, sería imposible entrenar una red neuronal como YOLO desde cero. Sin embargo, si necesitamos crear una red neuronal que reconozca nuestros propios objetos, no es necesario entrenar un nuevo modelo desde cero. En su lugar, podemos partir de una versión existente de YOLO y entrenarla con nuestro propio conjunto de datos.

Para esto, ejecutamos YOLO en modo 'train' (entrenamiento), partiendo del modelo 'yolo11s'. Específicamente, definimos el parámetro 'epochs' (número de veces que se procesará todo el set de entrenamiento) y 'batch' (cantidad de imágenes que se procesarán en paralelo en cada iteración). También se debe proporcionar el archivo de configuración de datos `data.yaml`, donde se especifican los detalles del conjunto de datos a utilizar.

---

¡Listo! Ahora puedes usar YOLO 11 para procesar imágenes, vídeos en tiempo real y entrenarlo con tus propios datos.

Fernando Valdés Herrera.
