import java.util.*;
import org.apache.xmlrpc.client.XmlRpcClient;
import org.apache.xmlrpc.client.XmlRpcClientConfigImpl;

public class JavaClient {
   public static void main (String [] args) {
   
      try {
         XmlRpcClientConfigImpl config = new XmlRpcClientConfigImpl();
         config.setServerURL(new java.net.URL("http://<ip-addr-of-windows>:80/RPC2")); //change the ip-address here
         XmlRpcClient client = new XmlRpcClient();
         client.setConfig(config);

         Object result = client.execute("sample.getCurrentTime", new Vector<>());

         String currentTime = (String) result;
         System.out.println("The current time is: " + currentTime);

      } catch (Exception exception) {
         System.err.println("JavaClient: " + exception);
      }
   }
}