package com.adrian.entity;

import java.util.Scanner;

public class Account {

    private double balance = 5000;

    public void deposit(Scanner input) {

        System.out.print("Ile pieniędzy chcesz wpłacić na konto: ");
        double money = input.nextDouble();

        balance += money;

        System.out.println("Pieniądze zostąły wpłacone!");
    }

    public void withdrawal(Scanner input) {

        System.out.print("Ile pieniędzy chcesz wypłacić: ");
        double money = input.nextDouble();

        if (money > balance) System.out.println("Brak wystarczających środków na koncie !!!");
        else balance -= money;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}
