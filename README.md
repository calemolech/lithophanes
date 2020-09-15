# lithophanes
3D Printed Lithophanes - Software Engineering Project

## Environment setup
### Requirements
An installation of Python
### Create running environment
- Install the virtualenv package
```bash
pip install virtualenv
```
- Create and activate the virtual environment
```bash
# Create venv
virtualenv venv
```
```bash
# Activate in MacOS/Linux
source venv/bin/activate

# Activate in Windows
venv\Scripts\activate
```
- Install requirement packages
```bash
pip install -r requirements.txt
```

## Application
- Run application by command line
```bash
python main.py
```
- Run application by executable file in "/dist/main"

## Build Application
- The easiest method to build application is use command with pre-defines spec:
```bash
#Mac OS/Linux
pyinstaller --onefile 3D\ Lithophanes.spec
```
- You also build from scratch by command:
```bash
#Mac OS/Linux
pyinstaller --onefile --additional-hooks-dir=hooks --name="3D Lithophane" --noconsole --icon="./resources/icons/app.icns" --runtime-tmpdir="/tmp main.py
```
- The result we appear in `dist` folder.

## Team members
- Tran Thanh Huy - huytran190194@gmail.com
- Phan Thanh Dat - phanthanhdat203@gmail.com
- Dang Thanh Minh - minhdangthanh1982@gmail.com