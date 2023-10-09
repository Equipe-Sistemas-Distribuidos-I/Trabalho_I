# Smart home simulada utilizando Sockets

Este é uma sistema que simula um ambiente de smart home, com alguns dispositivos, ele utiliza socket TCP e UDP para fazer as comunicações entre dispositivos e utiliza protocol buffers para serializar as mensagens, além disso existe um gateway com serviço de descoberta de equipamentos.

## Como usar

### Requisitos

- Python 3.x

### Exemplo de Uso

1. Abra um terminal.
2. Navegue até o diretório onde os arquivos `servidor.py` esta localizado.

```bash
  cd Trabalho_I/Parte_2
```

1. abra um terminal e execute.

```bash
  python ar_condicionado.py
```

2. abra outro terminal e execute o gateway

```bash
  python ambiente.py
```

3. por ultimo abra outro terminal e execute o client para assim poder interagir como ambiente

```bash
  python client.py
```

Com isso nós estaremos inicializando um dispositivo(ar condicionado) em um terminal e nos outros terminais estaremos iniciando nosso gateway e nosso client.

Para utilizar o cliente basta seguir as instruções na interface.
