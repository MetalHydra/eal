# EAL

1. Bewertung von Algorithmen
2. Berechenbarkeitstheorie
3. Komplexitätstheorie
4. Exakte Algorithmen für schwere Probleme


## Heap 
- Array den man sich als Binären Baum vorstellt
- schlechte Datenstruktur -> viele Cache Misses
- Binäre Suche auch schlecht bzgl. Cache Effizienz
- B-Bäume sind externe effiziente Datenstrukturen(werden in Datenbanken verwendet).

## Bewertung von Algorithmen

### Kriterien
- Korrektheit: 
- Laufzeit: 
- Speicherplatz:
- Kommunikationszeit: Wie schnell werden Informationen ausgetauscht
- Güte: Was ist die bestmögliche Lösung?

Je mehr Speicherplatz vorhanden ist, desto schneller kann ein Algorithmus laufen

Sortieren und die nebenliegenden Zahlen betrachten
-> $O(nlog (n)+n) = O(nlog(n))$ Sortieren und einmal durchlaufen

### Quadratische Laufzeit
$n -> n^2 = x \ sec$
$2n -> n^2 = 4n^2 = 4x \ sec$
- Doppelte Anzahl an Elementen -> 4mal so lange Laufzeit

### Groß $O$
- Menge an Funktionen
- $f = \mathbb{N_0} \rightarrow\mathbb{N_0}$ so definiert, man zählt Anzahl an schritten und gibt Anzahl an Elementen an
- wichiig Konstante Faktoren werden ignoriert
- Kann auch über Grenzwert angegeben werden
- $lim_{n \rightarrow \infty}\frac{f(n)}{g(n)} <= c$
- Es interessiert nur das Asymptotische Verhalten im unendlichen (das gleiche wie ab einer Stelle $n_0$)
- Man sucht immer die kleinste Obere Schranke
- Ebenso Untere Schranken $\Omega(g)$
- $\Theta(g)$ Funktioniert nur durch Konstanten Faktoren
- Keine Basen bei Logarithmen, da diese ineinander umrechenbar sind, die Umrechnung packt man dann in die Konstante $c$ rein.
  
- #TODO (Regel von L'Hospital anschauen)
### Aufwandsschätzungen von mehrstelligen Funktionen
- Bsp. Textsuche nach wort
- $f:\mathbb{N_0}^2$, und $f(x,y), g(x,y)$
- Notation für Tiefensiche wichtig (mehrere Knoten und Kanten)

# TODO Turingmachinen

# Nicht Berechenbare Probleme
Diagonalsprache ist nicht entscheidbar

# Reduktion
Halteproblem Gegeben ist Programm als Gödelnummer mit einer Eingabe
Halteproblem als Sprache formuliert
Halteproblem ohne Eingabe gleiche wie Halteproblem nur ohne Eingabe 
Wir wissen das Diagonalsprache nicht entscheidbar ist -> andere Sprachen auf diese Sprache abbilden (bzw. auf das Komplement)
Wenn Sprache nicht entscheidbar ist, ist Komplement auch nicht entscheibar

- $L <= L'$ (mittels einer Funktion $f$)

Zeige; $!DIAG <= H$
Baue Turingmachine die auf dem leeren Band hält


## Universelle Turingmachine 
Eingabe ist Programm als Gödelnummer

# Was ist besser?
- Viel Platz oder viel Zeit
- Turingmaschine: N Zeitschritte Nutzen maximal N Felder
- Zeit aus Platz bei Turingmaschine Ableitbar, wegen endlichen Zuständen und endlichem Bandalphabet
- $s(n) = n$
- $t(n) > |Z|x|\gamma|^n$
- Nehme 2. Band und Zähle Schritte. Wenn mehr Schritte als als mögliche Kombinationen -> endlosschleife

## Cliquenproblem
- Gegen Graph G(V,E) und einem $k \in \mathbb{N}$
- In polynomieller Zeit

## Hamiltonkreis 
- auch einfach
  
## Independent-Set
- Kein Knotenpaar ist durch eine Kante verbunden

## Dominating set
- Suche eine Möglichst kleine Knotenmenge

Sehr einfache Probleme, aber sind nicht sehr effizient
Für feste k = polynomielle Laufzeit, allerdings exponentiell wenn k nicht beschränkt ist

