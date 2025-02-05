
# API Planets

Este projeto é uma aplicação API basica feita na linguagem python que além de mostrar os dados dos planetas e do sol carrega as texturas de cada um.




## Funcionalidades

- Carregamento de dados e descricao de cada planeta
- Carregamento das texturas



## Documentação da API

#### Retorna todos os itens

```http
  GET /
```

#### Retorna um item

```http
  GET /${id}
```

#### Retorna a imagem de um item

```http
  GET /${id}/link
```

**Obrigatório**. O ID do item é importante para realizar as consultas GET de cada planeta e das imagens




## Stack utilizada

**Back-end:** Pandas, Flask e Openpyxl

