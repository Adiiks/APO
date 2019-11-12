Use Case 1: Dokonanie przelewu
=====================

**Aktor podstawowy:** Klient


Główni odbiorcy i oczekiwania względem systemu:
-----------------------------------------------

-Klient: Klient oczekuję możliwości szybkiego przelania pieniędzy z jednego konta na drugie.

-Bank: Chcę umożliwić prosty sposób na przelanie pieniędzy.

Warunki wstępne:
----------------

Klient jest zidentyfikowany i przeprowadzona została uwierzytelnianie

Warunki końcowe:
----------------

Przelew został wykonany. Konta Klienta i odbiorcy są aktualizowane. Potwierdzenie jest wydrukowane.

Scenariusz główny (ścieżka podstawowa):
---------------------------------------

  1. Klient wprowadza kartę.
  2. Klinet wprowadza PIN.
  3. System wyświetla wszystkie operacje możliwe do wykonania.
  4. Klient wybiera opcje dokonania przelewu.
  5. Klient wprowadza dane potrzebne do wykonania przelewu(tytuł,numer konta odbiorcy,kwotę)
  6. System prosi o potwierdzenie wykonania przelewu.
  7. System pobiera kwotę podaną przez Klienta i przelewa ją na konto odbiorcy.
  8. Klient odbiera potwierdzenie.


Rozszerzenia (ścieżki alternatywne):
------------------------------------

 *a.  W dowolnym czasie, dotyczy sytuacji kiedy system zawiesza się:
        1.Pracownik restartuje system.
        2.System wycofuje wszystkie operacje.
		2a. System wykrywa błędy.
			1.System wyświetla na ekranie informacje o błędzie,zapisuje błąd i resetuje się.
			2.System informuję pracownika banku o błędach.
  1a. Błąd z wczytaniem karty.
        1.System informuje o błędzie.
        2.System oddaję kartę Klientowi.
  2a. Błędny PIN.
        1.System informuję o błędnym numerze PIN i prosi o ponowne wprowadzenie PIN-u.
  5a. Wprowadzono błędne dane.
        1.System informuje o błędzie i prosi o poprawienie błędnych danych.
  5b. Wprowadzona kwota przekracza ilość pieniędzy na koncie.
        1.System informuje o błędzie i prosi o zmiane wprowadzonej kwoty.
  6a. Klient chce zmienić wprowadzone dane.
        1.Kleint nie potwierdza wykonania przelewu.
        2.System wraca do punktu 3.
  7a. System wykrywa błąd połączenia.
		1.System informuje o błędzie.
		2.System resetuje się.
        
        
Wymagania specjalne:
--------------------

  - Możliwość interfejsu wielojęzycznego.

  - Ekran dotykowy
  


Wymagania technologiczne oraz ograniczenia na wprowadzane dane:
---------------------------------------------------------------

 1a. Informacje o karcie kredytowej wprowadzone przez czytnik kart.

 2a. Kod PIN wprowadzony z klawiatury na ekranie dotykowym.

