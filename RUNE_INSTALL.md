Rune devs: To install Faiss for development

```
brew install libomp
brew install swig@3
./configure --without-cuda --with-python=python3.7m
make
make py
```

Now the Python interface is compiled and ready to use.