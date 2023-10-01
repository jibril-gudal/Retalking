from setuptools import setup, find_packages

setup(
    name='Retalking',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'basicsr',
        'kornia',
        'face-alignment',
        'ninja',
        'einops',
        'facexlib',
        'librosa',
        'dlib',
        'gradio',
        'numpy',
        'torch',
        'torchvision'
    ],
)
