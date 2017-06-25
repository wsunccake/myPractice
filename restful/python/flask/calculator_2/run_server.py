from sys import path
path.append('src/main/python')


from calculator import create_app


app = create_app()
app.run()
