# py-calculus-farenheit

- [Localmente](#localmente)
- [Deploy manual](#deploy-manual)

### Localmente

Para executar estag api localmente, deve primeiramente mover para a pasta `api`, e entao iniciar o servico `flask`.

```bash
cd .\api\
flask run
```

- Host local: `localhost`
- Porta local: `5000`

### Deploy manual

```bash
cf login -a https://api.cf.br10.hana.ondemand.com -u <seu email>
cf deploy
```