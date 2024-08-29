### Python 3.10 required for Linux for fr-robot driver issues

### Environment setup
1. create new env with python=3.10
2. `pip install -r requirements.txt`

### Launch GUI
`python main.py`

### Typical pipeline
1. start RTABmap
2. start robotic arm scirpt
3. wait for automatic moving and 3D scan
4. stop rtabmap
5. convert rtabmap db file to pointcloud
6. TODO next

### Testing unit typical
1. Create any testing code under tests
2. Import current package using `from context import <package>`