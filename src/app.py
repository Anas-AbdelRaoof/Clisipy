from dotenv import load_dotenv

# Load environment variables FIRST, before any other imports
load_dotenv()

from run import run


def main():
    run()


if __name__ == "__main__":
    main()
