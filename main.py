from consolemenu import *
from consolemenu.items import *

from katalog import Katalog
from samochod import Samochod

k = Katalog('lista.txt')


menu = ConsoleMenu("katalog samochodowy", "menu")

function_item1 = FunctionItem("Wczytaj liste", k.wczytajListe)
function_item2 = FunctionItem("Wypisz liste samochodow", k.wypiszListe)
function_item3 = FunctionItem("Dodaj samochod", k.dodajSamochod)
function_item4 = FunctionItem("Wyswietl dane pojedynczego samochodu", k.wyswietlJeden)
function_item5 = FunctionItem("Usun samochod z listy", k.usunSamochod)
function_item6 = FunctionItem("Wyswietl samochody do podanego rocznika", k.wyswietlenieWarunkowe)
function_item7 = FunctionItem("Posortuj i wyswietl najpierw samochody z najmniejszym przebiegiem", k.posortujPrzebiegiem)


menu.append_item(function_item1)
menu.append_item(function_item2)
menu.append_item(function_item3)
menu.append_item(function_item4)
menu.append_item(function_item5)
menu.append_item(function_item6)
menu.append_item(function_item7)

menu.show()