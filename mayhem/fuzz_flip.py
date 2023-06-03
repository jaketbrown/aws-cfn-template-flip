#!/usr/bin/env python3
from json import JSONDecodeError

import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    from cfn_flip import flip, to_yaml, to_json

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        flip(fdp.ConsumeRemainingString(), clean_up=fdp.ConsumeBool(), no_flip=fdp.ConsumeBool(), long_form=fdp.ConsumeBool())
    except JSONDecodeError:
        return
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()