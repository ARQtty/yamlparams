# yamlparams
Python library for dot-access to parameters in yaml file

## Install

`pip3 install yamlparams`

## Example

config.yaml
```
train:
  param1: 0
  param2: 'a'
  param3:
    param4:
      value: []
  param5: '${LDA}/l'

```

main.py
```
import os
from yamlparams.utils import Hparam

os.environ['LDA'] = 4
config = Hparam('./config.yaml')

print(config)
print(config.train)
print(config.train.param1)
```