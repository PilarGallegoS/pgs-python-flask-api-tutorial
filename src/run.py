from src.app import app  # Importa la instancia de Flask desde src.app

if __name__ == "__main__":  # Si se ejecuta directamente (no como un módulo)
    app.run(debug=True)  # Inicia el servidor en modo de depuración
