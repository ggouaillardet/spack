import llnl.util.cpu


class TestArmSve(CMakePackage):
    """Test including the <arm_sve.h> header file"""

    homepage = 'https://github.com/ggouaillardet/test-arm_sve'
    url      = 'https://github.com/ggouaillardet/test-arm_sve/archive/v0.1.tar.gz'
    git      = 'https://github.com/ggouaillardet/test-arm_sve.git'
    maintainers = ['ggouaillardet']


    version('0.1', sha256='65ff94bc68823170e6ccb1ff8d44ff169497bbfe30eccddcb379b546e39930d2')
    depends_on('cmake@3.13.0:3.99.99', type='build')
    depends_on('blas')
