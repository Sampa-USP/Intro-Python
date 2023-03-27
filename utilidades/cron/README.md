# README: Como agendar um comando SCP usando o Cron

Este README irá guiá-lo pelos passos para agendar um comando SCP usando a utilidade Cron em um sistema Unix/Linux. SCP é uma ferramenta de linha de comando que permite transferir arquivos com segurança entre servidores ou sistemas remotos.

## Passo 1: Criar o Comando SCP
O primeiro passo é criar o comando SCP que você deseja agendar. O comando deve seguir a seguinte sintaxe:
```bash
scp [opções] arquivo_origem arquivo_destino
```

Por exemplo, se você quiser copiar um arquivo chamado "arquivo.txt" de um servidor remoto com o endereço IP "192.168.0.100" para um diretório local "/home/user/backup", o comando SCP ficaria assim:

```bash
scp user@192.168.0.100:/caminho/para/o/arquivo.txt /home/user/backup
```

Certifique-se de que é possível executar o comando SCP com sucesso antes de prosseguir para o próximo passo.

## Passo 2: Criar um Script Bash
Em seguida, crie um script Bash que executará o comando SCP. Abra seu editor de texto favorito e crie um novo arquivo com o nome de sua escolha, por exemplo, "backup.sh".

Adicione o seguinte conteúdo ao arquivo:

```bash
#!/bin/bash
scp user@192.168.0.100:/caminho/para/o/arquivo.txt /home/user/backup
```

Substitua o nome de usuário, endereço IP, caminho do arquivo remoto e diretório de backup local pelos seus próprios valores.

Salve o arquivo e torne-o executável executando o seguinte comando:

```bash
chmod +x backup.sh
```

## Passo 3: Agendar o Script Bash Usando o Cron
Agora, você pode agendar o script Bash usando o Cron. Para fazer isso, abra o arquivo crontab usando o seguinte comando:

```bash
crontab -e
```

Isso abrirá o arquivo crontab em seu editor de texto padrão.

Adicione a seguinte linha ao arquivo crontab para agendar o script Bash para ser executado todos os dias às 2h da manhã:

```bash
0 2 * * * /caminho/para/backup.sh
```

Salve o arquivo crontab e saia do editor de texto.

Parabéns! Você agendou com sucesso um comando SCP usando o Cron. Agora o arquivo será transferido com segurança todos os dias no horário especificado.



