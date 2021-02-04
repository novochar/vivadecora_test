<h1>Instalação:</h1>

<p>Instale pip 9.0.1 ou superior, e python 3.6 ou superior
(testado com pip 9.0.1, python 3.6, no Ubunto 18.04)</p>

<p>Entre no terminal no diretório deste projeto. 
instale as dependências com o comando:</p>

```
sudo pip3 install -r requirements.txt
```

ou

```
sudo pip install -r requirements.txt
```

<h1> Execução </h1>

<p>Atualize o arquivo repositories.txt colocando <\USUARIO>\/<\NOME REPOSITORIO>\ en cada linha.</p>
<p>Execute este comando para rodar o script (estar no diretório do projeto): </p>

```
python3 main.py
```

ou

```
python main.py
```

<p> Os dados dos repositórios fica em output/[USUARIO]/[NOME REPOSITORIO].tree.txt (arvore de diretório) e output/[USUARIO]/[NOME REPOSITORIO].resume.txt (dados resumidos por tipo de arquivo)<p>

<h1>Instalação e execução com Docker Compose</h1>

<p>Caso tenha o Docker e o Docker Compose instalado, e possível executar o projeto digitando:</p>

```
sudo docker-compose up
```

ou

```
docker-compose up
```
<p>output funciona da mesma forma que na execução direta em Python</p>