import llnl.util.cpu


class TestGemm(CMakePackage):
    """Test {d,s}gemm"""

    homepage = 'https://github.com/ggouaillardet/test-gemm'
    url      = 'https://github.com/ggouaillardet/test-gemm/archive/v0.1.tar.gz'
    git      = 'https://github.com/ggouaillardet/test-gemm.git'
    maintainers = ['ggouaillardet']

    version('0.1', sha256='7e5dabc3c1a244db627ec793a912ca12244cc0f49a483293761161902a290b31')
    depends_on('cmake@3.13.0:3.99.99', type='build')
    depends_on('blas')

    def cmake_args(self):

        options = []

        options.append('-DBLAS_LIBS={0}'.format(self.spec['blas'].libs.joined(';')))

        return options
