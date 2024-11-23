class Phonebook:
    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add_user(self, name, number):
        #ajustes nas mensagens de retorno
        if any(char in name for char in ['#', '@', '!', '$', '%']):
            return 'Nome inválido'

        if len(number) == 0:
            return 'Número inválido'
            # ajuste na verificação do número.

        if name in self.entries:
            return 'Nome já existe'

        self.entries[name] = number
        return 'Número adicionado'

    def procura_nome(self, name):
        #ajustes nas mensagens de retorno
        if any(char in name for char in ['#', '@', '!', '$', '%']):
            return 'Nome inválido'

        return self.entries.get(name, 'Nome não encontrado')
        #verificação para nomes inexistentes


    def get_nomes(self):
        return list(self.entries.keys())

    def get_numeros(self):
        return list(self.entries.values())

    def limpar_lista(self):

        self.entries = {'POLICIA': '190'}
        return 'Phonebook limpo'
        #inserir os resultados iniciais após limpar a lista

    def buscar_nome(self, search_name):

        return [(name, number) for name, number in self.entries.items() if search_name in name]

    def lista_phonebook(self):
        return dict(sorted(self.entries.items()))

    def lista_phonebook_invertida(self):
        return dict(sorted(self.entries.items(), reverse=True))
        #ordenação dos dicionários
    def delete(self, name):

        if name in self.entries:
            del self.entries[name]
            return 'Número deletado'
        return 'Nome não encontrado'
        # verificação para evitar erros ao tentar excluir nomes inexistentes.

    def change_number(self, name, number):

        if any(char in name for char in ['#', '@', '!', '$', '%']):
            return 'Nome inválido'

        if len(number) == 0:
            return 'Número inválido'

        if name not in self.entries:
            return 'Nome não encontrado'

        self.entries[name] = number
        return 'Número alterado'

    def get_name_by_number(self, number):

        for name, num in self.entries.items():
            if num == number:
                return name
        return 'Número não encontrado'
