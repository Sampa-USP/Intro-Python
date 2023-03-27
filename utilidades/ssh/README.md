# SSH Config: Conectando-se a um servidor SSH sem senha


Este arquivo descreve como configurar o SSH Config para se conectar a um servidor SSH sem digitar uma senha toda vez que você fizer login.

## Passo 1: Gerar um par de chaves SSH
O primeiro passo é gerar um par de chaves SSH no seu computador. As chaves SSH são usadas para autenticar a conexão com o servidor SSH. Se você já tem um par de chaves SSH, pule para o Passo 2.

Para gerar um novo par de chaves SSH, execute o seguinte comando em um terminal:

```bash
ssh-keygen
```

O comando irá solicitar que você escolha um nome para as chaves e uma senha. Aceite as opções padrão, a menos que você precise alterá-las para um caso específico.

Isso criará um par de chaves SSH público/privado em seu computador.

## Passo 2: Adicionar a chave pública ao servidor remoto
O próximo passo é adicionar a chave pública gerada no Passo 1 ao servidor remoto. Para fazer isso, copie a chave pública para a área de transferência usando o comando:

```bash
pbcopy < ~/.ssh/id_rsa.pub
```

A seguir, faça login no servidor remoto usando a senha atual e crie ou edite o arquivo ~/.ssh/authorized_keys. Em seguida, cole a chave pública copiada na etapa anterior no arquivo e salve.

Agora, você pode fazer login no servidor remoto sem digitar a senha.

## Passo 3: Configurar o SSH Config
O próximo passo é configurar o arquivo SSH Config no seu computador para se conectar ao servidor remoto sem digitar uma senha toda vez que você fizer login.

Abra ou crie o arquivo ~/.ssh/config e adicione as seguintes linhas:

```bash
Host [NOME DO HOST]
    HostName [ENDEREÇO IP OU NOME DE DOMÍNIO]
    User [NOME DE USUÁRIO NO SERVIDOR]
    IdentityFile [CAMINHO PARA O ARQUIVO DA CHAVE PRIVADA]
```

Substitua [NOME DO HOST] pelo nome do host que você deseja usar para se conectar ao servidor remoto, [ENDEREÇO IP OU NOME DE DOMÍNIO] pelo endereço IP ou nome de domínio do servidor remoto, [NOME DE USUÁRIO NO SERVIDOR] pelo nome de usuário que você usa para fazer login no servidor remoto e [CAMINHO PARA O ARQUIVO DA CHAVE PRIVADA] pelo caminho completo para o arquivo da chave privada que você gerou no Passo 1.

Salve o arquivo e feche-o.

## Passo 4: Faça login no servidor remoto
Agora você pode fazer login no servidor remoto sem digitar a senha toda vez. Para fazer isso, execute o seguinte comando em um terminal:

```bash
ssh [NOME DO HOST]
```

Isso fará com que o SSH use as informações de configuração que você especificou no Passo 3 para se conectar ao servidor remoto.