Warum wird k mit übergeben?
- Weil sonst kein Zertifikat angegeben werden kann.
- Probleme in NP sind fast allesamt entscheidungsprobleme
- Probleme werden als Sprache formuliert

- Reicht es eine Entscheidungsvariante zu lösen
- DEC = Decision, MAX, SEARCH 
- $DEC \in NP$
- SEARCH -> MAX -> DEC (easy zu lösen) andersrum nicht
- Löse Entscheidungsproblem -> dann Max auch einfach (mithilfe von Binärer Suche)
- MAX -> SEARCH ist Problemspezifisch (bei der Clique einfach)
- Sukzessiv Knoten rausnehmen, guck ob sich größe der Clique dadurch ändert (wenn nicht, dann Knoten unwichtig, sonst Knoten gehört zur Clique)

# K-Färbung
- Jeder miteinander Verbunde Knoten muss eine andere Farbe haben
- MIN -> SEARCH ist Graph mit k-Farben Färbber, erzeuge weitere k-Clique
- Weise dem Graph Farben mit k-Clique zu (jeder Knoten in Clique hat Farbe $f(x_i) = i$)
- Füge dann neue Kanten hinzu zwischen Knoten und Clique
- Färbungen werden anhand Fehlender Kanten abgelesen
- Finde so ein Graph löst das Suchproblem

Wir machen nur Entscheidungsprobleme, weil die einfach sind und man diese sowieso auf die anderen Problme Reduzierbar sind

HCP = Hamiltion-Circuit-Problem

# Reduktion bei der Komplexitätstheorie
wie bei Berechenbarkeit
- Unterschied Funktion f muss nicht nur Berechenbar sein, sondern zusätzlich in Polynomieller Zeit Berechenbar
- Reduktion ist Transitiv $L_1 \leq L_2 und L_2 \leq L_3 = L_1 \leq L_3$

## Die Klasse NP
$P \in NP$
P ist in NP (man weiß aber nicht ob die gleich sind)
Daneben sind schwere Probleme in NP definiert (Dies sind die NP-vollständigen Probleme)
$L \in NP$
- alle $L' \in NP$ sind Polynomiell reduzierbar auf $L$

# SAT (Satisfiability) Erfüllbarkeitsproblem
- Erstes NP-vollständiges Problem
- Reduktionen von dieses Sat Problem
- Man baut Schaltkreis
- $SAT = {F | F ist eine erfüllbare aussagenlogische Formel}$
- Wenn alle Probleme nicht sc
- Mit Zertifkiaten (dann steht da NP)
- nicht deterministisch (mit nicht deterministischer Turingmaschine)

Formel:
- Reduktion muss in Polynomieller Zeit erzeugt werden.
- Teilformel $G$: von k vielen Variablen 
- sorgt dafür, dass genau eine einzige Variable auf 1 gesetzt ist

- U2 drückt auch aus, was sich nicht ändert
- Da wo nichts geändert wird bleibt das Zeichen gleich

# Wie zeigt man:
- man hat nur Polynomielle Anzahl an Variablen
- $x \in L <=> F(x)$ (x in Sprache L)
- F(x) ist berechnungsformel für Turingmaschine
- Man muss prüfen, wie lange die Teilformeln sind
- Man muss auch Anfangsbedingung 
- Sind andere Formeln leichter zu lösen?
- KNF und DNF sind villeicht leichter zu lösen aber Umwandlen hat exponentiellen 
- SAT ist NP-vollständig, Reduziere andere Formen auf das SAT Problem $SAT \leq_p 3KNF-SAT$
- SAT Formeln als Baumstruktur

## Hinweis Implikation
Hinweis: Aus was falschem kann man alles folgen deshalb 0 -> 1  = 1 !x 
ABER: aus etwas wahrem kann man nichts falsches folgern
Tiefensuche findet Graphen in Kreis (wenn Rückwärstkante existiert)

Formel als Baum darstellen

## 3KNF-SAT
Name weil 3 Literale in Term

## 2KNF-SAT
$\in P$

- Spezialfall von KNF SAT
## KNF-SAT 
- Auch Np-vollständig

## DNF SAT
- In P
- Easy nur eine Klausel muss erfüllt sein
- Klausel erfüllbar, wenn Variablen alle unterschiedlich sind
- Aber Umwandeln unter Umständen in exponentieller Zeit

