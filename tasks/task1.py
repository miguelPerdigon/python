from airflow.models import Variable


def load(ds, **kwargs):
    print('this is de value passed by parameter {}'.format(kwargs.get('country')))
    print('print some airflow environment variable {}'.format(Variable.get('NAME_KEY_VARIABLE')))
