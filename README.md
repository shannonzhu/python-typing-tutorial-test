# python-typing-tutorial

A sample Python project to demonstrate basic type checking concepts and best practices.

The four sample projects included correspond to each section of the PyCon 2022 "Python Types for Fun and Profit" tutorial.

1. `introduction_exercises`: Annotating examples of basic data structures.
2. `demo_project`: Getting-started demo for setting up Pyre locally in a new project.
3. `gradual_typing_project`: Example project for applying type checking modes and other approaches to gradually increasing type coverage.
4. `typing_pattern_exercises`: More detailed and advanced Python patterns to practice expressing dynamic behavior in the type system

## Resources

[Tutorial Handout Sheet](https://docs.google.com/document/d/15QZo9Sj_9RQJ79QdJdafRGITjU72jlQbMfQotnTVETo/edit?usp=sharing)

## Setting up

You'll want a python 3.10 environment and `watchman`, along with the
latest version of the `pyre-check` package.

If you run into trouble, an alternative way to get started is to sign up
for `repl.it` (you can sign in through github) and use
[the PyrePycon2022 repl](https://replit.com/@stroxler/PyrePycon2022-nix?v=1)
to try out Pyre on Linux in the browser.

### Installing watchman

[Watchman](https://facebook.github.io/watchman/) is a file monitoring service that records when files change. It is required to run a type checker server that delivers fast, incremental results based on file updates. Without it, you will need to run a full `pyre check` that type checks the entire project each time and cannot use editor integration. 

#### On MacOS

```bash
brew install watchman
```

#### On Ubuntu

```bash
sudo apt-get -y watchman
```


### Installing Python 3.10

How exactly to get the latest Python release varies system to system,
and you may already use a solution such as `conda`.

We have instructions for using `pyenv` for this, but you're welcome
to use any other approach you know.

#### On MacOS

```bash
brew install pyenv

echo '
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
eval "$(pyenv init -)"
' >> ~/.profile

. ~/.profile

pyenv install 3.10.4
```


#### On Ubuntu

```bash
sudo apt-get -y watchman\
    git make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
    
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo '
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
eval "$(pyenv init -)"
' >> ~/.profile

. ~/.profile

pyenv install 3.10.4
```

#### On windows:

We recommend using the Windows Subsystem for Linux:
- Open a windows console in administrator mode
- Run `wsl --install -d Ubuntu-20.04`
- Restart your computer
- When it restarts, the `Ubuntu-20.04` application should open
  - Create a user. We recommend reusing the user from your
    windows install, but you could create a user just for pycon
  - Now, follow the `Ubuntu` instructions above.
  
From this point forward, to work with pyre you can:
- Open the `Ubuntu-20.04` application
- Do any terminal actions (like running `pyre`) you want from
  that terminal session.
- In order to use native tools, like your (VSCode editor) with
  files here, run `explorer.exe <name_of_a_directory>`
  - This will open up the directory in windows explorer.
  - From there you can do things like open files in VSCode.


### Setting up pyre-check in a venv


You can clone this repo in one of two ways:
- First fork it to your user using the "Fork" button, and then
  clone from that repository
- Or, if you don't care about playing with github, just clone directly:
  `git clone https://fbsamples/python-typing-tutorial.git`
  
Then, set it up to use Python 3.10.4:
```
cd python-typing-tutorial

PYENV_VERSION=3.10.4 python -m venv pyre-venv
. pyre-venv/bin/activate

pip install pyre-check
```

You can make sure it works by running
```
cd gradual_typing_project
pyre init <<< '
'
pyre
```
which should spit out:
```
ƛ No type errors found
```

## Contributing

See the [CONTRIBUTING](CONTRIBUTING.md) file for how to help out.

## License

python-typing-tutorial is MIT licensed, as found in the LICENSE file.
