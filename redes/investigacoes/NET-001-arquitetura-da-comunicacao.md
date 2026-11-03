# NET-001 — Arquitetura da comunicação de dados

- **Pilar:** Engenharia de Redes.
- **Estado:** em investigação; síntese documental inicial, sem ensaios executados.
- **Data:** 2026-10-26.
- **Aplicação:** formação geral; não constitui diagnóstico do cliente RW-NET-001.

## 1. Pergunta e âmbito
Como a informação percorre redes locais e inter-redes, desde a aplicação ao meio físico? Estudar separadamente protocolos, equipamentos, responsabilidades das camadas e tecnologias de acesso.

## 2. Investigar — fontes primárias
- [RFC 1122 — Requirements for Internet Hosts, Communication Layers (IETF, 1989)](https://www.rfc-editor.org/rfc/rfc1122.html) — camadas de enlace, Internet e transporte. Documento histórico de referência; verificar RFCs posteriores e atualizações antes de tomar decisões de implementação.
- [IEEE 802.3 — Ethernet](https://www.ieee802.org/3/) — família de normas de redes Ethernet.
- [IEEE 802.11 — Wireless LAN](https://www.ieee802.org/11/) — família de normas Wi-Fi nas camadas MAC e PHY. Página do WG enumera a revisão 802.11-2024.
- [Cisco NetAcad — Packet Tracer](https://www.netacad.com/catalogs/learn/cisco-packet-tracer) — ferramenta educacional para simular e observar dispositivos e protocolos.
- [Cisco NetAcad — Catálogo de formação](https://www.netacad.com/pt/catalogs/learn) — Networking Basics e cursos introdutórios.

**Registo:** URLs consultadas para criar esta síntese; não se afirma leitura integral dos documentos normativos nem realização dos cursos.

## 3. Compreender — modelo conceptual

Em comunicação IP, aplicações produzem dados processados por protocolos de transporte (como TCP ou UDP), por IP e por uma tecnologia de acesso local (como Ethernet ou Wi-Fi). O meio de comunicação transporta sinais físicos. Routers encaminham pacotes entre redes; switches Ethernet comutam quadros dentro do domínio de enlace correspondente; pontos de acesso permitem associação por rádio e interligação à rede de distribuição conforme arquitetura concreta.

| Camada funcional (simplificada) | Questão | Exemplos |
|---|---|---|
| Aplicação | Que serviço procura comunicar? | HTTP, DNS |
| Transporte | Como comunicam processos? | TCP, UDP |
| Internet | Como alcançar redes remotas? | IPv4, IPv6 |
| Enlace e físico | Como transportar dados no salto local? | Ethernet, Wi-Fi |

A rede do ISP e a rede Wi-Fi interna não são sinónimos. Pode existir um problema no acesso sem fios local sem falha no serviço externo; também pode acontecer o inverso. Afirmar a causa de um caso real exige testes adequados.

## 4. Questionar
- Um sinal Wi-Fi forte garante boa taxa de dados? Não: estudar interferências, airtime, largura de canal, ruído, recursos do dispositivo e congestionamento.
- Um teste de velocidade externo mede apenas Wi-Fi? Não: inclui várias partes do percurso e efeitos de carga.
- Uma falha de DNS equivale a interrupção física? Não necessariamente.
- O mesmo equipamento pode implementar várias funções (router, switch e AP)? Investigar implementação e limitações concretas.

## 5. Comparar — perguntas em aberto
Comparar Ethernet vs Wi-Fi sob distância, ambiente eletromagnético, latência, throughput, instalação e mobilidade. Comparar repetidor, AP Ethernet e Mesh apenas no contexto de requisitos medidos e topologia confirmada.

## 6. Modelar
Topologia conceptual: dispositivo → enlace local (Ethernet/Wi-Fi) → router/gateway → ISP → rede remota → servidor. Trata-se de modelo simplificado, não de topologia completa, nem de uma constatação no cliente Clubnet.

## 7. Decidir
**Decisão pedagógica:** aprofundar mecanismos TCP/IP e meios locais antes de configurar equipamento de cliente. **Decisão comercial ou técnica do caso RW-NET-001:** pendente por ausência de medições.

## 8. Construir — laboratório proposto, NÃO executado
Utilizar Packet Tracer para desenhar 2 computadores, 1 switch, 1 router, e opcionalmente um access point de teste. Registar versão do software, endereços, portas, configurações e ficheiro `.pkt` somente depois de o abrir no simulador. Não inventar artefactos `.pkt` validados.

## 9. Testar — critérios, NÃO executado
Validar endereçamento; ping dentro e fora da sub-rede; captura/observação de ARP, ICMP e, quando suportado, DHCP; introduzir falhas controladas (gateway errado, porta desligada); documentar evidências e recuperação. Não publicar resultados antes da execução.

## 10. Consolidar e rever
Próximas unidades: Ethernet e switching; IPv4/IPv6 e encaminhamento; Wi-Fi/RF; medições; Linux/RouterOS; documentação de visita técnica. Manter este documento atualizado com revisão de fontes e resultados reais, sem misturar o relato de cliente com demonstrações de laboratório.
