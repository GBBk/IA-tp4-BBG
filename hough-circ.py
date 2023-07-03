import cv2 
import numpy as np 
  
# Imagen original
img = cv2.imread('motor.png', cv2.IMREAD_COLOR) 
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Gris', gray)
cv2.waitKey(0)

# Ahora se aplica un filtro pasabajas de 3x3
gray_blurred = cv2.blur(gray, (9, 9)) 
cv2.imshow('Borrosa', gray_blurred )
cv2.waitKey(0)

# parámetros:
# imagen a la cual se le va a aplicar
# método de detección a realizar, generalmente se utiliza HOUGH_GRADIENT
# relación inversa de la resolución del acumulador
# diatancia mínima (en pixeles) entre el centro y las circunferencias detectadas
# param1, En el caso de utilizar el método HOUGH_GRADIENT, es el umbral máximo en la detección de bordes por Canny
# param2, En el caso de utilizar el método HOUGH_GRADIENT, es el umbral mínimo en la detección de bordes por Canny
# minRadius, es el radio mínimo del círculo (no se interpone con la distancia mínima entre el centro y la circunferencia)
# maxRadius, es el radio mínimo del círculo (no se interpone con la distancia mínima entre el centro y la circunferencia)
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40) 
  
# Revisar que el método haya regresado algún valor
if detected_circles is not None: 
  
    # Convertir los parámetros el círculo a, b, y r en enteros de 16 bits
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    # Recorrer todos los círculos detectados
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Dibujar la circunferencia
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
        
        # Mostrar los datos de las circunferencias
        print("Centro ({:}, {:}), radio = {:}".format(a, b, r))
  
        # Dibujar un círculo pequeño alrededor del centro
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
		# Mostrar las circunferencias detectadas
        cv2.imshow("Detección de circunferencias", img) 
        cv2.waitKey(0) 
        
cv2.destroyAllWindows()