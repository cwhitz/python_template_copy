import re
import sys

package_name = '{{ cookiecutter.__package_slug }}'

# Skip validation if empty (still at default)
if package_name == '':
    sys.exit(0)  # Exit successfully without validating

if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', package_name):
    print(f'ERROR: {package_name} is not a valid Python module name!')
    sys.exit(1)
