# Machine Learning and AI Course

This repository contains all my work for the Machine Learning and AI course, assignments, code, and sample data. I will be using macOS

## Installation

#### Homebrew

1. Open the Terminal.
2. Install Homebrew by running:

```

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

3. Follow the instructions on the terminal.

#### Python

1. Install Python using Homebrew:

```

brew install python

```

2. Add the Homebrew Python path to your `~/.zshrc` file (for Zsh shell) or `~/.bash_profile` (for Bash shell):

```

echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH"' >> ~/.zshrc

# Use ~/.bash_profile if you are using Bash

```

3. Refresh your terminal session or source your profile to apply the changes:

```

source ~/.zshrc

# Or source ~/.bash_profile for Bash

```

4. Verify that the Homebrew version of Python is being used:

```

python3 --version

```

#### Dependencies

1. Create a virtual environment using venv (Virtual Environment):

```
python -m venv venv
```

2. Activate the environment

```
source venv/bin/activate
```

3. Install the required Python libraries:

```
pip install -r requirements.txt
```

## Recommended IDE

For this course, we recommend using **Visual Studio Code (VSCode)** as your Integrated Development Environment (IDE).

- [Visual Studio Code](https://code.visualstudio.com/)

### VSCode Extensions

Consider installing the following extensions:

- Python (by Microsoft)
- Jupyter (by Microsoft)
- Pylance (by Microsoft)

## Running Code

1. Open your Python file in VSCode.
2. To run the file, you can:
   - Use the play button in the top-right corner of the editor.
   - Press `F5` to run the file in debug mode.
