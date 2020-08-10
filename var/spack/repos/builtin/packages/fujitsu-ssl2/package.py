# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from shutil import which
import os

class FujitsuSsl2(Package):
    """Fujitsu SSL2 only for Fujitsu compiler."""

    homepage = "https://www.fujitsu.com/us/"

    conflicts('%arm')
    conflicts('%cce')
    conflicts('%clang')
    conflicts('%gcc')
    conflicts('%intel')
    conflicts('%nag')
    conflicts('%pgi')
    conflicts('%xl')
    conflicts('%xl_r')

    provides('blas')
    provides('lapack')
    provides('scalapack')

    def install(self, spec, prefix):
        raise InstallError(
            'Fujitsu SSL2 is not installable; it is vendor supplied')

    @property
    def external_prefix(self):
        return '/bogus'

    @property
    def blas_headers(self):
        return None

    @property
    def blas_libs(self):
        print("self.compiler.cc = %s\n" % (self.compiler.cc))
        return llnl.util.filesystem.LibraryList('%s/lib64/libfjlapacksve.so' % (os.path.dirname(os.path.dirname(self.compiler.cc))))

    @property
    def lapack_headers(self):
        return None

    @property
    def lapack_libs(self):
        return llnl.util.filesystem.LibraryList('%s/lib64/libfjlapacksve.so' % (os.path.dirname(os.path.dirname(self.compiler.cc))))

    @property
    def scalapack_headers(self):
        return None

    @property
    def scalapack_libs(self):
        return llnl.util.filesystem.LibraryList('%s/lib64/libfjscalapacksve.so' % (os.path.dirname(os.path.dirname(self.compiler.cc))))

