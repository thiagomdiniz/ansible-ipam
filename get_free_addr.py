#!/usr/bin/python

import sys
import orionsdk
from netaddr import IPAddress

# Endereco e credenciais para acesso ao IPAM
ipam_server = "ipam.yourdomain.com"
ipam_user = sys.argv[1]
ipam_password = sys.argv[2]

# Subrede a ser consultada. Ex: 10.180.200.0
subnet = sys.argv[3]

# Mascara da subrede a ser consultada. Ex: 22 ou 255.255.252.0
cidr = sys.argv[4]

# Transforma a mascara em CIDR caso tenha sido informada no padrao XXX.XXX.XXX.XXX
if len(cidr) > 2:
  cidr = IPAddress(cidr).netmask_bits()

#swis = orionsdk.SwisClient("SolarWinds-Orion","user","passwd", verify="server.pem")
swis = orionsdk.SwisClient(ipam_server, ipam_user, ipam_password)

#aliases = swis.invoke('Metadata.Entity', 'GetAliases', 'SELECT B.Caption FROM Orion.Nodes B')
#print(aliases)

#result = swis.query("SELECT TOP 10 IPAddress FROM Orion.Nodes")
#for node in result['results']:
#  print(node)

print(swis.invoke(
       'IPAM.SubnetManagement',
       'GetFirstAvailableIp',
       subnet,
       cidr
       )
)
