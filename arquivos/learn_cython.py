#pip install Cython
#python setup.py build_ext --inplace
import modulo_cythons.cumprimenta as comprimente

def main():
    nome:str = input("qual seu nome ")
    print(comprimente.cumprimentar(nome))

if __name__ == '__main__':
    main()