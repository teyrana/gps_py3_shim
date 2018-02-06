

References
====
[Sharing Your Labor of Love: PyPI Quick and Dirty]( https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/ )


Procedure
====
1.  Build Source Distribution

```
> python3 setup.py sdist
```


2a. Install to local system (development)

For use, testing or development.

```
pip3 install [-e] .
```



2b.  Upload to PyPl

```
> twine upload dist/*
```
