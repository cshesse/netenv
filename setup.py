import os
from setuptools import setup, find_packages

setup_dict = dict(
    name="netenv",
    version="0.1",
    packages=find_packages(),
    install_requires=["gym~=0.12.1", "numpy~=1.14"],
    extras_require={"dev": ["pytest", "pytest-benchmark"]},
)

if os.environ.get("USE_SCM_VERSION", "1") == "1":
    setup_dict["use_scm_version"] = {
        "root": "..",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp",
    }
    setup_dict["setup_requires"] = ["setuptools_scm"]

setup(**setup_dict)
