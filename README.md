Subiectul 2 - a)

```python
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip())
```
Pentru inceput codul dat extrage din variabila "txt" subsirul " results", iar apoi cu ajutorul "strip" elimina spatiul liber. 
Rezultatul afisat la consola fiind: "results".

b)
```python
txt = "More results from text..."
print(txt.split())
```
Rezultatul afisat la consola va fi:['More', 'results', 'from', 'text...'], deoarece "split" face din toate elementele unui string o lista.

c)
```python
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))
```
Rezulatul afisat va fi:"My name is Mary, and I am 36", deoarece metoda "format(age)" inlocuieste in variabila "txt",elementul "{}" cu valoarea din varibila "age".

