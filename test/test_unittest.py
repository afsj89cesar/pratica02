import unittest

from src.phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()

    def test_add_entrada_valida(self):
        self.assertEqual(self.phonebook.add_user('JOAO', '12345'), 'Número adicionado')

    def test_add_nome_invalido(self):
        self.assertEqual(self.phonebook.add_user('JO@O', '12345'), 'Nome inválido')

    def test_add_nome_duplicado(self):
        self.phonebook.add_user('JOAO', '12345')
        self.assertEqual(self.phonebook.add_user('JOAO', '67890'), 'Nome já existe')

    def test_procura_nome_valido(self):
        self.phonebook.add_user('MARIA', '54321')
        self.assertEqual(self.phonebook.procura_nome('MARIA'), '54321')

    def test_procura_nome_invalido(self):
        self.assertEqual(self.phonebook.procura_nome('PEDRO'), 'Nome não encontrado')

    def test_clear(self):
        self.phonebook.add_user('JOAO', '12345')
        self.phonebook.limpar_lista()
        self.assertEqual(self.phonebook.get_nomes(), ['POLICIA'])

    def test_buscar(self):
        self.phonebook.add_user('JOAO', '12345')
        self.phonebook.add_user('MARIA', '54321')
        self.assertEqual(self.phonebook.buscar_nome('JO'), [('JOAO', '12345')])

    def test_delete_nome_existente(self):
        self.phonebook.add_user('JOAO', '12345')
        self.assertEqual(self.phonebook.delete('JOAO'), 'Número deletado')

    def test_delete_nome_nao_existente(self):
        self.assertEqual(self.phonebook.delete('PEDRO'), 'Nome não encontrado')

    def test_lista_phonebook(self):
        self.phonebook.add_user('JOAO', '12345')
        self.phonebook.add_user('MARIA', '54321')
        self.assertEqual(self.phonebook.lista_phonebook(), {'JOAO': '12345', 'MARIA': '54321', 'POLICIA': '190'})

    def test_lista_phonebook_invertida(self):
        self.phonebook.add_user('JOAO', '12345')
        self.phonebook.add_user('MARIA', '54321')
        self.assertEqual(self.phonebook.lista_phonebook_invertida(), {'POLICIA': '190', 'MARIA': '54321', 'JOAO': '12345'})

    def test_change_number_valid(self):
        self.phonebook.add_user('JOAO', '12345')
        result = self.phonebook.change_number('JOAO', '54321')
        self.assertEqual(result, 'Número alterado')
        self.assertEqual(self.phonebook.procura_nome('JOAO'), '54321')

    def test_change_number_nonexistent_name(self):
        result = self.phonebook.change_number('MARIA', '54321')
        self.assertEqual(result, 'Nome não encontrado')

    def test_change_number_invalid_number(self):
        self.phonebook.add_user('JOAO', '12345')
        result = self.phonebook.change_number('JOAO', '')
        self.assertEqual(result, 'Número inválido')

    def test_change_number_invalid_name(self):
        result = self.phonebook.change_number('J@OAO', '54321')
        self.assertEqual(result, 'Nome inválido')

    def test_get_name_by_numero_existente(self):
        self.assertEqual(self.phonebook.get_name_by_number('12345'), 'JOAO')
        self.assertEqual(self.phonebook.get_name_by_number('54321'), 'MARIA')

    def test_get_name_by_numero_inexistente(self):
        self.assertEqual(self.phonebook.get_name_by_number('99999'), 'Número não encontrado')

    def test_get_name_by_numero_duplicado(self):
        self.phonebook.add_user('PEDRO', '12345')
        # Verificar comportamento em caso de duplicação
        self.assertIn(self.phonebook.get_name_by_number('12345'), ['JOAO', 'PEDRO'])