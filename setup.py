from setuptools import setup

APP = ['面试模拟器.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    # 'iconfile': 'xxx.icns',  # 替换成你的icns路径，或者注释掉
    'packages': [],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
