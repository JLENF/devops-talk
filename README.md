# DevOps Talk

Este projeto visa demonstrar os conceitos básicos de uma aplicação web com testes funcionais e integração contínua utilizando ferramentas DevOps. Ele inclui um exemplo de aplicação Flask que gera dados aleatórios e um pipeline de CI no GitHub Actions para validar o código e executar testes.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Conta no GitHub
- Docker / Podman
- Kubernetes

## Instalação

Clone o repositório:
```bash
git clone https://github.com/seu-usuario/devops-talk.git
cd devops-talk
```

Crie um virtualenv:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a Aplicação

Para iniciar a aplicação Flask, execute:
```bash
python app.py
```

A aplicação estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Testes

Para executar os testes, execute:
```bash
python test_app.py
```

## Pipeline de Integração Contínua

Este projeto inclui uma configuração de GitHub Actions para CI. O pipeline é acionado em push ou pull request e executa as seguintes etapas:

1. Checkout do código.
2. Configuração do Python.
3. Instalação das dependências.
4. Execução do Flake8 para verificação de estilo.
5. Execução dos testes funcionais.

A configuração do pipeline está no arquivo `.github/workflows/python-app.yml`.

## Container / Kubernetes

Gerar imagem do container:
```bash
podman build -t devops-talk:latest .
```

Deploy Kubernetes:
Gerar imagem do container:
```bash
kubectl create ns devops-talk
kubectl apply -f deployment.yaml -n devops-talk
```

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
