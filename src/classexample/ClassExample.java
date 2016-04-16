package classexample;

public class ClassExample {
    
    public static void main(String[] args) {
        Student S1 = new Student("Lydeth");
        Student S2 = new Student("Pek Thon");
        Student S3 = new Student("Susilu");
        
        S1.setName("Vannlydeth");
        S1.setAge(20);
        S1.setGPA(4.0);
        
        S2.setAge(19);
        S2.setGPA(3.5);
        
        System.out.println("The students' names are: " +
                            S1.getName() + ", " +
                            S2.getName() + ", " +
                            S3.getName() + ".");
        
        System.out.println(S1.getName() + " is " + S1.getAge() + " years old.");
        System.out.println(S1.getName() + "'s GPA is " + S1.getGPA() + ".");
        System.out.println();
        
        System.out.println(S1.toString());
        System.out.println(S2.toString());
        
    }
    
}
