# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright 2021-  QuOCS Team
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pytest
import os
import time
import numpy as np
from quocslib.utils.BestDump import BestDump


@pytest.fixture
def dump_obj():
    folder = os.path.dirname(os.path.realpath(__file__))
    return BestDump(folder, "000")


def test_dump_controls_record(dump_obj):

    test_pulse = np.array([1, 2, 3])
    test_timegrid = np.array([4, 5, 6])
    test_params = np.array([7, 8, 9])

    dump_obj.dump_controls([test_pulse],
                           [test_timegrid],
                           [test_params],
                           True)

    outfile_path = os.path.join(dump_obj.best_controls_path, "000_best_controls.npz")

    controls = np.load(outfile_path)

    # print(controls.files)

    assert (controls["pulse1"] == test_pulse).all()
    assert (controls["time_grid1"] == test_timegrid).all()
    assert (controls["parameter1"] == test_params).all()

    os.remove(outfile_path)
