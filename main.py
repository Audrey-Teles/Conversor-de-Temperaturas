from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import formulas as fr

# Instancia o objeto
janela = Tk()

# Define o título da janela
janela.title("Conversor")

# Define ícone da janela
janela.iconbitmap('temperature.ico')

# Espaço em branco
Label(janela, text="").pack()

# Define um texto de cabeçalho e a sua posição na janela
lblAviso = Label(janela, text="Selecione as escalas para conversão: ", padx=30, pady=10)
lblAviso.pack()

# Define os dados de uma caixa de combinação não editável e sua posição na janela
cbEscalas1 = ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"])
cbEscalas1.pack()

# Define um texto e a sua posição na janela
lblPara = Label(janela, text="para")
lblPara.pack()

# Define os dados de uma caixa de combinação não editável e sua posição na janela
cbEscalas2 = ttk.Combobox(janela, state="readonly", values=["Celsius", "Fahrenheit", "Kelvin"])
cbEscalas2.pack()


# Se as opções para a combobox forem selecionadas retorna true
def foiSelecionado():
    if cbEscalas1.get() == "" or cbEscalas2.get() == "":
        # Mostra uma mensagem de erro
        messagebox.showerror("Erro", "Selecione uma opção para os dois campos")
        return False
    elif cbEscalas1.get() == cbEscalas2.get():
        # Mostra uma mensagem de erro
        messagebox.showerror("Erro", "Selecione opções diferentes para os dois campos")
        return False
    else:
        return True


# Executa as ações do click no botão
def btnConverterAction():
    if foiSelecionado():
        # Ativa a edição para o campo de saída
        txtConvertido.configure(state="normal")
        txtConvertido.delete(1.0, END)
        # Condições para execução das conversões
        if cbEscalas1.get() == "Celsius":
            if cbEscalas2.get() == "Fahrenheit":
                txtConvertido.insert(1.0, fr.celsiusFahrenheit(txtEntradaTemperatura.get("1.0", END)))
            else:
                txtConvertido.insert(1.0, fr.celsiusKelvin(txtEntradaTemperatura.get("1.0", END)))

        elif cbEscalas1.get() == "Fahrenheit":
            if cbEscalas2.get() == "Celsius":
                txtConvertido.insert(1.0, fr.fahrenheitCelsius(txtEntradaTemperatura.get("1.0", END)))
            else:
                txtConvertido.insert(1.0, fr.fahrenheitKelvin(txtEntradaTemperatura.get("1.0", END)))

        elif cbEscalas1.get() == "Kelvin":
            if cbEscalas2.get() == "Celsius":
                txtConvertido.insert(1.0, fr.kelvinCelsius(txtEntradaTemperatura.get("1.0", END)))
            else:
                txtConvertido.insert(1.0, fr.kelvinFahrenheit(txtEntradaTemperatura.get("1.0", END)))

        # Desativa a edição do campo
        txtConvertido.configure(state="disabled")


# Define um texto e a sua posição na janela
lblEntradaTemperatura = Label(janela, text="Informe a temperatura: ")
lblEntradaTemperatura.pack()

# Campo de texto para inserção da temperatura a ser convertida
txtEntradaTemperatura = Text(height=1, width=17)
txtEntradaTemperatura.pack()

# Define as características de um botão e sua posição na janela
btnConverter = Button(janela, text="Converter", command=btnConverterAction)
btnConverter.pack()

# Define um texto e a sua posição na janela
lblConvertida = Label(janela, text="Temperatura convertida: ")
lblConvertida.pack()

# Campo de texto para mostrar a temperatura já convertida
txtConvertido = Text(height=1, width=17)
txtConvertido.pack()

# Espaço em branco
Label(janela, text="").pack()

# Faz com que a janela permaneça aparecendo até que eu a feche
janela.mainloop()
