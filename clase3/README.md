# CLASE 2 DE VISIÓN ARTITFICIAL: COLORS
## ¿Que aprenderemos?
- Others Multimedia Handle:
    - Espejo.
    - Rotación.
    - Traslación.
- Image Colored:
    - Canales de una imagen.
    - Separar una imagen en sus colores basicos (RGB).
    - Modificar el color de un pixel de la imagen.



### La forma de la imagen
```python
imagen.shape
```

### Accediendo a un pixel
```python
imagen[y,x]
```

### Cambiando el valor de un pixel
```python
imagen[y,x] = [0,0,0]
```

### Separar una imagen en sus colores
```python
(B, G, R) = cv2.split(imagen)
```

### Rotación.
```python
M = cv2.getRotationMatrix2D((ancho//2,alto//2),15,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))
```

### Traslación.
```python
M = np.float32([[1,0,100],[0,1,150]])
imageOut = cv2.warpAffine(image,M,(ancho,alto))
```

### Espejo
```python
anchoMitad = frame.shape[1] // 2
frame[:,:anchoMitad] = cv2.flip(frame[:,anchoMitad:],1)
```