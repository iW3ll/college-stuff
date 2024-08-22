package dao;

import modelo.Pessoa;

public class DAOFactory {
       public static PessoaDAO criarPessoaDAO() {
        return new PessoaDAOJDBC() {
            @Override
            public Pessoa listar(int codigo) {
                throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
            }
        };
    } 
       
}
