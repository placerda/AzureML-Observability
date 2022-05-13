import setuptools
with open("../README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aml-obs-client',
    version='0.0.1',
    author='James Nguyen; Nicole Serafino',
    author_email='janguy@microsoft.com;nserafino@microsoft.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/microsoft/AzureML-Observability',
    project_urls = {
        "Bug Tracker": "https://github.com/microsoft/AzureML-Observability/issues"
    },
    license='MIT',
    packages=['aml-obs-client'],
    install_requires=['azure-kusto-data==3.1.2','jupyter-dash==0.4.2'],
)