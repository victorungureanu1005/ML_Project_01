# ML_Maternal_Health_Risk

## 1. Reproductibilitate și organizare
Existența unui loc clar în cod (sau într-un fișier separat) unde sunt definite valorile importante folosite în experimente: seed, numele coloanei țintă și proporția train/test. 
    Am creat Constants.py pentru pastrarea numelui coloanei tinta, seed si a proportiei train/test
Dacă proiectul este rulat din nou cu aceleași setări, rezultatele trebuie să fie identice sau foarte apropiate.
## 2. Încărcare dataset și definirea clară a problemei
Definirea explicită a lui X și y; descrierea claselor. 
Raportarea dimensiunilor datasetului și a tipurilor de variabile. 
Distribuția claselor (count + %), cu concluzie privind dezechilibrul.
## 3. Verificarea datelor înainte de antrenare
Missing values (count + %), tipurile de coloane (numerice / categoriale, dacă există) și câteva informații de bază despre date (de exemplu: intervale de valori, minime / maxime, valori neobișnuite observabile). Identificarea valorilor extreme prin inspecția datelor și explicarea modului în care acestea influențează alegerea preprocesării. Decizii motivate privind imputarea și scalarea.
## 4. Separarea corectă a etapelor de lucru (fără folosirea testului înainte de evaluarea finală)
Este permis să analizați sau să comparați datele pe întregul dataset atunci când faceți descrieri generale (de exemplu: distribuția claselor, numărul de valori lipsă, comparații simple între coloane). În schimb, orice valori care sunt apoi folosite efectiv în preprocesare sau antrenare (de exemplu: media/mediana pentru completarea valorilor lipsă, valorile folosite la scalare, resampling) se calculează doar pe setul de antrenare. Setul de test se folosește exclusiv pentru evaluarea finală.