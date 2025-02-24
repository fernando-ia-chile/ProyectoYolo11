import cv2
import math
import ultralytics 
from pathlib import Path
import cv2
"""
    Procesando imágenes con YOLO 11 y Python
    Procesado imágenes programaticamente con Python para poder crear nuestras propias aplicaciones.
"""

model = ultralytics.YOLO("yolo11n.pt")

# Configuración de la fuente de texto
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.7
color = (0, 240, 0)
thickness = 1

# Asumiendo que el script se ejecuta desde la raíz del proyecto
img_path = Path("images") / "autopista3.jpg"
img = cv2.imread( img_path ) 
results = model(img)

# Dibujar los cuadros y etiquetas
for r in results:
    for box in r.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        confidence = math.ceil((box.conf[0]*100))
            
        cv2.rectangle(img, ( x1, y1 ), ( x2, y2 ), color, 1)
        cv2.putText(img, r.names[ int( box.cls[0] ) ]+" "+str(confidence)+"%", [ x1+4, y1+25 ], font, fontScale, color, thickness)

# Mostrar la imagen
cv2.imshow('Webcam', img)

# Esperar a que se presione la tecla 'q' para cerrar la ventana
while True:
    if cv2.waitKey(1) == ord('q'):
        break

# Cerrar la ventana
cv2.destroyAllWindows()