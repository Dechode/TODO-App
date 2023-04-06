# TODO App

CLI program for managing tasks with TODOs. 


## Dependencies
First install python and add it to PATH.
Then make sure you have installed jsonpickle

```bash
  pip install jsonpickle
```
    
## Usage/Examples

Clone the repository
```bash
git clone https://github.com/Dechode/TODO-App.gito
cd TODO-App
```

Create a new task
```bash
python app.py create <taskname>
```

Remova a task
```bash
python app.py remove <taskname>
```

Add TODO to a task
```bash
python app.py add-todo <taskname> "String of what needs to be done"
```

Remove TODO from a task
```bash
python app.py remove-todo <taskname> <todoID> 
```


List current tasks and their TODOs
```bash
python app.py list
```



## Authors

- [@Dechode](https://github.com/Dechode)


