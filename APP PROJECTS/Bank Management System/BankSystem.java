import java.sql.*;
import java.util.Random;
import java.util.Scanner;

public class BankSystem {

    public static Connection connect() throws SQLException {
        String url = "jdbc:mysql://localhost:3306/banking_system";
        String username = "root";
        String password = "1506";
        return DriverManager.getConnection(url, username, password);
    }

    public static boolean login(int accountNo, String pin) {
        try (Connection conn = connect()) {
            String query = "SELECT * FROM account_details WHERE account_no = ? AND pin = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, accountNo);
            stmt.setString(2, pin);
            ResultSet rs = stmt.executeQuery();
            return rs.next();
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public static double getBalance(int accountNo) {
        try (Connection conn = connect()) {
            String query = "SELECT balance FROM account_details WHERE account_no = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setInt(1, accountNo);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                return rs.getDouble("balance");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return 0.0;
    }

    public static void deposit(int accountNo, double amount) {
        try (Connection conn = connect()) {
            String query = "UPDATE account_details SET balance = balance + ? WHERE account_no = ?";
            PreparedStatement stmt = conn.prepareStatement(query);
            stmt.setDouble(1, amount);
            stmt.setInt(2, accountNo);
            stmt.executeUpdate();

            String transactionQuery = "INSERT INTO transactions (account_no, type, amount) VALUES (?, ?, ?)";
            PreparedStatement transactionStmt = conn.prepareStatement(transactionQuery);
            transactionStmt.setInt(1, accountNo);
            transactionStmt.setString(2, "deposit");
            transactionStmt.setDouble(3, amount);
            transactionStmt.executeUpdate();

            System.out.println("Deposited " + amount + " successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void withdraw(int accountNo, double amount) {
        try (Connection conn = connect()) {
            double currentBalance = getBalance(accountNo);
            if (currentBalance >= amount) {
                String query = "UPDATE account_details SET balance = balance - ? WHERE account_no = ?";
                PreparedStatement stmt = conn.prepareStatement(query);
                stmt.setDouble(1, amount);
                stmt.setInt(2, accountNo);
                stmt.executeUpdate();

                String transactionQuery = "INSERT INTO transactions (account_no, type, amount) VALUES (?, ?, ?)";
                PreparedStatement transactionStmt = conn.prepareStatement(transactionQuery);
                transactionStmt.setInt(1, accountNo);
                transactionStmt.setString(2, "withdraw");
                transactionStmt.setDouble(3, amount);
                transactionStmt.executeUpdate();

                System.out.println("Withdrew " + amount + " successfully.");
            } else {
                System.out.println("Insufficient funds!");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void showMenu(int accountNo) {
        Scanner scanner = new Scanner(System.in);
        boolean loggedIn = true;

        while (loggedIn) {
            double currentBalance = getBalance(accountNo);
            System.out.println("Welcome! Your current balance is: " + currentBalance);
            System.out.println("1. Withdraw Money");
            System.out.println("2. Deposit Money");
            System.out.println("3. Exit");

            System.out.print("Select an option: ");
            int option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    withdraw(accountNo, withdrawAmount);
                    break;
                case 2:
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    deposit(accountNo, depositAmount);
                    break;
                case 3:
                    loggedIn = false;
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        scanner.close();
    }

    // Signup functionality
    private static void signUp(Connection conn) {
        try {
            Scanner sc = new Scanner(System.in);

            // Generate unique account number
            long accountNumber;
            do {
                accountNumber = generateRandomAccountNumber();
            } while (accountExists(conn, accountNumber));

            // Generate random PIN
            int pin = generateRandomPin();

            System.out.println("Your Account Number is: " + accountNumber);
            System.out.println("Your PIN is: " + pin);

            System.out.print("Enter Name: ");
            String name = sc.nextLine();

            System.out.print("Enter Email: ");
            String email = sc.nextLine();

            System.out.print("Enter Phone: ");
            String phone = sc.nextLine();

            System.out.print("Enter Address: ");
            String address = sc.nextLine();

            System.out.print("Enter Date of Birth (YYYY-MM-DD): ");
            String dob = sc.nextLine();

            PreparedStatement ps = conn.prepareStatement(
                    "INSERT INTO account_details (account_no, pin, balance) VALUES (?, ?, ?)");
            ps.setLong(1, accountNumber);
            ps.setInt(2, pin);
            ps.setDouble(3, 0.0); // Initial balance

            int rows = ps.executeUpdate();
            if (rows > 0) {
                PreparedStatement ps2 = conn.prepareStatement(
                        "INSERT INTO personal_details (account_no, name, email, phone, address, dob) VALUES (?, ?, ?, ?, ?, ?)");
                ps2.setLong(1, accountNumber);
                ps2.setString(2, name);
                ps2.setString(3, email);
                ps2.setString(4, phone);
                ps2.setString(5, address);
                ps2.setDate(6, Date.valueOf(dob));

                ps2.executeUpdate();

                System.out.println("Account created successfully! Your Account Number is: " + accountNumber);
                System.out.println("Your PIN is: " + pin);
            } else {
                System.out.println("Failed to create account. Please try again.");
            }

            ps.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Generate a random 10-digit account number
    private static long generateRandomAccountNumber() {
        Random random = new Random();
        return Math.abs(random.nextLong() % 10000000000L);
    }

    // Generate a random 4-digit PIN
    private static int generateRandomPin() {
        Random random = new Random();
        return 1000 + random.nextInt(9000); // Ensures a 4-digit PIN
    }

    // Check if an account number already exists
    private static boolean accountExists(Connection conn, long accountNumber) {
        try {
            PreparedStatement ps = conn.prepareStatement(
                    "SELECT 1 FROM account_details WHERE account_no = ?");
            ps.setLong(1, accountNumber);

            ResultSet rs = ps.executeQuery();
            boolean exists = rs.next();

            rs.close();
            ps.close();

            return exists;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Bank System");
        System.out.println("1. Log In");
        System.out.println("2. Sign Up");

        System.out.print("Select an option: ");
        int choice = scanner.nextInt();

        try (Connection conn = connect()) {
            if (choice == 1) {
                System.out.print("Enter Account Number: ");
                int accountNo = scanner.nextInt();
                System.out.print("Enter PIN: ");
                String pin = scanner.next();

                if (login(accountNo, pin)) {
                    System.out.println("Login successful!");
                    showMenu(accountNo);
                } else {
                    System.out.println("Invalid account number or PIN.");
                }
            } else if (choice == 2) {
                signUp(conn);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        scanner.close();
    }
}

/* SQL Commands to create database and tables:

CREATE DATABASE IF NOT EXISTS bank_system;

USE bank_system;

CREATE TABLE IF NOT EXISTS account_details (
    account_no INT PRIMARY KEY,
    pin VARCHAR(4) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0.0
);

CREATE TABLE IF NOT EXISTS personal_details (
    account_no INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15),
    address TEXT,
    dob DATE,
    FOREIGN KEY (account_no) REFERENCES account_details(account_no)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_no INT,
    type VARCHAR(10), -- 'deposit' or 'withdraw'
    amount DECIMAL(10, 2),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_no) REFERENCES account_details(account_no)
);

*/
