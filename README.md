# Image converter


## Installation (Windows)

1. Create `venv` environment and activate it:

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\activate
```

*To deactivate the venv, use:*
```bash
deactivate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Ensure the `images` folder is present in the root directory of the project.

4. Save images to convert in `images` folder, then run `convert.py` script:

```bash
python convert.py
```

5. Results will be in `converted_images`.
