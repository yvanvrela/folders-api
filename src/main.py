from application import create_app
from dotenv import load_dotenv


app = create_app()


def main():
    load_dotenv()
    app.run()


if __name__ == '__main__':
    main()
