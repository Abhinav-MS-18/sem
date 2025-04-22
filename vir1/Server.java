import java.rmi.registry.*;

public class Server {
    public static void main(String[] args) {
        try {
            Calculator stub = new CalculatorImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("CalculatorService", stub);
            System.out.println("Server is running");
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
