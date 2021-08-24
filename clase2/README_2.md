# CLASE 2 DE VISIÓN ARTITFICIAL: BASICS
## ¿Que aprenderemos?
- Firts Steps:
    - Leer, ver y guardar una imagen.
    - Leer, ver y guardar un video.
- Multimedia Handle:
    - Recortar una imagen y video.
    - Escalar una imagen.


### Leer una imagen
```python
imagen = cv2.imread("path/to/image.jpg")
```

### Ver una imagen
```python
cv2.imshow("ventana",imagen)
```

### Guardar una imagen
```python
cv2.imwrite("name/of/image2.jpg",imagen)
```

### Capturar un video
```python
cap = cv2.VideoCapture(0)
```

### Ver un video
```python
while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
```

### Guardar un video
```python
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
```

### Recortar una iamgen
```python
imageOut = image[y1:y2,x1:x2]
```

### Escalar una imagen
```python
imageOut = cv2.resize(image,(dim_X,dim_y), interpolation=cv2.INTER_CUBIC)
```