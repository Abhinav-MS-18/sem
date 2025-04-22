before compiling the xmlrpc programs, make sure that all ".jar" files and java program are in the same folder.


this program retreives time from the server.

then compile them using the below command lines.
these lines include the classpath containing the name of all the ".jar" files.

run the Server on Windows and the Client Program on Ubuntu

NOTE: for windows, the jar files are separated using ';' and in linux , we will use ':'

Make sure to change the IP address in the JavaClient program before compiling

for finding ip-address in windows, use ipconfig, and replace the ip address , in the code it will be like this <ip-addr-of-windows>



In Windows,

javac -cp "xmlrpc-client-3.1.2.jar;xmlrpc-common-3.1.2.jar;ws-commons-util-1.0.2;xmlrpc-server-3.1.2.jar;commons-logging-1.2.jar" JavaServer.java 

java -cp ".;xmlrpc-client-3.1.2.jar;xmlrpc-common-3.1.2.jar;ws-commons-util-1.0.2.jar;xmlrpc-server-3.1.2.jar;commons-logging-1.2.jar" JavaServer




In Ubuntu(Linux),

javac -cp ".:xmlrpc-client-3.1.2.jar:xmlrpc-common-3.1.2.jar:ws-commons-util-1.0.2.jar:xmlrpc-server-3.1.2.jar:commons-logging-1.2.jar" JavaClient.java

java -cp ".:xmlrpc-client-3.1.2.jar:xmlrpc-common-3.1.2.jar:ws-commons-util-1.0.2.jar:xmlrpc-server-3.1.2.jar:commons-logging-1.2.jar" JavaClient