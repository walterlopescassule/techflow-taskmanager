# TechFlow TaskManager

> Sistema CRUD de Gerenciamento de Tarefas Logísticas voltado para a otimização de fluxos operacionais em startups de logística.

## 🚀 Sobre o Projeto
O **TechFlow TaskManager** foi concebido para centralizar e coordenar o ciclo de vida de tarefas operacionais, mitigando falhas de comunicação e provendo visibilidade em tempo real sobre o estado de cada demanda. O sistema foi robustecido com um atributo de priorização (`priority`) para destacar fretes emergenciais de alto impacto financeiro.

### 🛠️ Pilares de Engenharia Adotados
*   **Metodologia Ágil:** Fluxo de trabalho gerenciado via quadro Kanban (GitHub Projects).
*   **Controle de Versão:** Rastreabilidade incremental utilizando Git e a convenção *Conventional Commits*.
*   **Qualidade & Integração Contínua (CI):** Testes unitários automatizados com `PyTest` e esteira de verificação integrada via `GitHub Actions`.

---

## 📦 Estrutura do Repositório
*   `src/`: Contém toda a lógica de negócio e os módulos CRUD do sistema logístico.
*   `tests/`: Agrupa a suíte de testes automatizados e asserções de validação.
*   `.github/workflows/`: Configuração da esteira automatizada de build e testes.

---

## 🔧 Instalação e Execução Local

### 1. Clonar o Repositório
```bash
git clone [https://github.com/walterlopescassule/techflow-taskmanager.git](https://github.com/walterlopescassule/techflow-taskmanager.git)
cd techflow-taskmanager
