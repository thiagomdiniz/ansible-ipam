IPAM
=========

Role criada para interegir com a solução SolarWinds IPAM.

Requirements
------------

pip install orionsdk

pip install netaddr

Referencias:

- https://github.com/solarwinds/orionsdk-python
- http://solarwinds.github.io/OrionSDK/schema/
- https://github.com/solarwinds/OrionSDK/wiki/IPAM-4.7-API
- https://github.com/solarwinds/OrionSDK

Role Variables
--------------

- ipam_user - Usuário para se conectar à API do IPAM. (default: api)
- ipam_password - Senha para se autenticar na API do IPAM.
- subnet - Endereço da subrede a ser utilizada na consulta de IP livre. (default: 10.180.200.0)
- cidr - Máscara da subrede a ser utilizada na consulta por IP livre (aceita os formatos 22 ou 255.255.252.0) (default: 22)

Dependencies
------------

Como não encontramos um módulo Ansible pronto para interação com o IPAM,
criamos um script Python (get_free_addr.py) e colocamos dentro da estrutura de diretórios
da Role para permitir o funcionamento adequado.

Author Information
------------------

Thiago Murilo Diniz <thiagodiniz.info@gmail.com>
