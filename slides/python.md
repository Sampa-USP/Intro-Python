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
- tipos primitivos (int, float, str e bool);
- sintaxe básica (soma, divisão, multiplicação e exponenciação); 
- estrutura condicional e laços (if, while e for);
- estrutura de dados (dicionários e listas);
- funções (operações e escopo);
---
# "E no principio era trevas, no inicio do inicio..."
- Python : utilizaremos a partir do 3.x;
- notebook vs python :
    - python :
        - arquivo termina em .py;
        - bom para pós processamento e execução de códigos 'pesados';
        - executado por inteiro;
        ```bash
        python arquivo.py
        ```
    - notebook :
        - arquivo termina em .ipynb;
        - executado em 'células';
        - bacana para códigos que você quer conhecer seus dados
        ```bash
        jupyter notebook
        ```
---
# "E no principio era trevas, no inicio do inicio..."
- use o conda para evitar conflitos [instalar conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html);
- **JAMAIS** use o python do seu SO, instale pacotes com pip ou conda:
    - PIP Python Package Index :
    ```bash 
    pip install package_name
    ```

    - CONDA 
    ```
    conda install package_name
    ```
---
# Tipos primitivos:

- Basicamente, número e letra.
```python
2 #int
2.0 #float
True #bool
'paulo' #str
```
- Para atribuir, basta
```python
x = 2
y = 2.0
z = True
k = 'paulo'
```
- OBS : variável só deve começar com letras ou "_": 
```python
2x = 3 #ERRO!!!
@a = 3 #ERRO!!!
)a = #ERRO!!!
```
---
# Sintaxe Básica:

- Uma vez definida uma variável, o que fazer com ela ? Operações!
```python
x = 5 # x = 5
x_dot_2= x*2 # x_dot_2 = 10
x_dot_x = x*x # x_dot_x = 25
x_square = x**2 # x_square = 25

nome = 'paulo' # nome = paulo
dois_nome = 'paulo' * 2 # dois_nome = paulopaulo
soma_nome = 'andreia' + 'paulo' # soma_nome = andreiapaulo

_nome = nome + x #erro
_nome = nome + str(x) # _nome = paulo5
_nome = nome * str(x) # erro
_nome = nome * x # _nome = paulopaulopaulopaulopaulo
```
---
# Exercício 1 : 
- dadas duas variáveis, troque seus valores; **note1.ipynb**
- soma de tipos booleanos; **note1.ipynb**
- resultado de operadores aritméticos comparativos ; **note1.ipynb**
---