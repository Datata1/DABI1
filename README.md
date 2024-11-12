# DABI1

### Contributors
- Benjamin
- Vladi
- wija1025

### set up project

1. activate/setup your virtual environment

2. install python dependencies to virtual environment
```sh
pip install -r requirements.txt
```

3. start locally deployed postgres db
```sh
docker-compose up -d
```

4. load data into db 
```sh
python ./scripts/load_data_into_db.py
```


### close project

1. 
```sh
docker-compose down
```