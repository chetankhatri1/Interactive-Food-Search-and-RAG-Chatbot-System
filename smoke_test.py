import importlib
import sys

modules = [
    ("numpy", "__version__"),
    ("scipy", "__version__"),
    ("chromadb", "__version__"),
    ("sentence_transformers", "__version__"),
    ("ibm_watsonx_ai", "__version__"),
    ("dotenv", "__version__"),
]

print("Python:", sys.version.replace('\n', ' '))
for mod, ver_attr in modules:
    try:
        m = importlib.import_module(mod)
        ver = getattr(m, ver_attr, 'unknown')
        print(f"{mod}: {ver}")
    except Exception as e:
        print(f"{mod}: import failed ({e})")
