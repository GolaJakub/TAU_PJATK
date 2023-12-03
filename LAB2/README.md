# Testy Automatyczne Lab 2

### Opis Projektu

Projekt zawiera dwa scenariusze testowe napisane przy użyciu biblioteki Selenium w Pythonie

## Scenariusz Testowy 1: Logowanie i dodanie pracownika na stronie orangehrmlive.com

**Kroki:**

1. Otwórz przeglądarkę Chrome.
2. Wejdź na stronę https://opensource-demo.orangehrmlive.com/web/index.php/auth/login.
3. Zaloguj się na konto administratora używając poprawnych danych (login: Admin, hasło: admin123).
4. Sprawdź, czy logowanie przebiegło pomyślnie, poprzez sprawdzenie obecności elementu dashboard.
5. Przejdź do sekcji PIM.
6. Kliknij przycisk dodawnia pracownika.
7. Uzupełnij formularz odpowiednio danymi: firstName = Test, middleName = Testowski, lastName = Testowy.
8. Kliknij przycisk save aby zapisac pracownika.

**Oczekiwania:**

- Logowanie się powiodło.
- Po zapisaniu pracownika powinno nas przekierować do strony z jego informacjami na której będzie element zawierający jego firsName i lastName.
- Test zakończył się sukcesem.

---

## Scenariusz Testowy 2: Dodawanie produktu do koszyka na stronie amazon.pl

**Kroki:**

1. Otwórz przeglądarkę Edge.
2. Wejdź na stronę https://www.amazon.pl/.
3. Wyszukaj Iphone 13.
4. Wejdź w aukcję z iphonem 13.
5. Dodaj iphone 13 do koszyka.
6. Sprawdź czy w koszyku znajduję się jeden przedmiot.
7. Zamknij przeglądarkę.

**Oczekiwane rezultaty:**

- W koszyku powinien znajdować się jeden przedmiot.
- Test zakończył się sukcesem.

