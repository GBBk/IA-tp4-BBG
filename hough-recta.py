import cv2
import numpy as np

# Lectura de la imagen
img = cv2.imread('motor.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

# Se convierte a nivel de grises
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gray)
cv2.waitKey(0)

# Se aplica la detección de bordes por Canny 
edges = cv2.Canny(gray,50,150,apertureSize = 3)
cv2.imshow('Bordes', edges)
cv2.waitKey(0)

# La función HpughLines permitirá obtener el arreglo 2D requerido
# en la transformada de Hough
# Parámetros (en orden):
# imagen a la que se le aplicará la transformación
# La resolución de la distancia para el acumulador (r)
# La resolución en ángulo para el acumulador (theta)
# umbral para conocer si se toma como línea o no
# posteriormente se incluye un None en 
# este parámetro, ya que en caso contrario, el programa falla
lines = cv2.HoughLines(edges,1,np.pi/180,150,None)

if lines is not None:
    # Recorrer los resultados
    for i in range(0, len(lines)):
        # Obtener los valores de rho (distacia)
        rho = lines[i][0][0]
		# y de theta (ángulo)
        theta = lines[i][0][1]
		# guardar el valor del cos(theta)
        a = np.cos(theta)
		# guardar el valor del sen(theta)
        b = np.sin(theta)
		# guardar el valor de r cos(theta)
        x0 = a*rho
		# guardar el valor de r sen(theta)
        y0 = b*rho
		# Ahora se recorrerá de -1500 a 1500 pixeles
        x1 = int(x0 + 1500*(-b))
        y1 = int(y0 + 1500*(a))
        x2 = int(x0 - 1500*(-b))
        y2 = int(y0 - 1500*(a))
        
		# Mostrar los valores hallados
        print("({},{})  ({},{})".format(x1,y1, x2,y2))
		# Generar las líneas para montarlas en la imagen original
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# Mostrar la imagen original con todas las líneas halladas
cv2.imshow('Rectas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()