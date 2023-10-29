# Imagem base do Python (Vai rodar no python versao 3.8)
FROM python:3.8

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia todos os arquivos do diretorio local para o diretorio dentro do conteiner
COPY . .

# Atualizando pip
RUN pip install --upgrade pip

# Instalando as dependências da api
RUN pip install -r requirements.txt

# Indicando a porta 
EXPOSE 8000