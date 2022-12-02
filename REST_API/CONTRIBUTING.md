# CONTRIBUTING

## How to build the image

```
docker build -t <nome_da_imagem> .
```

## How to run the Dockerfile locally

```
docker run -p 5000:5000 -w /app -v "/c/<caminho_do_arquivo>:/app" <nome_da_imagem>
```