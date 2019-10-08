package com.adrian.component;

import com.adrian.entity.Account;

import java.util.Scanner;

public class Menu {

    private boolean displayMenu = true;
    private Scanner input = new Scanner(System.in);
    private Account account = new Account();

    public void displayMenu() {

        while (displayMenu) {

            System.out.println("Witam w bankomacie!!");
            System.out.println("1. Wpłać środki na konto.");
            System.out.println("2. Wypłać środki z konta. ");
            System.out.println("3. Sprawdź saldo.");
            System.out.println("4. Wyjdź");
            System.out.println();
            System.out.print("Wybierz operację: ");

            serveMenu();
        }
    }

    private void serveMenu() {

        int choice = input.nextInt();
        System.out.println();

        switch (choice) {

            case 1:
                account.deposit(input);
                break;
            case 2:
                account.withdrawal(input);
                break;
            case 3:
                System.out.println("Aktualne saldo: " + account.getBalance());
                break;
            case 4:
                displayMenu = false;
                break;
            default:
                System.out.println("Nie obsługuje takeij opcji !!!");
                break;
        }

        System.out.println();
    }
}
