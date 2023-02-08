import os
import sys
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup_requires = [
    'enum34==1.1.10'
    ]
install_requires = [
    'docassemble==1.4.36',
    'docassemble.base==1.4.36',
    'docassemble.demo==1.4.36',
    "3to2==1.1.1",
    "airtable-python-wrapper==0.15.3",
    "alembic==1.9.2",
    "amqp==5.1.1",
    "asn1crypto==1.5.1",
    "astunparse==1.6.3",
    "async-generator==1.10",
    "async-timeout==4.0.2",
    "atomicwrites==1.4.1",
    "attrs==22.2.0",
    "azure-common==1.1.28",
    "azure-core==1.26.3",
    "azure-identity==1.12.0",
    "azure-keyvault-secrets==4.6.0",
    "azure-nspkg==3.0.2",
    "azure-storage-blob==12.14.1",
    "Babel==2.11.0",
    "bcrypt==4.0.1",
    "beautifulsoup4==4.11.2",
    "behave==1.2.6",
    "bidict==0.22.1",
    "billiard==3.6.4.0",
    "bleach==6.0.0",
    "blinker==1.5",
    "boto==2.49.0",
    "boto3==1.26.64",
    "botocore==1.29.64",
    "cachetools==5.3.0",
    "cairocffi==1.4.0",
    "CairoSVG==2.6.0",
    "celery==5.2.7",
    "certifi==2022.12.7",
    "cffi==1.15.1",
    "chardet==5.1.0",
    "charset-normalizer==3.0.1",
    "click==8.1.3",
    "click-didyoumean==0.3.0",
    "click-plugins==1.1.1",
    "click-repl==0.2.0",
    "clicksend-client==5.0.72",
    "colorama==0.4.6",
    "commonmark==0.9.1",
    "configparser==5.3.0",
    "convertapi==1.5.0",
    "crayons==0.4.0",
    "cryptography==38.0.4",
    "cssselect2==0.7.0",
    "da-pkg-resources==0.0.1",
    "defusedxml==0.7.1",
    "Deprecated==1.2.13",
    "deprecation==2.1.0",
    "dnspython==2.3.0",
    "Docassemble-Flask-User==0.6.28",
    "Docassemble-Pattern==3.6.5",
    "docassemble-textstat==0.7.2",
    "docassemblekvsession==0.7",
    "docopt==0.6.2",
    "docutils==0.19",
    "docxcompose==1.4.0",
    "docxtpl==0.16.5",
    "email-validator==1.3.1",
    "et-xmlfile==1.1.0",
    "eventlet==0.33.3",
    "exceptiongroup==1.1.0",
    "Flask==2.2.2",
    "Flask-Babel==3.0.1",
    "Flask-Cors==3.0.10",
    "Flask-Login==0.6.2",
    "Flask-Mail==0.9.1",
    "Flask-SocketIO==5.3.2",
    "Flask-SQLAlchemy==3.0.3",
    "Flask-WTF==1.1.1",
    "future==0.18.3",
    "gcs-oauth2-boto-plugin==2.7",
    "geographiclib==2.0",
    "geopy==2.3.0",
    "google-api-core==2.11.0",
    "google-api-python-client==2.76.0",
    "google-auth==2.16.0",
    "google-auth-httplib2==0.1.0",
    "google-auth-oauthlib==0.8.0",
    "google-cloud-core==2.3.2",
    "google-cloud-storage==2.7.0",
    "google-cloud-translate==3.10.1",
    "google-cloud-vision==3.3.1",
    "google-crc32c==1.5.0",
    "google-i18n-address==2.5.2",
    "google-reauth==0.1.1",
    "google-resumable-media==2.4.1",
    "googleapis-common-protos==1.58.0",
    "greenlet==2.0.2",
    "grpcio==1.51.1",
    "grpcio-status==1.51.1",
    "gspread==5.7.2",
    "guess-language-spirit==0.5.3",
    "h11==0.14.0",
    "httplib2==0.21.0",
    "humanize==4.6.0",
    "Hyphenate==1.1.0",
    "idna==3.4",
    "img2pdf==0.4.4",
    "importlib-metadata==6.0.0",
    "importlib-resources==5.10.2",
    "iniconfig==2.0.0",
    "iso8601==1.1.0",
    "isodate==0.6.1",
    "itsdangerous==2.1.2",
    "jaraco.classes==3.2.3",
    "jdcal==1.4.1",
    "jeepney==0.8.0",
    "jellyfish==0.6.1",
    "Jinja2==3.1.2",
    "jmespath==1.0.1",
    "joblib==1.2.0",
    "keyring==23.13.1",
    "kombu==5.2.4",
    "libcst==0.4.9",
    "links-from-link-header==0.1.0",
    "lxml==4.9.2",
    "Mako==1.2.4",
    "Markdown==3.3.6",
    "markdown-it-py==2.1.0",
    "MarkupSafe==2.1.2",
    "mdurl==0.1.2",
    "mdx-smartypants==1.5.1",
    "minio==7.1.13",
    "monotonic==1.6",
    "more-itertools==9.0.0",
    "msal==1.21.0",
    "msal-extensions==1.0.0",
    "msrest==0.7.1",
    "mypy-extensions==1.0.0",
    "namedentities==1.5.2",
    "netifaces==0.11.0",
    "nltk==3.8.1",
    "num2words==0.5.12",
    "numpy==1.24.1",
    "oauth2client==4.1.3",
    "oauthlib==3.2.2",
    "openpyxl==3.1.0",
    "ordered-set==4.1.0",
    "outcome==1.2.0",
    "packaging==23.0",
    "pandas==1.5.3",
    "parse==1.19.0",
    "parse-type==0.6.0",
    "passlib==1.7.4",
    "pdfminer.six==20221105",
    "phonenumbers==8.13.5",
    "pikepdf==6.2.9",
    "Pillow==9.4.0",
    "pkginfo==1.9.6",
    "pluggy==1.0.0",
    "ply==3.11",
    "portalocker==2.7.0",
    "prompt-toolkit==3.0.36",
    "proto-plus==1.22.2",
    "protobuf==4.21.12",
    "psutil==5.9.4",
    "psycopg2-binary==2.9.5",
    "py==1.11.0",
    "pyasn1==0.4.8",
    "pyasn1-modules==0.2.8",
    "pycountry==22.3.5",
    "pycparser==2.21",
    "pycryptodome==3.17",
    "pycryptodomex==3.17",
    "pycurl==7.45.2",
    "Pygments==2.14.0",
    "PyJWT==2.6.0",
    "PyLaTeX==1.4.1",
    "PyNaCl==1.5.0",
    "pyOpenSSL==23.0.0",
    "pyotp==2.8.0",
    "pyparsing==3.0.9",
    "pypng==0.20220715.0",
    "PySocks==1.7.1",
    "pytest==7.2.1",
    "python-dateutil==2.8.2",
    "python-docx==0.8.11",
    "python-dotenv==0.21.1",
    "python-editor==1.0.4",
    "python-engineio==4.3.4",
    "python-http-client==3.3.7",
    "python-ldap==3.4.3",
    "python-socketio==5.7.2",
    "pytz==2022.7.1",
    "pytz-deprecation-shim==0.1.0.post0",
    "pyu2f==0.1.5",
    "PyYAML==6.0",
    "pyzbar==0.1.9",
    "qrcode==7.4.1",
    "rauth==0.7.3",
    "readme-renderer==37.3",
    "redis==4.4.2",
    "regex==2022.10.31",
    "reportlab==3.6.12",
    "repoze.lru==0.7",
    "requests==2.28.2",
    "requests-oauthlib==1.3.1",
    "requests-toolbelt==0.10.1",
    "retry-decorator==1.1.1",
    "rfc3339==6.2",
    "rfc3986==2.0.0",
    "rich==13.3.1",
    "rsa==4.9",
    "ruamel.yaml==0.17.21",
    "ruamel.yaml.clib==0.2.7",
    "s3transfer==0.6.0",
    "s4cmd==2.1.0",
    "scikit-learn==1.2.1",
    "scipy==1.10.0",
    "SecretStorage==3.3.3",
    "selenium==4.8.0",
    "sendgrid==6.9.7",
    "simplekv==0.14.1",
    "six==1.16.0",
    "sniffio==1.3.0",
    "SocksiPy-branch==1.1",
    "sortedcontainers==2.4.0",
    "soupsieve==2.3.2.post1",
    "SQLAlchemy==2.0.1",
    "starkbank-ecdsa==2.2.0",
    "tailer==0.4.1",
    "telnyx==1.5.0",
    "threadpoolctl==3.1.0",
    "tinycss2==1.2.1",
    "titlecase==2.4",
    "toml==0.10.2",
    "tomli==2.0.1",
    "tqdm==4.64.1",
    "trio==0.22.0",
    "trio-websocket==0.9.2",
    "twilio==7.16.2",
    "twine==4.0.2",
    "typing-inspect==0.8.0",
    "typing_extensions==4.4.0",
    "tzdata==2022.7",
    "tzlocal==4.2",
    "ua-parser==0.16.1",
    "uritemplate==4.1.1",
    "urllib3==1.26.14",
    "us==2.0.2",
    "user-agents==2.2.0",
    "uWSGI==2.0.21",
    "vine==5.0.0",
    "wcwidth==0.2.6",
    "webdriver-manager==3.8.5",
    "webencodings==0.5.1",
    "Werkzeug==2.2.2",
    "wrapt==1.14.1",
    "wsproto==1.2.0",
    "WTForms==3.0.1",
    "xfdfgen==0.4",
    "xlrd==2.0.1",
    "XlsxWriter==3.0.8",
    "xlwt==1.3.0",
    "zipp==3.12.0"
]

