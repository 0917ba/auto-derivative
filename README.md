# Auto-Derivative - 가장 혁신적인 미분 도구!

미분이 두려우신가요? 이제 걱정하지 마세요. 
Auto-Derivative가 있다면, 복잡한 미적분 문제도 단번에 해결됩니다!
이 강력한 라이브러리는 복잡한 합성함수도 마치 산책하듯이 간단하게 미분해줍니다.<br> 더 이상 머리를 싸매고 미분 공식을 떠올릴 필요가 없어요! 
직관적이고 간편한 사용법으로 여러분의 모든 미분 고민을 한 방에 해결해드립니다.

Auto-Derivative와 함께라면 복잡한 수식 앞에서도 미소를 지을 수 있습니다. 한 번의 클릭으로 모든 문제를 해결해주는 놀라운 이 라이브러리! 
이제는 그냥 쓰면 될 뿐이죠. 더 빠르고 더 쉽게, 프로처럼 미분하세요. 

## 😄 Usage
### Function Class
```python
from Function import *

# A parameter for function we make
x = Function.parameter()

# Define a new function
f = x**2 + 2*x + 1

# Use it!
for i in range(-10, 11):
    print(f(i))
```
```python
from Function import *
from matplotlib import pyplot as plt
import numpy as np

x = Function.parameter()
a = x**3
b = Sin(1/(x**2))
f = a * b

X = np.linspace(-0.2, 0.2, 1000)
Y = np.array([f(i) for i in X])

plt.plot(X, Y)
plt.show()
```

### Derivative
Not implemented yet

