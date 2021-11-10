class Display {
    constructor(displayValorActual) {
        this.displayValorActual = displayValorActual;
        this.tipoOperador = undefined;
        this.valorActual = '';
    }

    borrar() {
        this.valorActual = this.valorActual.toString().slice(0,-1);
        this.mostrar_valores();
    }

    borrar_todo() {
        this.valorActual = '';
        this.tipoOperador = undefined;
        this.mostrar_valores();
    }

    agregar_numero(numero) {
        if (numero == '.' && this.valorActual.includes('.')) return
        this.valorActual = this.valorActual.toString() + numero.toString();
        this.tipoOperador = undefined;
        this.mostrar_valores();
    }

    agregar_operador(operador) {
        if (this.tipoOperador == undefined) {
            this.valorActual = this.valorActual.toString() + operador.toString();
            this.tipoOperador = operador;
        } else {
            this.valorActual = this.valorActual.toString().slice(0,-1) + operador.toString();
        }
        this.mostrar_valores();
    }

    mostrar_valores() {
        this.displayValorActual.value = this.valorActual;
    }

}
