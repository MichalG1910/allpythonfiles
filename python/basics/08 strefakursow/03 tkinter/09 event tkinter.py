from tkinter import *
'''
Aplikacja Tkinter działa przez większość czasu wewnątrz pętli zdarzeń, która jest wprowadzana za pomocą metody mainloop. Czeka na rozwój wydarzeń. Zdarzeniami mogą być naciśnięcia klawiszy lub operacje myszy wykonywane przez użytkownika.
Tkinter zapewnia mechanizm pozwalający programiście radzić sobie ze zdarzeniami. Dla każdego widgetu możliwe jest powiązanie funkcji i metod Pythona ze zdarzeniem.
Jeśli zdefiniowane zdarzenie wystąpi w widżecie, funkcja „handler” zostanie wywołana z obiektem zdarzenia. opisując zdarzenie.

widget.bind(event, handler) - widget.bind(zdarzenie, procedura obsługi)
'''

def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop")
    widget.quit()  
    widget.destroy() 
    

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 
widget.mainloop()

'''
Weźmy inny prosty przykład, który pokazuje, jak użyć zdarzenia ruchu, tj. czy mysz jest poruszana wewnątrz widżetu:
Za każdym razem, gdy poruszymy myszką w widgecie Wiadomość, zostanie wydrukowana pozycja wskaźnika myszy. Gdy wyjdziemy z tego widżetu, funkcja motion() nie jest już wywoływana.
'''
def motion(event): 
  print("Pozycja myszy: (%s %s)" % (event.x, event.y)) 
  return 

master = Tk() 
cokolwiek_robisz = "Cokolwiek zrobisz, będzie nieistotne, ale bardzo ważne jest, abyś to zrobił.\n(Mahatma Gandhi)" 
msg = Message(master, text = cokolwiek_robisz) 
msg.config(bg='lightgreen', font=('times', 24, 'italic') ) 
msg.bind('<Motion>',motion) 
msg.pack() 
mainloop()
'''
<Button>	Button myszy jest wciśnięty, gdy wskaźnik myszy znajduje się nad widżetem. Część szczegółowa określa, który Button, np. 
            Lewy Button myszy jest zdefiniowany przez zdarzenie <Button-1>, środkowy Button przez <Button-2>, a skrajny prawy Button myszy przez <Button-3>.
            <Button-4> definiuje zdarzenie przewijania w górę na myszach z obsługą kółka, a <Button-5> przewijanie w dół.
            
            Jeśli naciśniesz Button myszy nad widżetem i przytrzymasz go, Tkinter automatycznie „chwyci” wskaźnik myszy. Dalsze zdarzenia myszy, takie jak zdarzenia
            ruchu i zwolnienia, będą wysyłane do bieżącego widżetu, nawet jeśli mysz zostanie przesunięta poza bieżący widżet. Bieżąca pozycja wskaźnika myszy 
            względem widżetu jest podawana w składowych x i y obiektu zdarzenia przekazanego do wywołania zwrotnego. Możesz użyć ButtonPress zamiast Button, 
            a nawet całkowicie go pominąć: , , i <1> to wszystkie synonimy.

<Motion>	Mysz porusza się przy wciśniętym Buttonu myszy. Aby określić lewy, środkowy lub prawy Button myszy, użyj odpowiednio <B1-Motion>, <B2-Motion> i <B3-Motion>. 
            Bieżąca pozycja wskaźnika myszy jest podawana w składowych x i y obiektu zdarzenia przekazanego do wywołania zwrotnego, tj. event.x, event.y

<ButtonRelease>	    Zdarzenie, jeśli Button zostanie zwolniony. Aby określić lewy, środkowy lub prawy Button myszy, użyj odpowiednio <ButtonRelease-1>, 
                    <ButtonRelease-2> i <ButtonRelease-3>. Bieżąca pozycja wskaźnika myszy jest podawana w składowych x i y obiektu zdarzenia przekazanego do 
                    wywołania zwrotnego, tj. event.x, event.y
<Double-Button>	    Podobnie jak w przypadku zdarzenia Button, patrz wyżej, ale Button jest klikany dwukrotnie zamiast pojedynczego kliknięcia. Aby określić lewy, 
                    środkowy lub prawy Button myszy, użyj odpowiednio <Double-Button-1>, <Double-Button-2> i <Double-Button-3>.
                    Możesz użyć Double lub Triple jako prefiksów. Zauważ, że jeśli powiążesz zarówno pojedyncze kliknięcie (<Button-1>), 
                    jak i podwójne kliknięcie (<Double-Button-1>), oba powiązania zostaną wywołane.

<Enter>	    Wskaźnik myszy najechał na widżet.
            Uwaga: Nie oznacza to, że użytkownik nacisnął klawisz Enter!. Do tego celu służy <Return>.

<Leave>	    Wskaźnik myszy opuścił widżet.
<FocusIn>	Aktywność klawiatury został przeniesiona do tego widżetu lub elementu podrzędnego tego widżetu.
<FocusOut>	Aktywność klawiatury została przeniesiona z tego widżetu do innego widżetu.
<Return>	Użytkownik nacisnął klawisz Enter. Możesz powiązać praktycznie wszystkie klawisze na klawiaturze: Klawisze specjalne to  
            Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, 
            Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, 
            F11, F12, Num_Lock, and Scroll_Lock.
<Key>	    Użytkownik nacisnął dowolny klawisz. Klucz jest dostarczany w elemencie char obiektu event przekazywanym do wywołania zwrotnego 
            (jest to pusty ciąg dla kluczy specjalnych).
a	        Użytkownik wpisał klawisz „a”. Większość znaków drukowalnych może być używana bez zmian. Wyjątkami są spacja (<space>) i mniejsza niż (<less>). 
            Zauważ, że 1 to powiązanie klawiatury, podczas gdy <1> to powiązanie Buttonu.
<Shift-Up>	Użytkownik nacisnął strzałkę w górę, trzymając wciśnięty klawisz Shift. Możesz używać przedrostków, takich jak Alt, Shift i Control.
<Configure>	Zmieniono rozmiar widżetu. Nowy rozmiar jest podany w atrybutach width i height obiektu zdarzenia przekazanego do wywołania zwrotnego. 
            Na niektórych platformach może to oznaczać zmianę lokalizacji.
'''