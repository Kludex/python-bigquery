# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools


# Package metadata.

name = "google-cloud-bigquery"
description = "Google BigQuery API client library"

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    "google-api-core[grpc] @ git+https://github.com/googleapis/python-api-core.git@main",
    "google-auth >= 2.14.1, <3.0.0dev",
    "google-cloud-core >= 2.4.1, <3.0.0dev",
    "google-resumable-media >= 2.0.0, < 3.0dev",
    "packaging >= 20.0.0",
    "python-dateutil >= 2.7.3, <3.0dev",
    "requests >= 2.21.0, < 3.0.0dev",
]
pyarrow_dependency = "pyarrow >= 3.0.0"
extras = {
    # bqstorage had a period where it was a required dependency, and has been
    # moved back to optional due to bloat.  See
    # https://github.com/googleapis/python-bigquery/issues/1196 for more background.
    "bqstorage": [
        "google-cloud-bigquery-storage >= 2.6.0, <3.0.0dev",
        # Due to an issue in pip's dependency resolver, the `grpc` extra is not
        # installed, even though `google-cloud-bigquery-storage` specifies it
        # as `google-api-core[grpc]`. We thus need to explicitly specify it here.
        # See: https://github.com/googleapis/python-bigquery/issues/83 The
        # grpc.Channel.close() method isn't added until 1.32.0.
        # https://github.com/grpc/grpc/pull/15254
        "grpcio >= 1.47.0, < 2.0dev",
        "grpcio >= 1.49.1, < 2.0dev; python_version>='3.11'",
        pyarrow_dependency,
    ],
    "pandas": [
        "pandas>=1.1.0",
        pyarrow_dependency,
        "db-dtypes>=0.3.0,<2.0.0dev",
        "importlib_metadata>=1.0.0; python_version<'3.8'",
    ],
    "ipywidgets": [
        "ipywidgets>=7.7.0",
        "ipykernel>=6.0.0",
    ],
    "geopandas": ["geopandas>=0.9.0, <1.0dev", "Shapely>=1.8.4, <3.0.0dev"],
    "ipython": [
        "bigquery-magics >= 0.1.0",
    ],
    "tqdm": ["tqdm >= 4.7.4, <5.0.0dev"],
    "opentelemetry": [
        "opentelemetry-api >= 1.1.0",
        "opentelemetry-sdk >= 1.1.0",
        "opentelemetry-instrumentation >= 0.20b0",
    ],
    "bigquery_v2": [
        "proto-plus >= 1.22.3, <2.0.0dev",
        "protobuf>=3.20.2,<6.0.0dev,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5",  # For the legacy proto-based types.
    ],
}

all_extras = []

for extra in extras:
    all_extras.extend(extras[extra])

extras["all"] = all_extras

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

version = {}
with open(os.path.join(package_root, "google/cloud/bigquery/version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in setuptools.find_namespace_packages()
    if package.startswith("google")
]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/googleapis/python-bigquery",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
