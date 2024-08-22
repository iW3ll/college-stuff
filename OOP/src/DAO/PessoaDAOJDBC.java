
package dao;

import java.util.ArrayList;
import java.util.List;
import java.sql.*;
import modelo.Pessoa;




public abstract class PessoaDAOJDBC implements PessoaDAO {

    Connection conexao = null;
    PreparedStatement sql = null;
    ResultSet rset = null;
    
    @Override
    public int inserir(Pessoa pessoa) {
        StringBuilder sqlBuilder = new StringBuilder();
        sqlBuilder
                .append("INSERT INTO modelo(descricao) ")
                .append("VALUES (?)");
     
        String insert = sqlBuilder.toString();
        int linha = 0;
        try {  
            linha = DAOGenerico.executarComando(insert, pessoa.getDescricao());
        } catch (SQLException | ClassNotFoundException e) {
        } 
        
        return linha;
    }

    @Override
    public int editar(Pessoa pessoa) {
        StringBuilder sqlBuilder = new StringBuilder();
        sqlBuilder
                .append("UPDATE pessoa SET ")
                .append("nome = ?")
                .append("data_nascimento = ?")
                .append("WHERE codigo = ?");
        
        String update = sqlBuilder.toString();
        int linha = 0;
        try {
            
            linha = DAOGenerico.executarComando(update, pessoa.getNome(), pessoa.getDataNascimento(), pessoa.getCodigo());
        } catch (SQLException | ClassNotFoundException e) {

        }
        return linha;
    }

    @Override
    public int apagar(int codigo) throws ClassNotFoundException, SQLException, SQLIntegrityConstraintViolationException{
        StringBuilder sqlBuilder = new StringBuilder();
        sqlBuilder
                .append("DELETE FROM pessoa ")
                .append("WHERE codigo = ?");
        
        String delete = sqlBuilder.toString();
        int linha = 0;
                 
         linha = DAOGenerico.executarComando(delete, codigo);
    

        return linha;
    }

    @Override
    public List<Pessoa> listar() {
        String select = "SELECT * FROM pessoa";

        List<Pessoa> pessoas = new ArrayList<Pessoa>();

        try {        
            rset = DAOGenerico.executarConsulta(select);


            while (rset.next()) {

                Pessoa pessoa = new Pessoa();
                pessoa.setCodigo(rset.getInt("codigo"));
                pessoa.setDescricao(rset.getString("Nome"));

                pessoas.add(pessoa);

            }
        } catch (SQLException | ClassNotFoundException e) {

        }
        return pessoas;
    }

}
    

