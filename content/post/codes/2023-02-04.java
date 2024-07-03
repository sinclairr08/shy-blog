package test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Test2 {
    public static long useCharAt(String s){
        long startTime = System.currentTimeMillis();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.append(s.charAt(i));
        }

        return System.currentTimeMillis() - startTime;
    }
    public static long useCharArray(String s){
        long startTime = System.currentTimeMillis();

        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            sb.append(c);
        }

        return System.currentTimeMillis() - startTime;
    }

    public static long useChars(String s){
        long startTime = System.currentTimeMillis();

        StringBuilder sb = new StringBuilder();
        
        s.chars().forEach((c) -> sb.append((char)c));

        return System.currentTimeMillis() - startTime;
    }

    public static void generateString() throws IOException {
        File file = new File("./Java11/test/Test2In.txt");
        FileWriter f = new FileWriter(file, true);

        for (int i = 0; i < 10000000; i++) {
            f.write((char)(Math.random() * 26 + 97));
        }

        f.flush();
        f.close();

        return;
    }
    
    public static void main(String[] args) throws IOException {
        // generateString();

        File readFile = new File("./Java11/test/Test2In.txt");
        BufferedReader br = new BufferedReader(new FileReader(readFile));

        String s = br.readLine();
        br.close();

        File writeFile = new File("./Java11/test/Test2Out.txt");
        FileWriter fw = new FileWriter(writeFile, true);

        long result;
        int option = 3;

        if (option == 1){
            result = useCharAt(s);
            fw.write("Char At 결과 : " + result + "\n");
        }

        else if (option == 2){
            result = useCharArray(s);
            fw.write("Char Array 결과 : " + result + "\n");
        }

        else if (option == 3){
            result = useChars(s);
            fw.write("Chars 결과 : " + result + "\n");
        }

        fw.flush();
        fw.close();

        return;
    }
    
}
