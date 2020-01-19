from application.app import create_app

# Instantiate app from YOUR_PACKAGE.__init__ file
app = create_app()

if __name__ == '__main__':
  app.run(
    host     =  '0.0.0.0',
    port     =  '1111',
    debug    =  True,
    threaded =  True,
  )
