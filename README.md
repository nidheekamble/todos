# todos

A dummy app that has a React PWA and a Flask Server

### Initial setup
1. Create a venv/ folder
```
python3 -m venv venv
```
2. Install all needed dependencies from dependencies.txt
```
pip3 install -r dependencies.txt
```
3. In the pwa/ folder, run the following commands
```
npm install
npm run build
```

### To run

1. run the Flask server
```
python3 run.py
```

2. To run the React dev server,
```
cd pwa/
npm run start
```
### NOTE:
1. All AJAX requests from React are to start with route /api
```
e.g: /api/hello
```
2. React application can be accessed on localhost:8080 (react dev server) or 0.0.0.0:5000 (flask)
3. You need not run the react dev server if you are using flask. Just make sure you *npm run build* to use the latest version of the PWA
