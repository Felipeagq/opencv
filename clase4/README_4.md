# CLASE 2 DE VISIÓN ARTITFICIAL: LOGICS OPERATORS

## ¿Que aprenderemos?
- operadores bitwise:
    - NOT.
    - AND.
    - XOR.
    - OR.
- thresholding:
    - Masking.
    - Simple Threshold.

### NOT
```python
bitwiseNot = cv2.bitwise_not(circle)
```

### AND
```python
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
```

### XOR
```python
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
```

### OR
```python
bitwiseOr = cv2.bitwise_or(rectangle, circle)
```

### Masking.
```python
masked = cv2.bitwise_and(image, image, mask=mask)
```

### Threshold.
``` python
(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
```

### OTSU Thresholding.
```python
(T, threshInv) = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] otsu's thresholding value: {}".format(T))
```