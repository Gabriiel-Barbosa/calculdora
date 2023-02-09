# Parte Lógica 
import calculadora as clc
#Biblioteca GUI
import tkinter as tk

#Criando Janela
root = tk.Tk()
root.geometry("500x400")
text_widget = tk.Text(root, height=2, width=50)
text_widget.grid(row=0, column=0, columnspan=3)
root.title("Calculadora")

#Função Pra Adicionar Conteúdo na Tela
def press_button(num):
    text_widget.insert(tk.END, str(num))

#Interável Pra criar Botões
for i in range(10):
    button = tk.Button(root, text=str(i), command=lambda x=i:press_button(x))
    button.grid(row=i//3 +1, column=i%3)



root.mainloop()


