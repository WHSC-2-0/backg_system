import os
if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.join(BASE_DIR, "simpleui", "static"))
