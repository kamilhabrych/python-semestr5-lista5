# Lista 5 - Języki programowania wysokiego poziomu

**Python (5) - Listy**

(1) Stwórz listę 4-elementową l zawierającą po kolei:
3,’alfa’,2.71,’kot’
Za pomocą print zinterpretuj l[i] dla i całkowitych (ujemnych też).
Dla których i nie będzie błędu?
Zmień pierwszy element listy na 4, a ostatani na ’pies’ i wyświetl listę l.
Skopiuj listę l do listy l2. Wyświetl l oraz l2. Zmodyfikuj pierwszy element
l2 i wyświetl obie listy. Co można zauważyć? (nie stworzyliśmy nowej listy
tylko stworzyliśmy nowy odnośnik-reference do starej listy.)
Skopiuj teraz l do l3 za pomocą: l3=l.copy()
Zmień pierwszy element l3 i wyświetl listy l i l3. Co można zauważyć?

(2) Dwie listy można połączyć (konkatenacja) za pomocą +, np. aby dodać element 6.4 do listy l stosujemy składnię:
l = l + [6.4] ([6.4] jest listą 1-elementową)
Pustą listę można zdefiniować przez:
l=[]
Stwórz (za pomocą pętli) listę 10-elementową kwadratów: 1, 4, 9, .., 100
Wyświetl listę (print). Następnie zmień znak elementów parzystych listy i
wyświetl taką zmienioną listę.

(3) Napisz program w którym użytkownik najpierw podaje ilość liczb n
do wpisania. Następnie n liczb jest wpisywane do listy. Wreszcie program
ma znaleźć i wyświetlić największą i najmniejszą z tych liczb.

(4) Użytkownik wprowadza n. Stoworzona jest n-elementowa lista zawierająca:
sin(1), sin(2), ..., sin(n).
Wreszcie program znajduje i wyświetla największy i najmniejszy element
tablicy. Przetestuj z coraz większymi n. Co się dzieje z elementami największym i najmniejszym?

(5) Polecenie del służy do usuwania elementów listy, składnia:
del lista[5] (usuwa 6-sty element listy lista)
Stwórz listę składającą się z liczb od 100 do 150.
Następnie usuń z listy elementy z liczbami 105, 110, 115,..,140, 145 i wyświetl końcową listę.
Jeśli końcowa lista jest inna niż oczekujemy zastanów się dlaczego i zmodyfikuj program.

(6) Stwórz 10-elementową listę l zawierającą różne liczby całkowite. Następnie (jak najprościej) utwórz listy (pamiętaj o kopiowaniu z l.copy() patrz (1)):
l2, w której początkowy element listy jest przeniesiony na koniec.
l3, końcowy element listy jest przeniesiony na początek.
l4, odwrócona lista l.
l5, lista składająca się tylko z parzystych elementów l.
l6, lista składająca się z nieparzystych elementów l o indeksach parzystych
Sprawdź wyświetlając wszystkie te listy.

(7) Liczba π znajduje się w module math, jako pi. Napisz program który wpisuje kolejne 50 cyfr rozwinięcia pi do listy. Wreszcie wyświetl tą listę.
