# Install

To create the environment run:

```
conda env create -f environment.yml --prefix ./env/{{cookiecutter.publication_slug}}/
```

and activate using:

```
conda activate ./env/{{cookiecutter.publication_slug}}
```

The specific environment (potentially very OS specific) can be exported

```
conda env export --prefix ./env/{{cookiecutter.publication_slug}} --file exact_environment.yml
```

and updated:

```
conda env update --prefix ./env/{{cookiecutter.publication_slug}} --file exact_environment.yml  --prune
```
