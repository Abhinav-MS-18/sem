import org.apache.xmlrpc.webserver.WebServer;
import org.apache.xmlrpc.server.XmlRpcServer;
import org.apache.xmlrpc.server.PropertyHandlerMapping;

public class JavaServer { 

   public Integer sum(int x, int y){
      return Integer.valueOf(x + y);
   }

   public String getCurrentTime(){
      return java.time.LocalDateTime.now().toString();
   }

   public static void main (String [] args){
   
      try {

         System.out.println("Attempting to start XML-RPC Server...");
         
         WebServer server = new WebServer(80);
         XmlRpcServer xmlRpcServer = server.getXmlRpcServer();
         PropertyHandlerMapping phm = new PropertyHandlerMapping();
         phm.addHandler("sample", JavaServer.class);
         xmlRpcServer.setHandlerMapping(phm);
         server.start();
         
         System.out.println("Started successfully.");
         System.out.println("Accepting requests. (Halt program to stop.)");
         
      } catch (Exception exception){
         System.err.println("JavaServer: " + exception);
      }
   }
}