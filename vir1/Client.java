import java.rmi.registry.*;

public class Client {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            Calculator calc = (Calculator) registry.lookup("CalculatorService");
            System.out.println("Result = " + calc.add(10, 50));
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
