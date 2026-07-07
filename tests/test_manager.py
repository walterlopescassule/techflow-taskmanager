# -*- coding: utf-8 -*-
import pytest
from src.task_manager import TaskManager

def test_create_task_success():
    """Valida se uma tarefa é criada corretamente com status inicial padrão"""
    manager = TaskManager()
    task = manager.create_task("Entrega Urgente", "Rota Zona Sul - SP")
    assert task["id"] == 1
    assert task["title"] == "Entrega Urgente"
    assert task["status"] == "A Fazer"

def test_create_task_empty_title():
    """Garante que o sistema bloqueia a criação de tarefas sem título"""
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.create_task("", "Descrição da rota sem título")

def test_update_status_success():
    """Testa a transição de estados de uma tarefa dentro do fluxo Kanban"""
    manager = TaskManager()
    task = manager.create_task("Carga Pesada", "Rota Porto de Santos")
    updated = manager.update_status(task["id"], "Em Progresso")
    assert updated["status"] == "Em Progresso"