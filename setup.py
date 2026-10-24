from pathlib import Path
from typing import List

from setuptools import find_packages, setup


PROJECT_ROOT = Path(__file__).parent


def get_requirements(file_path: str) -> List[str]:
    """Read runtime dependencies from a requirements file."""
    requirements = []
    for requirement in (PROJECT_ROOT / file_path).read_text().splitlines():
        requirement = requirement.strip()
        if requirement and requirement != "-e ." and not requirement.startswith("#"):
            requirements.append(requirement)
    return requirements

setup(
    name="ml-project-1",
    version="0.0.1",
    author="Jenison J",
    author_email="jenison717@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
