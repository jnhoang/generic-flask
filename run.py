from application.app import create_app

# Instantiate app from YOUR_PACKAGE.__init__ file
app = create_app()

if __name__ == '__main__':
  port = '1111'
  print(f'running on port: {port}')
  app.run(
    host     =  '0.0.0.0',
    port     =  port,
    debug    =  True,
    threaded =  True,
  )
