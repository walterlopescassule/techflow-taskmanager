# -*- coding: utf-8 -*-

class TaskManager:
    def __init__(self):
        # Banco de dados simulado em memória utilizando dicionário
        self.tasks = {}
        self.counter = 1

    def create_task(self, title, description, priority="Normal"):
        """Cria uma nova tarefa no sistema para a startup de logística"""
        if not title:
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        task = {
            "id": self.counter,
            "title": title,
            "description": description,
            "priority": priority,  # Requisito adicionado na mudança de escopo
            "status": "A Fazer"
        }
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def read_tasks(self):
        """Retorna a lista com todas as tarefas registradas"""
        return list(self.tasks.values())

    def update_status(self, task_id, new_status):
        """Modifica o status de uma tarefa (A Fazer -> Em Progresso -> Concluído)"""
        valid_statuses = ["A Fazer", "Em Progresso", "Concluído"]
        if new_status not in valid_statuses:
            raise ValueError("Status inválido.")
        
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = new_status
            return self.tasks[task_id]
        return None

    def delete_task(self, task_id):
        """Remove uma tarefa do sistema através do ID"""
        if task_id in self.tasks:
            return self.tasks.pop(task_id)
        return None