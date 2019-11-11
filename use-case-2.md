Use Case 2: Pobranie pieniędzy
=====================

**Aktor podstawowy:** Klient


Główni odbiorcy i oczekiwania względem systemu:
-----------------------------------------------

- Klient: chce szybko I natychmiastowo wypłacić dowolną ilość środków pienieżnych z konta

- Bank: chce, aby klient nie był w stanie pobrać więcej pieniędzy niż ma na swoim koncie  

Warunki wstępne:
----------------

W bankomacie znajdują się środki pieniężne. Klient wkłada kartę do bankomatu i wpisuje poprawny PIN.

Warunki końcowe:
----------------

Klientowi zostają wypłacone pieniądze. Bank zaksięgowuje transakcje.

Scenariusz główny (ścieżka podstawowa):
---------------------------------------

1. Klient wybiera opcję pobrania pieniędzy.
2. Klient wpisuję kwotę pieniędzy jaką chce pobrać.
3. System sprawdza stan konta klienta.
4. System prosi o potwierdzenie transakcji.
5. Klient zatwierdza.
6. System zaksięgowuje transakcje.
7. System przelicza pieniądze do wydania.
8. Bankomat wydaje pieniądze klientowi.
9. System pyta się klienta, czy chce wydrukować potwierdzenie.
10. Klient wybiera opcję “tak”.
11. Bankomat drukuje potwierdzenie.

Rozszerzenia (ścieżki alternatywne):
------------------------------------

 *a. W dowolnym czasie, dotyczy sytuacji kiedy system się zawiesza:
	1. Pracownik banku resetuje system.
	2. System wycofuję całą transakcję.
  3a. Na koncie klienta nie ma wystarczających środków pieniężnych do wypłacania:
	1. System zwraca klientowi komunikat o nie wystarczających środkach 	pieniężnych na koncie.
	2a. Klient wpisuje nową kwotę.
      2b. Klient rezygnuje z transakcji.
  4-6a. Klient nie zatwierdza transakcji:
	1. System przekierowuje klienta do menu głównego.
  7-8a. W bankomacie nie ma wystarczających ilości środków pieniężnych do wydania:
	1. System powiadamia klienta odpowiednim komunikatem.
	2. System wycofuje całą transakcje.
	3. System wysyła do centralnego systemu banku zgłoszenie o braku środków pieniężnych w obsługiwanym przez niego bankomacie.
  9a. Klient nie chce wydrukować potwierdzenia:
	1. Klient wybiera opcję “nie”.  
      

Wymagania specjalne:
--------------------

  - wielojęzyczny interfejs dla klienta
  
  - monitor wyświetlający interfejs dla klienta

  - przyciski wokół ekranu odpowiadające opcjom w menu 

Wymagania technologiczne oraz ograniczenia na wprowadzane dane:
---------------------------------------------------------------

  2a. Klient może wpisywać za pomocą klawiatury tylko cyfry. Wpisana kwota musi być podzielna przez 10 i może wynosić maksymalnie 500 zł.

Kwestie otwarte:
----------------

  
