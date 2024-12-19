import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

    __version__="0.0.0"

    REPO_NAME="Kidney-Disease-Classification-Deep-learning-project"
    AUTHOR_USER_NAME ="Endless20"
    SRC_REPO = "cnnClassifier"
    AUTHOR_EMAIL = "kaleananta2011@gmail.com"


    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="A small python package for CNN app",
        Long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        projects_urls={
            "Bug Trackers":f"https:github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
            },
            pakage_dir={"":"src"},
            packages=setuptools.find_packages(where="src")



    )