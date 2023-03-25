# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypiglatin']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pypiglatin',
    'version': '0.1.1',
    'description': 'A module that can convert words or strings of words from English to Pig Latin.',
    'long_description': '# PyPigLatin\n\nPyPigLatin is a module which can convert words or strings of words from English, into Pig Latin\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install PyPigLatin.\n\n```bash\npip install pypiglatin\n```\n\n## Usage\n\n```python\nimport pypiglatin as p\n\n# Example showing translation of a single word\nsingle_word = "Hello"\n\nprint(p.translate_word(single_word)\n# This would print \'ellohay\'\n\n\n# To trnalsate a larger string, use the translate_string function\nlarger_string = "Pig Latin is hard to speak"\n\np.translate_string(larger_string)\n# This would print \'igpay atinlay isway ardhay otay eakspay\'\n```\n\n## License\n\n[GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)',
    'author': 'Owen Plimer',
    'author_email': 'o.plimer@outlook.com',
    'maintainer': 'Sonosus',
    'maintainer_email': 'sonosusoshwa@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
