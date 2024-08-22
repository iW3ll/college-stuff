
package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;


public abstract class DAOGenerico {
    
    
    
    public static Connection getConexao() throws SQLException, ClassNotFoundException {
        String USUARIO = "root";
        String SENHA = "computer";
        String URL_BANCO = "jdbc:mysql://localhost:3306/papelaria";
        //Faz com que a classe seja carregada pela JVM
        Class.forName("com.mysql.cj.jdbc.Driver");

        return DriverManager.getConnection(URL_BANCO, USUARIO, SENHA);
    }
    
     public static int executarComando(String query, Object... params) throws SQLException, ClassNotFoundException {
         int result;
        try (PreparedStatement sql = (PreparedStatement)  getConexao().prepareStatement(query)) {
            for (int i = 0; i < params.length; i++) {
                sql.setObject(i+1,params[i]);
            }   result = sql.executeUpdate();
        }
        return result;
     }
     
     public static ResultSet executarConsulta(String query, Object... params) throws SQLException, ClassNotFoundException {
        PreparedStatement sql = (PreparedStatement)  getConexao().prepareStatement(query);
        for (int i = 0; i < params.length; i++) {
            sql.setObject(i+1,params[i]);
        }
        return sql.executeQuery();
    }
    
}
