@app.route('/cantinho')
@login_necessario
def cantinho():
    nome = session.get('usuario_nome')

    # Contador de visitas
    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

    return render_template(
        'cantinho.html',
        nome=nome,
        cor='Azul',
        linguagem='Python',
        frase='Nunca desista dos seus sonhos!',
        visitas=visitas
    )