Die Untersuchung ob ein Problem schwer ist, muss für jedes Problem einzeln gestellt werden
Spezialfälle 
Zertifikat

## 3KNF-SAT $\leq_p Clique$
-(x v y) = (x v x v y)

## Hornklauseln 
- $\in P$ mithilfe von Markierungsalgorithmus
  
- Aussagenlogische Formlen müssen in Graphen umgewandelt werden
- 

## Hamiltonkreis
- Jeder Knoten muss einmal besucht werden
- ist Np vollständig
- Klauselgraph bilden
- Der Graph ist so aufgebaut, dass jeder Knoten besuht werden
- Ist erfüllende Belegnung, wenn Ausgang oberer Knoten ist

## Eulerkreisproblem
- einfahc zu lösen, gucken ob Knotengrad gerade ist
- Wenn es ein Eulerkreis gibt, suche Kreis mit Tiefensuche, entferne diesen aus dem Graph und suche in jeder Zusammenhangskomponente einen Euler kreis

## Knotenfärbung
- Schreibe Zahlen an die Knoten 
- Reduktion von 3KNF-Sat ist einfach 
- Beginne mit 3 Clique
- FÜhre für jede Variable 2 Knoten ein (je ein KNoten für positive und Negative Komponente)
- 

## 2-Färbbar wie kann man das zeigen?
- Einfache Datenstruktur
- Jede gerde ebene kriegt Farbe 1, jede ungerade ebene bekommt Farbe 2
- Hat ein Graph eine ungerade Anzahl an Knoten
- Bei Kreisen mit ungeraden Knoten
- Tiefensuche machen
- Bei der Tiefensuche kann man Färbung direkt dranschreiben


## 
Basisänderungen bei exponentiellen Laufzeiten, machen viel aus

## Algorithmen Independent set
Independent Set bei Kreisen leicht zu finden
Man fängt mit einem einfachen Algorithmus an
Man nimmt irgendein Knoten und schaut sich den Worst Case an
Anschließend weiter verbessern

# Entwurfsmethoden 
- Greedy Algorithmen
- dynamische Programmierung
- Greedy
- local Search

## Divide and Conquer
Problem wird in Teilprobleme aufgeteilt, welche dann rekursiv gelöst werden

## Laufzeit Rekursionsgleichungen
Vorne stehen zweierpotenzen wegen *2
Leite aus dem eingesetzen eine Formel ab
Falls Wurzel oder log da steht -> Variablensubstitution

## Strassen Algorithmus
Effiziente Matrix Multiplikation
weniger Multiplikationen dafür mehr Additionen

Charakteristische Operationen:
- Addition und Multiplikation

## Untere Schranke der Matrixmultiplikation: $O(n^2)$

## Algorithmus von Karazuba (Matrixmultiplikation)
- Zerlege Ziffern in Obere und Untere Bereiche

## Master Thereom
- $T(n) = a (T(n/b) + \Theta(n^k))$ a = Anzahl rekursive Aufrufe

# Dynamische Programmierung
Berechnung von Fibbonacci Zahlen
Lösungen werden zwischengespeichert werden
Das Speichern nennt man Memorieren (Top-Down-Ansatz)
Immer noch Rekursiv aber mit zusätzlichem Array zum Speichern von zwischenergebnissen

Folie 244: gestrichelte Linien sind Arrayzugriffe

Bottom-Up: Iterativer Ansatz, verwende for schleifen und Arrays zum Speichern
-> Bessere Laufzeit
Dynamische Programmierung, verwendet man bei Optimierungsproblemen

Beispiel ist die Matrix-Ketten Multiplikation
Finde beste Reihenfolge an Matrixmultiplikationen, dass Operationen minimal werden
Wieviele Klammerungen gibt es
Probiere alle Kombinationen durch

Rekursionsende i = j

## 0-1 Rucksackproblem (Dynamische Programmierung)
Jedes Objekt hat eine Größe, Wert, Gewicht
Maximiere den Wert, ohne ein Gewicht zu überschreiten
Das 0/1 Rucksackproblem ist Schwach NP-Vollständig
Der dynamische Algorithmus ist ein pseudo polynomieller Algorithmus
G ist ein numerischer Wert der binär kodiert wird
Eingabelänge ist $log_2(G)$
$O(n G) = O(n 2^{log_2(G)}) = O(n2^{|G|})$


