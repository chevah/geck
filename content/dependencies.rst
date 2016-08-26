Dependencies
############

:menu_order: 160

.. contents::


PyPi Mirror/Custom Index
========================

As our development tools are based on Python, we rely heavily on the Python
stdlib but also on the Python non-stdlib packages ecosystem.

Most of the Python packages are published on the
`pypi.python.com <https://pypi.python.org/pypi>`_ website.

For the Chevah project we are not making direct use of the PyPi official index,
but rather we use a separate PyPi index at
`pypi.chevah.com <https://pypi.chevah.com>`_

We are doing this for the following reasons:

* reduce the load to the official PyPi index
* have our development system working even when the official PyPI site is down
* keep a copy of a package, even if the upstream developer have removed it from
  the official PyPI site
* be able to publish our own private / experimental / junk packages without
  creating unnecessarily load on the official PyPI site

pypi.chevah.com is handled using the
`pypiserver <https://pypi.python.org/pypi/pypiserver>`_ minimal PyPI server
implementation.

The server is configured to reject duplicate versions.

Any developer can upload to pypi.chevah.com using the standard HTTP
credentials.

No package should be removed from pypi.chevah.com.

pypiserver has the capability of automatically downloading and caching
packages from the upstream PyPI site, but in our case this functionality
is disabled in order to help us detect what dependencies are needed and to pin
those dependencies.


Python
======

All packages used by the Chevah projects should be present on the
pypi.chevah.com site.

All packages used by a branch should be pinned to exact versions
(using only the **==** operator).
In this way we can reinstall the dependencies at any time and we will still
get the same versions.

Pinning is very important to keep the test suite under control and make sure
the test execution is deterministic.

They can be pinned via the pavement.py or the requirements.txt file. It is not
important how you pinned them, but is important to make sure that they are
pinned.

When pinning a package which has various dependencies, make sure you are also
pinning those dependencies.

If an upstream package is used by the Chevah project in vanilla form (without
any changes) then the upstream source distribution or wheels are copied
to the pypi.chevah.com site using the same version.
This can be done using twine or manual copy.

If an upstream package needs to be re-packaged either for applying changes to
the code or to the packaging system, then the `.chevahN` prefix is appended to
the upstream version.

If some upstream Python code is not present on PyPi, we get a copy of that
code and package/repackage it. Even if we are not making any changes to the
code, we will still publish it with a version suffixed by `.chevahN` to
prevent future conflicts in the case in which the upstream package is
published on the official PyPi site.

MAYBE ADD A SECTION ABOUT .PYPIRC AND python setup.py sdist upload -r chevah


Javascript
==========

Since we are a Python shop, and node-js is not supported on all our targeted
platform, we are pushing the envelope and using python/setuptools/pip to
manage the JS packages.

All JS packages used for the projects should be *browser ready*. We don't run
anything in node-js and we run everything in a browser... multiple browsers
in fact.

The JS packages are re-packages as Python packages and hosted into our
`pip-expectations <https://github.com/chevah/pip-expectations>`_ repository.

The JS packages are then pushed to pypi.chevah.com

All JS packages live in the **chevah.weblibs** namespace and are named
**chevah-weblibs-JS-PACKAGE-NAME-upstream.version.chevahN** where:

* `chevah-weblibs-` is the prefix for all re-packaged JS libraries/packages
* `JS-PACKAGE-NAME` is the name of the project
* `upstream.version` is the same version as the upstream project
* `.chevahN` is the Chevah downstream repackaging version.

Most of the time the repackaging version will be `.chevah1`, but in some
cases you might need to re-package the same upstream version again (
for example if you forgot to include certain file) and then a new version
is required.

Each package contain the following code in the top level `__init__.py` file,
in order to help detect the path where the JS files are located:

.. sourcecode:: python

    MODULE_PATH = os.path.dirname(__file__)

Then, the code needing access to a JS package can use:

.. sourcecode:: python

    from chevah.weblibs.some_js_package import MODULE_PATH

    # Make the JS files accessible inside the HTTP server.
    root_location.putChild('some_js_name', MODULE_PATH)
