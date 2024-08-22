
package dao;

import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
import java.util.List;
import modelo.Pessoa;


public interface PessoaDAO {
    public int inserir(Pessoa pessoa);
    public int editar(Pessoa pessoa);
    public int apagar(int codigo) throws ClassNotFoundException, SQLException, SQLIntegrityConstraintViolationException;
    public List<Pessoa> listar();
    public Pessoa listar(int codigo);
}
