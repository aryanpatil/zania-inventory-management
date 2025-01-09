## SETUP

To initialise Database and Tables while running for the first time, runt he following commands from the root directory of the project:
```
pip install -r requirements.txt
python3 init_db.py
```

To run the application in Docker, perform the following commands:
```
docker build -t zania-inventory-management .
docker run -p 8000:8000 zania-inventory-management
```

## USAGE

Once the application is run, please open the localhost ```http://127.0.0.1:8000``` to access the Swagger UI for the 3 APIs as requested in the task.

<img width="1503" alt="Screenshot 2025-01-09 at 11 58 23 PM" src="https://github.com/user-attachments/assets/3fcf4e44-f37a-49ef-b7f0-ad7ab9c31f83" />



## TEST

To Run all the unit tests, run the following bash command from root directory of the project:
```
pytest tests/
```

