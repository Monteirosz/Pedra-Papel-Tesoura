from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'cdg'


@app.route('/', methods=['GET', 'POST'])
def jogo():
    # Inicializa o placar na sessão
    session.setdefault('placar1', 0)
    session.setdefault('placar2', 0)
    placar1 = session['placar1']
    placar2 = session['placar2']
    jogador1_escolha = session.get('jogador1_escolha')
    jogador2_escolha = session.get('jogador2_escolha')
    resultado = ""
    

    if request.method == 'POST':
        # botão Ver Resultado for pressionado processa o jogo
        if 'ver_resultado' in request.form and jogador1_escolha and jogador2_escolha:
            if jogador1_escolha == jogador2_escolha:
                resultado = "Empate!"
            elif (jogador1_escolha == "pedra" and jogador2_escolha == "tesoura") or \
                 (jogador1_escolha == "papel" and jogador2_escolha == "pedra") or \
                 (jogador1_escolha == "tesoura" and jogador2_escolha == "papel"):
                resultado = "Jogador 1 venceu!"
                session['placar1'] += 1
            else:
                resultado = "Jogador 2 venceu!"
                session['placar2'] += 1

        # Salva a escolha dos jogadores 1 e 2
        if 'jogador1_escolha' in request.form:
            session['jogador1_escolha'] = request.form['jogador1_escolha']
        if 'jogador2_escolha' in request.form:
            session['jogador2_escolha'] = request.form['jogador2_escolha']

        if 'reset' in request.form: # verificar se o botão foi precionado
            session.clear()  # Limpa tudo
            session['placar1'] = 0
            session['placar2'] = 0
            return render_template("index.html", placar1=0, placar2=0, res="Placar resetado!")
        
        session.modified = True  # Garante que as mudanças são salvas
 
    return render_template("index.html", res=resultado, jogador1_escolha=session.get('jogador1_escolha'), jogador2_escolha=session.get('jogador2_escolha'), placar1=session['placar1'], placar2=session['placar2'])

if __name__ == '__main__':
    app.run(debug=True, port=2237)