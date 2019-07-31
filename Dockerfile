FROM python:3.6

# garante que a saída do python seja definida diretamente para o terminal sem armazená-lo em buffer primeiro
ENV PYTHONUNBUFFERED 1

# cria o diretório root para o projeto
RUN mkdir /code

# seta o diretório do projeto como diretório de trabalho do container
WORKDIR /code

# copia o arquivo com os pacotes para dentro do container
COPY requirements.txt /code/

# instala as dependências através do arquivo requirements.txt
RUN pip install -r requirements.txt

# copia os arquivos do diretório para dentro do container
COPY . /code/