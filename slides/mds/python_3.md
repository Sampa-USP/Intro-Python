---
marp: true
title: Python
paginate: true
theme: default 
---
# Introdução ao Python

## Repositório : https://github.com/Sampa-USP/Intro-Python.git

## Dúvidas : https://github.com/Sampa-USP/Intro-Python/issues
---

# Sumário de hoje:
- # Numpy !!!
---

# NumPy

- NumPy &rarr; Numerical Python

- A biblioteca NumPy é uma das bases da pilha de ferramentas científicas em Python, juntamente com outras bibliotecas como Pandas, Matplotlib e Scikit-learn.

- Por que é rápido ? 
  - C/C++ no por trás dos panos;
  - vetorização (**broadcasting**);
  - memória contígua.

---
# NumPy

- O que pode ser feito com NumPy ?
  - integrais;
  - derivadas;
  - n dimensional fft;
  - escrita de arquivos;
  - correlação;
  - etc...
---

# Numpy - Hands On
- Crie um array unidimensional com os números de 0 a 9.
```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
---

# Numpy - Hands On
- Crie um array bidimensional com 3 linhas e 4 colunas preenchido com números aleatórios.
```python
import numpy as np

arr = np.random.rand(3, 4)
```

---

# Numpy - Hands On
- Calcule a média, a mediana e o desvio padrão do array abaixo:
```python
import numpy as np

arr = np.array([2, 3, 7, 9, 1, 5, 6, 8])
media = np.mean(arr)
mediana = np.median(arr)
desvio_padrao = np.std(arr)
print(f"Média: {media}\nMediana: {mediana}\nDesvio padrão: {desvio_padrao}")
```

---

# Numpy - Hands On
- Crie um array unidimensional com os números de 0 a 9 e crie outro array unidimensional com os números de 10 a 19. Concatene os dois arrays em um único array.
```python
import numpy as np

arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
arr_concatenado = np.concatenate((arr1, arr2))
```
---

# Numpy - Hands On
- Crie um array bidimensional com 3 linhas e 4 colunas preenchido com números aleatórios. Em seguida, calcule a soma de todos os elementos do array.

```python
import numpy as np

arr = np.random.rand(3, 4)
soma = np.sum(arr)
```