from setuptools import setup, find_packages

setup(
    name='Retalking',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'basicsr==1.4.2',
        'kornia==0.5.1',
        'face-alignment==1.3.4',
        'ninja==1.10.2.3',
        'einops==0.4.1',
        'facexlib==0.2.5',
        'librosa==0.9.2',
        "build-essential",
        "cmake",
        'dlib==19.24.0',
        'gradio>=3.7.0',
        'numpy==1.21.6',
        "dominate"
    ]
)