if sys.version_info < (3, 9):
    install_requires.append("backports.zoneinfo==0.2.1")
else:
    install_requires.append("docassemble-backports==1.0")

setup(name='docassemble.webapp',
      version='1.4.36',
      python_requires='>=3.8',
      description=('The web application components of the docassemble system.'),
      long_description=read("README.md"),
      long_description_content_type='text/markdown',
      author='Jonathan Pyle',
      author_email='jhpyle@gmail.com',
      license='MIT',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=install_requires,
      zip_safe=False,
      package_data={'docassemble.webapp': ['alembic.ini', os.path.join('alembic', '*'), os.path.join('alembic', 'versions', '*'), os.path.join('data', '*.*'), os.path.join('data', 'static', '*.*'), os.path.join('data', 'static', 'favicon', '*.*'), os.path.join('data', 'questions', '*.*'), os.path.join('templates', 'base_templates', '*.html'), os.path.join('templates', 'flask_user', '*.html'), os.path.join('templates', 'flask_user', 'emails', '*.*'), os.path.join('templates', 'pages', '*.html'), os.path.join('templates', 'pages', '*.xml'), os.path.join('templates', 'pages', '*.js'), os.path.join('templates', 'users', '*.html'), os.path.join('static', 'app', '*.*'), os.path.join('static', 'localization', '*.*'), os.path.join('static', 'yamlmixed', '*.*'), os.path.join('static', 'sounds', '*.*'), os.path.join('static', 'examples', '*.*'), os.path.join('static', 'fontawesome', 'js', '*.*'), os.path.join('static', 'office', '*.*'), os.path.join('static', 'bootstrap-fileinput', 'img', '*'), os.path.join('static', 'img', '*'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'locales', '*'), os.path.join('static', 'bootstrap-fileinput', 'js', 'plugins', '*'), os.path.join('static', 'bootstrap-slider', 'dist', '*.js'), os.path.join('static', 'bootstrap-slider', 'dist', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'css', '*.css'), os.path.join('static', 'bootstrap-fileinput', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fa', '*.js'), os.path.join('static', 'bootstrap-fileinput', 'themes', 'fas', '*.js'), os.path.join('static', 'bootstrap-combobox', 'css', '*.css'), os.path.join('static', 'bootstrap-combobox', 'js', '*.js'), os.path.join('static', 'bootstrap-fileinput', '*.md'), os.path.join('static', 'bootstrap', 'js', '*.*'), os.path.join('static', 'bootstrap', 'css', '*.*'), os.path.join('static', 'labelauty', 'source', '*.*'), os.path.join('static', 'codemirror', 'lib', '*.*'), os.path.join('static', 'codemirror', 'addon', 'search', '*.*'), os.path.join('static', 'codemirror', 'addon', 'display', '*.*'), os.path.join('static', 'codemirror', 'addon', 'scroll', '*.*'), os.path.join('static', 'codemirror', 'addon', 'dialog', '*.*'), os.path.join('static', 'codemirror', 'addon', 'edit', '*.*'), os.path.join('static', 'codemirror', 'addon', 'hint', '*.*'), os.path.join('static', 'codemirror', 'mode', 'yaml', '*.*'), os.path.join('static', 'codemirror', 'mode', 'markdown', '*.*'), os.path.join('static', 'codemirror', 'mode', 'javascript', '*.*'), os.path.join('static', 'codemirror', 'mode', 'css', '*.*'), os.path.join('static', 'codemirror', 'mode', 'python', '*.*'), os.path.join('static', 'codemirror', 'mode', 'htmlmixed', '*.*'), os.path.join('static', 'codemirror', 'mode', 'xml', '*.*'), os.path.join('static', 'codemirror', 'keymap', '*.*'), os.path.join('static', 'areyousure', '*.js'), os.path.join('static', 'popper', '*.*'), os.path.join('static', 'popper', 'umd', '*.*'), os.path.join('static', 'popper', 'esm', '*.*'), os.path.join('static', '*.html')]}
      )
