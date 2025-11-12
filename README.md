# Descomplicando-Istio

# 📦 Service Mesh com Istio

## O que é uma Service Mesh?

Uma *service mesh* é uma camada de infraestrutura que gerencia a comunicação entre microsserviços em ambientes distribuídos, como Kubernetes. Ela oferece funcionalidades como:

- **Gerenciamento de tráfego**: roteamento inteligente, balanceamento de carga, retries e timeouts.
- **Segurança**: autenticação mútua (mTLS), controle de acesso e criptografia.
- **Observabilidade**: métricas, logs e rastreamento distribuído.
- **Resiliência**: circuit breakers, failovers e políticas de tolerância a falhas.

## O que é o Istio?

O **Istio** é uma das service meshes mais populares e robustas do ecossistema cloud native. Ele atua como uma camada de rede inteligente entre os microsserviços, sem exigir mudanças no código das aplicações.

### Principais recursos:

- 🔀 **Proxy Sidecar (Envoy)**: cada serviço recebe um proxy que intercepta e gerencia o tráfego.
- 🧠 **Plano de controle**: gerencia políticas, configurações e coleta telemetria.
- 🔐 **Segurança zero-trust**: autenticação mútua entre serviços e políticas de acesso.
- 📊 **Monitoramento avançado**: integração com Prometheus, Grafana, Jaeger, entre outros.
- ⚙️ **Integração com Kubernetes**: se encaixa perfeitamente em clusters Kubernetes.

## Como o Istio funciona?

1. **Sidecar Proxy**: o Istio injeta um proxy Envoy ao lado de cada serviço.
2. **Control Plane**: gerencia os proxies e aplica políticas.
3. **Data Plane**: os proxies formam o plano de dados por onde o tráfego passa.

## Por que usar Istio?

- 📈 Escalabilidade: facilita o crescimento de aplicações distribuídas.
- 🔒 Segurança centralizada: sem modificar o código dos serviços.
- 👀 Visibilidade total: rastreamento e métricas detalhadas.
- 🧹 Menos complexidade no código: funcionalidades como retries e circuit breakers são configuradas externamente.

---

> Este projeto está sendo desenvolvido com base no curso **Descomplicando Istio** da [LinuxTips](https://www.linuxtips.io/), que oferece uma abordagem prática e direta para dominar o Istio.