## Schwach-Np-vollständig
treten nur bei Numerischen auf
Effiziente Alogorithmen nur wenn Numerische Werte nicht zu groß werden

## Polygon Triangulierung
Trinagliere so, dass Umfang der Dreiecke möglichst klein sind

## Levenshtein Distanz
WIeviele Schritte sind Nötig, um ein Wort in ein anderes Wort zu überführen

## CYK Algorithmus
Prüft ob ein Wort zu einer Sprache gehört

## Dynamische Programmierung Traveling Salesman
Das Optimalitätsprinzip gilt nicht -> Dann keine reukrsionsgleichung
Es gibt Trick. ersten Knoten rausnehmen -> Dadurch keine Kreise sondern kürzesete Wege 
In jedem Schritt wird ein Schritt rausgenommen,mächtigkeit $2^n$
größe Tablle $n 2^n$

## Greedy Algorithmen
Optimal Merge Patterns
2 Datein Mergen Laufzeit = $O(q1+q2)$ q1,q2 Länge von Array 1,2
Man will Reihenfolge ermitteln für optimalen Merge
Merge nach größen
Ähnlich zu Matrix-Ketten-Multiplikation

### Warum interessiert die Korrektheit bei Greedy und nicht bei dynmaischer Programmierung?
Weil bei Dynamischer Programmierung alle möglicheiten Durchprobiert worden sind.
Bei Greedy-Algorithmus wird nur eine Möglichkeit überprüft -> deshalb muss Korrektheit mit vollständiger Indution gezeigt werden.

Greedy Algorithmen sind sehr einfach

## Fractional Knapsack
Objekte können auch halb reinkommen
Alpha ist Faktor wie sich Wert für 1 ändert

## Coin Changing Problem
Geld wechseln
möglichst wenig Münzen benutzen
wie oft passt die größte Münze in das Wechselgeld
Greedy funktioniert nur bei bestimmten Zahlensystemen
Man muss scih überlegen pb ein anderer Algorithmus eine bessere Lösung produziert
es gibt eine optimale Suchstruktur -> dynamische Programmierung 
Alle möglichkeiten durchprobieren
Das Problem ist Schwach-NP-vollständig 

## Präfix-Code
Kein Codewort ist Anfangswort von einem anderen
Greedy nach Wahrscheinlichkeiten

Zu jedem Greedy Algorithmus muss gezeigt werden, dass die Wahl korrekt ist, dass muss man bei der dynamischen Programmierung nicht.

# Lokale Suche
Man beginnt bei einer beliebigen Lösung und modifiziert diese
Wenn neue Lösung besser ist, übernehme die neue Lösung

## Beim Travelling salesman
Wähle zwei zufällige Knoten die nicht aufeinanderfolgend sind
lokal nur, wenn Matrix symmetrisch ist, Weil zurückgehen nicht teuer wird

## Permutationen
jeweils immer 2 Zahlen tauschen, und Ret des Arrays Rekursiv genauso machen

## Graph Partitionierung
Unterteile Graoh so, dass Kanten zwischen den Mengen minimale Kantengewichte haben

# Sortieren
## Quicksort
- Divide and conquer
- nehme Pivot-Element und sortiere linken und rechten Teil rekursiv
- Welche Laufzeit hat Quicksort, wenn die Aufteilung immer in einem festen Verhältnis erfolgt?
- Benutze Rekursionsbäume für die Herleitung
- Setze rekursiv ein Daraus ergibt sich das Pascalsche Dreieck mit den Binomialkoeffizienten
- Auf einer Ebene
- $T(1) = k => k \in O(1)$ tritt auf,wenn $(\frac{9}{10})^k n = 1$ ist
- Es gibt ein Aufteilungsaufwand $cn$
- Summen wegmachen, indem man mit andere Summe subtrahiert
- Worst case tritt in stark vorsortierten folgen auf
- Verwende Zufallsstrategie  
- In der Praxis ist quicksort nicht toll :(
- Laufzeit bei eingeschränktem Wertebereich (ca. Quadratische Laufzeit (Worst-Case tritt ein))
- Viele Zahlen aus kleinem Wertebereich führen zu Worst Case, da viele Zahlen doppelt vorkommen
- Viele doppelte Zahlen
- Quicksort kann man besser machen. indem man 3-Wege Split Quicksort macht
- In Standard lib ist kein 3 wege split implementiert
- 
