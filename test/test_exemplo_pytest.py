class TestPhonebook:

    def test_add_1(self):
        assert 1 == 2
        # Deve ser igual para passar --> 1 == 1

    def test_add_2(self):
        assert "1" == 1
        # precisa ser string para passar --> "1" == "1"

    def test_add_3(self):
        assert "F" == "f"
        # precisam ser iguais para passar --> 'F' == 'F'

    def test_add_4(self):
        assert False
        # precisa ser true para passar -- > assert True

    def test_add_5(self):
        assert True
        # passou