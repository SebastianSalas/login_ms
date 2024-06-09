1. Instala dependencias usando pip:
    ```bash
    python -m venv venv
    pip install -r requirements.txt
    .\venv\Scripts\Activate  

2. Inicia el servidor: 
    ```bash
    uvicorn main:app --reload

3. Actualizar requirements
pip freeze > requirements.txt