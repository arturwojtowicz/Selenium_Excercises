import os
import shutil

import pytest

from libs.utils import get_absolute_path_of_file

from .fixtures import *


@pytest.fixture(scope="session", autouse=True)
def temporary_folder():
    if not os.path.exists(get_absolute_path_of_file('temp/')):
        os.mkdir('temp')
    yield
    shutil.rmtree('temp/')
