import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;



public class Main
{
    public static void main(String[] args)
    {
        Connection connection = null;
        try
        {
            // create a database connection
            connection = DriverManager.getConnection("jdbc:sqlite:/Users/jasonrocha/Documents/CSE111/Project/project.db");
            Statement stat = connection.createStatement();
            statement.setQueryTimeout(30);  // set timeout to 30 sec.
            System.out.println("connected database.");
            ResultSet rs = statement.executeQuery("select * from beer as Beer");
            
            while(rs.next()){
                System.out.println("hello");
                System.out.println(rs.getString("Beer"));
                
            }
            rs.close();

        }
        catch(SQLException e)
        {
            // if the error message is "out of memory",
            // it probably means no database file is found
            System.err.println(e.getMessage());
        }
        finally
        {
            try
            {
                if(connection != null)
                    connection.close();
            }
            catch(SQLException e)
            {
                // connection close failed.
                System.err.println(e.getMessage());
            }
        }
    }
    
    

//    public static void createTable(){
//
//    }
}
