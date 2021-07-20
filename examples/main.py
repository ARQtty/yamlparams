import os
from yamlparams.utils import Hparam

os.environ['LDA'] = 4
config = Hparam('./config.yaml')

print(config)
print(config.train)
print(config.train.param1)