package test;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Test1 {
    public static long stringPlus() throws IOException {
        long startTime = System.currentTimeMillis();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
        for(int i = 0; i < 1000000; i++) {
            bw.write(i + "\n");
        }

        bw.flush();
        bw.close();

        return System.currentTimeMillis() - startTime;
    }

    public static long stringNewLine() throws IOException {
        long startTime = System.currentTimeMillis();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
        for(int i = 0; i < 1000000; i++) {
            bw.write(Integer.toString(i));
            bw.newLine();
        }

        bw.flush();
        bw.close();

        return System.currentTimeMillis() - startTime;
    }
    public static long stringBuild() throws IOException {
        long startTime = System.currentTimeMillis();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
       
        for(int i = 0; i < 1000000; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(i);
            sb.append("\n");
            bw.write(sb.toString());
        }

        bw.flush();
        bw.close();
        
        return System.currentTimeMillis() - startTime;
    }
    public static long stringBuildAll() throws IOException {
        long startTime = System.currentTimeMillis();
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
       
        for(int i = 0; i < 1000000; i++) {
            sb.append(i);
            sb.append("\n");
        }
        
        bw.write(sb.toString());
        bw.flush();
        bw.close();

        return System.currentTimeMillis() - startTime;
    }
    public static long printLn() throws IOException {
        long startTime = System.currentTimeMillis();

        for(int i = 0; i < 1000000; i++) {
            System.out.println(i);
        }
       
        return System.currentTimeMillis() - startTime;
    }
    public static void main(String[] args) throws IOException {
        File file = new File("./Java11/test/Test1.txt");
        FileWriter fw = new FileWriter(file, true);

        long result;
        int option = 5;

        if (option == 1){
            result = stringPlus();
            fw.write("String Plus 결과 : " + result + "\n");
        }

        else if (option == 2){
            result = stringNewLine();
            fw.write("String New Line 결과 : " + result + "\n");
        }

        else if (option == 3){
            result = stringBuild();
            fw.write("String Build 결과 : " + result + "\n");
        }
        else if (option == 4){
            result = stringBuildAll();
            fw.write("String Build All 결과 : " + result + "\n");
        }
        else if (option == 5){
            result = printLn();
            fw.write("printLn 결과 : " + result + "\n");
        }

        fw.flush();
        fw.close();
    }
    
}
