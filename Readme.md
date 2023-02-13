# Batalha Naval
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

Este projeto tem como objetivo atualizar o projeto desenvolvido em 2021 para a disciplina CET080 - Computação Gráfica. Através do OpenGl simular um dado rolando sobre a tela e mostrando uma face *aleatória*.

Conteúdo:
- Tecnologias
- Instalação/Execução
- Instruções
- Autores
- Organização do projeto
- License

## Tecnologias
Esse projeto utiliza as seguintes bibliotecas:

- python
- numpy
- pyopengl
- pillow
- sys

## Instalação/Execução
Foi utilizado o [Python](https://www.python.org/) v3.11.

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create -f environment.yml
```

- Ativar
```sh
conda activate rolling_dices_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requirements.txt para criar o ambiente virtual.

- Criar ambiente virtual
```sh
python -m venv rolling_dices_venv
```

- Ativar
```sh
source ./rolling_dices_venv/bin/activate
```

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```

### Execução
- Navegar até a pasta de destino
```sh
cd rolling_dices
```

- Execute o programa
```sh
python __init__.py
```

## Instruções
Após iniciar o programa aperte o 'Espaço' do teclado que o dado rolará, cada vez que bater em uma extremidade mudará sua cor.

## Autores
Projeto desenvolvido pelo Dev:

- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Organização do projeto
```sh
.rolling_dices
    ├── License
    ├── Readme.md
    ├── rolling_dices
    │   ├── __init__.py
    │   ├── index
    │   │   ├── Dice.py
    │   │   └── Rolling.py
    │   └── media
    │       ├── dice_1.png
    │       ├── dice_2.png
    │       ├── dice_3.png
    │       ├── dice_4.png
    │       ├── dice_5.png
    │       └── dice_6.png
    └── utils
        ├── environment.yml
        └── requirements.txt
```

## License
MIT