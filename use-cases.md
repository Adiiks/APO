Opis skrócony przypadków użycia
===============================

Aktorzy procesu i ich cele
--------------------------

Aktor       Cel 
----------- -----------------------------
Użytkownik  Zlecenie dokonania przelewu
Użytkownik  Zlecenie wypłacenia pieniędzy z konta
Użytkownik  Zlecenie wpłacenia pieniędzy na konto
Użytkownik  Sprawdzenie stanu konta
Użytkownik  Zakup kodu podarunkowego
Użytkownik  Wydruk historii rachunków
Pracownik   Utrzymanie odpowiedniej liczby pieniędzy w bankomacie
Pracownik   Włączenie i wyłączenie systemu

Słownik
-------

Hasło             Opis
-----------       -----------------------------
Użytkownik        Klient banku, który posiada konto i może nim zarządzać
Pracownik         Osoba zatrudniona przez bank do obsługi bankomatu
System            Oprogramowanie zarządzające pojedynczym bankomatem
Panel Pracownika  Oprogramowanie zarządzające systemami

Przypadki użycia
----------------

### Use case 1: Dokonanie przelewu

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje dokonania przelewu. Użytkownik wprowadza dane do przelewu. System weryfikuje wprowadzone dane. System dokonuje przelewu. Użytkownik wylogowuje się.

### Use case 2: Pobranie pieniędzy

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje wypłacenia pieniędzy. Użytkownik podaje kwotę wypłaty. System sprawdza stan konta w celu weryfikacji. System wypłaca pieniądze. Użytkownik odbiera pieniądze i wylogowuje się.

### Use case 3: Sprawdzenie stanu konta

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje sprawdzenia stanu konta. System informuje użytkownika o stanie konta. Użytkownik wylogowuje się.

### Use case 4: Wpłacenie na konto pieniędzy

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje wpłacenia pieniędzy. Użytkownik podaje kwotę wpłaty. Użytkownik wkłada pieniądze. System weryfikuje stan banknotów. System zaksięgowuje pieniądze na koncie. Użytkownik wylogowuje się.

### Use case 5: Zakup kodów podarunkowych

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje zakupu kodu podarunkowego. System informuje o dostępnych kodach podarunkowych. Użytkownik wybiera kod podarunkowy. System weryfikuje stan konta uzytkownika.
System pobiera pieniądze z konta użytkownika. System drukuje kod podarunkowy. Użytkownik odbiera kod i wylogowuje się.

### Use case 6: Wydruk historii rachunków

Użytkownik wkłada kartę. System prosi o podanie pinu. Użytkownik wprowadza pin. Następuje weryfikacja przez system pinu.
Użytkownik wybiera opcje wydruku historii rachunków. System generuje raport historii rachunków. System drukuje historie rachunków. Użytkownik odbiera wydruk i wylogowuje się. 

### Use case 7: Uzupełnienie pieniędzy dostępnych w bankomacie

Pracownik odłącza bankomat od zasilania. Pracownik otwiera zamek szyfrowy. Pracownik otwiera kluczem pojemnik, wkłada do pojemnika pieniądze. Zamyka pojemnik kluczem. Zamyka zamek szyfrowy.
Pracownik przywraca zasilanie w bankomacie.

### Use case 8: Wyłączenie systemu

Pracownik loguje się do panelu pracownika. Panel pracownika weryfikuje nazwę i hasło pracownika. Pracownik wybiera opcje wyłączenia systemu. Panel wyłącza system. Pracownik wylogowuje się.

### Use case 9: Włączenie systemu

Pracownik loguje się do panelu pracownika. Panel pracownika weryfikuje nazwę i hasło pracownika. Pracownik wybiera opcje włączenia systemu. Panel włącza system. Pracownik wylogowuje się.



