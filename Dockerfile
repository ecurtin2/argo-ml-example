FROM frolvlad/alpine-miniconda3:python3.7
RUN conda install matplotlib pandas scikit-learn jsonschema flask
RUN pip install loguru
ADD code /code
ENTRYPOINT ["python", "/code/cli.py"]