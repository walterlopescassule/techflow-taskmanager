# TechFlow TaskManager 🚀

Sistema de gerenciamento de tarefas desenvolvido sob os princípios da Engenharia de Software para otimização dos fluxos operacionais de uma startup de logística.

## 🎯 Objetivo e Escopo Inicial
O objetivo do projeto é fornecer uma ferramenta visual e funcional de controle de tarefas (CRUD). O escopo original englobava a criação, listagem, atualização de status e exclusão de demandas logísticas cotidianas.

## 🔄 Metodologia Ágil
Adotou-se o uso do quadro Kanban via **GitHub Projects** para gerenciar o fluxo de desenvolvimento das tarefas divididas entre *To Do*, *In Progress* e *Done*, limitando gargalos e distribuindo a carga de trabalho do time.

## ⚠️ Gestão de Mudanças e Alteração de Escopo
* **Justificativa:** Durante o acompanhamento do projeto, percebeu-se que fretes de caráter emergencial e de alto impacto financeiro se misturavam com entregas padrão.
* **Nova Feature:** Inclusão do campo opcional de `priority` (Prioridade Crítica) na criação de tarefas para destacar visualmente os cards mais urgentes no painel.

## 🛠️ Como Executar os Testes Localmente
1. Instale o PyTest através das dependências:
   ```bash
   pip install -r requirements.txt