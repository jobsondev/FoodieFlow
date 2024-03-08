import pytest
from unittest.mock import Mock
from app.core.model.categoria import Categoria as CategoriaModel
from app.core.usecases.categoria_service_impl import CategoriaServiceImpl


class TestCategoriaServiceImpl:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.mock_repo = Mock()
        self.mock_db = Mock()
        self.mock_categoria = CategoriaModel(nome="Teste")
        self.service = CategoriaServiceImpl(categoria_repository=self.mock_repo)

    def test_create_categoria(self):
        # Configura o mock para retornar None quando get_categoria_by_nome for chamado
        self.mock_repo.get_categoria_by_nome.return_value = None

        result = self.service.create_categoria(self.mock_db, self.mock_categoria)

        # Verifica se o método create_categoria do repositório foi chamado com os argumentos corretos
        self.mock_repo.create_categoria.assert_called_once_with(self.mock_db, self.mock_categoria)

    def test_create_categoria_already_exists(self):
        # Configura o mock para retornar um objeto quando get_categoria_by_nome for chamado
        self.mock_repo.get_categoria_by_nome.return_value = self.mock_categoria

        # Verifica se a exceção é lançada quando a categoria já existe
        with pytest.raises(Exception):
            self.service.create_categoria(self.mock_db, self.mock_categoria)
