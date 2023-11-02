from app import create_app

# Creating app instance
app = create_app('production')


if __name__ == '__main__':
   app.run()