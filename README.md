# MalariaDetectNet
# Projeto de Classificação de Imagens

Este é um projeto de classificação de imagens para identificar células parasitadas e não parasitadas.

## Instalação

### Instalando o Conda

1. Baixe o script do Miniconda:
    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

2. Crie e ative o ambiente Conda:
    ```bash
    conda env create -f environment.yml
    conda activate project_template
    ```

3. Para atualizar o arquivo `environment.yml`:
    ```bash
    conda env export | grep -v "^prefix: " > environment.yml
    ```

## Usando a ferramenta

Após a instalação e ativação do ambiente, você pode treinar o modelo com o comando:

```bash
python train_model.py
