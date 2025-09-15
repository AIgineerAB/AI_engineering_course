# Packaging python application to build scalable apps

**Practical coding**

<a href="https://youtu.be/WNdsLWiyJ-I" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/ai_engineering/packaging_fullstack.png?raw=true" alt="pydantic for data validation" width="600">
</a>

This is the structure of the files that we'll be packaging

```md
.
├── explorations
│   └── eda.ipynb
├── README.md
├── setup.py
└── src
    └── taxipred
        ├── __init__.py
        ├── backend
        │   ├── __init__.py
        │   ├── api.py
        │   └── data_processing.py
        ├── data
        │   └── taxi_trip_pricing.csv
        ├── frontend
        │   ├── __init__.py
        │   └── dashboard.py
        └── utils
            ├── __init__.py
            ├── constants.py
            └── helpers.py
```

In order to install this package which is defined in setup.py script you need to start installing setuptools 

```bash
uv pip install setuptools
```

Afterwards you should navigate to same folder as setup.py and then run 

```bash
uv pip install -e .
```

-e makes it editable so that you don't need to reinstall everytime you change the source code. 


## Read more

## Other videos