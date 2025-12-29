from dataclasses import dataclass, asdict

@dataclass
class Tarefa:
    descricao: str
    status: str = 'Pendente'

    def concluir(self):
        self.status = 'Concluida'

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Tarefa(
            descricao=data['descricao'],
            status=data.get('status', 'Pendente')
        )
