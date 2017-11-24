from distutils.core import setup

setup(
    name='jupyter_slack',
    version='1.0.0',
    packages=['jupyter_slack'],
    url='https://github.com/keitakurita/jupyter-slack-notify',
    license='MIT',
    author='keitakurita',
    author_email='keita.kurita@gmail.com',
    description='A magic command for notifying the status of code completion in jupyter notebooks via slack',
    install_requires=['requests', 'ipython']
)
