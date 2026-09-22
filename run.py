"""Ponto de entrada da API para notebook e demonstração em rede local."""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # 0.0.0.0 permite que um Android/iPhone na mesma rede Wi-Fi acesse o notebook.
    app.run(
        host=app.config["API_HOST"],
        port=app.config["API_PORT"],
        debug=app.config["API_DEBUG"],
    )
