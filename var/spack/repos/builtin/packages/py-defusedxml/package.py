# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyDefusedxml(PythonPackage):
    """defusing XML bombs and other exploits"""

    homepage = "https://github.com/tiran/defusedxml"
    url      = "https://pypi.io/packages/source/d/defusedxml/defusedxml-0.5.0.tar.gz"

    version('0.5.0', sha256='24d7f2f94f7f3cb6061acb215685e5125fbcdc40a857eff9de22518820b0a4f4')

    depends_on('py-setuptools', type='build')
