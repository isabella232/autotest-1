from distutils.core import setup
import os, sys

try:
    import autotest.common as common
except ImportError:
    import common

from autotest.client.shared import version

#mostly needed when called one level up
scheduler_dir = os.path.dirname(sys.modules[__name__].__file__) or '.'
autotest_dir = os.path.abspath(os.path.join(scheduler_dir, ".."))

def run():
    setup(name='autotest',
          description='Autotest testing framework - scheduler module',
          author='Autotest Team',
          author_email='autotest@test.kernel.org',
          version=version.get_version(),
          url='autotest.kernel.org',
          package_dir={'autotest.scheduler': scheduler_dir },
          package_data={'autotest.scheduler': ['archive_results.control.srv']},
          packages=['autotest.scheduler' ],
          scripts=[scheduler_dir + '/autotest-scheduler',
                   scheduler_dir + '/autotest-scheduler-watcher',
                   ],
    )

if __name__ == "__main__":
    run()
