/// Create a calculator that can add, subtract, multiply and divide two numbers.
/// import standard library
use std::io;
fn add (a: i32, b: i32) -> i32 {
    a + b
}

fn subtract (a: i32, b: i32) -> i32 {
    a - b
}

fn multiply (a: i32, b: i32) -> i32 {
    a * b
}

fn divide (a: i32, b: i32) -> i32 {
    a / b
}

/// ask the user for two numbers and an operation to perform
/// perform the operation on the two numbers
/// print the result
/// ask the user if they want to perform another operation
/// if they want to perform another operation, repeat the above steps
/// if they don't want to perform another operation, print a message and exit the program
/// if the user enters an invalid operation, print a message and exit the program


fn main() {
    println!("Welcome to the calculator!");
    println!("Enter two numbers and an operation to perform.");
    println!("Enter 'q' to quit.");

    let mut a = String::new();
    let mut b = String::new();
    let mut operation = String::new();

    loop {
        println!("Enter the first number:");
        io::stdin().read_line(&mut a).expect("Failed to read line");
        let a: i32 = match a.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid input.");
                continue;
            }
        };

        println!("Enter the second number:");
        io::stdin().read_line(&mut b).expect("Failed to read line");
        let b: i32 = match b.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid input.");
                continue;
            }
        };

        println!("Enter the operation to perform:");
        io::stdin().read_line(&mut operation).expect("Failed to read line");
        let operation: String = match operation.trim() {
            "q" => {
                println!("Goodbye!");
                break;
            },
            "+" => "+".to_string(),
            "-" => "-".to_string(),
            "*" => "*".to_string(),
            "/" => "/".to_string(),
            _ => {
                println!("Invalid input.");
                continue;
            }
        };

        let result = match operation.as_str() {
            "+" => add(a, b),
            "-" => subtract(a, b),
            "*" => multiply(a, b),
            "/" => divide(a, b),
            _ => {
                println!("Invalid input.");
                continue;
            }
        };

        println!("{} {} {} = {}", a, operation, b, result);
    }   // end of loop
}   // end of main
