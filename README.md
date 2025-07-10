# Gongo ⏰
*Seu Sincronizador de Foco Pessoal*

O **Gongo** é um script simples em Python criado para auxiliar na administração do tempo e em técnicas de foco, como o método Pomodoro. Ele roda em segundo plano no seu terminal e emite alertas sonoros em intervalos fixos dentro da hora.

Em vez de ser um simples cronômetro que dispara a cada X minutos a partir do início, o Gongo se **sincroniza com o relógio**. Ele dispara alertas em momentos previsíveis (por exemplo, a cada 15 minutos: às xx:00, xx:15, xx:30, xx:45), ajudando a criar um ritmo de trabalho e pausa mais natural.

## ✨ Funcionalidades

* **Alertas Sonoros:** Utiliza o sintetizador de voz nativo do seu sistema operacional para falar.
* **Sincronização com o Relógio:** Alertas em intervalos fixos e pré-definidos (`10`, `15`, `30` ou `60` minutos).
* **Mensagens Personalizáveis:** Você define exatamente o que o Gongo vai dizer.
* **Placeholders Dinâmicos:** Use `{hora}` e `{minuto}` na sua mensagem para que o Gongo anuncie o horário do alerta.
* **100% Offline:** Não requer conexão com a internet.
* **Leve e Multiplataforma:** Roda em Windows, macOS e Linux com baixo consumo de recursos.

## ⚙️ Pré-requisitos

* **Python 3.x** instalado.
* A biblioteca `pyttsx3`.

## 🚀 Instalação e Configuração

1.  Clone este repositório ou simplesmente baixe o arquivo `gongo.py` (ou o nome que você deu a ele).

2.  Abra seu terminal e navegue até a pasta onde o arquivo está salvo.

3.  Instale a dependência necessária com o seguinte comando:
    ```bash
    pip install pyttsx3
    ```

## ▶️ Como Usar

1.  Ainda no terminal, na pasta do projeto, execute o script:
    ```bash
    python gongo.py
    ```
2.  O script fará duas perguntas interativas:
    * O intervalo desejado (você deve escolher um dos valores válidos).
    * A mensagem customizada que você quer ouvir.

3.  Após responder, ele começará a rodar e exibirá o horário do próximo alerta.

4.  Para encerrar o script, simplesmente volte à janela do terminal e pressione `Ctrl+C`.

### Exemplo de Uso
```
Qual o intervalo do alerta? Escolha entre [10, 15, 30, 60]: 15
Qual a mensagem que você quer ouvir? (Use {hora} e {minuto}) 
> Hora da pausa para o café! Já são {hora} e {minuto}.

Ok! Sincronizando alertas para cada 15 minutos dentro da hora.
Pressione Ctrl+C para parar.
O próximo alerta será às 11:45:00.
```
---
```

**Como usar isso:**
1.  Crie um novo arquivo de texto na mesma pasta do seu script.
2.  Nomeie este arquivo como `README.md` (a extensão `.md` é importante).
3.  Copie e cole todo o conteúdo acima dentro desse arquivo.
4.  Salve.

Quando você subir seu projeto para o GitHub, ele vai automaticamente renderizar este arquivo, deixando a página do seu repositório super profissional.
