/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package classexample;

/**
 *
 * @author DETH
 */
public class Student {
    // Data fields = {name, age, GPA}
    private String name;
    private int age;
    private double GPA;
    
    // Non-Default Constructor 
//    public Student(){}
    public Student(String name){
        this.name = name;
    }
    
    // set & get methods
    // name
    public String getName(){
        return this.name;
    }
    public void setName(String newName){
        this.name = newName;
    }
    
    // age
    public int getAge(){
        return this.age;
    }
    public void setAge(int newAge){
        this.age = newAge;
    }
    
    // GPA
    public double getGPA(){
        return this.GPA;
    }
    public void setGPA(double newGPA){
        this.GPA = newGPA;
    }
    
    // Year of birth
    public int getYearOfBirth(){
        return (2016 - this.age);
    }
    
    // Design toString method
    public String toString(){
        return "Student's Name: " + this.name + "\n" +
                "Student's Age: " + this.age + "\n" +
                "Student's GPA: " + this.GPA + "\n" +
                "Student's Year of Birth: " + getYearOfBirth() + "\n";
    }
}
