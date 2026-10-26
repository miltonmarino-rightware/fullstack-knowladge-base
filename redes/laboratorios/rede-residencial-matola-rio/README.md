# RIGHTWARE | Simulacao de rede residencial — Matola-Rio

**Versao:** 0.1 — modelo conceptual, ainda nao validado em campo.

## Objetivo
Simular uma rede local residencial com Internet representada conceptualmente, router, switch, ponto de acesso sem fios e clientes. O segundo AP e opcional ate levantamento de cobertura.

## Topologia
```text
[ISP / Internet - apenas representacao]
              |
        [Router 2911]
       LAN 192.168.50.1
              |
        [Switch 2960]
         /         \
      [PC]        [AP1] ... clientes Wi-Fi
                    |
             [AP2 opcional via switch]
```

## Plano IPv4
- LAN: `192.168.50.0/24`
- Router LAN: `192.168.50.1`
- Switch gestao: `192.168.50.2`
- AP principal: `192.168.50.3`, caso a interface permita IP estatico
- Clientes: DHCP `192.168.50.100-199`
- SSID de laboratorio: `RIGHTWARE-LAB`; configurar WPA2-PSK AES com segredo criado localmente

## Procedimento no Packet Tracer
1. File > New e abrir o ambiente Logical.
2. Adicionar router 2911, switch 2960, Access Point-PT, PC-PT e Laptop-PT.
3. Interligar router G0/0 -> switch F0/1; PC -> switch F0/2; AP -> switch F0/3 com cabos Copper Straight-Through.
4. Aplicar `router_basico_ios.txt` na CLI do router, ajustando a interface se necessario.
5. Aplicar `switch_basico_ios.txt` na CLI do switch.
6. No PC, configurar DHCP em Desktop > IP Configuration.
7. No AP, configurar SSID e seguranca Wi-Fi. Configurar o laptop para associar-se ao SSID e obter IP por DHCP.
8. Testar ping para `192.168.50.1`, `192.168.50.2` e entre os clientes.
9. Guardar o ficheiro real em File > Save As como `RIGHTWARE-CASA-CLIENTE-V01.pkt`.

## Limites do modelo
- Localizacao da casa e referencia Quinta Happy foram fornecidas em capturas do utilizador; sem levantamento do interior.
- Nao foi validada a localizacao actual do router, cablagem, potencia de sinal, paredes ou distancias.
- O Packet Tracer valida conectividade logica, nao faz previsao realista de propagacao Wi-Fi.
- Nao se assume qualquer ligacao a Quinta Happy.
- O acesso Internet real exige configuracao do equipamento ISP e das interfaces WAN; representar uma cloud isolada nao fornece acesso a Internet.
- Por privacidade, a captura de satelite do imovel **nao foi publicada neste repositorio publico**.
- **Este repositorio ainda nao contem um .pkt valido.** O formato nativo deve ser produzido no Cisco Packet Tracer.

## Levantamento futuro
Inventariar ONT/router ISP, pontos de energia, areas e pisos, materiais de paredes, RSSI/SNR, bandas e canais, latencia, velocidades, viabilidade de Ethernet/PoE e orcamento. A escolha do AP adicional depende dessas medidas.
